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

# PATH_TRANSFORMATIONS defines how project-relative paths of link targets are changed.
PATH_TRANSFORMATIONS = [
    ('docs/ai-guides', 'ai-guides'),
    ('docs/stories', 'stories'),
]

# Regex to find Markdown links: [text](link)
MD_LINK_REGEX = re.compile(r'(\[([^\]]*)\]\(([^)\s]+)\))')

# Regexes for bare paths. These aim to match 'docs/ai-guides' or 'docs/stories'
# when they appear as a path segment, potentially followed by more path components.
# We use word boundaries (\b) to avoid matching parts of other words.
# And negative lookbehind (?<!]\() to avoid re-processing markdown links.
# And negative lookahead (?!\S) to ensure it's not part of a non-whitespace sequence (like a full URL).
# Or more simply, just replace the direct string if it's safer given the context.
# For this version, we'll stick to targeted string replacement in Phase 2,
# but make the dry run output more informative.

REPLACEMENT_MAP = {
    "docs/ai-guides": "ai-guides",
    "docs/stories": "stories"
}
# Specific regex for replacing bare paths to be more precise
# This looks for the exact strings, possibly within backticks or as part of a sentence.
# It ensures we don't accidentally replace parts of words or URLs.
# The key is to replace 'docs/ai-guides' with 'ai-guides' and 'docs/stories' with 'stories'.
# We will use a simple string.replace for phase 2, but be very specific in logging.
BARE_PATH_REPLACEMENTS = [
    ("docs/ai-guides", "ai-guides"),
    ("docs/stories", "stories")
]


def get_story_status(filepath_abs):
    """Reads the status from a story.md file's frontmatter."""
    try:
        with open(filepath_abs, 'r', encoding='utf-8') as f:
            in_frontmatter = False
            for _ in range(20):  # Check first 20 lines for frontmatter
                line = f.readline()
                if not line:
                    break
                line_stripped = line.strip()
                if line_stripped == '---':
                    in_frontmatter = not in_frontmatter
                    if not in_frontmatter:  # End of frontmatter
                        break
                    continue
                if in_frontmatter:
                    match = re.match(r'^status:\s*"([^"]+)"', line_stripped)
                    if match:
                        return match.group(1)
            return None
    except Exception:
        return None

def normalize_path_from_project_root(path_str, project_root_abs_str):
    """Normalizes a path and makes it relative to the project root, using forward slashes."""
    project_root_path = Path(project_root_abs_str)
    normalized_path = Path(os.path.normpath(path_str))

    abs_path_to_check = normalized_path
    if not normalized_path.is_absolute():
        abs_path_to_check = Path(os.path.abspath(os.path.join(project_root_abs_str, path_str)))

    if abs_path_to_check.as_posix().startswith(project_root_path.as_posix() + '/'):
        return abs_path_to_check.relative_to(project_root_path).as_posix()
    elif abs_path_to_check == project_root_path:
         return "." 
    return abs_path_to_check.as_posix() 

