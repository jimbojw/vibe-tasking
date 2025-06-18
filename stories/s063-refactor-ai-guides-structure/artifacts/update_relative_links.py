# Copyright 2025 Google LLC 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re
import argparse
from pathlib import Path

# This list maps old "absolute-like" project paths to new ones.
# Order can be important: more specific paths should come before more general ones
# if there's a chance of incorrect partial matching by a general rule.
PATH_TRANSFORMATIONS = [
    # Specific files from old vibe-tasking/stories to new core/stories
    ('docs/ai-guides/vibe-tasking/stories/journal.template.md', 'docs/ai-guides/core/stories/journal.template.md'),
    ('docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md', 'docs/ai-guides/core/stories/stories-planning-guide.md'),
    ('docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md', 'docs/ai-guides/core/stories/stories-structuring-guide.md'),
    ('docs/ai-guides/vibe-tasking/stories/stories-working-guide.md', 'docs/ai-guides/core/stories/stories-working-guide.md'),
    ('docs/ai-guides/vibe-tasking/stories/story.template.md', 'docs/ai-guides/core/stories/story.template.md'),
    
    # Specific files from old vibe-tasking to new core/ai-guides
    ('docs/ai-guides/vibe-tasking/ai-guide.template.md', 'docs/ai-guides/core/ai-guides/ai-guide.template.md'),
    ('docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md', 'docs/ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md'),
    
    # General vibe-tasking directory to core directory (catches other files in vibe-tasking if any)
    # This should come after specific file mappings from vibe-tasking.
    ('docs/ai-guides/vibe-tasking', 'docs/ai-guides/core'), # Match as a prefix

    # Specific files from old top-level ai-guides to new contrib subdirectories
    ('docs/ai-guides/adr.template.md', 'docs/ai-guides/contrib/adrs/adr.template.md'),
    ('docs/ai-guides/adrs-writing-guide.md', 'docs/ai-guides/contrib/adrs/adrs-writing-guide.md'),
    ('docs/ai-guides/article.template.md', 'docs/ai-guides/contrib/articles/article.template.md'),
    ('docs/ai-guides/articles-writing-guide.md', 'docs/ai-guides/contrib/articles/articles-writing-guide.md'),

    # Tutorials directory
    ('docs/ai-guides/tutorials', 'docs/ai-guides/contrib/tutorials'), # Match as a prefix

    # Other specific top-level files moved to contrib
    ('docs/ai-guides/ascii-art-diagrams-authoring-guide.md', 'docs/ai-guides/contrib/ascii-art-diagrams-authoring-guide.md'),
    ('docs/ai-guides/sequence-diagrams-authoring-guide.md', 'docs/ai-guides/contrib/sequence-diagrams-authoring-guide.md'),
    ('docs/ai-guides/updating-onboarding-guide.md', 'docs/ai-guides/contrib/updating-onboarding-guide.md'),
]

# Regex to find Markdown links: [text](link)
MD_LINK_REGEX = re.compile(r'(\[([^\]]*)\]\(([^)\s]+)\))')

