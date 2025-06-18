---
id: "s065-enhance-ai-guide-discoverability"
title: "Enhance AI Guide Discoverability and Usage"
status: "Done"
priority: "High"
tags: "ai-guides;documentation;workflow;adr"
resolution: "Implemented"
---

# Story: s065-enhance-ai-guide-discoverability - Enhance AI Guide Discoverability and Usage

## Description

Currently, AI assistants and users must either remember the available AI guides or rely on hints within `CONTEXT.md`. This approach is not scalable as the number of guides grows. This story aims to improve the discoverability and targeted usage of AI guides by introducing metadata and updating related processes.

As a Vibe Tasking user/developer, I want AI guides to be more easily discoverable and their purposes clearly defined, so that AI assistants can more effectively identify and utilize the correct guide for a given task, improving workflow efficiency and accuracy.

## Artifacts

- New ADR: `docs/adrs/adr-027-ai-guide-metadata-for-discoverability.md` (to be created)
- Existing related ADR: [`docs/adrs/adr-023-standardize-ai-guides-naming.md`](../../docs/adrs/adr-023-standardize-ai-guides-naming.md)
- AI Guide Template: [`ai-guides/core/ai-guides/ai-guide.template.md`](../../ai-guides/core/ai-guides/ai-guide.template.md)
- AI Guide Design Guide: [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md)
- Project Context: [`CONTEXT.md`](../../CONTEXT.md)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Design and Document AI Guide Metadata Standard**

  - [x] **Design:** Define YAML frontmatter fields for AI guides, including a field for "purpose" or "when_to_use" (e.g., `usage_context: "Use this guide when X..."`).
  - [x] **ADR:** Create a new ADR (e.g., `docs/adrs/adr-027-ai-guide-metadata-for-discoverability.md`) detailing the decision to adopt YAML frontmatter for AI guides.
    - [x] The ADR explains the rationale (improved discoverability, programmatic access to guide purposes).
    - [x] The ADR specifies the required frontmatter fields, including the "purpose" field.
    - [x] The ADR links to [`docs/adrs/adr-023-standardize-ai-guides-naming.md`](../../docs/adrs/adr-023-standardize-ai-guides-naming.md) as a related decision.
  - [x] **Process:** All ACs within this 'Design and Document AI Guide Metadata Standard' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Update AI Guide Templates and Authoring Guidance**

  - [x] **Template Update:** Modify [`ai-guides/core/ai-guides/ai-guide.template.md`](../../ai-guides/core/ai-guides/ai-guide.template.md) to include the new standard YAML frontmatter block with placeholder values and comments.
  - [x] **Guidance Update:** Update [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) to:
    - [x] Include instructions on adding and populating the new YAML frontmatter in AI guides.
    - [x] Emphasize the importance of the "purpose" field for discoverability.
    - [x] Reference the new ADR for the metadata standard.
  - [x] **Process:** All ACs within this 'Update AI Guide Templates and Authoring Guidance' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Revise CONTEXT.md for Meta-Guidance**

  - [x] **Content Revision:** Modify [`CONTEXT.md`](../../CONTEXT.md) to replace or augment the current "Task-Specific Instructions" section.
    - [x] The new guidance should instruct AI assistants to programmatically (e.g., via `grep` or similar file searching tools) enumerate all AI guides (`ai-guides/**/*.md`).
    - [x] The AI should then parse the "purpose" (or equivalent) field from each guide's frontmatter.
    - [x] The AI should use this summarized list of guide purposes to identify the most relevant guide(s) based on the user's stated intent or task, rather than relying on a hardcoded list in `CONTEXT.md`.
    - [x] The new guidance should explain how an AI can present these findings to the user (e.g., "I found these guides that might be relevant: ...").
  - [x] **Process:** All ACs within this 'Revise CONTEXT.md for Meta-Guidance' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
