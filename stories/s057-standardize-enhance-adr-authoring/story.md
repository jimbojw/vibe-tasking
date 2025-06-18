---
id: "s057-standardize-enhance-adr-authoring"
title: "Standardize and Enhance ADR Authoring Process"
status: "Done"
priority: "High"
tags: "adr;process;documentation;template;ai-guide;standards;refactor;compliance"
resolution: "Implemented"
---

# Story: s057-standardize-enhance-adr-authoring - Standardize and Enhance ADR Authoring Process

## Description

This story addresses inconsistencies in the current ADR (Architecture Decision Record) authoring process and aims to formalize it for better quality, consistency, and AI collaboration.
Background:

- `adr-003-yaml-frontmatter.md` defines the requirement for YAML frontmatter in ADRs.
- ADRs `adr-017`, `adr-018`, and `adr-019` are known to be non-compliant (missing frontmatter). Other ADRs may also be non-compliant.
- There is an existing user-facing article `docs/articles/using-architecture-decision-records.md`.

This story will:

1.  Create a standard ADR template (`docs/ai-guides/adr.template.md`).
2.  Create an AI guide (`docs/ai-guides/adrs-writing-guide.md`) to instruct AI assistants on collaboratively authoring ADRs with users, inspired by `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md`.
3.  Identify and remediate all non-compliant ADRs in the `docs/adrs/` directory to ensure they meet the `adr-003` standard.
4.  Create a meta-ADR to document the decisions made in this story regarding the formalization of the ADR authoring process.
5.  Update relevant existing documentation (`docs/articles/using-architecture-decision-records.md`, `docs/adrs/README.md`, and `CONTEXT.md`) to reflect the new standards and guide AI assistants.

## Artifacts

**New Files:**

- `docs/ai-guides/adr.template.md`
- `docs/ai-guides/adrs-writing-guide.md`
- `docs/adrs/adr-021-formalize-adr-authoring-process.md` (Meta-ADR, number tentative)

**Modified Files:**

- `docs/adrs/adr-017-documentation-refactor.md`
- `docs/adrs/adr-018-standardize-ai-guide-authoring-collaboration.md`
- `docs/adrs/adr-019-adopt-sibling-template-convention.md`
- Potentially other non-compliant ADRs in `docs/adrs/`
- `docs/articles/using-architecture-decision-records.md`
- `docs/adrs/README.md`
- `CONTEXT.md`

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Research and Define ADR Template Content**

  - [x] **AC1.1:** Review `adr-003-yaml-frontmatter.md` to confirm all required and recommended frontmatter fields for ADRs (e.g., `id`, `title`, `status`, `date`, `tags`).
  - [x] **AC1.2:** Review existing compliant ADRs (e.g., `adr-001` through `adr-016`) to identify common body sections (e.g., Context, Decision, Consequences) and their typical content.
  - [x] **AC1.3:** Define the standard structure and placeholder content for `docs/ai-guides/adr.template.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [x] **Checkpoint: Create ADR Template**

  - [x] **AC2.1:** Create the file `docs/ai-guides/adr.template.md` based on the defined structure from Checkpoint 1.
    - The template must include YAML frontmatter placeholders (for `id`, `title`, `status`, `date`, `tags`) and standard ADR sections (e.g., Context, Decision, Consequences) with instructional comments.
    - The template must adhere to `docs/ai-guides/vibe-tasking/template-files-working-guide.md` and be placed according to `docs/adrs/adr-019-adopt-sibling-template-convention.md` (i.e., in `docs/ai-guides/` as a sibling to the `adrs-writing-guide.md`).
  - [x] **AC2.2:** User reviews and approves `docs/ai-guides/adr.template.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [x] **Checkpoint: Design and Draft AI Guide for Writing ADRs**

  - [x] **AC3.1:** Outline the structure for `docs/ai-guides/adrs-writing-guide.md`, ensuring it's inspired by `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md` and instructs AI assistants on collaboratively helping users:
    - Understand ADR purpose.
    - Conceptualize the ADR (problem, decision, alternatives).
    - Utilize `docs/ai-guides/adr.template.md` to populate frontmatter and sections.
    - Refine content for clarity, completeness, and adherence to ADR conventions.
  - [x] **AC3.2:** Draft the content for `docs/ai-guides/adrs-writing-guide.md`.
  - [x] **AC3.3:** User reviews and approves `docs/ai-guides/adrs-writing-guide.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [x] **Checkpoint: Identify and Remediate Non-Compliant ADRs**

  - [x] **AC4.1:** List all `.md` files in `docs/adrs/` (excluding `README.md`).
  - [x] **AC4.2:** For each listed ADR file, check for the presence and correctness of YAML frontmatter as defined in `adr-003-yaml-frontmatter.md` (specifically an `id:` field).
  - [x] **AC4.3:** Identify all non-compliant ADRs (including `adr-017`, `adr-018`, `adr-019`, and any others found).
  - [x] **AC4.4:** For each non-compliant ADR:
    - Add/correct YAML frontmatter (inferring `id`, `title`, `date` if possible; setting `status` and `tags` appropriately).
    - Ensure the body structure aligns with standard ADR sections (Context, Decision, Consequences), refactoring content carefully.
  - [x] **AC4.5:** User reviews and approves all remediated ADRs.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [x] **Checkpoint: Create Meta-ADR for ADR Process Formalization**

  - [x] **AC5.1:** Draft content for a new ADR (e.g., `adr-021-formalize-adr-authoring-process.md`) documenting the decisions made in this story (s057) regarding the ADR authoring process, template, and AI guide. Use the newly created `docs/ai-guides/adr.template.md`.
  - [x] **AC5.2:** User reviews and approves the content for the meta-ADR.
  - [x] **AC5.3:** Create the meta-ADR file in `docs/adrs/`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [x] **Checkpoint: Update Relevant Documentation**

  - [x] **AC6.1:** Review and update `docs/articles/using-architecture-decision-records.md` to reference the new `docs/ai-guides/adr.template.md` and `docs/ai-guides/adrs-writing-guide.md`.
  - [x] **AC6.2:** Review and update `docs/adrs/README.md` to reflect the formalized ADR process, including the use of the new template and AI guide.
  - [x] **AC6.3:** Add a task-specific directive to `CONTEXT.md` instructing AI assistants to consult `docs/ai-guides/adrs-writing-guide.md` for any tasks involving ADR creation or modification.
  - [x] **AC6.4:** User reviews and approves updates to `docs/articles/using-architecture-decision-records.md`, `docs/adrs/README.md`, and `CONTEXT.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [x] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set to "Implemented" in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