def get_story_status(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            in_frontmatter = False
            for _ in range(20): 
                line = f.readline()
                if not line: break
                line_stripped = line.strip()
                if line_stripped == '---':
                    in_frontmatter = not in_frontmatter
                    if not in_frontmatter: break # End of frontmatter
                    continue
                if in_frontmatter:
                    match = re.match(r'^status:\s*"([^"]+)"', line_stripped)
                    if match: return match.group(1)
            return None
    except Exception: return None

def normalize_path_from_project_root(path_str, project_root_abs):
    # Normalize and ensure it's relative to project root, using forward slashes
    normalized = Path(os.path.normpath(path_str)).as_posix()
    project_root_posix = Path(project_root_abs).as_posix()
    if normalized.startswith(project_root_posix + '/'):
        return normalized[len(project_root_posix)+1:]
    elif normalized.startswith(project_root_posix): # Should not happen if / is appended
         return normalized[len(project_root_posix):]
    return normalized # Or raise error if not under project root

def process_file_content(content, current_file_abs_path, project_root_abs, dry_run=True):
    modified_content = content
    changes_made_to_file = False
    
    current_file_dir_abs = os.path.dirname(current_file_abs_path)

    def replace_link(match):
        nonlocal changes_made_to_file
        full_match_text = match.group(1)
        link_text = match.group(2)
        original_link_target = match.group(3)

        # Skip external links, absolute paths from system root, or page anchors
        if original_link_target.startswith(('http://', 'https://', '/', '#')):
            return full_match_text

        # Resolve original link target to an absolute path from system root
        resolved_old_target_abs = os.path.normpath(os.path.join(current_file_dir_abs, original_link_target))
        
        # Convert to a project-relative "absolute-like" path (e.g., "docs/...")
        old_project_path = normalize_path_from_project_root(resolved_old_target_abs, project_root_abs)
        
        new_project_path = old_project_path
        transformed = False

        for old_prefix, new_prefix in PATH_TRANSFORMATIONS:
            if old_project_path == old_prefix: # Exact match for full file paths
                new_project_path = new_prefix
                transformed = True
                break
            if old_project_path.startswith(old_prefix + '/'): # Directory/prefix match
                new_project_path = new_prefix + old_project_path[len(old_prefix):]
                transformed = True
                break
        
        if transformed:
            # Convert the new project path back to an absolute system path to calculate new relative
            new_target_abs = os.path.join(project_root_abs, new_project_path)
            new_relative_target = os.path.relpath(new_target_abs, current_file_dir_abs)
            new_relative_target = Path(new_relative_target).as_posix() # Ensure forward slashes

            if new_relative_target != original_link_target:
                changes_made_to_file = True
                new_link_md = f"[{link_text}]({new_relative_target})"
                if dry_run:
                    print(f"  File: {normalize_path_from_project_root(current_file_abs_path, project_root_abs)}")
                    print(f"    Original Link: [{link_text}]({original_link_target})")
                    print(f"    Resolved Old:  {old_project_path}")
                    print(f"    Transformed New: {new_project_path}")
                    print(f"    New Rel. Link: [{link_text}]({new_relative_target})")
                return new_link_md
        return full_match_text

    modified_content = MD_LINK_REGEX.sub(replace_link, content)
    return modified_content, changes_made_to_file

def main():
    parser = argparse.ArgumentParser(description="Update relative links in Markdown files after docs/ai-guides restructuring.")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be changed without modifying files.")
    parser.add_argument('--path', default='docs', help="Directory to scan for Markdown files (default: 'docs').")
    args = parser.parse_args()

    project_root_abs = os.path.abspath('.') # Assuming script is run from project root
    scan_path_abs = os.path.abspath(args.path)

    print(f"Starting relative link update script. Dry run: {args.dry_run}. Path: {args.path}")
    
    total_md_files_found = 0
    files_skipped_artifacts = 0
    files_skipped_status = 0
    files_processed_for_changes = 0
    files_that_would_change = 0
    files_actually_changed = 0

    for root, dirs, files in os.walk(scan_path_abs):
        if 'artifacts' in dirs:
            dirs.remove('artifacts')

        for filename in files:
            if not filename.endswith(".md"):
                continue
            
            total_md_files_found += 1
            filepath_abs = os.path.join(root, filename)
            filepath_project_rel = normalize_path_from_project_root(filepath_abs, project_root_abs)

            path_parts = filepath_project_rel.split("/")
            if 'artifacts' in path_parts:
                files_skipped_artifacts += 1
                continue

            is_story_file = "docs/stories/s" in filepath_project_rel and filename == "story.md"
            is_journal_file = "docs/stories/s" in filepath_project_rel and filename == "journal.md"
            
            skip_due_to_status_flag = False
            if is_story_file:
                status = get_story_status(filepath_abs)
                if status in ["Done", "Closed"]:
                    print(f"Skipping story.md (status: {status}): {filepath_project_rel}")
                    files_skipped_status += 1
                    skip_due_to_status_flag = True
            elif is_journal_file:
                story_md_path_abs = os.path.join(os.path.dirname(filepath_abs), "story.md")
                if os.path.exists(story_md_path_abs):
                    status = get_story_status(story_md_path_abs)
                    if status in ["Done", "Closed"]:
                        print(f"Skipping journal.md (story status: {status}): {filepath_project_rel}")
                        files_skipped_status += 1
                        skip_due_to_status_flag = True
            
            if skip_due_to_status_flag:
                continue
            
            files_processed_for_changes += 1
            
            try:
                with open(filepath_abs, 'r', encoding='utf-8') as f:
                    original_content = f.read()
            except Exception as e:
                print(f"Error reading file {filepath_project_rel}: {e}")
                continue

            if not args.dry_run: # Only print "Processing" if not dry_run, as dry_run prints per change
                 print(f"Processing: {filepath_project_rel}")

            modified_content, changes_were_made = process_file_content(original_content, filepath_abs, project_root_abs, dry_run=args.dry_run)

            if changes_were_made:
                if args.dry_run:
                    files_that_would_change +=1 # Count files that would have at least one change
                else:
                    try:
                        with open(filepath_abs, 'w', encoding='utf-8') as f:
                            f.write(modified_content)
                        print(f"MODIFIED: File '{filepath_project_rel}'")
                        files_actually_changed += 1
                    except Exception as e:
                        print(f"Error writing file {filepath_project_rel}: {e}")
            
    print(f"\nScript finished.")
    print(f"Total Markdown files found: {total_md_files_found}")
    print(f"Files skipped (in 'artifacts' directories): {files_skipped_artifacts}")
    print(f"Files skipped (story/journal status Done/Closed): {files_skipped_status}")
    print(f"Files processed for link changes: {files_processed_for_changes}")
    if args.dry_run:
        print(f"Files that would be changed: {files_that_would_change}")
    else:
        print(f"Files actually changed: {files_actually_changed}")

if __name__ == "__main__":
    main()