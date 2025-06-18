---
id: "stories-structuring-guide"
title: "Guide: Structuring Vibe Tasking Stories"
usage: "Consult this guide *whenever planning, creating, interpreting, or progressing* Vibe Tasking stories to ensure adherence to standard structure, naming conventions, and content requirements for story directories and their core files (`story.md`, `journal.md`)."
tags: "stories;structure;conventions;yaml;frontmatter;acceptance-criteria;journaling"
---

# Guide: Structuring Vibe Tasking Stories

**(Primary Audience: AI Assistant (for understanding and assisting with the standard structure of Vibe Tasking story directories and files), Human User (for reference on story conventions).)**

## Introduction

This guide details the standard structure, naming conventions, and content requirements for Vibe Tasking story directories and their core files (`story.md`, `journal.md`). Adhering to these conventions is crucial for consistency, discoverability, and effective collaboration between users and AI assistants within the Vibe Tasking framework.

For a high-level overview of the `stories/` directory itself, please refer to the main [`stories/README.md`](../../../stories/README.md).

## Core Concepts: Story Organization

Vibe Tasking stories are organized into individual directories, each containing the necessary files to define, track, and manage a specific unit of work.

### Story Directory Naming Convention

Story directories should follow a consistent naming convention to ensure clarity and organization:

`sXXX-descriptive-slug`

- **`s`**: A literal 's' prefix to aid in discoverability (e.g., for `@` mentions in some UIs).
- **`XXX`**: A numeric prefix (e.g., `001`, `002`) for easy identification and ordering.
- **`descriptive-slug`**: A short, lowercase, hyphenated string briefly describing the story's content (e.g., `initial-setup`, `user-authentication`).

Example: `s001-initial-project-setup` (This would be a directory name)

### Core Story Directory Structure

Each story is represented by a directory named according to the convention above. This directory should contain the following standard files and may contain an optional subdirectory:

- **`story.md`**: The main file detailing the user story.
- **`journal.md`**: A chronological log of progress and discussions related to the story.
- **`artifacts/` (directory, optional)**: For storing any actual files related to the story.