def process_file_content(content, current_file_abs_path_str, project_root_abs_str, dry_run=True):
    modified_content = content
    changes_made_to_file = False
    
    current_file_dir_abs_str = os.path.dirname(current_file_abs_path_str)
    current_file_project_rel_str = normalize_path_from_project_root(current_file_abs_path_str, project_root_abs_str)

    # Phase 1: Process Markdown-style links [text](target)
    def replace_markdown_link(match):
        nonlocal changes_made_to_file
        full_match_text = match.group(1)
        link_text = match.group(2)
        original_link_target = match.group(3)

        if original_link_target.startswith(('http://', 'https://', '/', '#')) or Path(original_link_target).is_absolute():
            return full_match_text

        resolved_current_target_abs_str = os.path.normpath(os.path.join(current_file_dir_abs_str, original_link_target))
        old_project_path_str = normalize_path_from_project_root(resolved_current_target_abs_str, project_root_abs_str)
        
        new_project_path_str = old_project_path_str
        transformed_md_link = False

        for old_prefix, new_prefix in PATH_TRANSFORMATIONS:
            if old_project_path_str == old_prefix: 
                new_project_path_str = new_prefix
                transformed_md_link = True
                break
            if old_project_path_str.startswith(old_prefix + '/'): 
                new_project_path_str = new_prefix + old_project_path_str[len(old_prefix):]
                transformed_md_link = True
                break
        
        if transformed_md_link:
            new_target_abs_str = os.path.join(project_root_abs_str, new_project_path_str)
            new_relative_target_str = os.path.relpath(new_target_abs_str, current_file_dir_abs_str)
            new_relative_target_str = Path(new_relative_target_str).as_posix()

            if new_relative_target_str != original_link_target:
                changes_made_to_file = True
                new_link_md = f"[{link_text}]({new_relative_target_str})"
                if dry_run:
                    print(f"  MD Link Change | File: {current_file_project_rel_str}")
                    print(f"    Original: [{link_text}]({original_link_target}) -> Resolves to project path: {old_project_path_str}")
                    print(f"    New Rel.: [{link_text}]({new_relative_target_str}) (from new project path: {new_project_path_str})")
                return new_link_md
        return full_match_text

    modified_content_phase1 = MD_LINK_REGEX.sub(replace_markdown_link, content)
    if content != modified_content_phase1:
        changes_made_to_file = True

    # Phase 2: Process bare paths (e.g., `docs/ai-guides/...` in backticks or plain text)
    modified_content_phase2 = modified_content_phase1
    for old_bare_path, new_bare_path in BARE_PATH_REPLACEMENTS:
        # Count occurrences before replacement for more precise logging
        occurrences = modified_content_phase2.count(old_bare_path)
        if occurrences > 0:
            modified_content_phase2 = modified_content_phase2.replace(old_bare_path, new_bare_path)
            if modified_content_phase1 != modified_content_phase2 and not changes_made_to_file: # check if this phase made the first change
                 changes_made_to_file = True # ensure this is set if phase 1 made no changes but phase 2 did

            if dry_run: # Always log if a bare path rule *could* apply, even if content doesn't change due to prior phase
                # This specific logging will show if this rule *would* have done something
                # To be more precise, we should check if this specific replacement changed the content
                # from its state *before this specific replacement rule*.
                # For simplicity in dry_run, we'll just note the attempt.
                # A more robust dry_run for bare paths would show diffs or specific lines.
                # The current dry_run for bare paths is a bit broad.
                # Let's refine to only print if this specific replacement caused a change from the previous state of modified_content_phase2
                # This requires comparing before and after *this specific* replacement.
                # For now, the global `changes_made_to_file` will cover if *any* change happened.
                # The dry_run output for bare paths will be a summary at the end of process_file_content.
                pass # Logging for bare paths will be summarized to avoid too much noise per rule.


    if dry_run and (modified_content_phase1 != modified_content_phase2): # If phase 2 made changes
        print(f"  Bare Path(s) Change | File: {current_file_project_rel_str}")
        print(f"    Content was modified by bare path replacements (details not shown per line in dry_run for brevity).")
        # To see exact bare path changes, run without dry_run and check git diff, or enhance dry_run logging.

    modified_content = modified_content_phase2
        
    return modified_content, changes_made_to_file

