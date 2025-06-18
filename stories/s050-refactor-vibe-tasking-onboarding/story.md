---
id: "s050-refactor-vibe-tasking-onboarding"
title: "Refactor Vibe Tasking Onboarding Material"
status: "Closed"
priority: "High"
tags: "documentation;onboarding;refactor;vibe-tasking;vibe-coding"
resolution: "Obsolete"
---

# Story: s050 - Refactor Vibe Tasking Onboarding Material

## Description

**User Story:** As a Vibe Tasking project maintainer, I want to refactor the existing Vibe Tasking onboarding documentation to align with the new "Vibe Coding" tutorial series (created in `s049`), so that users have a clear, logical, and streamlined learning path from general AI collaboration skills to specific Vibe Tasking framework usage.

**Details:** This story involves a significant refactoring of the current Vibe Tasking onboarding articles located in `docs/articles/onboarding/`. The goal is to make this series more focused on the Vibe Tasking framework itself, assuming that foundational "Vibe Coding" best practices are covered in the new, separate tutorial series (from `s049`).

Key activities will include:

- Reviewing all current onboarding articles.
- Identifying content that should be moved to, or is superseded by, the "Vibe Coding" tutorial.
- Restructuring the Vibe Tasking onboarding to ensure it builds upon the "Vibe Coding" tutorial.
- Updating introductions, prerequisites, and cross-links to clearly direct users between the two tutorial series.
- Ensuring the refactored Vibe Tasking onboarding provides a concise and effective guide to installing, understanding, and using the Vibe Tasking framework.
- Creating or adapting sequence diagrams that illustrate Vibe Tasking-specific workflows, such as the story planning process including the AI's consultation of `planning-guide.md`.

**Dependencies:**

- `s054-create-article-tutorial-ai-guides-templates`: This story defines standards and templates for tutorials and articles, which will inform the refactoring of the onboarding material.
- `s049-create-vibe-coding-tutorial-series`: This story should be substantially complete or have a well-defined structure and content outline before major work on `s050` begins, as `s050` will heavily reference and align with `s049`'s outputs.

## Artifacts

- This `story.md` file.
- All files within `docs/articles/onboarding/` (to be reviewed and modified).
- Potentially new or consolidated articles within `docs/articles/onboarding/`.
- Links to the "Vibe Coding" tutorial series (from `s049`).

## Acceptance Criteria

- [ ] **Checkpoint: Initial Story Setup**
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete.
  - [ ] **Dependency Check:** The status and output structure of `s049-create-vibe-coding-tutorial-series` are reviewed to ensure a clear understanding of the "Vibe Coding" tutorial content that this refactoring will depend on.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Content Audit and Restructuring Plan' Checkpoint.
- [ ] **Checkpoint: Content Audit and Restructuring Plan**
  - [ ] All existing articles in `docs/articles/onboarding/` are audited.
  - [ ] Content to be kept, moved, removed, or rewritten is identified.
  - [ ] A restructuring plan for the Vibe Tasking onboarding series is created, outlining the new flow and focus of each article.
  - [ ] User reviews and approves the content audit and restructuring plan.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained.
- [ ] **Checkpoint: Refactor Onboarding Articles**
  - [ ] Each article in the Vibe Tasking onboarding series is refactored according to the approved plan.
  - [ ] Introductions and prerequisite sections are updated to clearly reference the "Vibe Coding" tutorial series.
  - [ ] Redundant or superseded content is removed or appropriately archived/redirected if necessary.
  - [ ] New content is written as needed to ensure the Vibe Tasking onboarding is comprehensive for framework-specific knowledge.
  - [ ] User reviews the refactored articles iteratively or as a whole.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained.
- [ ] **Checkpoint: Illustrative Vibe Tasking Interaction Diagrams**
  - [ ] An ASCII sequence diagram is created to illustrate the Vibe Tasking-specific story planning interaction. This diagram will show the general modal flow (Plan -> Act -> Refine) and explicitly include the AI assistant consulting `ai-guides/core/stories/stories-planning-guide.md` upon recognizing a user's intent to create a new story.
  - [ ] This diagram is integrated into an appropriate article within the refactored Vibe Tasking onboarding series (e.g., the article on planning stories).
  - [ ] User reviews and approves the Vibe Tasking-specific sequence diagram and its placement.
  - [ ] **Process:** All ACs in this Checkpoint complete, journal updated, user approval to proceed.
- [ ] **Checkpoint: Update Links and Navigation**
  - [ ] All internal links within the refactored Vibe Tasking onboarding series are checked and updated.
  - [ ] Cross-links to and from the "Vibe Coding" tutorial series are implemented correctly.
  - [ ] The main `docs/articles/onboarding/README.md` is updated to reflect the new structure and flow.
  - [ ] Any other relevant index pages or high-level documentation (e.g., main project `README.md`) are updated if they reference the onboarding material.
  - [ ] User reviews the updated links and navigation.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained.
- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed, and the refactored Vibe Tasking onboarding is clear, accurate, and well-integrated with the "Vibe Coding" tutorial.
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status) and `resolution` field is set appropriately (e.g., "Implemented").
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
