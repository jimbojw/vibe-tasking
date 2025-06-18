id: "s061-standardize-ai-guides-naming"
title: "Standardize Naming Convention for AI-Guides and Implement Changes"
status: "Done"
priority: "Medium"
tags: "documentation;convention;refactor;ai-guide;adr"
resolution: "Implemented"

# s061-standardize-ai-guides-naming: Standardize Naming Convention for AI-Guides and Implement Changes

## Description

As a project maintainer, I want to establish and implement a standardized naming convention for files within the `ai-guides/` directory and its subdirectories. This includes codifying the convention in an ADR, updating relevant guidance documentation, and renaming existing files to adhere to the new standard. The goal is to improve discoverability, consistency, and maintainability of AI-Guide documents.

The agreed-upon convention is: `[plural-object-noun]-[gerund-action]-guide.md` (e.g., `stories-planning-guide.md`), with singular object nouns for abstract concepts (e.g., `onboarding-updating-guide.md`).

## Artifacts

- New ADR: `docs/adrs/adr023-standardize-ai-guides-naming.md` (to be created)
- Updated AI-Guide: (e.g., `ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md` - to be updated)
- List of files to be renamed in `ai-guides/` (to be compiled)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

**[x] Checkpoint 1: Define and Document Naming Convention in ADR**

- [x] Finalize the 'plural-object-noun-gerund-action-guide.md' naming convention, including handling of singular abstract concepts.
- [x] Draft a new ADR (`adr023-standardize-ai-guides-naming.md`) detailing the chosen convention, rationale, examples, and any exceptions.
- [x] Review the ADR for clarity, completeness, and accuracy.
- [x] User confirms ADR is satisfactory and ready to be considered "Accepted" (status to be updated in ADR frontmatter).
  - [x] **Process:** All ACs within this 'Define and Document Naming Convention in ADR' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Define and Document Naming Convention in ADR' Checkpoint and any significant decisions made within it.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

**[x] Checkpoint 2: Update Guidance Documentation**

- [x] Identify the primary AI-Guide that provides instructions on creating/designing other AI-Guides (e.g., `ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md` or similar).
- [x] Update this guide to incorporate a clear section detailing the new naming convention, its rationale, and examples.
- [x] Review the updated guide for clarity, accuracy, and consistency with the ADR.
  - [x] **Process:** All ACs within this 'Update Guidance Documentation' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Update Guidance Documentation' Checkpoint and any significant decisions made within it.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

**[x] Checkpoint 3: Implement File Renaming**

- [x] Compile a comprehensive list of all files within `ai-guides/` and its subdirectories that do not currently conform to the new naming convention.
- [x] For each non-conforming file, document its proposed new name.
- [x] (Requires Code Mode or manual action) Rename all identified files according to the new convention.
- [x] (Requires Code Mode or manual action) Identify and update any internal project links (e.g., in other guides, stories, `CONTEXT.md`) that pointed to the old filenames to now point to the new filenames.
- [x] Verify all renames and link updates have been successfully applied.
  - [x] **Process:** All ACs within this 'Implement File Renaming' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Implement File Renaming' Checkpoint and any significant decisions made within it.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

**Checkpoint 4: Final Review and Closure (Standard)**

- [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
- [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
- [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
- [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