def process_single_md_file(filepath_abs_str, project_root_abs_str, args):
    files_processed_for_changes = 0
    files_that_would_change = 0
    files_actually_changed = 0
    
    filepath_project_rel_str = normalize_path_from_project_root(filepath_abs_str, project_root_abs_str)

    # Skip files in 'artifacts' directories
    if 'artifacts' in Path(filepath_project_rel_str).parts:
        return 0, 0, 0 

    # Skip specific ADR files (adr-*.md), but not docs/adrs/README.md
    path_obj = Path(filepath_project_rel_str)
    if path_obj.parent.name == 'adrs' and path_obj.name.startswith('adr-') and path_obj.name != 'README.md':
        if args.dry_run: print(f"Skipping ADR file: {filepath_project_rel_str}")
        return 0,0,0
    # Also ensure docs/adrs/README.md is NOT skipped if it's directly targeted or part of 'docs' scan
    # The above rule correctly handles this: it skips adr-*.md but not README.md in adrs.

    # Story/Journal status skipping logic
    path_parts = Path(filepath_project_rel_str).parts
    filename = Path(filepath_project_rel_str).name
    is_story_file = False
    is_journal_file = False

    if len(path_parts) > 1 and path_parts[0] == 'stories' and path_parts[1].startswith('s'):
        if filename == "story.md":
            is_story_file = True
        elif filename == "journal.md":
            is_journal_file = True
    
    skip_due_to_status_flag = False
    if is_story_file:
        status = get_story_status(filepath_abs_str)
        if status in ["Done", "Closed"]:
            if args.dry_run: print(f"Skipping story.md (status: {status}): {filepath_project_rel_str}")
            skip_due_to_status_flag = True
    elif is_journal_file:
        story_md_path_abs_str = str(Path(filepath_abs_str).parent / "story.md")
        if os.path.exists(story_md_path_abs_str):
            status = get_story_status(story_md_path_abs_str)
            if status in ["Done", "Closed"]:
                if args.dry_run: print(f"Skipping journal.md (story status: {status}): {filepath_project_rel_str}")
                skip_due_to_status_flag = True
    
    if skip_due_to_status_flag:
        return 0, 0, 0

    files_processed_for_changes = 1
    
    try:
        with open(filepath_abs_str, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"Error reading file {filepath_project_rel_str}: {e}")
        return files_processed_for_changes, 0, 0

    if not args.dry_run:
         print(f"Processing: {filepath_project_rel_str}")

    modified_content, changes_were_made = process_file_content(original_content, filepath_abs_str, project_root_abs_str, dry_run=args.dry_run)

    if changes_were_made:
        if args.dry_run:
            files_that_would_change = 1 
        else:
            try:
                with open(filepath_abs_str, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"MODIFIED: File '{filepath_project_rel_str}'")
                files_actually_changed = 1
            except Exception as e:
                print(f"Error writing file {filepath_project_rel_str}: {e}")
    
    return files_processed_for_changes, files_that_would_change, files_actually_changed

def main():
    parser = argparse.ArgumentParser(description="Update links in Markdown files after moving docs/ai-guides and docs/stories to root.")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be changed without modifying files.")
    args = parser.parse_args()

    project_root_abs_str = os.path.abspath('.') 
    
    scan_locations_rel = ['ai-guides', 'stories', 'docs', 'README.md', 'CONTEXT.md']

    if args.dry_run:
        print(f"Starting link update script. Dry run: {args.dry_run}.")
    else:
        print(f"Starting link update script. APPLYING CHANGES.")

    total_md_files_found = 0
    total_files_processed_for_changes = 0
    total_files_that_would_change = 0
    total_files_actually_changed = 0

    for location_rel_str in scan_locations_rel:
        location_abs_str = os.path.join(project_root_abs_str, location_rel_str)

        if os.path.isdir(location_abs_str):
            if args.dry_run: print(f"Scanning directory: {location_rel_str}")
            for root, dirs, files in os.walk(location_abs_str):
                if 'artifacts' in dirs: 
                    dirs.remove('artifacts') 
                
                # Special handling for docs/adrs to ensure README.md is processed but adr-*.md are skipped by process_single_md_file
                if Path(root).name == 'adrs' and Path(root).parent.name == 'docs':
                    # We let process_single_md_file handle the skipping of adr-*.md
                    pass # No special directory skipping here, file-level skip is now in process_single_md_file

                for filename in files:
                    if not filename.endswith(".md"):
                        continue
                    
                    total_md_files_found += 1
                    filepath_abs_str = os.path.join(root, filename)
                    
                    processed, would_change, changed = process_single_md_file(filepath_abs_str, project_root_abs_str, args)
                    total_files_processed_for_changes += processed
                    total_files_that_would_change += would_change
                    total_files_actually_changed += changed

        elif os.path.isfile(location_abs_str) and location_rel_str.endswith(".md"):
            if args.dry_run: print(f"Scanning file: {location_rel_str}")
            total_md_files_found += 1
            processed, would_change, changed = process_single_md_file(location_abs_str, project_root_abs_str, args)
            total_files_processed_for_changes += processed
            total_files_that_would_change += would_change
            total_files_actually_changed += changed
        elif os.path.isfile(location_abs_str):
            if args.dry_run: print(f"Skipping non-Markdown file specified in scan_locations_rel: {location_rel_str}")
        else:
            print(f"Warning: Scan location not found or not a file/directory: {location_rel_str}")
            
    print(f"\nScript finished.")
    print(f"Total Markdown files encountered (across all scan locations): {total_md_files_found}")
    print(f"Total files processed for link changes: {total_files_processed_for_changes}")
    if args.dry_run:
        print(f"Total files that would be changed: {total_files_that_would_change}")
    else:
        print(f"Total files actually changed: {total_files_actually_changed}")

if __name__ == "__main__":
    main()