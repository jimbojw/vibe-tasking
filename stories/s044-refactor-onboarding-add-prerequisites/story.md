---
id: "s044-refactor-onboarding-add-prerequisites"
title: "Refactor Onboarding Documentation to Add Prerequisites and Update Structure"
status: "Done"
priority: "High"
tags: "documentation;onboarding;refactor"
resolution: "Implemented"
---

# Story: s044 - Refactor Onboarding Documentation to Add Prerequisites and Update Structure

## Description

This story involves a significant refactoring of the `docs/onboarding/` documentation. The primary goals are to:

1.  Introduce a new "Prerequisites" document (`02-prerequisites.md`) early in the onboarding flow. This document will include existing prerequisite text and a tailored summary of AI assistant capabilities relevant to Vibe Tasking.
2.  Renumber all subsequent onboarding documents (current 02-07 will become 03-08).
3.  Update all internal links within the project (excluding historical records in completed stories/journals) to reflect the new numbering and filenames.
4.  Create a new guide (`docs/guides/updating-onboarding-guide.md`) that codifies the process of refactoring the onboarding documentation sequence.

## Related Stories

- **Unblocks:** Completion of this story unblocks [s042 - Harmonize Onboarding Documentation](../s042-harmonize-onboarding-docs/story.md) and requires updating its scope.

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** An initial journal entry is appended to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list (including all Checkpoints and their nested ACs) for this story is accurate and complete before proceeding.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Create Prerequisites Document' Checkpoint.

- [x] **Checkpoint: Create Prerequisites Document (`02-prerequisites.md`)**

  - [x] A new file `docs/onboarding/02-prerequisites.md` is created.
  - [x] The "Prerequisites" section from the original `docs/onboarding/02-installation.md` is moved into `docs/onboarding/02-prerequisites.md`.
  - [x] An introductory paragraph explaining the importance of AI assistant capabilities for Vibe Tasking is added to `docs/onboarding/02-prerequisites.md`.
  - [x] The "Assistant Vibe Tasking Profile Summary" table is copied from `docs/reference/ai-assistant-capabilities.md` into `docs/onboarding/02-prerequisites.md`.
  - [x] A new, contextually appropriate set of footnotes for the summary table is created within `docs/onboarding/02-prerequisites.md`, tailored to the prerequisite context.
  - [x] `docs/onboarding/02-prerequisites.md` includes a prominent link to the main `docs/reference/ai-assistant-capabilities.md` document.
  - [x] **Process:** All ACs within this 'Create Prerequisites Document' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Update Installation Document' Checkpoint.

- [x] **Checkpoint: Update Installation Document (to `03-installation.md`)**

  - [x] The content of the original `docs/onboarding/02-installation.md` (excluding its old "Prerequisites" section) is written to a new file `docs/onboarding/03-installation.md`.
  - [x] The H1 title in `docs/onboarding/03-installation.md` is updated to "# 03 - Installing Vibe Tasking".
  - [x] The "Next Steps" link in `docs/onboarding/03-installation.md` is updated to point to `./04-planning-stories.md`.
  - [x] **Process:** All ACs within this 'Update Installation Document' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Renumber Subsequent Onboarding Documents' Checkpoint.

- [x] **Checkpoint: Renumber Subsequent Onboarding Documents (04-08)**

  - [x] `docs/onboarding/03-planning-stories.md` is moved/renamed to `docs/onboarding/04-planning-stories.md`, its H1 title updated to "# 04 - ...", and its "Next Steps" link updated to `./05-...md`.
  - [x] `docs/onboarding/04-working-with-stories.md` is moved/renamed to `docs/onboarding/05-working-with-stories.md`, its H1 title updated to "# 05 - ...", and its "Next Steps" link updated to `./06-...md`.
  - [x] `docs/onboarding/05-example-walkthrough.md` is moved/renamed to `docs/onboarding/06-example-walkthrough.md`, its H1 title updated to "# 06 - ...", and its "Next Steps" link updated to `./07-...md`.
  - [x] `docs/onboarding/06-workflow-feature-lifecycle.md` is moved/renamed to `docs/onboarding/07-workflow-feature-lifecycle.md`, its H1 title updated to "# 07 - ...", and its "Next Steps" link updated to `./08-...md`.
  - [x] `docs/onboarding/07-workflow-architectural-challenges.md` is moved/renamed to `docs/onboarding/08-workflow-architectural-challenges.md`, and its H1 title updated to "# 08 - ...".
  - [x] **Process:** All ACs within this 'Renumber Subsequent Onboarding Documents' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Update Onboarding README' Checkpoint.

