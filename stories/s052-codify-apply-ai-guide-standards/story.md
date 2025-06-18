---
id: "s052-codify-apply-ai-guide-standards"
title: "Codify and Apply AI Guide Writing Standards"
status: "Done"
priority: "Medium"
tags: "documentation;ai-guide;refactor;consistency;voice;audience;standards"
resolution: "Implemented"
---

# Story: s052 - Codify and Apply AI Guide Writing Standards

## Description

As a project maintainer, I want to **first codify standards for writing AI guides** (including imperative voice and audience declaration) into a new `writing-ai-guides.md` document, and then **align all existing AI guides** in `docs/ai-guides/` to these standards. This will ensure AI assistants consistently receive clear, actionable instructions and understand their role as the target reader.

## Artifacts

- `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md` (New guide to be created, focusing on collaborative design and authoring standards)
- `docs/ai-guides/vibe-tasking/ai-guide.template.md` (New template to be created as a sibling)
- Potentially a new ADR in `docs/adrs/`

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup and Confirmation**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list (including all Checkpoints and nested ACs) for this story is accurate and complete before substantive work begins on later Checkpoints.

- [x] **Checkpoint: Create `collaboratively-designing-ai-guides.md` Standard and `ai-guide.template.md`**

  - [x] Create `docs/ai-guides/vibe-tasking/ai-guide.template.md` with a basic structure for new AI guides.
  - [x] Draft initial content for the new guide: `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md`.
  - [x] The draft includes guidance on the AI's role in collaboratively designing guides with users (eliciting intent, structuring, refining content).
  - [x] The draft incorporates standards for imperative voice, audience declaration, structure, and formatting, referencing the new `ai-guide.template.md`.
  - [x] User reviews and provides feedback on the content of both `ai-guides-collaborative-designing-guide.md` and `ai-guide.template.md`.
  - [x] Revisions are made to both files based on user feedback.
  - [x] The final `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md` and `docs/ai-guides/vibe-tasking/ai-guide.template.md` are approved by the user.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and link to the new/updated files.

- [x] **Checkpoint: Document Standardization Decision with ADR**

  - [x] Draft an Architecture Decision Record (ADR) outlining the context, decision, and consequences related to establishing the standard for AI guide authorship (as to be defined in `writing-ai-guides.md`).
  - [x] User reviews and approves the ADR content.
  - [x] The ADR is created in the `docs/adrs/` directory following project conventions (e.g., `adr-XXX-standardize-ai-guide-authoring.md`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and link to the ADR.

- [x] **Checkpoint: Scope Definition for Applying New Standard**

  - [x] The following existing AI guides are confirmed as in scope for alignment with the new `ai-guides-collaborative-designing-guide.md` standard (primarily for structural/formatting aspects, as the collaborative design part is for new guide creation):
    - [x] `docs/ai-guides/README.md`
    - [x] `docs/ai-guides/updating-installing-md-guide.md`
    - [x] `docs/ai-guides/updating-onboarding-guide.md`
    - [x] `docs/ai-guides/vibe-tasking/command-output-issues-handling-guide.md`
    - [x] `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md`
    - [x] `docs/ai-guides/vibe-tasking/README.md`
    - [x] `docs/ai-guides/vibe-tasking/stories/stories-working-guide.md`
    - [x] `docs/ai-guides/vibe-tasking/context-documents-writing-guide.md`
  - [x] User confirms this list is complete and correct for the scope of applying the new standard.

- [x] **Checkpoint: Align Existing AI Guides to the New Standard**
      _For each identified existing AI guide:_ - [x] `docs/ai-guides/README.md`: Reviewed, no changes needed, user approved. Journal updated. - [x] `docs/ai-guides/updating-installing-md-guide.md`: Aligned with new standards. User approved. Journal updated. - [x] `docs/ai-guides/updating-onboarding-guide.md`: Aligned with new standards. User approved. Journal updated. - [x] `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md`: Aligned with new standards. User approved. Journal updated. - [x] `docs/ai-guides/vibe-tasking/README.md`: Reviewed, no changes needed. Journal updated. - [x] `docs/ai-guides/vibe-tasking/stories/stories-working-guide.md`: Reviewed, no changes needed. Journal updated. - [x] `docs/ai-guides/vibe-tasking/context-documents-writing-guide.md`: Aligned with new standards. User approved. Journal updated.
      (All individual guide ACs are now implicitly covered by the list above)

  - [x] The guide's content is reviewed against the structural and formatting standards defined in `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md`.
  - [x] Necessary edits are made to align the voice to be imperative and action-oriented for an AI.
  - [x] The guide is checked for an explicit statement of its primary audience; if missing or unclear, the standard audience statement (as defined in `ai-guides-collaborative-designing-guide.md`) is added.
  - [x] User reviews and approves changes to each guide.
  - [x] **Process:** Journal updated after each guide modification, noting the file changed and a brief summary of alignment activities.

- [x] **Checkpoint: Final Review and Closure**
  - [x] User confirms the new `ai-guides-collaborative-designing-guide.md` and `ai-guide.template.md` are satisfactory.
  - [x] User confirms the ADR is satisfactory.
  - [x] User confirms all identified existing AI guides have been reviewed and updated satisfactorily as per the new standard.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set to "Implemented" in this `story.md`.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
