---
id: "s075-research-optional-template-sections"
title: "Research and Define Convention for Marking Optional Template Sections"
status: "To Do"
priority: "Medium"
tags: "templates;conventions;documentation;research;design;ai-usability"
resolution: "Unresolved"
---

# Story: s075-research-optional-template-sections - Research and Define Convention for Marking Optional Template Sections

## Description

As a Vibe Tasking maintainer, I want to research and define a clear, unambiguous convention for marking optional sections in templates so that AI assistants can correctly interpret and use these templates without including the markers in rendered output.

Currently, suffixes like "(Optional)" in headings (e.g., in `adr.template.md`) can be misinterpreted. The new method must clearly indicate:

1. The entire section is optional and can be omitted.
2. If the section is included, the marker itself should not appear in the final rendered heading or content.

The chosen method will be documented in the [`ai-guides/core/template-files-working-guide.md`](../../../../ai-guides/core/template-files-working-guide.md). An ADR may be created if the decision has broad architectural implications.

## Artifacts

- [`ai-guides/core/template-files-working-guide.md`](../../../../ai-guides/core/template-files-working-guide.md) (To be updated)
- [`ai-guides/contrib/adrs/adr.template.md`](../../../../ai-guides/contrib/adrs/adr.template.md) (Example of current problematic marking)
- `artifacts/s075-optional-section-research.md` (To be created: Document for research findings)
- (Potentially) `docs/adrs/adr-XXX-optional-template-sections.md` (To be created if an ADR is needed)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Research Optional Section Marking Methods**

  - [ ] Research various methods for marking optional sections in text-based templates (e.g., Markdown).
  - [ ] Consider options such as HTML comments (under or within headings), specific placeholder syntax, or other conventions.
  - [ ] Evaluate each method based on clarity for human users, unambiguous interpretation by AI assistants, and ease of ensuring markers are not rendered.
  - [ ] Document findings, including pros and cons of different approaches, in `artifacts/s075-optional-section-research.md`.
  - [ ] User reviews research findings.
  - [ ] **Process:** All ACs within this 'Research Optional Section Marking Methods' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Define and Document New Convention**

  - [ ] Based on research, select or design a preferred method for marking optional template sections.
  - [ ] If the decision is significant or has broad implications, draft an ADR in `docs/adrs/adr-XXX-optional-template-sections.md` (XXX determined at execution) to document the chosen convention, rationale, and consequences.
  - [ ] Update the [`ai-guides/core/template-files-working-guide.md`](../../../../ai-guides/core/template-files-working-guide.md) to clearly document the new convention, providing examples.
  - [ ] (Optional) Identify 1-2 existing templates (e.g., `adr.template.md`) and update them to use the new convention as a proof of concept.
  - [ ] User reviews and approves the new convention and updated documentation.
  - [ ] **Process:** All ACs within this 'Define and Document New Convention' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [ ] **Process:** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [ ] **Process:** AI invites the user to provide their own retrospective feedback and discusses any suggestions.
  - [ ] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [ ] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