The specific structure and boilerplate content for `story.md` and `journal.md` are based on templates, detailed further in the [Core Story Templates](#core-story-templates) section.

## `story.md` File Details

The `story.md` file is the heart of a Vibe Tasking story. It **must** begin with a YAML frontmatter block for metadata, followed by the Markdown content detailing the story.

### 1. YAML Frontmatter (Required)

- **Purpose:** Provides structured metadata for the story, enabling easy parsing, querying, and integration with potential tooling.
- **Core Fields:**
  - `id`: (String) A unique identifier for the story. This should ideally match the story's directory slug (e.g., `"s001-initial-project-setup"`).
  - `title`: (String) The human-readable title of the story (e.g., `"Initial Project Setup"`).
  - `status`: (String) The current workflow status of the story. Recommended values: `"To Do"`, `"In Progress"`, `"Done"`, `"Closed"`, `"Blocked"`. See `resolution` field for outcome details.
  - `priority`: (String) The priority of the story. Recommended values: `"High"`, `"Medium"`, `"Low"`.
  - `tags`: (String) A semicolon-separated list of keywords or labels for categorization and filtering (e.g., `"design;feature;ui"`). For lightweight stories, it's conventional to include the `lightweight` tag (e.g., `"fix;lightweight"`), as detailed in [`docs/adrs/adr-029-lightweight-story-type.md`](../../../docs/adrs/adr-029-lightweight-story-type.md).
  - `resolution`: (String) The outcome or reason for a story's terminal state, or `"Unresolved"` for active stories. Always present.
    - Default for active statuses (`"To Do"`, `"In Progress"`, `"Blocked"`): `"Unresolved"`.
    - For `status: "Done"`: e.g., `"Implemented"`, `"Fixed"`, `"Completed"`.
    - For `status: "Closed"`: e.g., `"Obsolete"`, `"Won't Do"`, `"Duplicate"`, `"Cannot Reproduce"`, `"Invalid"`.
- **Formatting for Queryability:**
  - Each field and its value must be on a single line.
  - All string values within the frontmatter (for these core fields) should be enclosed in double quotes.
- **Example Frontmatter:** Refer to the [`story.template.md`](story.template.md) for a complete example and standard fields.
- **Note on Dates:** `created_date` and `updated_date` fields are intentionally excluded. Version Control Systems (e.g., Git) are the source of truth for this information.

### 2. Story Title (Markdown)

A main heading (H1) indicating the story ID and a concise title, typically mirroring the frontmatter `title`. Refer to [`story.template.md`](story.template.md) for the standard format (e.g., `# Story: {{id}} - {{title}}`).

### 3. Description Section

- **User Story Format:** Clearly state the user story, often using the format: "As a [type of user], I want [an action] so that [a benefit/value]."
- **Details:** Provide any additional context or elaboration necessary to understand the story's scope and purpose.

### 4. Artifacts (Links) Section

A section to list and link to all relevant artifacts. This keeps all related information centralized.

- For files stored directly within this story's `artifacts/` subdirectory: `[Design Sketch](artifacts/sketch-v1.png)`
- For external documents: `[Technical Design Doc](https://link.to/your/doc)`
- For related code elsewhere in the repository: `src/module/component.js`
- For design documents or test scripts from other stories: `[Design Document for s002](../../../../stories/s002-design-enhanced-story-structure/artifacts/enhanced-story-structure-design.md)`

### 5. Acceptance Criteria (ACs) Section

A checklist of specific, verifiable criteria that must be met for the story to be considered complete. Vibe Tasking uses a "Checkpoint" model for structuring and progressing through ACs.

- **Checkpoints (Top-Level ACs):**
  - Major phases or logical groupings of work within a story are defined as **Checkpoints**.
  - These are typically represented as **bolded**, top-level list items in the AC list.
  - A Checkpoint is considered complete when all its nested Acceptance Criteria (see below) are completed and confirmed.
  - Upon completion of a Checkpoint (including performing the Checkpoint Review Protocol), the AI assistant **MUST** pause and explicitly ask the user for approval to proceed to the next Checkpoint. This is detailed in the **[Story Working Guide](stories-working-guide.md)**.
- **Acceptance Criteria (ACs - Nested or Standalone):**
  - These are the detailed, verifiable tasks. They are the items that get marked with `- [x]`.
  - ACs can be nested under a Checkpoint or can be standalone top-level items if the Checkpoint is simple enough to be described by a single AC.
  - **IMPORTANT:** As you complete each individual Acceptance Criterion (typically as part of a Checkpoint Review Protocol), you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).
- **Standard Process Checkpoints & ACs (Recommended Structure):** It's good practice to structure initial and final process steps as Checkpoints with their respective ACs. The [`story.template.md`](story.template.md) provides a recommended set of these process-oriented ACs for common checkpoints like "Initial Story Setup," "Substantive Work Phases," and "Final Review and Closure." These ensure key Vibe Tasking protocols are followed.
- **Tailoring Criteria to Story Type:** Beyond the standard process ACs, substantive Acceptance Criteria within Checkpoints should be tailored to the nature of the story. For instance:
  - **Research stories** typically focus on documented findings, analyses, or proof-of-concept results.
  - **Design stories** often culminate in specifications, diagrams, or mockups.
  - **Implementation stories** usually involve delivering working features, passing tests, and code deployment.
- **Note on Crafting Effective Substantive Criteria:** Beyond process steps, well-defined acceptance criteria for the story's actual deliverables **SHOULD** include steps for:
  - **User Confirmation:** Explicitly stating that the user reviews and approves the outcome (e.g., `- [ ] User confirms the implemented changes meet requirements.`).
  - **Validation & Testing:** Where applicable, including steps to run tests, execute scripts, or demonstrate functionality (e.g., `- [ ] All relevant tests pass.`, `- [ ] The updated script \`run_report.sh\` executes successfully and produces the expected output.`, `- [ ] AI demonstrates the new UI component rendering correctly.`).
    This practice ensures a clear definition of "Done" and facilitates a robust validation phase before story closure.

