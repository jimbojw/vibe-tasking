---
id: "s064-refactor-directory-structure-ai-guides-stories"
title: "Refactor Directory Structure: Promote ai-guides and stories to Root"
status: "Done"
priority: "Medium"
tags: "refactor;directory-structure;links;adr;python"
resolution: "Implemented"
---

# Story: s064-refactor-directory-structure-ai-guides-stories - Refactor Directory Structure: Promote ai-guides and stories to Root

## Description

As a project maintainer, I want to move the `ai-guides` and `stories` directories to be top-level directories in the project root (i.e., `ai-guides/` and `stories/`). This change aims to elevate their importance and improve project organization. This will require moving the directories and then updating all internal Markdown links that are broken by this move, using a Python script. An Architecture Decision Record (ADR) should also be created to document this change.

## Artifacts

- Guide for Python script dry run: `../../ai-guides/core/python-script-dry-run-guide.md`
- Guide for writing ADRs: `../../ai-guides/contrib/adrs/adrs-writing-guide.md`
- Similar link update script in story s063: `../s063-refactor-ai-guides-structure/story.md`
- Python script to be created: `artifacts/update_moved_links.py` (tentative location)
- ADR to be created: `../../../adrs/adr-XXX-promote-docs-subdirs.md` (tentative location)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Author ADR for Directory Structure Change**

  - [x] **Process:** ADR is drafted following the guidance in `../../ai-guides/contrib/adrs/adrs-writing-guide.md`.
  - [x] **Content:** ADR proposes moving `ai-guides` to `ai-guides/` (root) and `stories` to `stories/` (root).
  - [x] **Content:** ADR clearly states the rationale for this change (e.g., elevating visibility, simplifying paths).
  - [x] **Content:** ADR outlines the necessity of a script to update internal Markdown links affected by the move.
  - [x] **Process:** ADR is reviewed and accepted by the user.
  - [x] **Process:** The new ADR file (e.g., `adr-XXX-promote-docs-subdirs.md`) is created in the `docs/adrs/` directory.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Move Directories**

  - [x] **Action:** The `ai-guides` directory is moved to `ai-guides/` at the project root.
  - [x] **Action:** The `stories` directory is moved to `stories/` at the project root.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Develop Link Update Script**

  - [x] **Action:** A Python script (e.g., `update_moved_links.py`) is created, potentially in this story's `artifacts/` directory.
  - [x] **Functionality:** The script is designed to identify all Markdown files (`.md`) within the newly moved `ai-guides/` and `stories/` directories, the remaining `docs/` subdirectories (e.g., `docs/adrs`, `docs/articles`, `docs/reference`), and the root `README.md` and `CONTEXT.md`.
  - [x] **Functionality:** The script correctly updates relative Markdown links that previously pointed to `ai-guides/...` to now point to `ai-guides/...` (adjusting for path depth).
  - [x] **Functionality:** The script correctly updates relative Markdown links that previously pointed to `stories/...` to now point to `stories/...` (adjusting for path depth).
  - [x] **Functionality:** The script correctly handles various link depths and relative path constructions (e.g., `../`, `../../`, `./`).
  - [x] **Process:** The script includes a `--dry-run` mode that logs intended changes without modifying files, as per `../../ai-guides/core/python-script-dry-run-guide.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Execute Link Update Script**

  - [x] **Action:** The Python script is executed with the `--dry-run` flag.
  - [x] **Process:** The output of the dry run (detailing all proposed link changes) is presented to the user for review.
  - [x] **Process:** User explicitly confirms the dry run output is correct and approves proceeding with the live run.
  - [x] **Action:** The Python script is executed without the `--dry-run` flag to apply the changes.
  - [x] **Verification:** A selection of modified files (e.g., 3-5 files from different locations like root, `ai-guides`, `stories`, `docs/articles`) are manually inspected to confirm links have been updated correctly.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Further Enhance and Re-Execute Python Script**

  - [x] **Action (User):** Revert changes made by previous `sed` commands. (This step is now complete by the user).
  - [x] **Analysis:** Review `search_files` output (from `grep` simulation that showed remaining `ai-guides` paths after Python script V2 execution) to understand all patterns of incorrect links that need fixing (bare paths, internal relative links, ADRs to skip, etc.).
  - [x] **Action:** Further enhance the Python script `artifacts/update_moved_links.py` to:
    - Add logic to skip processing for all files matching `docs/adrs/adr-*.md` (but ensure `docs/adrs/README.md` is still processed if it's in a scan location).
    - Improve identification and transformation of bare path strings (e.g., `` `ai-guides/...` ``).
    - Ensure accurate recalculation of relative links for files _within_ the moved `ai-guides/` and `stories/` directories.
    - Retain existing logic for skipping `artifacts/` directories and "Done"/"Closed" stories.
  - [x] **Process:** The script includes a `--dry-run` mode.
  - [x] **Action:** The further enhanced Python script is executed with the `--dry-run` flag, and output is saved to `artifacts/dry_run_output_v3.txt`.
  - [x] **Process:** The output of this new dry run is presented to the user for review.
  - [x] **Process:** User explicitly confirms the new dry run output is correct and approves proceeding with its live run.
  - [x] **Action:** The further enhanced Python script is executed without the `--dry-run` flag to apply the changes, and output is saved to `artifacts/live_run_output_v3.txt`.
  - [x] **Verification:** `search_files` is used again for `ai-guides` and `stories` to confirm all instances (excluding intentionally skipped ADRs/stories) are corrected.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
