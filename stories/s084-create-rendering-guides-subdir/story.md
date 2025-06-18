---
id: "s084-create-rendering-guides-subdir"
title: "Create 'ai-guides/contrib/rendering/' Subdirectory and Refactor Rendering Guides"
status: "Done"
priority: "Medium"
tags: "refactoring;documentation;ai-guide;implementation;file-structure"
resolution: "Implemented"
---

# Story: s084-create-rendering-guides-subdir - Create 'ai-guides/contrib/rendering/' Subdirectory and Refactor Rendering Guides

## Description

As a Vibe Tasking maintainer, I want to create a new subdirectory `ai-guides/contrib/rendering/` and move existing rendering-related AI Guides into it, so that documentation about rendering techniques is centralized and easier to discover. This involves creating a `README.md` for the new directory and updating all internal links pointing to the moved guides (excluding links in finished stories/artifacts).

## Artifacts

- [`ai-guides/contrib/rendering/README.md`](../../../../ai-guides/contrib/rendering/README.md) (To be created)
- Original: [`ai-guides/contrib/ascii-art-diagrams-authoring-guide.md`](../../../../ai-guides/contrib/ascii-art-diagrams-authoring-guide.md)
- New: [`ai-guides/contrib/rendering/ascii-art-diagrams-authoring-guide.md`](../../../../ai-guides/contrib/rendering/ascii-art-diagrams-authoring-guide.md) (To be moved)
- Original: [`ai-guides/contrib/sequence-diagrams-authoring-guide.md`](../../../../ai-guides/contrib/sequence-diagrams-authoring-guide.md)
- New: [`ai-guides/contrib/rendering/sequence-diagrams-authoring-guide.md`](../../../../ai-guides/contrib/rendering/sequence-diagrams-authoring-guide.md) (To be moved)
- [`ai-guides/core/documentation-refactoring-guide.md`](../../../../ai-guides/core/documentation-refactoring-guide.md) (To be created by s083, will be consulted for link updating process)
- [`ai-guides/contrib/python-script-dry-run-guide.md`](../../../../ai-guides/contrib/python-script-dry-run-guide.md) (Reference if Python scripts are used for link updates)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Create `rendering` Subdirectory and `README.md`**

  - [x] The directory `ai-guides/contrib/rendering/` is created.
  - [x] A `README.md` file is created in `ai-guides/contrib/rendering/`.
  - [x] The `README.md` describes that the directory contains AI Guides related to "drawing" or rendering various kinds of things using Markdown, either in saved `*.md` documents or in AI chat dialogue.
  - [x] The `README.md` explicitly states it does _not_ contain an index or list of the contained files.
  - [x] User reviews and approves the content of `ai-guides/contrib/rendering/README.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Move Existing Rendering Guides**

  - [x] The file `ai-guides/contrib/ascii-art-diagrams-authoring-guide.md` is moved to `ai-guides/contrib/rendering/ascii-art-diagrams-authoring-guide.md`.
  - [x] The file `ai-guides/contrib/sequence-diagrams-authoring-guide.md` is moved to `ai-guides/contrib/rendering/sequence-diagrams-authoring-guide.md`.
  - [x] User confirms the files have been moved to the correct new locations.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Update Links to Moved Guides**

  - [x] **Process:** The (to be created by s083) `ai-guides/core/documentation-refactoring-guide.md` is consulted for the link updating process. (Skipped due to unavailability; best-effort approach used for internal links within moved files.)
  - [x] All internal Markdown links in the project (excluding those within `stories/sXXX-.../` directories where `sXXX` corresponds to a story with status "Done" or "Closed", and excluding links within `stories/**/artifacts/`) that previously pointed to `ai-guides/contrib/ascii-art-diagrams-authoring-guide.md` are identified. (No action taken as per user instruction.)
  - [x] All identified links are updated to point to `ai-guides/contrib/rendering/ascii-art-diagrams-authoring-guide.md`. (No action taken as per user instruction.)
  - [x] All internal Markdown links in the project (excluding specified story directories/artifacts) that previously pointed to `ai-guides/contrib/sequence-diagrams-authoring-guide.md` are identified. (No action taken as per user instruction.)
  - [x] All identified links are updated to point to `ai-guides/contrib/rendering/sequence-diagrams-authoring-guide.md`. (No action taken as per user instruction.)
  - [x] Link updates are verified (e.g., by checking a sample of modified files or using a script). (Internal links within moved guides updated and verified.)
  - [x] User confirms link updates are complete and correct.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [x] **Process:** AI performs an internal reflection on the completed story, analyzing its execution (e.g., tool usage, user feedback patterns, AC clarity, AI-Guide effectiveness).
  - [x] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [x] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [x] **Process:** AI invites the user to provide their own retrospective feedback and discusses any suggestions.
  - [x] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`. (No additional user feedback to journal at this time.)
  - [x] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
