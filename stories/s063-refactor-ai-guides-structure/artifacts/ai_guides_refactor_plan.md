# AI Guides Directory Refactoring Plan (Story s063)

This document outlines the plan for restructuring the `docs/ai-guides/` directory.

## 1. Current Structure of `docs/ai-guides/`

As of 2025-05-30, the contents are:

- `adr.template.md`
- `adrs-writing-guide.md`
- `article.template.md`
- `articles-writing-guide.md`
- `ascii-art-diagrams-authoring-guide.md`
- `README.md` (This will remain in `docs/ai-guides/`)
- `sequence-diagrams-authoring-guide.md`
- `updating-onboarding-guide.md`
- `tutorials/` (directory)
- `vibe-tasking/` (directory, containing framework-specific guides like `python-script-dry-run-guide.md`, `stories/` subdirectory, etc.)

## 2. Target Structure

The `docs/ai-guides/` directory will be reorganized as follows:

```
docs/ai-guides/
├── core/                  # Renamed from 'vibe-tasking/', for essential Vibe Tasking framework guides
│   ├── command-output-issues-handling-guide.md
│   ├── context-documents-writing-guide.md
│   ├── python-script-dry-run-guide.md
│   ├── README.md (from original vibe-tasking/README.md)
│   ├── template-files-working-guide.md
│   ├── stories/
│   │   ├── journal.template.md
│   │   ├── stories-planning-guide.md
│   │   ├── stories-structuring-guide.md
│   │   ├── stories-working-guide.md
│   │   └── story.template.md
│   └── ai-guides/  # Subdir for AI guide authoring guides & templates
│       ├── ai-guide.template.md
│       └── ai-guides-collaborative-designing-guide.md
├── contrib/               # For all other non-core AI guides, templates, tutorials
│   ├── ascii-art-diagrams-authoring-guide.md
│   ├── sequence-diagrams-authoring-guide.md
│   ├── updating-onboarding-guide.md
│   ├── adrs/       # Subdir for ADR authoring guides & templates
│   │   ├── adr.template.md
│   │   └── adrs-writing-guide.md
│   ├── articles/   # Subdir for Article authoring guides & templates
│   │   ├── article.template.md
│   │   └── articles-writing-guide.md
│   └── tutorials/
│       ├── tutorial-part.template.md
│       ├── tutorial-series-readme.template.md
│       └── tutorials-writing-guide.md
└── README.md              # Top-level README for ai-guides, to be updated
```

_(Note: The file listings for `core/`, `core/stories/`, `core/ai-guides/`, `contrib/adrs/`, `contrib/articles/`, and `contrib/tutorials/` are based on actual directory contents and this refined plan as of 2025-05-30.)_

## 3. Detailed Move Operations

1.  **Create `contrib` directory:**
    - `mkdir docs/ai-guides/contrib`
2.  **Rename `vibe-tasking` to `core`:** (This moves all its contents, including `ai-guide.template.md`, `ai-guides-collaborative-designing-guide.md`, etc., into `docs/ai-guides/core/`)
    - `mv docs/ai-guides/vibe-tasking docs/ai-guides/core`
3.  **Create new authoring subdirectories:**
    - `mkdir docs/ai-guides/core/ai-guides`
    - `mkdir docs/ai-guides/contrib/adrs`
    - `mkdir docs/ai-guides/contrib/articles`
4.  **Move specific guides and templates into their new authoring subdirectories:**
    - `mv docs/ai-guides/core/ai-guide.template.md docs/ai-guides/core/ai-guides/`
    - `mv docs/ai-guides/core/ai-guides-collaborative-designing-guide.md docs/ai-guides/core/ai-guides/`
    - `mv docs/ai-guides/adr.template.md docs/ai-guides/contrib/adrs/` (Source was top-level `docs/ai-guides/`)
    - `mv docs/ai-guides/adrs-writing-guide.md docs/ai-guides/contrib/adrs/` (Source was top-level `docs/ai-guides/`)
    - `mv docs/ai-guides/article.template.md docs/ai-guides/contrib/articles/` (Source was top-level `docs/ai-guides/`)
    - `mv docs/ai-guides/articles-writing-guide.md docs/ai-guides/contrib/articles/` (Source was top-level `docs/ai-guides/`)
5.  **Move remaining general guides and `tutorials/` directory from `docs/ai-guides/` to `docs/ai-guides/contrib/`:**
    - `mv docs/ai-guides/ascii-art-diagrams-authoring-guide.md docs/ai-guides/contrib/`
    - `mv docs/ai-guides/sequence-diagrams-authoring-guide.md docs/ai-guides/contrib/`
    - `mv docs/ai-guides/updating-onboarding-guide.md docs/ai-guides/contrib/`
    - `mv docs/ai-guides/tutorials docs/ai-guides/contrib/`

## 4. Post-Move Tasks (Covered by other ACs in s063)

- Update `docs/ai-guides/README.md`.
- Create and run a Python script to update cross-references project-wide.
- Draft and approve an ADR for this restructuring decision.
