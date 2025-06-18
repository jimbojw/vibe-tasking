---
id: "s083-design-doc-refactoring-guide"
title: "Design Documentation Refactoring Guide"
status: "To Do"
priority: "Medium"
tags: "ai-guide;design;documentation;refactoring;core-guide"
resolution: "Unresolved"
---

# Story: s083-design-doc-refactoring-guide - Design Documentation Refactoring Guide

## Description

As a Vibe Tasking user or AI assistant, I want a clear AI Guide that details the process for refactoring documentation, specifically when files are moved (e.g., into new subdirectories within `ai-guides/core` or `ai-guides/contrib`), so that all internal links across the project are correctly updated and documentation remains consistent and accurate.

This guide will instruct an AI assistant on how to handle the link updating aspect when documentation files are moved (the files to be moved and their new locations will typically be provided as part of a story). The guide will focus on:

- Discovering existing links to the documentation files slated for moving. This can involve direct tool invocations (e.g., `search_files`) or using `execute_command` with CLI tools like `grep`.
- Modifying these links to point to the new file locations, potentially using command-line tools (e.g., inline `sed`) or by generating and using one-off scripts (e.g., Python scripts, similar to the approach in [`stories/s062-refactor-story-documentation-guides/artifacts/update_xrefs.py`](../s062-refactor-story-documentation-guides/artifacts/update_xrefs.py:0)).
- Verifying that all identified links have been correctly updated.
  The aim is to codify best practices learned from previous refactoring efforts like story `s062`.

## Artifacts

- [`ai-guides/core/documentation-refactoring-guide.md`](../../../../ai-guides/core/documentation-refactoring-guide.md) (To be created: The new AI Guide)
- [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) (Reference for designing AI Guides)
- [`stories/sXXX-example-refactor-story/story.md`](../sXXX-example-refactor-story/story.md) (To be created: A small, hypothetical story that uses this new guide for testing purposes)

- [`ai-guides/contrib/python-script-dry-run-guide.md`](../../../../ai-guides/contrib/python-script-dry-run-guide.md) (Reference for using Python scripts with dry-run capability if a script is used for link updates)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Design Documentation Refactoring Guide Content**

  - [ ] **Process:** The [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) has been consulted.
  - [ ] Draft the initial content for `ai-guides/core/documentation-refactoring-guide.md`.
  - [ ] The guide details methods for discovering existing links to specified documentation files (e.g., using `search_files` or `execute_command` with `grep`).
  - [ ] The guide provides strategies for modifying these links to point to new locations, including the use of CLI tools (e.g., `sed`) or generating one-off scripts (e.g., Python, referencing approaches like in `s062`).
  - [ ] The guide includes advice on verifying that all identified links have been correctly updated.
  - [ ] The guide emphasizes a systematic approach to link updating.
  - [ ] User reviews the drafted content of the `documentation-refactoring-guide.md`.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Test Documentation Refactoring Guide**

  - [ ] A small, example refactoring task is defined (e.g., create a new subdirectory in `ai-guides/contrib/temp-test/` and move an existing, non-critical guide into it, then update one or two known links). This can be a hypothetical story `sXXX-example-refactor-story`.
  - [ ] An AI assistant (or user role-playing) attempts to perform this refactoring task _strictly following_ the newly drafted `documentation-refactoring-guide.md`.
  - [ ] The effectiveness of the guide in leading to a successful refactoring (files moved, links updated) is evaluated.
  - [ ] Any ambiguities, missing steps, or areas for improvement in the `documentation-refactoring-guide.md` are identified.
  - [ ] The `documentation-refactoring-guide.md` is iteratively refined based on this testing feedback.
  - [ ] User confirms the `documentation-refactoring-guide.md` is clear, comprehensive, and effective.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [ ] **Process:** AI performs an internal reflection on the completed story, analyzing its execution (e.g., tool usage, user feedback patterns, AC clarity, AI-Guide effectiveness).
  - [ ] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [ ] **Process:** AI invites the user to provide their own retrospective feedback and discusses any suggestions.
  - [ ] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [ ] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