### Lightweight Story Variant

For simple, single-focus tasks, a "Lightweight Story" variant exists to streamline the process. Its definition and rationale are detailed in [`docs/adrs/adr-029-lightweight-story-type.md`](../../../docs/adrs/adr-029-lightweight-story-type.md).

Key characteristics relevant to structure:

- **Template:** Uses the [`lightweight-story.template.md`](lightweight-story.template.md).
- **Acceptance Criteria Structure:** Features a single "Combined Checkpoint" that encompasses initial setup, the core task, user approval, retrospective, and final closure ACs. This contrasts with the multi-checkpoint structure of standard stories.
- **Intended Use:** Suitable for tasks with one primary deliverable where the overhead of multiple distinct checkpoints is unnecessary (e.g., fixing a typo, updating a configuration value).
- **Tagging:** Conventionally tagged with `lightweight` in the YAML frontmatter for easy identification (see `tags` field description above).

When planning a story, if the task appears to fit these criteria, the [`stories-planning-guide.md`](stories-planning-guide.md) provides guidance on when and how to opt for this lightweight structure.

## `journal.md` File Details

A chronological log for progress, updates, decisions, discussions, and notes related to the story over time. This helps maintain a history of the story's lifecycle. For the standard structure and an example initial entry, refer to [`journal.template.md`](journal.template.md).

**Tip for Initial Journal Entry:** When drafting a new story, use the very first journal entry in its `journal.md` to capture any important context, discussions, decisions, or nuanced thoughts from the story drafting phase itself. This includes details not captured in `story.md`, such as options considered but discarded. This ensures that valuable, potentially unstated, background information is preserved right from the story's inception and is available for future reference by anyone (including AI assistants) working on or reviewing the story.

## `artifacts/` Directory (Optional)

An optional subdirectory for storing any actual files related to the story (e.g., images, small data files, scripts, text snippets). This directory should only be created when a story has artifacts to store. It provides a consistent location for story-specific assets.

- Artifacts within this directory **MUST** begin with a descriptive slug representing their purpose (e.g., `example-story-for-testing/` or `run_query_tests.sh`). This naming convention ensures they are distinct from story ID directory patterns and avoids confusion during autocompletion.

## Core Story Templates

To facilitate the creation of new stories and journals that adhere to the Vibe Tasking conventions, the following sibling template files are provided in this directory (`ai-guides/core/stories/`):

- **[`story.template.md`](story.template.md):** Use this template as the starting point for all new `story.md` files. It includes the standard YAML frontmatter structure, placeholder content, and the recommended Acceptance Criteria checkpoint layout.
- **[`journal.template.md`](journal.template.md):** Use this template for creating new `journal.md` files. It includes placeholders for the title and guidance for the initial journal entry.
- **[`lightweight-story.template.md`](lightweight-story.template.md):** Use this template for simple, single-focus tasks. It features a streamlined "Combined Checkpoint" structure.

AI assistants should be instructed to use these templates when creating new stories. Users can also copy these templates manually. For more detailed guidance on using and authoring templates, refer to the **[Template Files Working Guide](../template-files-working-guide.md)**.

## Flexibility

Vibe Tasking is unopinionated. Feel free to adapt the contents of `story.md` (beyond the core frontmatter) or `journal.md`, or add other files to the story directory to best suit your project's workflow and documentation needs. The key is consistency within your team and project regarding the core structure, for which these templates provide a baseline.

## Conclusion

Understanding and adhering to these structural conventions for Vibe Tasking stories ensures clarity, consistency, and efficient collaboration. By using the provided templates and following the guidelines for `story.md`, `journal.md`, and directory naming, both users and AI assistants can effectively manage and progress development tasks.
