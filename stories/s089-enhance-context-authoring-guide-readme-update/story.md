---
id: "s089-enhance-context-authoring-guide-readme-update"
title: "Enhance Context Authoring Guide to Add CONTEXT.md Usage to Host README"
status: "To Do"
priority: "Medium"
tags: "context;documentation;readme;onboarding;ai-guides;lightweight"
resolution: "Unresolved"
---

# Story: s089-enhance-context-authoring-guide-readme-update - Enhance Context Authoring Guide to Add CONTEXT.md Usage to Host README

## Description

As a user of Vibe Tasking, I want the AI assistant that helps me create my project's `CONTEXT.md` file to also offer to update my project's main `README.md` with instructions on how to use `@CONTEXT.md` to initialize chat sessions, so that this crucial step is clearly documented for all project collaborators.

This involves updating the [`ai-guides/core/context/context-documents-authoring-guide.md`](ai-guides/core/context/context-documents-authoring-guide.md) to add a new procedural step for the AI assistant. After successfully guiding the user through `CONTEXT.md` creation, the AI should:

1.  Check for the existence of a `README.md` in the host project root.
2.  If it exists, offer to add a section or update an existing one with clear instructions on how to start an AI chat session using `@CONTEXT.md`.
3.  Provide example wording for these `README.md` instructions.
4.  If the user agrees, attempt to make the modification to `README.md` (similar to how `INSTALL_VIBE_TASKING.md` handles adding submodule instructions).

## Artifacts

- [`ai-guides/core/context/context-documents-authoring-guide.md`](ai-guides/core/context/context-documents-authoring-guide.md) (The primary file to be modified)
- [`inbox/2025-06-10-enhance-contextmd-training-visibility-in-install-guide.md`](inbox/2025-06-10-enhance-contextmd-training-visibility-in-install-guide.md) (Original inbox item that sparked this idea)
- (Potential) Example `README.md` snippet for `CONTEXT.md` usage instructions.

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced (with correct timestamp).
  - [ ] **Process:** AI has performed spot grooming (consulting `stories-spot-grooming-guide.md`) and assisted in reviewing/confirming AC validity and completeness (especially the 'Core Task' AC).
  - [ ] **Process:** User confirms the 'Core Task' AC below is accurate, complete, and suitable for a lightweight story.
  - [ ] **Core Task:** The [`ai-guides/core/context/context-documents-authoring-guide.md`](ai-guides/core/context/context-documents-authoring-guide.md) is updated to include instructions for the AI assistant to:
    - After `CONTEXT.md` creation, offer to add usage instructions for `@CONTEXT.md` to the host project's `README.md`.
    - Include example wording for these `README.md` instructions.
    - Detail the process for the AI to attempt this `README.md` modification if the user agrees.
  - [ ] **Core Task:** The updated `context-documents-authoring-guide.md` is reviewed for clarity, accuracy, and completeness of the new procedural steps.
  - [ ] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [ ] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
