---
id: "s072-adr-ai-guide-discovery-mechanism"
title: "Create ADR for AI Guide Discovery Mechanism"
status: "Done"
priority: "Medium"
tags: "adr;design;documentation;ai-guides;lightweight"
resolution: "Implemented"
---

# Story: s072-adr-ai-guide-discovery-mechanism - Create ADR for AI Guide Discovery Mechanism

## Description

As a project maintainer, I want to create an Architecture Decision Record (ADR) for the current AI Guide discovery mechanism so that the rationale, alternatives, and consequences of this core architectural decision are formally documented and easily accessible. This mechanism, detailed in `ai-guides/core/ai-guides/ai-guides-discovering-guide.md`, relies on `find` and `grep` shell commands.

## Artifacts

- [`ai-guides/core/ai-guides/ai-guides-discovering-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-discovering-guide.md) (Reference for current mechanism)
- [`ai-guides/contrib/adrs/adrs-writing-guide.md`](../../../../ai-guides/contrib/adrs/adrs-writing-guide.md) (Guide for writing the ADR)
- [`ai-guides/contrib/adrs/adr.template.md`](../../../../ai-guides/contrib/adrs/adr.template.md) (Template for the new ADR)
- `docs/adrs/adr-XXX-ai-guide-discovery-mechanism.md` (The ADR to be created, XXX determined at execution)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [x] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the 'Core Task' AC below is accurate, complete, and suitable for a lightweight story.
  - [x] **Core Task:** An ADR is created at `docs/adrs/adr-XXX-ai-guide-discovery-mechanism.md` (where XXX is the next sequential ADR number determined during execution) that:
    - Follows the [`adrs-writing-guide.md`](../../../../ai-guides/contrib/adrs/adrs-writing-guide.md) (which includes determining the next ADR number) and uses [`adr.template.md`](../../../../ai-guides/contrib/adrs/adr.template.md) as a basis.
    - Clearly documents the context, problem statement, decision drivers, considered options, decision outcome (rationale for `find`/`grep`), and consequences for the AI Guide discovery mechanism.
    - Includes pros/cons for the chosen solution and key alternatives.
    - Links to [`ai-guides-discovering-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-discovering-guide.md).
  - [x] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [x] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [x] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [x] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
