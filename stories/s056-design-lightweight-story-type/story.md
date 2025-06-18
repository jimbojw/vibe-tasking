---
id: "s056-design-lightweight-story-type"
title: "Design and Implement Lightweight Story Type"
status: "Done"
priority: "Medium"
tags: "design;process;template;story-structure;adr"
resolution: "Implemented"
---

# Story: s056-design-lightweight-story-type - Design and Implement Lightweight Story Type

## Description

As a project maintainer, I want to design and implement a 'lightweight story' type suitable for simple, single-AC tasks, to reduce process overhead while maintaining core Vibe Tasking principles. This includes creating a new story template, AI guidance, and an ADR.

## Artifacts

- `docs/adrs/adr-XXX-lightweight-story-type.md` (To be created)
- `stories/lightweight-story.template.md` (To be created)
- `ai-guides/core/stories/stories-planning-guide.md` (Potentially modified)
- `ai-guides/core/stories/stories-structuring-guide.md` (Potentially modified)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Define Lightweight Story Concept & ADR**

  - [x] Consult the [ADR Writing Guide](../../../ai-guides/contrib/adrs/adrs-writing-guide.md) for best practices.
  - [x] Draft an ADR for the Lightweight Story type. This ADR should detail its purpose, the streamlined process (including the "Combined Checkpoint" structure), criteria for when to use it, and the chosen identification method (e.g., the specific tag).
  - [x] Update the [`ADR Writing Guide`](../../../ai-guides/contrib/adrs/adrs-writing-guide.md:0) to instruct AI assistants to list existing ADRs in `docs/adrs/` to determine the next sequential ADR number before suggesting one.
  - [x] User reviews and approves ADR and the overall concept definition for lightweight stories.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Create Lightweight Story Template**

  - [x] Create a new template file, `stories/lightweight-story.template.md`, that reflects the defined structure for lightweight stories, including the "Combined Checkpoint".
  - [x] User reviews and approves the new template.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Develop AI Guidance**

  - [x] Draft guidance for AI assistants and add it as a new section in [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md:0). This guidance should explain when it's appropriate to use or suggest a lightweight story versus a full story, and how to handle them.
  - [x] User reviews and approves the AI guidance.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Update Core Documentation**

  - [x] Update `ai-guides/core/stories/stories-structuring-guide.md` to include information about the new lightweight story type, its template, and its intended use.
  - [x] Review other relevant documentation (e.g., `README.md`) for any necessary mentions or updates and implement them.
  - [x] User reviews and approves all documentation updates.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
