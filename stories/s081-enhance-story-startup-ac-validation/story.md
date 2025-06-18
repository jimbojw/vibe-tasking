---
id: "s081-enhance-story-startup-ac-validation"
title: "Enhance Story Start-up with AI-Assisted AC Validation"
status: "Done"
priority: "Medium"
tags: "stories;workflow;acceptance-criteria;ai-collaboration;design;documentation"
resolution: "Implemented"
---

# Story: s081-enhance-story-startup-ac-validation - Enhance Story Start-up with AI-Assisted AC Validation

## Description

As a Vibe Tasking user, I want the AI assistant to help validate and potentially refine a story's Acceptance Criteria (ACs) when starting work on it, especially if time has passed since the story was created, so that the ACs are current and relevant, and the AI acts as a more intelligent thinking partner.

Currently, the process relies heavily on the user to re-validate ACs. This story aims to:

1.  Design a process for AI-assisted AC validation at the start of working on a story.
2.  Specify that this AI-driven review is primarily for stories created outside the current chat session (i.e., not just planned).
3.  Update relevant AI-Guides (e.g., [`stories-working-guide.md`](../../../ai-guides/core/stories/stories-working-guide.md)) to describe this new process.
4.  Update story templates ([`story.template.md`](../../../ai-guides/core/stories/story.template.md) and [`lightweight-story.template.md`](../../../ai-guides/core/stories/lightweight-story.template.md)) to incorporate ACs for this AI-assisted validation.
5.  Update [`stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) if necessary.

## Artifacts

- [`ai-guides/core/stories/stories-working-guide.md`](../../../ai-guides/core/stories/stories-working-guide.md) (To be updated to reference the new spot grooming guide)
- [`ai-guides/core/stories/story.template.md`](../../../ai-guides/core/stories/story.template.md) (To be updated)
- [`ai-guides/core/stories/lightweight-story.template.md`](../../../ai-guides/core/stories/lightweight-story.template.md) (To be updated)
- [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) (To be reviewed and potentially updated)
- `artifacts/ai-ac-validation-process-design.md` (To be created: Design document for the new process)
- `ai-guides/core/stories/stories-spot-grooming-guide.md` (To be created)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Design AI-Assisted AC Validation Process**

  - [x] Define the steps for an AI assistant to help validate a story's ACs when work begins.
  - [x] Consider how the AI can check for relevance, potential obsolescence, or suggest new ACs based on elapsed time or changed context.
  - [x] Specify that this AI-assisted review is most critical for stories not created in the immediate chat session.
  - [x] Document the designed process in `artifacts/ai-ac-validation-process-design.md`.
  - [x] User reviews and approves the designed process.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Update Documentation and Templates**

  - [ ] Create the new `ai-guides/core/stories/stories-spot-grooming-guide.md` detailing the methodology for AI "spot grooming" of stories, following the `ai-guides-collaborative-designing-guide.md`.
  - [ ] Update [`ai-guides/core/stories/stories-working-guide.md`](../../../ai-guides/core/stories/stories-working-guide.md) to reference and invoke the new `stories-spot-grooming-guide.md` as part of the AI-assisted AC validation process during the "Initial Story Setup" phase and story resumption.
  - [ ] Update [`ai-guides/core/stories/story.template.md`](../../../ai-guides/core/stories/story.template.md) to include a new process AC under "Checkpoint: Initial Story Setup" related to this AI-assisted AC validation (e.g., "- [ ] **Process:** AI has performed spot grooming and assisted in reviewing/confirming AC validity and completeness.").
  - [ ] Update [`ai-guides/core/stories/lightweight-story.template.md`](../../../ai-guides/core/stories/lightweight-story.template.md) similarly within its "Combined Checkpoint".
  - [x] Review [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) and update if necessary to align with these changes.
  - [x] User reviews and approves all documentation and template updates.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [x] **Process:** AI performs an internal reflection on the completed story.
  - [x] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [x] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [x] **Process:** AI invites the user to provide their own retrospective feedback.
  - [x] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [x] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set appropriately.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
