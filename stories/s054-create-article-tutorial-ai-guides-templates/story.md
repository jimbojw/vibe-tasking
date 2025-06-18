---
id: "s054-create-article-tutorial-ai-guides-templates"
title: "Create AI Guides and Templates for Authoring User Articles and Tutorials"
status: "Done"
priority: "Medium"
tags: "documentation;templates;articles;tutorials;ai-guide;standards;authoring;adr"
resolution: "Implemented"
---

# Story: s054 - Create AI Guides and Templates for Authoring User Articles and Tutorials

## Description

To ensure consistency and quality in user-facing documentation (articles and tutorials) for the Vibe Tasking project, this story will create:

1.  AI guides (in `docs/ai-guides/`) detailing how an AI assistant should help author standalone articles and multi-part tutorial series. These guides should be developed following `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md`.
2.  Corresponding document templates for these content types, which will be placed according to the sibling template convention outlined in `docs/adrs/adr-019-adopt-sibling-template-convention.md`. These templates should be developed following `docs/ai-guides/vibe-tasking/template-files-working-guide.md`.
    An ADR will document the decisions regarding these new standards and assets.

**Note on Template Placement:** Template placement will follow the conventions established in `docs/adrs/adr-019-adopt-sibling-template-convention.md`.

## Artifacts

- `docs/ai-guides/articles-writing-guide.md` (New AI guide)
- `docs/ai-guides/tutorials/tutorials-writing-guide.md` (New AI guide)
- `docs/ai-guides/article.template.md` (New template)
- `docs/ai-guides/tutorials/tutorial-series-readme.template.md` (New template)
- `docs/ai-guides/tutorials/tutorial-part.template.md` (New template)
- A new ADR in `docs/adrs/`

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list (including all Checkpoints and nested ACs) for this story is accurate and complete before substantive work begins on later Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Develop AI Guide and Template for Standalone Articles' Checkpoint.

- [x] **Checkpoint: Develop AI Guide and Template for Standalone Articles**

  - [x] Research and define best practices/standards for standalone technical articles within the Vibe Tasking project context.
  - [x] Create the AI guide `docs/ai-guides/articles-writing-guide.md`, following `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md`. This guide will instruct AI assistants on how to help users draft, structure, and refine standalone articles. It should cover common sections, tone, and linking conventions.
  - [x] Create the article template `docs/ai-guides/article.template.md`, following `docs/ai-guides/vibe-tasking/template-files-working-guide.md`. This template should include placeholders for standard sections (e.g., Introduction, Target Audience, Main Content, Conclusion, Related Links).
  - [x] User reviews and approves `docs/ai-guides/articles-writing-guide.md` and `docs/ai-guides/article.template.md`.
  - [x] **Process:** Journal updated.

- [x] **Checkpoint: Develop AI Guide and Templates for Multi-Part Tutorials**

  - [x] Research and define best practices/standards for multi-part tutorial series (referencing `docs/articles/onboarding/` as an example).
  - [x] Create the AI guide `docs/ai-guides/tutorials/tutorials-writing-guide.md`, following `docs/ai-guides/vibe-tasking/ai-guides-collaborative-designing-guide.md`. This guide will instruct AI assistants on structuring a tutorial series, creating individual parts, ensuring consistent navigation (Prev/Next/Up links), and managing a series `README.md`.
  - [x] Create the series overview template `docs/ai-guides/tutorials/tutorial-series-readme.template.md`, following `docs/ai-guides/vibe-tasking/template-files-working-guide.md` (for the main `README.md` of a tutorial series).
  - [x] Create the individual part template `docs/ai-guides/tutorials/tutorial-part.template.md`, following `docs/ai-guides/vibe-tasking/template-files-working-guide.md` (for `.md` files within a series, including navigation placeholders).
  - [x] User reviews and approves `docs/ai-guides/tutorials/tutorials-writing-guide.md`, `docs/ai-guides/tutorials/tutorial-series-readme.template.md`, and `docs/ai-guides/tutorials/tutorial-part.template.md`.
  - [x] **Process:** Journal updated.

- [x] **Checkpoint: Compose ADR for Article and Tutorial Authoring Standards**

  - [x] An ADR is drafted documenting the decision to establish these standards, AI guides, and templates for authoring user-facing articles and tutorials.
  - [x] The ADR outlines the rationale, the structure of the new assets, and their intended use.
  - [x] User reviews and approves the ADR content.
  - [x] The ADR is created in the `docs/adrs/` directory following project conventions (e.g., `adr-XXX-standardize-user-doc-authoring.md`).
  - [x] **Process:** Journal updated.

- [x] **Checkpoint: Final Review and Closure**
  - [x] User confirms `docs/ai-guides/articles-writing-guide.md` and `docs/ai-guides/article.template.md` are satisfactory.
  - [x] User confirms `docs/ai-guides/tutorials/tutorials-writing-guide.md`, `docs/ai-guides/tutorials/tutorial-series-readme.template.md`, and `docs/ai-guides/tutorials/tutorial-part.template.md` are satisfactory.
  - [x] User confirms the ADR is satisfactory.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set to "Implemented" in this `story.md`.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
