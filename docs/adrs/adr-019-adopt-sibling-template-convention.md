---
id: "adr-019"
title: "Adopt `*.template.md` Sibling Convention for Template Files"
status: "Accepted"
date: "2025-05-23" # Assuming acceptance date based on related story work
tags: "template;convention;standards;documentation;maintainability"
---

# ADR-019: Adopt `*.template.md` Sibling Convention for Template Files

## Context

The Vibe Tasking project relies on various standardized Markdown document structures (e.g., for stories, journals, ADRs, guides). Currently, guidance for creating these documents often involves copying and pasting from examples within existing documentation (like `docs/stories/README.md`) or relying on AI assistants to generate them based on general descriptions. This can lead to inconsistencies, outdated structures being propagated, and difficulty in maintaining a single source of truth for document formats.

A more robust system for managing and utilizing document templates is needed to improve maintainability, ensure consistency, and make it easier for both users and AI assistants to create new documents that adhere to project conventions.

## Alternatives Considered

No specific alternatives were detailed in the original ADR text. The decision appears to have been made to directly adopt a formal convention.

## Decision

We will adopt a formal convention for template files within the Vibe Tasking project:

1.  **Naming Convention:** Template files will use the `*.template.md` suffix (e.g., `story.template.md`, `adr.template.md`).
2.  **Placement Principle (Sibling Placement):**
    - Templates will generally reside as "siblings" to the content they are intended to help create. This means a template file will be located in the same directory as the typical location for documents generated from it. For example, `docs/ai-guides/core/stories/story.template.md` is the template for new stories, co-located with the guides on story structure and usage.
    - If a template serves documents across multiple sibling subdirectories, it should be placed in the most logical immediate parent directory. For example, a template for a generic guide that could be placed in `docs/ai-guides/` or `docs/articles/` might reside in `docs/guide.template.md` (if such a generic guide type existed and was common).
3.  **Guideline for Multiple Local Templates (Optional Subdirectory):**
    - If a specific document type or a directory requires a _group_ of dedicated templates (more than one or two), these templates can optionally be placed within a local subdirectory named `_templates/` (e.g., `docs/stories/_templates/advanced_story_variant.template.md`). This helps keep the primary directory cleaner while still ensuring templates are co-located with the content they serve. The leading underscore indicates it's a utility directory.
    - For most common cases, a single `*.template.md` file directly alongside its target content's typical location (or in the immediate parent) is preferred for simplicity.

## Consequences

### Positive

- **Improved Maintainability:** Templates provide a single source of truth for document structures, making updates easier to manage and propagate.
- **Enhanced Consistency:** New documents created from templates will adhere more reliably to project conventions.
- **Better Usability:** Users and AI assistants will have clear, easily discoverable starting points for new documents.
- **Reduced Duplication:** Boilerplate content can be removed from instructional guides (like the original `docs/stories/README.md` or the new `docs/ai-guides/core/stories/stories-structuring-guide.md`) and centralized in templates.
- **Clearer Intent:** The `*.template.md` suffix clearly identifies the purpose of these files.
- **Co-location:** Sibling placement makes templates easy to find and associate with the content they relate to.

### Negative

- **Initial Effort:** Requires creating the initial set of core templates and refactoring existing guides to reference them.
- **Discovery:** Users and AI assistants need to be aware of this convention and where to find templates. This will be mitigated by updating relevant guides (e.g., `docs/ai-guides/core/stories/stories-planning-guide.md`, `docs/ai-guides/core/stories/stories-structuring-guide.md`, and the lightweight `docs/stories/README.md`) and the glossary.

## Links / References

- The "Next Steps" mentioned in the original ADR (Create initial core templates, Update `docs/stories/README.md`, Update `docs/ai-guides/core/stories-planning-guide.md`, Create `docs/ai-guides/core/template-files-working-guide.md`, Add to glossary) are considered part of the implementation of story `s053-formalize-sibling-template-convention`.