- [x] **Checkpoint: Update Onboarding README (`docs/onboarding/README.md`)**

  - [x] The `docs/onboarding/README.md` file is updated to include a new entry for "02 - Prerequisites" linking to `./02-prerequisites.md`.
  - [x] All subsequent entries (originally 02-07) in `docs/onboarding/README.md` are renumbered to 03-08, and their links are updated accordingly.
  - [x] **Process:** All ACs within this 'Update Onboarding README' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Project-Wide Link Updates' Checkpoint.

- [x] **Checkpoint: Project-Wide Link Updates**

  - [x] All internal links to `docs/onboarding/0X-...` files throughout the project (e.g., in guides, other stories) are identified and updated to reflect the new numbering and filenames.
  - [x] **Constraint:** Links within existing `journal.md` files are NOT updated.
  - [x] **Constraint:** Links within `story.md` files for stories with `status: "Done"` or `status: "Closed"` are NOT updated.
  - [x] For active stories (not Done/Closed) whose `story.md` links are updated, a note is appended to their respective `journal.md` files (e.g., "- System: Onboarding documentation links updated due to refactoring of the onboarding sequence.").
  - [x] **Process:** All ACs within this 'Project-Wide Link Updates' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Create Onboarding Update Guide' Checkpoint.

- [x] **Checkpoint: Create Onboarding Update Guide**

  - [x] A new guide file `docs/guides/updating-onboarding-guide.md` is created.
  - [x] The guide documents the general process for refactoring the onboarding documentation sequence, based on the steps performed in this story.
  - [x] **Process:** All ACs within this 'Create Onboarding Update Guide' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Update Meta-Documentation for Onboarding Changes' Checkpoint.

- [x] **Checkpoint: Update Meta-Documentation for Onboarding Changes**

  - [x] The `docs/guides/updating-onboarding-guide.md` is updated to include a note/section advising AI assistants to encourage creating a story for complex onboarding changes, referencing the guide itself for the process.
  - [x] The root `CONTEXT.md` file is updated under "Task-Specific Instructions for AI Assistants" to instruct AI assistants to consult `docs/guides/updating-onboarding-guide.md` when users request significant changes to onboarding documentation, and to suggest creating a story for such complex changes.
  - [x] **Process:** All ACs within this 'Update Meta-Documentation for Onboarding Changes' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Post-Completion Tasks & Unblocking' Checkpoint.

- [x] **Checkpoint: Post-Completion Tasks & Unblocking**

  - [x] **Process:** Update `docs/stories/s042-harmonize-onboarding-docs/story.md`:
    - [x] Change its `status` frontmatter field from "Blocked" to "To Do".
    - [x] Change its `resolution` frontmatter field from "Pending completion of s044-refactor-onboarding-add-prerequisites" back to "Unresolved".
    - [x] Update the "Files to Harmonize" list in its description to reflect the new 01-08 onboarding document structure (i.e., `docs/onboarding/README.md`, `docs/onboarding/01-introduction.md`, `docs/onboarding/02-prerequisites.md`, `docs/onboarding/03-installation.md`, `docs/onboarding/04-planning-stories.md`, `docs/onboarding/05-working-with-stories.md`, `docs/onboarding/06-example-walkthrough.md`, `docs/onboarding/07-workflow-feature-lifecycle.md`, `docs/onboarding/08-workflow-architectural-challenges.md`).
    - [x] Update the list of files in the Acceptance Criteria under the "Checkpoint: Implementation of Harmonization Plan" in `s042` to match the new 01-08 structure.
    - [x] Remove or update the note in `s042`'s description about its scope needing review post-s044.
  - [x] **Process:** All ACs within this 'Post-Completion Tasks & Unblocking' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Final Review and Closure' Checkpoint.

- [x] **Checkpoint: Final Review and Closure**
  - [x] User confirms all file renames, content changes, link updates, and the new guide are correct and complete.
  - [x] **Process:** Story status is updated to "Done" and `resolution` is set appropriately (e.g., "Implemented") upon successful completion and user confirmation.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
