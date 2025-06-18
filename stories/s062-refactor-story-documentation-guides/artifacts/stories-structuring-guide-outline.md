# Outline for ../../ai-guides/vibe-tasking/stories/stories-structuring-guide.md

1.  **Introduction**
    - Purpose of this guide: To detail the standard structure and conventions for Vibe Tasking story directories and their core files.
    - Link to the main `docs/stories/README.md` for a high-level overview of the stories directory.
2.  **Story Directory Naming Convention**
    - (Content from original `docs/stories/README.md` lines 7-15)
    - `sXXX-descriptive-slug` format explanation.
3.  **Core Story Directory Structure**
    - Overview of the standard files: `story.md`, `journal.md`, and optional `artifacts/` directory.
4.  **`story.md` File Details**
    - **YAML Frontmatter (Required)**
      - Purpose (metadata, querying).
      - Core Fields (id, title, status, priority, tags, resolution) with explanations and recommended values.
      - Formatting for Queryability.
      - Note on Dates (handled by Git).
      - Reference to `story.template.md` (sibling file).
    - **Story Title (Markdown)**
      - Standard format (referencing `story.template.md`).
    - **Description Section**
      - User Story Format.
      - Additional Details.
    - **Artifacts (Links) Section**
      - Purpose and examples.
    - **Acceptance Criteria (ACs) Section**
      - Checkpoint Model (Top-Level ACs).
      - Detailed ACs (Nested or Standalone).
      - Importance of marking ACs complete.
      - Standard Process Checkpoints & ACs (from `story.template.md` - sibling file).
      - Tailoring Criteria to Story Type (Research, Design, Implementation).
      - Note on Crafting Effective Substantive Criteria (User Confirmation, Validation/Testing).
5.  **`journal.md` File Details**
    - Purpose: Chronological log.
    - Tip for Initial Journal Entry.
    - Reference to `journal.template.md` (sibling file).
6.  **`artifacts/` Directory (Optional)**
    - Purpose: Storing story-specific files.
    - Naming convention for test scripts/examples within `artifacts/`.
7.  **Core Story Templates (`story.template.md`, `journal.template.md`)**
    - (Content from original `docs/stories/README.md` lines 131-137, adapted)
    - Brief description of each template.
    - Location (sibling files in `docs/ai-guides/vibe-tasking/stories/`).
    - Link to `docs/ai-guides/vibe-tasking/template-files-working-guide.md` for more details on template usage.
8.  **Flexibility**
    - (Content from original `docs/stories/README.md` lines 139-140)
    - Note on adapting contents while maintaining core structure.
