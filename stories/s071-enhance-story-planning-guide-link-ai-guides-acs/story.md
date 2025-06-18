---
id: "s071-enhance-story-planning-guide-link-ai-guides-acs"
title: "Enhance Story Planning Guide to Link AI Guides in ACs"
status: "To Do"
priority: "Medium"
tags: "stories;planning;documentation;lightweight"
resolution: "Unresolved"
---

# Story: s071-enhance-story-planning-guide-link-ai-guides-acs - Enhance Story Planning Guide to Link AI Guides in ACs

## Description

The [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) needs to be updated. It should explicitly instruct the AI assistant and user to consider and link to known, relevant AI-Guides directly within a story's Acceptance Criteria (ACs) when those ACs involve tasks covered by specific guides. This aims to make the requirement to follow specific procedural guides an explicit part of the story's tasks. For example, if an AC involves drafting an Architecture Decision Record (ADR), that AC should include a step or reference to consult the [`ai-guides/contrib/adrs/adrs-writing-guide.md`](../../../ai-guides/contrib/adrs/adrs-writing-guide.md). This idea was captured during the retrospective for story s068.

## Artifacts

- [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) (Target for modification)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [ ] **Process:** The '[`stories-working-guide.md`](../../../ai-guides/core/stories/stories-working-guide.md)' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the 'Core Task' AC below is accurate, complete, and suitable for a lightweight story.
  - [ ] **Core Task:** The [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) is updated to include explicit instructions for linking relevant AI Guides within Acceptance Criteria when ACs pertain to tasks covered by those guides, including an illustrative example.
  - [ ] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [ ] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
