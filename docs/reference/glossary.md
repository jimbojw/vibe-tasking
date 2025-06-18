# Glossary of Vibe Tasking Documentation Terms

This glossary defines the key types of documentation used within the Vibe Tasking project and framework. Understanding these distinctions is crucial for both users navigating the documentation and AI assistants tasked with managing or utilizing it.

## Core Documentation Types

- **Article:**

  - **Audience:** Primarily Users.
  - **Purpose:** To provide user-focused documentation intended for readers. Articles explain concepts, offer guidance on how to use various aspects of the Vibe Tasking framework, or discuss best practices and related methodologies.
  - **Characteristics:** Explanatory, informative, and advisory.
  - **Examples:**
    - `understanding-vibe-tasking-story-structure.md`.

- **AI-Guide (AI Conceptual):**

  - **Audience:** Primarily AI Assistants.
  - **Purpose:** To provide AI-focused documentation that offers conceptual understanding, outlines scenarios, or presents decision-making frameworks for an AI assistant. AI-Guides are not direct scripts but help the AI understand _how_ or _why_ to perform certain actions, interpret situations, or assist users effectively within specific contexts.
  - **Characteristics:** Explanatory for AI, context-setting, and provides a basis for AI reasoning.

- **Reference:**

  - **Audience:** Both Users and AI Assistants.
  - **Purpose:** To provide factual, descriptive information about elements of the Vibe Tasking project or framework. This category is for materials that are consulted for specific pieces of information rather than read sequentially like an article or guide.
  - **Characteristics:** Factual, descriptive, and often list-based or definitional.
  - **Examples:**
    - This `glossary.md` file.
    - `ai-assistant-capabilities.md`.
    - `README.md` files that primarily list contents or provide brief overviews of a directory's purpose.

- **Template File (`*.template.md`):**
  - **Audience:** Primarily AI Assistants, but also Users creating new documents.
  - **Purpose:** To provide a standardized starting structure for various Vibe Tasking documents (e.g., `story.md`, `journal.md`, ADRs, new guides). Template files use the `*.template.md` naming convention and typically reside as siblings to the content they serve or in the most logical parent directory.
  - **Characteristics:** Pre-formatted Markdown files containing boilerplate structure, YAML frontmatter placeholders (where appropriate for the document type), and instructional comments to guide the creation of new documents, ensuring consistency and adherence to project conventions.
  - **Examples:**
    - `ai-guides/core/stories/story.template.md`
    - `ai-guides/core/stories/journal.template.md`
    - `ai-guides/contrib/adrs/adr.template.md`

## Core Vibe Tasking Concepts

- **Story (Vibe Tasking Story):**

  - **Audience:** Both Users and AI Assistants.
  - **Purpose:** A self-contained unit of work, task, or feature to be developed or addressed within a project using the Vibe Tasking framework. Each story is documented in a dedicated directory (e.g., `sXXX-descriptive-slug/`) and typically includes a `story.md` file (detailing its purpose, metadata, and acceptance criteria) and a `journal.md` file (for logging progress, decisions, and discussions).
  - **Characteristics:** The primary mechanism for defining, managing, and tracking development efforts and other project tasks in Vibe Tasking.

- **Checkpoint (within a Story):**

  - **Audience:** Both Users and AI Assistants.
  - **Purpose:** A major phase, milestone, or logical grouping of work within a Vibe Tasking story. Checkpoints are defined as top-level, typically bolded, list items in the story's Acceptance Criteria section in `story.md`.
  - **Characteristics:** A Checkpoint is considered complete when all its nested Acceptance Criteria are fulfilled and confirmed by the user. Progressing from one Checkpoint to the next requires explicit user approval as per the Checkpoint Review Protocol.

- **Acceptance Criteria (AC) (within a Story):**

  - **Audience:** Both Users and AI Assistants.
  - **Purpose:** Specific, verifiable conditions, tasks, or requirements that must be met for a Vibe Tasking story (or a Checkpoint within it) to be considered complete.
  - **Characteristics:** Presented as a checklist (e.g., `- [ ] Task description`) within the `story.md` file. ACs are marked as complete (`- [x]`) upon verification, typically during a Checkpoint Review Protocol.

- **User:**
  - **Audience:** N/A (Defines a role)
  - **Purpose:** Represents the individual, typically a developer or technical writer, interacting with the Vibe Tasking framework and AI assistants to manage and execute project tasks.
  - **Note on Terminology:** While "User" typically implies a human, the prefix "human" (e.g., "Human User") is generally superfluous and not required. "User" is sufficient unless specific distinction from an AI entity acting in a user-like role is necessary, which is rare in current Vibe Tasking contexts.

## AI Assistant Mechanisms

- **AI Guide Index:**

  - **Audience:** Primarily AI Assistants.
  - **Purpose:** Represents the AI assistant's in-memory, recallable knowledge of available AI Guides within the current project workspace. This "index" is typically formed by the AI assistant executing a specific shell command (as detailed in the **[Guide: Indexing, Discovering, and Using AI Guides](../../ai-guides/core/ai-guides/ai-guides-discovering-guide.md)**) which outputs each guide's `relative_path` and its `usage_string`.
  - **Characteristics:** The AI Guide Index is not necessarily a formal, rigidly defined data structure but rather the functional awareness the AI has of the guides. This awareness allows the AI to consult its "index" (i.e., its understanding of the command output) to identify potentially relevant guides for a given task by matching user intent against the `usage_string`s.
