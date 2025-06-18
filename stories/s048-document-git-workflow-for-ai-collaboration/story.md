---
id: "s048-document-git-workflow-for-ai-collaboration"
title: "Document Git Workflow Best Practices for AI Collaboration"
status: "Closed"
priority: "Medium"
tags: "documentation;article;onboarding;git;workflow;best-practices"
resolution: "Superseded by s049"
---

# Story: s048 - Document Git Workflow Best Practices for AI Collaboration

## Description

**User Story:** As a Vibe Tasking user, I want to understand best practices for managing my code and documentation changes using Git when collaborating with an AI assistant, so that I can maintain a clean, recoverable, and efficient workflow.

**Details:** This story involves creating a new **Article**, likely as part of the `docs/articles/onboarding/` series, to explain a recommended Git workflow for users collaborating with AI assistants within the Vibe Tasking framework.

The article should cover the stages of changes:

1.  Suggested Edit (AI proposes, user reviews/modifies in editor, unsaved)
2.  Changed File (Saved to disk)
3.  Staged Change (`git add` - a "safe point" after a checkpoint or significant step)
4.  Committed to Local Repo (`git commit` - a more solid snapshot, amendable using `git commit --amend`)
5.  Pushed to Remote (`git push` - sharing/backing up the commit)
6.  (Optional) PR Merge into Main (if using dev branches)

The article should emphasize the user's role in strategically moving changes through this pipeline to capture useful states, manage WIP (Work In Progress), and ensure recoverability. It should also touch upon starting work from a clean state and the benefits of committing/pushing at logical points (e.g., after Checkpoints).

The article may include one or more ASCII-art diagrams (as per `docs/adrs/adr-016-ascii-art-diagrams.md`) to illustrate this data flow/pipeline.

## Artifacts

- This `story.md` file.
- A new Article file (e.g., `docs/articles/onboarding/05a-managing-changes-with-git.md` - exact name and location to be finalized).
- Potentially ASCII diagrams embedded in the new article.

## Acceptance Criteria

- [ ] **Checkpoint: Initial Story Setup**
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete.
  - [ ] The final title, filename, and location for the new Article (e.g., within `docs/articles/onboarding/`) are decided and documented in the journal.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Draft Article Content' Checkpoint.
- [ ] **Checkpoint: Draft Article Content**
  - [ ] The core content for the new Article is drafted, explaining the Git workflow stages (Suggested Edit, Changed File, Staged, Committed, Pushed, PR Merge) in the context of AI collaboration.
  - [ ] The draft emphasizes the user's role in managing this pipeline and the benefits of each stage for WIP management and recoverability.
  - [ ] The draft includes practical advice, such as starting from a clean state and using `git commit --amend`.
  - [ ] User reviews the drafted content for clarity, accuracy, and completeness.
  - [ ] **Process:** All ACs within this 'Draft Article Content' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Create Supporting Diagrams (Optional)**
  - [ ] One or more ASCII-art sequence or flow diagrams are designed to visually represent the Git workflow pipeline.
  - [ ] Diagrams feature relevant lifelines/participants (e.g., User, AI Assistant, Editor, Filesystem, Local Git, Remote Git).
  - [ ] Diagrams are created adhering to `docs/adrs/adr-016-ascii-art-diagrams.md`.
  - [ ] User reviews and approves the diagrams.
  - [ ] **Process:** All ACs within this 'Create Supporting Diagrams' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Finalize and Integrate Article**
  - [ ] The drafted content and any diagrams are combined into the final Article file at the agreed-upon location.
  - [ ] If part of the onboarding series, links to the previous and next articles are updated accordingly in the new article and potentially in adjacent articles.
  - [ ] The main `docs/articles/onboarding/README.md` (or other relevant index) is updated to include the new article if necessary.
  - [ ] User performs a final review of the integrated article.
  - [ ] **Process:** All ACs within this 'Finalize and Integrate Article' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status) and `resolution` field is set appropriately (e.g., "Implemented").
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
