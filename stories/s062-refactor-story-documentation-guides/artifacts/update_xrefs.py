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
import argparse

# Define search and replace patterns
REPLACEMENTS = [
    (
        "docs/stories/README.md",
        "docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md"
    ),
    (
        "docs/ai-guides/vibe-tasking/stories-planning-guide.md",
        "docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md"
    ),
    (
        "docs/ai-guides/vibe-tasking/stories-working-guide.md",
        "docs/ai-guides/vibe-tasking/stories/stories-working-guide.md"
    )
]

# Files/paths to explicitly skip
# These were already manually updated or are test data that shouldn't change
FILES_TO_SKIP_PROCESSING = [
    "CONTEXT.md", # Root CONTEXT.md
    "README.md",  # Root README.md
    "docs/articles/onboarding/01-introduction.md",
    "docs/articles/onboarding/03-installation.md",
    "docs/articles/onboarding/04-planning-stories.md",
    "docs/articles/onboarding/05-working-with-stories.md",
    "docs/articles/onboarding/06-example-walkthrough.md",
    "docs/ai-guides/vibe-tasking/context-documents-writing-guide.md",
    "docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md",
    "docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md", # The new guide itself
    "docs/adrs/adr-011-story-readme-sot.md",
    "docs/adrs/adr-019-adopt-sibling-template-convention.md",
    "docs/adrs/adr-024-story-documentation-refactor.md",
    # s062 (this story's) files are generally okay as they were written with new paths
    "docs/stories/s062-refactor-story-documentation-guides/story.md",
    "docs/stories/s062-refactor-story-documentation-guides/journal.md",
    "docs/stories/s062-refactor-story-documentation-guides/artifacts/content_migration_and_new_readme_plan.md",
    "docs/stories/s062-refactor-story-documentation-guides/artifacts/stories-structuring-guide-outline.md",
    "docs/stories/s062-refactor-story-documentation-guides/artifacts/stories-planning-guide-outline.md",
    "docs/stories/s062-refactor-story-documentation-guides/artifacts/stories-working-guide-outline.md",
]

# Path segments to skip (e.g. specific story artifacts)
PATH_SEGMENTS_TO_SKIP = [
    "docs/stories/s043-research-zip-installer-path/artifacts/"
]

def update_file_content(filepath, dry_run=False):
    """Reads a file, performs replacements, and writes back if not dry_run."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    original_content = content
    modified_content = content
    made_change_overall = False # Tracks if any replacement changed the content

    for old_path, new_path in REPLACEMENTS:
        if old_path in modified_content:
            temp_content = modified_content.replace(old_path, new_path)
            if temp_content != modified_content: # Check if this specific replacement had an effect
                modified_content = temp_content
                made_change_overall = True


    if made_change_overall:
        print(f"Changes proposed for {filepath}:")
        if dry_run:
            # For dry run, just indicate which replacements would occur
            for old_path, new_path in REPLACEMENTS:
                if old_path in original_content and new_path in modified_content and original_content.count(old_path) > 0 :
                     # A bit heuristic: if old path was there and new one is now, and old one is gone from where it was
                    if original_content.replace(old_path,new_path) == modified_content or old_path not in modified_content:
                        print(f"  Would replace '{old_path}' with '{new_path}'")
        else:
            try:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(modified_content)
                print(f"Updated {filepath}")
            except Exception as e:
                print(f"Error writing {filepath}: {e}")
                return False
        return True # A change was made (or would be made)
    elif dry_run: # If no changes were made AND it's a dry run
        print(f"No changes proposed for {filepath}")
    return False # No change was made

def main():
    parser = argparse.ArgumentParser(description="Update cross-references in project files.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print changes that would be made without modifying files."
    )
    parser.add_argument(
        "--xrefs-file",
        default="../../../../.tmp_ai_output/s062_cross_references.txt", # Relative from script location
        help="Path to the file containing the list of files to process."
    )
    args = parser.parse_args()

    # Determine project root assuming script is in docs/stories/sXXX/artifacts/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, "../../../.."))
    
    xrefs_filepath_abs = os.path.join(project_root, args.xrefs_file.replace('../../../../', '')) # Adjust for relative path from root

    if not os.path.exists(xrefs_filepath_abs):
        print(f"Error: Cross-references file not found at {xrefs_filepath_abs}")
        return

    print(f"Project root determined as: {project_root}")
    print(f"Processing files listed in: {xrefs_filepath_abs}")
    if args.dry_run:
        print("DRY RUN: No files will be modified.")

    files_processed_count = 0
    files_changed_count = 0
    
    # Ensure FILES_TO_SKIP_PROCESSING and PATH_SEGMENTS_TO_SKIP use normalized forward slashes
    normalized_files_to_skip = [p.replace(os.sep, '/') for p in FILES_TO_SKIP_PROCESSING]
    normalized_path_segments_to_skip = [p.replace(os.sep, '/') for p in PATH_SEGMENTS_TO_SKIP]


    with open(xrefs_filepath_abs, 'r', encoding='utf-8') as f:
        for line in f:
            filepath_from_grep = line.strip()
            if not filepath_from_grep:
                continue

            # Path from grep usually starts with ./
            if filepath_from_grep.startswith("./"):
                path_relative_to_root = filepath_from_grep[2:]
            else:
                path_relative_to_root = filepath_from_grep
            
            abs_filepath = os.path.join(project_root, path_relative_to_root)
            
            # Normalize for skip checks
            normalized_path_for_skip_check = path_relative_to_root.replace(os.sep, '/')

            if normalized_path_for_skip_check in normalized_files_to_skip:
                # print(f"Skipping (explicitly listed): {normalized_path_for_skip_check}")
                continue

            skip_by_segment = False
            for skip_segment in normalized_path_segments_to_skip:
                if normalized_path_for_skip_check.startswith(skip_segment):
                    # print(f"Skipping (path segment): {normalized_path_for_skip_check}")
                    skip_by_segment = True
                    break
            if skip_by_segment:
                continue
            
            if os.path.isfile(abs_filepath):
                files_processed_count += 1
                if update_file_content(abs_filepath, args.dry_run):
                    files_changed_count +=1
            else:
                print(f"Warning: File not found or is not a file: {abs_filepath} (original: {line.strip()})")
    
    print(f"\n--- Summary ---")
    print(f"Files considered for processing (after skips): {files_processed_count}")
    if args.dry_run:
        print(f"Files that would be changed: {files_changed_count}")
    else:
        print(f"Files actually changed: {files_changed_count}")

if __name__ == "__main__":
    main()