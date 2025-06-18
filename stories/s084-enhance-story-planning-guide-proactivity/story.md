---
id: "s084-enhance-story-planning-guide-proactivity"
title: "Enhance Story Planning Guide to Clarify AI Proactivity Discussion"
status: "To Do"
priority: "Medium"
tags: "ai-guides;stories;planning;lightweight"
resolution: "Unresolved"
---

# Story: s084-enhance-story-planning-guide-proactivity - Enhance Story Planning Guide to Clarify AI Proactivity Discussion

## Description

As a user of Vibe Tasking, I want the `stories-planning-guide.md` to prompt AI assistants (who are helping plan new stories) to discuss and document the desired level of AI proactivity for the task being planned, so that expectations for the AI's behavior in the new story are clear from the outset and iterative refinement is reduced.

This involves updating the `stories-planning-guide.md` to include:

1.  A step or prompt for the assisting AI to discuss with the user the desired level of proactivity for the AI in the new process/task being defined by the story under planning. (e.g., should the AI wait for explicit instructions, or be more proactive in investigation and proposing plans?)
2.  Encouragement to draft Acceptance Criteria for the new story that explicitly reflect this agreed-upon level of proactivity.

## Artifacts

- [`ai-guides/core/stories/stories-planning-guide.md`](ai-guides/core/stories/stories-planning-guide.md) (The file to be modified)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** AI has performed spot grooming (consulting `stories-spot-grooming-guide.md`) and assisted in reviewing/confirming AC validity and completeness (especially the 'Core Task' AC).
  - [ ] **Process:** User confirms the 'Core Task' AC below is accurate, complete, and suitable for a lightweight story.
  - [ ] **Core Task:** The [`stories-planning-guide.md`](ai-guides/core/stories/stories-planning-guide.md) is updated to include prompts for the AI (assisting in planning) to discuss and encourage documenting the desired level of AI proactivity for the story being planned, including suggesting ACs reflecting this.
  - [ ] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [ ] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
