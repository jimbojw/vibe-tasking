---
id: "s036-adr-ascii-art-diagrams"
title: "ADR: Document Decision to Use ASCII-Art for Diagrams"
status: "Done"
priority: "Medium"
tags: "adr;documentation;design-decision;diagrams"
resolution: "Implemented"
---

# Story: s036 - ADR: Document Decision to Use ASCII-Art for Diagrams

## Description

**User Story:** As a project maintainer, I want to document the architectural decision to use ASCII-art for diagrams, so that the rationale is clear and can be referenced by current and future contributors.

**Details:** Create a new ADR (`adr-016-ascii-art-diagrams.md`) to formalize the decision. The ADR should detail the context (lack of Mermaid support in current Git host, alignment with ADR-001), alternatives considered (Mermaid, embedded images, ASCII-art), the decision itself, and its consequences.

## Artifacts

- `../adrs/adr-016-ascii-art-diagrams.md` (to be created)

## Acceptance Criteria

- [ ] **Checkpoint: Initial Story Setup**
  - [x] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is appended to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Create ADR for ASCII-Art Diagrams' Checkpoint.
- [ ] **Checkpoint: Create ADR for ASCII-Art Diagrams**
  - [x] A new ADR file `docs/adrs/adr-016-ascii-art-diagrams.md` is created.
  - [x] The ADR follows the formatting guidelines in `docs/adrs/README.md` (YAML frontmatter, required sections).
  - [x] The ADR's `Context` section accurately reflects the user's reasoning: lack of Mermaid support in the current Git host, desire for direct viewability, and alignment with `adr-001-code-free-framework.md`.
  - [x] The ADR's `Alternatives Considered` section includes "Mermaid," "Embedded Images," and "ASCII-Art."
    - [x] For "Embedded Images," pros (rich visuals, SVG textual/scalable) and cons (PNGs binary/hard diffs/repo size; SVGs complex/hard to diff meaningfully; both require external tools; binary images may have less AI support) are noted.
  - [x] The ADR's `Decision` section clearly states the choice to use ASCII-art.
  - [x] The ADR's `Consequences` section outlines positive impacts (viewability, no build, ADR-001 alignment, versioning), negative impacts (visuals, complexity for large diagrams), and notes the possibility of superseding the ADR if tool support changes.
  - [x] User confirms the ADR content is accurate, complete, and captures the decision rationale effectively.
  - [x] **Process:** All ACs within this 'Create ADR for ASCII-Art Diagrams' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Create ADR for ASCII-Art Diagrams' Checkpoint and any significant decisions made within it.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status) and `resolution` field is set appropriately.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
