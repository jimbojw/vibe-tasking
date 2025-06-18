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

# Define the transformations
TRANSFORMATIONS = [
    (r'docs/ai-guides/vibe-tasking/ai-guide\.template\.md', r'docs/ai-guides/core/ai-guides/ai-guide.template.md'),
    (r'docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide\.md', r'docs/ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md'),
    (r'docs/ai-guides/vibe-tasking/', r'docs/ai-guides/core/'),
    (r'docs/ai-guides/adr\.template\.md', r'docs/ai-guides/contrib/adrs/adr.template.md'),
    (r'docs/ai-guides/adrs-writing-guide\.md', r'docs/ai-guides/contrib/adrs/adrs-writing-guide.md'),
    (r'docs/ai-guides/article\.template\.md', r'docs/ai-guides/contrib/articles/article.template.md'),
    (r'docs/ai-guides/articles-writing-guide\.md', r'docs/ai-guides/contrib/articles/articles-writing-guide.md'),
    (r'docs/ai-guides/tutorials/', r'docs/ai-guides/contrib/tutorials/'),
    (r'docs/ai-guides/ascii-art-diagrams-authoring-guide\.md', r'docs/ai-guides/contrib/ascii-art-diagrams-authoring-guide.md'),
    (r'docs/ai-guides/sequence-diagrams-authoring-guide\.md', r'docs/ai-guides/contrib/sequence-diagrams-authoring-guide.md'),
    (r'docs/ai-guides/updating-onboarding-guide\.md', r'docs/ai-guides/contrib/updating-onboarding-guide.md'),
]

def get_story_status(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            in_frontmatter = False
            for _ in range(20): 
                line = f.readline()
                if not line:
                    break
                line_stripped = line.strip()
                if line_stripped == '---':
                    if not in_frontmatter:
                        in_frontmatter = True
                        continue
                    else: 
                        return None
                if in_frontmatter:
                    match = re.match(r'^status:\s*"([^"]+)"', line_stripped)
                    if match:
                        return match.group(1)
            return None
    except Exception:
        return None

def update_links_in_file_content(content, filepath_for_dry_run_msg, dry_run=True):
    """
    Processes content for link updates.
    Returns (modified_content, changes_made_bool)
    """
    modified_content = content
    changes_made = False

    for old_pattern, new_path in TRANSFORMATIONS:
        modified_content, num_subs = re.subn(old_pattern, new_path.replace('\\', r'\\'), modified_content)
        if num_subs > 0:
            changes_made = True
            if dry_run:
                print(f"  Would replace '{old_pattern}' with '{new_path}' ({num_subs} times) in {filepath_for_dry_run_msg}")
    return modified_content, changes_made

def main():
    parser = argparse.ArgumentParser(description="Update links in Markdown files after docs/ai-guides restructuring.")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be changed without modifying files.")
    parser.add_argument('--path', default='docs', help="Directory to scan for Markdown files (default: 'docs').")
    args = parser.parse_args()

    print(f"Starting link update script. Dry run: {args.dry_run}. Path: {args.path}")
    
    total_md_files_found = 0
    files_skipped_artifacts = 0
    files_skipped_status = 0
    files_processed_for_changes = 0
    files_that_would_change = 0
    files_actually_changed = 0

    for root, dirs, files in os.walk(args.path):
        # Prune 'artifacts' directories from being walked further
        if 'artifacts' in dirs:
            dirs.remove('artifacts')

        for filename in files:
            if not filename.endswith(".md"):
                continue
            
            total_md_files_found += 1
            filepath = os.path.join(root, filename)
            normalized_filepath = filepath.replace("\\", "/") # For consistent path segment checking

            # Skip if path contains '/artifacts/' segment (covers files if os.walk started deep)
            if "/artifacts/" in normalized_filepath:
                # print(f"Skipping (in artifacts path): {filepath}") # Optional debug
                files_skipped_artifacts += 1
                continue

            # Story status checks
            is_story_file = "docs/stories/s" in normalized_filepath and filename == "story.md"
            is_journal_file = "docs/stories/s" in normalized_filepath and filename == "journal.md"
            
            skip_due_to_status_flag = False
            if is_story_file:
                status = get_story_status(filepath)
                if status in ["Done", "Closed"]:
                    print(f"Skipping story.md (status: {status}): {filepath}")
                    files_skipped_status += 1
                    skip_due_to_status_flag = True
            elif is_journal_file:
                story_md_path = os.path.join(os.path.dirname(filepath), "story.md")
                if os.path.exists(story_md_path):
                    status = get_story_status(story_md_path)
                    if status in ["Done", "Closed"]:
                        print(f"Skipping journal.md (story status: {status}): {filepath}")
                        files_skipped_status += 1
                        skip_due_to_status_flag = True
            
            if skip_due_to_status_flag:
                continue

            # If not skipped, proceed with processing
            print(f"Processing: {filepath}")
            files_processed_for_changes += 1
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    original_content = f.read()
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")
                continue

            modified_content, changes_were_made = update_links_in_file_content(original_content, filepath, dry_run=args.dry_run)

            if changes_were_made:
                if args.dry_run:
                    files_that_would_change += 1
                    # DRY RUN message is now part of update_links_in_file_content if changes are found
                else:
                    try:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(modified_content)
                        print(f"MODIFIED: File '{filepath}'")
                        files_actually_changed += 1
                    except Exception as e:
                        print(f"Error writing file {filepath}: {e}")
            
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