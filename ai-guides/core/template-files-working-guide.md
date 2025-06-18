---
id: "template-files-working-guide"
title: "AI Guide: Authoring Template Files (`*.template.md`)"
usage: "Use this guide to understand how to create, name, structure, organize, use, and maintain *.template.md files within the Vibe Tasking framework."
tags: "templates;documentation-standards;authoring;workflow;consistency"
---

# AI Guide: Authoring Template Files (`*.template.md`)

**(Primary Audience: AI Assistant (for understanding how to create, use, and maintain \*.template.md files).)**

This guide details how to create, name, structure, and organize `*.template.md` files within the Vibe Tasking framework. These templates serve as standardized starting points for various project documents.

## Purpose of Template Files

Template files (`*.template.md`) aim to:

- Ensure consistency in document structure and formatting.
- Reduce errors when creating new documents.
- Streamline the document creation process for both users and AI assistants.
- Provide a single source of truth for the basic layout of common document types.

## Naming Convention

- All template files **MUST** use the `.template.md` suffix.
  - Example: `story.template.md`, `adr.template.md`, `guide.template.md`.

## Placement Convention (Sibling Placement)

As defined in `docs/adrs/adr-019-adopt-sibling-template-convention.md`:

1.  **General Rule (Sibling or Parent):**

    - Templates should generally reside as "siblings" to the content they are intended to help create. This means a template file will be located in the same directory as the typical location for documents generated from it.
      - Example: `stories/story.template.md` is the template for new stories, which are created in subdirectories like `stories/sXXX-some-story/`.
    - If a template serves documents that could be placed in multiple sibling subdirectories (e.g., a generic `article.template.md` for articles in `docs/articles/topic-a/` or `docs/articles/topic-b/`), it should be placed in the most logical immediate parent directory (e.g., `docs/articles/article.template.md`).

2.  **Guideline for Multiple Local Templates (Optional `_templates/` Subdirectory):**
    - If a specific document type or a directory requires a _group_ of dedicated templates (more than one or two, e.g., variants of a story template), these templates can optionally be placed within a local subdirectory named `_templates/`.
      - Example: `stories/_templates/research_story.template.md`, `stories/_templates/bug_report_story.template.md`.
    - The leading underscore (`_`) indicates it's a utility directory, not part of the primary content structure.
    - For most common cases, a single `*.template.md` file directly alongside its target content's typical location (or in the immediate parent) is preferred for simplicity and discoverability.

## Structure and Content of Template Files

Template files are Markdown files and should include:

1.  **YAML Frontmatter (If Applicable):**

    - If the document type typically includes YAML frontmatter (e.g., `story.md`, ADRs), the template **MUST** include the standard frontmatter block with placeholder values and/or instructional comments.
    - Placeholders should clearly indicate what kind of information is expected (e.g., `id: "sXXX-your-story-slug"`, `title: "A Concise and Descriptive Title"`).
    - Use comments within the frontmatter (e.g., `# Status: To Do | In Progress | Done | Closed | Blocked`) to guide choices for specific fields.
    - Example for `story.template.md` frontmatter:
      ```yaml
      ---
      id: "sXXX-your-story-slug" # e.g., s001-initial-setup
      title: "A Concise and Descriptive Title for the Story"
      status: "To Do" # To Do | In Progress | Done | Closed | Blocked
      priority: "Medium" # High | Medium | Low
      tags: "tag1;tag2;feature" # Semicolon-separated list of relevant tags
      resolution: "Unresolved" # Unresolved | Implemented | Fixed | Obsolete | Won't Do | Duplicate | Cannot Reproduce | Invalid
      # created_date: (Handled by Git)
      # updated_date: (Handled by Git)
      ---
      ```

