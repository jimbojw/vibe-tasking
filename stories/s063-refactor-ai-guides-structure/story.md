---
id: "s063-refactor-ai-guides-structure"
title: "Refactor docs/ai-guides Structure and Update Cross-References"
status: "Done"
priority: "Medium"
tags: "refactoring;documentation;scripting"
resolution: "Implemented"
---

# Story: s063-refactor-ai-guides-structure - Refactor docs/ai-guides Structure and Update Cross-References

## Description

As a project maintainer, I want to restructure the `docs/ai-guides/` directory and update all affected cross-references so that the AI guide documentation is better organized and all links remain functional.

### Current Structure:

The `docs/ai-guides/` directory currently contains:

- A `vibe-tasking/` subdirectory for core Vibe Tasking framework guides.
- Other guides, templates (e.g., `adr.template.md`, `adrs-writing-guide.md`), and subdirectories (e.g., `tutorials/`) at its top level.
- A `README.md` at its top level.

### Target Structure:

The `docs/ai-guides/` directory will be reorganized to have two primary subdirectories:

- `core/`: This directory will be the result of renaming the existing `docs/ai-guides/core/` directory. It will house all guides essential to the Vibe Tasking framework itself.
- `contrib/`: This directory will house all other guides, templates, and subdirectories that were previously at the top level of `docs/ai-guides/` (e.g., `adr.template.md`, `adrs-writing-guide.md`, `tutorials/`).
  The `docs/ai-guides/README.md` will remain at the top level of `docs/ai-guides/` and will be updated to describe this new `core` and `contrib` structure.

### Link Updates:

After the file and directory restructuring, an ad-hoc Python script will be developed and used to find and replace outdated cross-references throughout the project. This script will adhere to the practices outlined in `@/docs/ai-guides/core/python-script-dry-run-guide.md` (note: this path will become `@/docs/ai-guides/core/python-script-dry-run-guide.md` after the refactor), including a `--dry-run` mode and user confirmation before live execution.

## Artifacts

- [ADR-025: Restructure docs/ai-guides Directory for Clarity](../../adrs/adr-025-restructure-ai-guides-directory.md)
- [Python Link Update Script](artifacts/update_ai_guides_links.py) (To be created)
- [List of files/dirs to move](artifacts/ai_guides_refactor_plan.md) (To be created, or documented in journal)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Plan and Confirm Refactoring Strategy**

  - [ ] Current structure of `docs/ai-guides/` listed and documented (e.g., in journal or `artifacts/ai_guides_refactor_plan.md`).
  - [ ] Target structure with `core/` and `contrib/` subdirectories clearly defined.
  - [ ] A comprehensive list of all files and directories to be moved, detailing their current and new locations, is created.
  - [x] An ADR is drafted (using `docs/ai-guides/contrib/adrs/adr.template.md` - path will be valid post-refactor) documenting the decision to restructure `docs/ai-guides/`, its rationale, and consequences.
  - [x] The drafted ADR (e.g., `docs/adrs/adr-XXX-restructure-ai-guides.md`) is reviewed and approved by the user.
  - [x] The approved ADR is linked in this story's Artifacts section (see above).
  - [x] User confirms the detailed refactoring plan, including the ADR.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Execute Directory and File Restructuring**

  - [x] Directory `docs/ai-guides/vibe-tasking` is renamed to `docs/ai-guides/core`. (This implicitly creates `core` with the contents of `vibe-tasking`)
  - [x] Directory `docs/ai-guides/contrib` is created.
  - [x] New authoring subdirectories (`core/ai-guides/`, `contrib/adrs/`, `contrib/articles/`) are created; relevant files moved into them; remaining specified items moved from `docs/ai-guides/` to `docs/ai-guides/contrib/`.
  - [x] The `docs/ai-guides/README.md` remains in `docs/ai-guides/`.
  - [x] File system changes are verified to ensure all items are in their correct new locations.
  - [x] User confirms the file system restructuring is complete and correct.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Update `docs/ai-guides/README.md`**

  - [x] Draft content for `docs/ai-guides/README.md` to accurately describe the new `core/` and `contrib/` directory structure and their purposes.
  - [x] User reviews and approves the drafted changes for `docs/ai-guides/README.md`.
  - [x] The approved changes are applied to `docs/ai-guides/README.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Develop Link Update Script**

  - [x] A Python script is designed to identify and update outdated cross-references throughout the project, considering the new `docs/ai-guides/core/` and `docs/ai-guides/contrib/` paths.
  - [x] The Python script implements a `--dry-run` argument to preview changes without modifying files.
  - [x] The Python script is written and its code is presented to the user for review.
  - [x] User reviews and approves the Python script code.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Execute Link Update Script (Dry Run and Live Run)**

  - [x] The Python script is executed with the `--dry-run` flag across the project.
  - [x] The output of the dry run (detailing all proposed link changes) is presented to the user.
  - [x] User confirms the dry-run output is correct and approves the live run.
  - [x] The Python script is executed in live mode to apply the link updates.
  - [x] A sample of updated links is verified to ensure correctness.
  - [x] User confirms that link updates are complete and appear correct.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Design Relative Path Update Script**

  - [x] Define strategy for identifying relative links (e.g., those not starting with `http`, `/`, or `docs/`).
  - [x] Outline logic for resolving relative links to an absolute-like project path based on their containing file's location.
  - [x] Detail method for mapping these resolved old absolute-like paths to their new absolute-like locations post-refactor.
  - [x] Specify how to convert the new absolute-like target path back to a new relative path, correct for the containing file.
  - [x] User reviews and approves the design for the relative path update script.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Develop Relative Path Update Script**

  - [x] A new Python script (e.g., `update_relative_links.py` in artifacts) is written based on the approved design.
  - [x] The script implements a `--dry-run` argument.
  - [x] The script code is presented to the user for review.
  - [x] User reviews and approves the Python script code for relative paths.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Execute Relative Path Update Script (Dry Run and Live Run)**

  - [x] The relative path Python script is executed with the `--dry-run` flag across the project.
  - [x] The output of the dry run (detailing all proposed relative link changes) is presented to the user.
  - [x] User confirms the dry-run output is correct and approves the live run for relative links.
  - [x] The relative path Python script is executed in live mode to apply the link updates.
  - [x] A sample of updated relative links is verified to ensure correctness.
  - [x] User confirms that relative link updates are complete and appear correct.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval is obtained to proceed.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
