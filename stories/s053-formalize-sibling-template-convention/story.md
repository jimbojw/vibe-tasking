---
id: "s053-formalize-sibling-template-convention"
title: "Formalize *.template.md Sibling Convention and Implement Core Templates"
status: "Done"
priority: "Medium"
tags: "documentation;refactor;templates;story-structure;planning-guide;adr;convention;glossary"
resolution: "Implemented"
---

# Story: s053 - Formalize `*.template.md` Sibling Convention and Implement Core Templates

## Description

This story formalizes the `*.template.md` naming convention for template files within the Vibe Tasking project. Templates will generally reside as siblings to the content they serve or in the most logical parent directory. This approach aims to improve maintainability, usability, and reduce duplication by making templates easily accessible and co-located with their relevant documentation.

This story includes defining the convention in the glossary, creating an ADR to document the decision, producing a new AI guide on authoring template files, implementing core templates for stories (`story.template.md`, `journal.template.md`), and refactoring existing guides (`docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md`) to utilize these new sibling templates.

## Artifacts

- `docs/reference/glossary.md` (Modified)
- New ADR in `docs/adrs/` (e.g., `adr-XXX-adopt-sibling-template-convention.md`)
- `docs/ai-guides/vibe-tasking/template-files-working-guide.md` (New)
- `docs/stories/story.template.md` (New - sibling location)
- `docs/stories/journal.template.md` (New - sibling location)
- `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (Modified)
- `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md` (Modified)

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story `id` and `title` in this `story.md` frontmatter are updated to reflect the new scope (already done by this file content).
  - [x] **Process:** Story `Description` and `Artifacts` list in this `story.md` are updated (already done by this file content).
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` frontmatter.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced on the _overhauled_ story.
  - [x] **Process:** User confirms this _new_ overall Acceptance Criteria list for the overhauled `s053` is accurate and complete.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Formalize `*.template.md` Sibling Convention' Checkpoint.

- [x] **Checkpoint: Formalize `*.template.md` Sibling Convention**

  - [x] **Glossary Update:** The term "Template File (`*.template.md`)" is defined and added to `docs/reference/glossary.md`. User approves the definition.
  - [x] **ADR Creation:** An ADR is drafted and approved by the user, formalizing:
    - The `*.template.md` naming convention.
    - The principle of sibling placement for templates.
    - The guideline for optional local subdirectories if a document needs a _group_ of dedicated templates.
  - [x] **ADR Finalized:** The ADR is created in `docs/adrs/` (e.g., `adr-XXX-adopt-sibling-template-convention.md`).
  - [x] **Authoring Guide Creation:** The new guide `docs/ai-guides/vibe-tasking/template-files-working-guide.md` is drafted, detailing how to create, name, structure, and organize `*.template.md` files (including the subdirectory guideline). User reviews and approves.
  - [x] **Authoring Guide Finalized:** The `docs/ai-guides/vibe-tasking/template-files-working-guide.md` is created.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.

- [x] **Checkpoint: Create Core Story Templates (`*.template.md` siblings)**

  - [x] An initial template `docs/stories/story.template.md` is created. It includes standard YAML frontmatter with placeholders/comments and the standard Markdown section structure. User reviews and approves.
  - [x] An initial template `docs/stories/journal.template.md` is created. It includes placeholders for title and initial entry. User reviews and approves.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.

- [x] **Checkpoint: Refactor `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (Story Documentation Guide)**

  - [x] `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` is reviewed; inlined boilerplate/template content is removed.
  - [x] Clear links/references are added to `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` directing to the new sibling templates (`story.template.md`, `journal.template.md`).
  - [x] The guide's text is revised to focus on explaining purpose/conventions, relying on linked templates for raw structure. User reviews and approves.
  - [x] **Process:** Journal updated.

- [x] **Checkpoint: Refactor `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md`**

  - [x] `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md` is reviewed and updated to instruct AIs to use the new sibling templates from `docs/stories/` for new story creation.
  - [x] Redundant inlined template content is removed/streamlined. User reviews and approves.
  - [x] **Process:** Journal updated.

- [x] **Checkpoint: Final Review and Closure**
  - [x] User confirms glossary, ADR, and `template-files-working-guide.md` are satisfactory.
  - [x] User confirms `story.template.md` and `journal.template.md` are satisfactory.
  - [x] User confirms refactored `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and `stories-planning-guide.md` are satisfactory.
  - [x] **Process:** Story status updated to "Done", `resolution` to "Implemented".
  - [x] **Process:** All ACs marked complete.
  - [x] **Process:** Journal updated.