2.  **Markdown Body Structure:**

    - Include all standard top-level Markdown headings and sections expected for the document type.
    - Use placeholder text or instructional comments to guide the content for each section.

      - Example for a `story.template.md` body:

        ```markdown
        # Story: {{id_placeholder}} - {{title_placeholder}}

        ## Description

        (As a [type of user], I want [an action] so that [a benefit/value].)
        (Provide additional details and context here.)

        ## Artifacts

        - (Link to relevant design documents, e.g., `artifacts/design-v1.png`)
        - (Link to related stories, e.g., `../sYYY-related-story/story.md`)
        - (Link to code, e.g., `src/module/component.js`)

        ## Acceptance Criteria

        **IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

        - [ ] **Checkpoint: Initial Story Setup**

          - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
          - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
          - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
          - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
          - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
          - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

        - [ ] **Checkpoint: [First Substantive Phase of Work]**

          - [ ] (Define specific, verifiable ACs for this phase)
          - [ ] ...
          - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
          - [ ] **Process:** Journal updated.
          - [ ] **Process:** User approval obtained to proceed.

        - [ ] **Checkpoint: Final Review and Closure**
          - [ ] **Process:** User confirms all Checkpoints and ACs are complete.
          - [ ] **Process:** Story status updated to "Done" (or other terminal status) and `resolution` field set.
          - [ ] **Process:** All ACs within this Checkpoint are reviewed and marked complete.
          - [ ] **Process:** Journal updated.
        ```

    - Placeholders like `{{id_placeholder}}` or `{{title_placeholder}}` can be used to indicate where dynamic content (often derived from frontmatter) should be inserted. AI assistants should be instructed to replace these.

3.  **Instructional Comments:**
    - Use Markdown comments `<!-- Comment -->` or in-line parenthetical comments `(Comment)` to provide guidance directly within the template. These should explain how to fill out sections or what kind of information is expected. These comments should generally be removed when the template is used to create an actual document.

## Using Template Files

- **AI Assistants:** When tasked with creating a new document of a type that has a template (e.g., "Create a new story for X"), AI assistants **MUST** follow this general workflow:
  1.  **Locate Template:** Identify and read the appropriate `*.template.md` file.
  2.  **Determine File Path:** Determine the correct path and filename for the new document based on user instructions and project conventions (e.g., `stories/sXXX-new-story/story.md`).
  3.  **Gather Information & Resolve Placeholders:**
      - Obtain or confirm all necessary information to fill in template placeholders (especially critical fields like `id` and `title` in frontmatter).
      - If any required information is missing, ambiguous, or cannot be confidently inferred from the current context or prior user instructions (e.g., a specific date, a unique identifier), **prompt the user** for clarification or the precise value _before_ attempting to write the file. Avoid unnecessary prompting if the information is already clearly available.
      - **Crucially, all placeholder markers** (e.g., `{{placeholder}}`, `[USER_INPUT_HERE]`, `(some instruction like 'describe the benefit here')`) **MUST be replaced** with actual, determined values. **Under no circumstances should placeholder markers or instructional parentheticals intended for removal be left in the final document.** If unsure about a value for a placeholder after attempting to infer it, **always ask the user for the correct input** before proceeding to write the file.
  4.  **Prepare Full Content:** Internally, prepare the complete content for the new file:
      a. Start with the content of the template.
      b. Substitute all placeholders with their determined values.
      c. Populate any other sections of the document based on user input and further instructions.
      d. Remove any instructional Markdown comments (e.g., `<!-- ... -->`) unless they are explicitly intended to remain in the final document (which is rare).
  5.  **Write to File:** Write the fully prepared and populated content to the new file path.
  6.  **User Interaction for Review (Write-First, Check-After Preference):**
      - After successfully writing the file, if a direct user review of the newly created file is appropriate at this stage (i.e., not already covered by an imminent process step like a story's Checkpoint Review Protocol), **inform the user** that the file has been created (providing the path) and offer it for their review. For example: "I have created the file at `path/to/new/file.md`. It is available for your review."
      - This "write-first, then offer for review" approach is generally preferred if a check-in is made, as it aligns with common user preference for reviewing concrete artifacts.
      - Only deviate from writing first if:
        - The user explicitly requests to review draft content _before_ it's written.
        - Critical information is missing that prevents a sensible file from being written at all (as per step 3).
        - The specific context or governing process (e.g., a detailed story AC) dictates a different review timing or method.
- **Users:** Users can manually copy template content to create new files, then edit as needed.

## Maintaining Templates

- Templates should be kept up-to-date with any changes to project conventions or standard document structures.
- Updates to templates should be version-controlled like any other project file.
- When a template is updated, consider if existing documents created from older versions need to be retroactively updated (this is a case-by-case decision).

By following these guidelines, `*.template.md` files will serve as a valuable and reliable resource for maintaining documentation quality and consistency across the Vibe Tasking project.
