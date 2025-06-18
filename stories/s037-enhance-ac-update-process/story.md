---
id: "s037-enhance-ac-update-process"
title: "Enhance AI Process for Acceptance Criteria Updates"
status: "Done"
priority: "High"
tags: "process-improvement;ai-collaboration;story-management;documentation;adr;checkpoint"
resolution: "Implemented"
---

# Story: s037 - Enhance AI Process for Acceptance Criteria Updates

## Description

**User Story:** As a Vibe Tasking user, I want AI assistants to more reliably update the Acceptance Criteria checklist in `story.md` as tasks are completed, so that story progress is accurately reflected.

**Details:** This story implements a multi-faceted approach to improve AI compliance with updating Acceptance Criteria (ACs). It involves creating an Architecture Decision Record (ADR) to document this process change, updating `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` with new instructions and a process AC, creating a new guide tentatively named `docs/guides/working-on-stories-guide.md` (final name to be confirmed during implementation), and updating `CONTEXT.md` and `INSTALLING.md`. The ADR created will use the next available sequential number (e.g., `adr-XXX`). **This story will also define and implement a 'Checkpoint' system for Acceptance Criteria to guide AI interaction flow.**

## Artifacts

- `../adrs/adr-XXX-enhancing-ac-update-compliance.md` (to be created, XXX determined at implementation)
- `../../docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (to be modified)
- `../../docs/guides/working-on-stories-guide.md` (to be created/modified, final name TBD)
- `../../docs/guides/planning-guide.md` (to be modified)
- `../../CONTEXT.md` (to be modified)
- `../../INSTALLING.md` (to be modified)
- `../../docs/guides/updating-installing-md-guide.md` (to be referenced)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`). Upon completing all Acceptance Criteria for a bolded **Checkpoint**, perform the End-of-Interaction AC Review Protocol (summarize completed ACs, await user confirmation) and then **ask the user if you should proceed to the next Checkpoint.**

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.

- [x] **Checkpoint: ADR for "Checkpoint" Model and Enhanced AC Update Compliance**

  - [x] The next available ADR number is identified (e.g., if `adr-015` is the last, this becomes `adr-016`).
  - [x] A new ADR file (e.g., `docs/adrs/adr-XXX-enhancing-ac-update-compliance.md`) is created using the identified number.
  - [x] The ADR follows the formatting guidelines in `docs/adrs/README.md`.
  - [x] The ADR `Context` details the problem of ACs not being consistently updated and the need for clearer AI pause points.
  - [x] The ADR `Alternatives Considered` includes prior ideas and the newly chosen "Checkpoint" model.
  - [x] The ADR `Decision` clearly states the adoption of:
    - The "Checkpoint" structure (top-level Checkpoints, nested ACs).
    - AI pausing after each Checkpoint and asking to proceed.
    - The in-line `story.md` prompt for marking ACs.
    - The "End-of-Interaction AC Review Protocol" for nested ACs.
    - The new "Process" AC in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` for this review.
    - The new/updated `docs/guides/working-on-stories-guide.md` detailing these.
    - Updates to `docs/guides/planning-guide.md` for creating stories with Checkpoints.
  - [x] The ADR `Consequences` are documented.

- [x] **Checkpoint: Update Story Structure Guide (`docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`)**

  - [x] `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` is updated to define "Checkpoint" (bolded, top-level, mandatory pause-and-ask point) and "Acceptance Criteria" (nested or standalone, checkable items).
  - [x] Examples in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` are updated to show this structure (e.g., bolded Checkpoints, indented ACs).
  - [x] The `**IMPORTANT:** ... **MUST** mark ACs ...` in-line prompt is added/verified.
  - [x] The standard "Process" AC for AI-initiated review of completed (nested) ACs is added/verified.

- [x] **Checkpoint: Create/Update AI Operational Guide (`docs/guides/working-on-stories-guide.md`)**

  - [x] The guide (e.g., `docs/guides/working-on-stories-guide.md`, final name TBD) is created/updated.
  - [x] Guide explicitly instructs AI: "Upon completing all Acceptance Criteria for a **Checkpoint**, perform the End-of-Interaction AC Review Protocol, then **ask the user if you should proceed to the next Checkpoint**."
  - [x] Guide details the "End-of-Interaction AC Review Protocol" for individual/grouped ACs within a Checkpoint.
  - [x] Guide includes/updates the "Guidance for Modal AI Assistants (e.g., Cline)" to state that a "Cline Task" ideally corresponds to completing one Checkpoint.
  - [x] Guide reinforces general good practices (journaling, status updates).

- [x] **Checkpoint: Update Planning Guide (`docs/guides/planning-guide.md`)**

  - [x] `docs/guides/planning-guide.md` is updated to instruct users/AIs to structure stories using "Checkpoints" for major phases, with detailed ACs nested under them where appropriate.
  - [x] Examples in the planning guide are updated to reflect this structure.

- [x] **Checkpoint: Update Context & Installation Files**

  - [x] `CONTEXT.md` is updated to reference the (revised) `docs/guides/working-on-stories-guide.md`.
  - [x] `INSTALLING.md` is synchronized with the (revised) `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, following `docs/guides/updating-installing-md-guide.md`.

- [x] **Checkpoint: Final User Confirmation and Story Closure**
  - [x] User reviews and confirms all created/modified documents (ADR, `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, `docs/guides/working-on-stories-guide.md`, `docs/guides/planning-guide.md`, `CONTEXT.md`, `INSTALLING.md`) accurately implement all agreed-upon changes and the "Checkpoint" model.
  - [x] **Process:** User confirms the revised `s037/story.md` (this story itself, with its new Checkpoint structure) accurately reflects the planned work and adheres to the (newly defined) Story Documentation Guide.
