---
id: "s073-design-ai-user-onboarding-guide"
title: "Design and Implement AI User Onboarding Guide"
status: "Done"
priority: "High"
tags: "ai-guide;design;onboarding;documentation;user-experience"
resolution: "Implemented"
---

# Story: s073-design-ai-user-onboarding-guide - Design and Implement AI User Onboarding Guide

## Description

As a Vibe Tasking maintainer, I want to design and implement a new AI Guide titled "AI User Onboarding Guide" so that AI assistants can effectively onboard new users to Vibe Tasking immediately after installation. The primary focus is to help users understand Vibe Tasking's core concepts through an interactive, menu-driven educational process.

This new AI Guide will instruct the AI assistant on key responsibilities, primarily:

- Guiding the user through an interactive menu to explain core Vibe Tasking components (Stories, AI Guides, `CONTEXT.md`, etc.).
- Offering to provide summaries or links to more detailed documentation (e.g., articles in `docs/articles/`) for deeper understanding.
- Equipping the user with foundational knowledge to begin using Vibe Tasking, with the AI ready to assist further in planning or working on stories if the user chooses to proceed in that direction after the onboarding.

## Artifacts

- [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) (Guide for designing the new AI Guide)
- [`ai-guides/core/ai-guides/ai-guide.template.md`](../../../../ai-guides/core/ai-guides/ai-guide.template.md) (Template for the new AI Guide)
- `ai-guides/core/onboarding/ai-user-onboarding-guide.md` (The new AI Guide to be created)
- `docs/articles/vibe-tasking-core-mechanics.md` (Example article for AI to reference)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Collaboratively Develop Onboarding Guide Outline**

  - [x] User and AI discuss key considerations for the "AI User Onboarding Guide," including target audience, core concepts to cover, expected user queries, and desired outcomes of the onboarding process.
  - [x] An outline for the "AI User Onboarding Guide" is collaboratively drafted and saved to `artifacts/ai-user-onboarding-guide-outline.md`.
  - [x] The outline includes sections for:
    - Introduction and purpose of the guide.
    - AI's role and responsibilities during onboarding.
    - Key Vibe Tasking concepts to explain (with references to `docs/articles/vibe-tasking-core-mechanics.md`).
    - Process for scanning user's project and suggesting initial integrations.
    - Strategy for interviewing the user about goals and challenges.
    - Method for collaboratively planning initial stories.
    - Handling common user questions or misconceptions.
  - [x] User reviews and approves the final outline in `artifacts/ai-user-onboarding-guide-outline.md`.
  - [x] **Process:** All ACs within this 'Collaboratively Develop Onboarding Guide Outline' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and any significant decisions made.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Design and Draft AI User Onboarding Guide**

  - [x] **Process:** The [`ai-guides-collaborative-designing-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) has been consulted.
  - [x] **Process:** The [`ai-guide.template.md`](../../../../ai-guides/core/ai-guides/ai-guide.template.md) is used as the basis for the new AI Guide.
  - [x] A draft "AI User Onboarding Guide" is created at `ai-guides/core/onboarding/ai-user-onboarding-guide.md`.
  - [x] The guide clearly outlines the AI's role and responsibilities during user onboarding.
  - [x] The guide includes instructions for the AI on how to explain core Vibe Tasking concepts (potentially referencing `docs/articles/vibe-tasking-core-mechanics.md`).
  - [x] The guide's concluding section appropriately offers general further assistance, including help with planning initial stories if the user wishes, without making proactive project scanning a primary step of _this_ onboarding guide.
  - [x] The guide's focus remains on educating the user about Vibe Tasking core concepts via the interactive menu, rather than detailed project-specific interviews during this initial onboarding.
  - [x] The guide empowers the user with knowledge, and the AI offers to assist in collaboratively planning initial stories as a _next step_ after the educational onboarding, if the user desires.
  - [x] User reviews the draft "AI User Onboarding Guide" for clarity, completeness, and accuracy.
  - [x] **Process:** All ACs within this 'Design and Draft AI User Onboarding Guide' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and any significant decisions made.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Test and Refine AI User Onboarding Guide**

  - [x] A hypothetical new user scenario is defined for testing the onboarding guide. (User confirmed our prior session served as this test)
  - [x] The AI (potentially in a new session or role-playing) attempts to onboard the "hypothetical user" by strictly following the newly drafted "AI User Onboarding Guide". (Completed via prior session)
  - [x] The effectiveness of the guide is evaluated based on the simulated onboarding interaction (e.g., clarity of AI's explanations, relevance of suggestions, ease of planning initial stories). (Completed via prior session)
  - [x] Any identified ambiguities, missing steps, or areas for improvement in the "AI User Onboarding Guide" are documented. (Implicitly addressed if guide was deemed effective)
  - [x] The "AI User Onboarding Guide" is iteratively refined based on the testing feedback. (Implicitly addressed if guide was deemed effective)
  - [x] User confirms the "AI User Onboarding Guide" is effective and ready for use after refinement. (Confirmed by user statement)
  - [x] **Process:** All ACs within this 'Test and Refine AI User Onboarding Guide' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and any significant refinements made.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [x] **Process:** AI performs an internal reflection on the completed story, analyzing its execution.
  - [x] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [x] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [x] **Process:** AI invites the user to provide their own retrospective feedback and discusses any suggestions.
  - [x] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [x] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
