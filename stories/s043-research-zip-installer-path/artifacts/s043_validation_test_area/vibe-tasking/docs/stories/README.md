# Vibe Tasking - Story Documentation Guide

This directory (`docs/stories`) is where user stories and their associated artifacts for the Vibe Tasking project itself are documented. It also serves as a living example of how the Vibe Tasking framework can be used.

## Story Directory Naming Convention

Story directories should follow a consistent naming convention to ensure clarity and organization:

`sXXX-descriptive-slug`

- **`s`**: A literal 's' prefix to aid in discoverability (e.g., for `@` mentions in some UIs).
- **`XXX`**: A numeric prefix (e.g., `001`, `002`) for easy identification and ordering.
- **`descriptive-slug`**: A short, lowercase, hyphenated string briefly describing the story's content (e.g., `initial-setup`, `user-authentication`).

Example: `s001-initial-project-setup` (This would be a directory name)

## Story Directory Structure

Each story is represented by a directory named according to the convention above. This directory should contain the following standard files and subdirectories:

- **`story.md`**: This is the main file detailing the user story. It **must** begin with a YAML frontmatter block for metadata, followed by the Markdown content.

  - **1. YAML Frontmatter (Required):**

    - **Purpose:** Provides structured metadata for the story, enabling easy parsing, querying, and integration with potential tooling.
    - **Core Fields:**
      - `id`: (String) A unique identifier for the story. This should ideally match the story's directory slug (e.g., `"s001-initial-project-setup"`).
      - `title`: (String) The human-readable title of the story (e.g., `"Initial Project Setup"`).
      - `status`: (String) The current workflow status of the story. Recommended values: `"To Do"`, `"In Progress"`, `"Done"`, `"Closed"`, `"Blocked"`. See `resolution` field for outcome details.
      - `priority`: (String) The priority of the story. Recommended values: `"High"`, `"Medium"`, `"Low"`.
      - `tags`: (String) A semicolon-separated list of keywords or labels for categorization and filtering (e.g., `"design;feature;ui"`).
      - `resolution`: (String) The outcome or reason for a story's terminal state, or `"Unresolved"` for active stories. Always present.
        - Default for active statuses (`"To Do"`, `"In Progress"`, `"Blocked"`): `"Unresolved"`.
        - For `status: "Done"`: e.g., `"Implemented"`, `"Fixed"`, `"Completed"`.
        - For `status: "Closed"`: e.g., `"Obsolete"`, `"Won't Do"`, `"Duplicate"`, `"Cannot Reproduce"`, `"Invalid"`.
    - **Formatting for Queryability:**
      - Each field and its value must be on a single line.
      - All string values within the frontmatter (for these core fields) should be enclosed in double quotes.
    - **Example Frontmatter:**
      ```yaml
      ---
      id: "s003-new-feature-x"
      title: "Implement New Feature X"
      status: "To Do"
      priority: "Medium"
      tags: "feature;backend;api"
      resolution: "Unresolved"
      ---
      ```
    - **Note on Dates:** `created_date` and `updated_date` fields are intentionally excluded. Version Control Systems (e.g., Git) are the source of truth for this information.

  - **2. Story Title (Markdown):** A main heading indicating the story ID and a concise title, typically mirroring the frontmatter `title`.
    Example: `# Story: s001 - Initial Project Setup`

  - **3. Description:**

    - **User Story Format:** Clearly state the user story, often using the format: "As a [type of user], I want [an action] so that [a benefit/value]."
    - **Details:** Provide any additional context or elaboration necessary to understand the story's scope and purpose.

  - **4. Artifacts (Links):** A section to list and link to all relevant artifacts. This keeps all related information centralized.

    - For files stored directly within this story's `artifacts/` subdirectory: `[Design Sketch](artifacts/sketch-v1.png)`
    - For external documents: `[Technical Design Doc](https://link.to/your/doc)`
    - For related code elsewhere in the repository: `src/module/component.js`
    - For design documents or test scripts from other stories: `[Design Document for s002](../s002-design-enhanced-story-structure/artifacts/enhanced-story-structure-design.md)`

  - **5. Acceptance Criteria:** A checklist of specific, verifiable criteria that must be met for the story to be considered complete. Vibe Tasking uses a "Checkpoint" model for structuring and progressing through ACs.

    - **Checkpoints (Top-Level ACs):**

      - Major phases or logical groupings of work within a story are defined as **Checkpoints**.
      - These are typically represented as **bolded**, top-level list items in the AC list.
      - A Checkpoint is considered complete when all its nested Acceptance Criteria (see below) are completed and confirmed.
      - Upon completion of a Checkpoint (including performing the Checkpoint Review Protocol), the AI assistant **MUST** pause and explicitly ask the user for approval to proceed to the next Checkpoint. This is detailed in `docs/guides/working-on-stories-guide.md`.

    - **Acceptance Criteria (ACs - Nested or Standalone):**

      - These are the detailed, verifiable tasks. They are the items that get marked with `- [x]`.
      - ACs can be nested under a Checkpoint or can be standalone top-level items if the Checkpoint is simple enough to be described by a single AC.
      - **IMPORTANT:** As you complete each individual Acceptance Criterion (typically as part of a Checkpoint Review Protocol), you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

    - **Standard Process Checkpoints & ACs (Recommended Structure):** It's good practice to structure initial and final process steps as Checkpoints with their respective ACs. For example:

      - `- [ ] **Checkpoint: Initial Story Setup**`
        - `- [ ] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.`
        - `- [ ] **Process:** A new journal entry is appended to `journal.md` for this story, noting work has commenced.`
        - `- [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.`
        - `- [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).`
        - `- [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.`
        - `- [ ] **Process:** User approval is obtained to proceed to the 'First Substantive Phase of Work' Checkpoint (or next appropriate checkpoint).`
      - `- [ ] **Checkpoint: [First Substantive Phase of Work]**`
        - `- [ ] AC 1 for this phase...`
        - `- [ ] AC 2 for this phase...`
        - `- [ ] **Process:** All ACs within this '[First Substantive Phase of Work]' Checkpoint are reviewed with the user and marked as complete (`- [x]`).`
        - `- [ ] **Process:** Journal updated to reflect completion of this '[First Substantive Phase of Work]' Checkpoint and any significant decisions made within it.`
        - `- [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.`
      - `- [ ] **Checkpoint: [Second Substantive Phase of Work]**`
        - `- [ ] ...`
        - `- [ ] **Process:** All ACs within this '[Second Substantive Phase of Work]' Checkpoint are reviewed with the user and marked as complete (`- [x]`).`
        - `- [ ] **Process:** Journal updated to reflect completion of this '[Second Substantive Phase of Work]' Checkpoint and any significant decisions made within it.`
        - `- [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.`
      - `- [ ] **Checkpoint: Final Review and Closure**`
        - `- [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.`
        - `- [ ] **Process:** Story status is updated to "Done" (or other terminal status) and `resolution` field is set appropriately.`
        - `- [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).`
        - `- [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.`

    - **Tailoring Criteria to Story Type:** Acceptance Criteria within Checkpoints should be tailored to the nature of the story. For instance:

      - **Research stories** typically focus on documented findings, analyses, or proof-of-concept results.
      - **Design stories** often culminate in specifications, diagrams, or mockups.
      - **Implementation stories** usually involve delivering working features, passing tests, and code deployment.

    - **Note on Crafting Effective Substantive Criteria:** Beyond process steps, well-defined acceptance criteria for the story's actual deliverables **SHOULD** include steps for:
      - **User Confirmation:** Explicitly stating that the user reviews and approves the outcome (e.g., `- [ ] User confirms the implemented changes meet requirements.`).
      - **Validation & Testing:** Where applicable, including steps to run tests, execute scripts, or demonstrate functionality (e.g., `- [ ] All relevant tests pass.`, `- [ ] The updated script `run_report.sh` executes successfully and produces the expected output.`, `- [ ] AI demonstrates the new UI component rendering correctly.`).
        This practice ensures a clear definition of "Done" and facilitates a robust validation phase before story closure.

- **`journal.md`**: A chronological log for progress, updates, decisions, discussions, and notes related to the story over time. This helps maintain a history of the story's lifecycle.
  Example initial content for `s001-initial-project-setup/journal.md`:

  ```markdown
  # Journal: s001 - Initial Project Setup

  ## 2025-05-16T10:30:00Z

  - Initial project setup completed.
  - Core documentation files (`README.md`, `LICENSE`, `CONTRIBUTING.md`) established.
  - Vibe Tasking story structure defined with a directory per story (`story.md`, `journal.md`, `artifacts/`).
  - Story documentation guide (`docs/stories/README.md`) created.
  - This story (s001) updated to reflect the completion of these setup tasks.
  ```

  **Tip for Initial Journal Entry:** When drafting a new story, consider using the very first journal entry in its `journal.md` to capture any important context, discussions, decisions, or nuanced thoughts from the story drafting phase itself. This ensures that valuable, potentially unstated, background information is preserved right from the story's inception and is available for future reference by anyone (including AI assistants) working on or reviewing the story.

- **`artifacts/` (directory)**: An optional subdirectory for storing any actual files related to the story (e.g., images, small data files, scripts, text snippets). This directory should only be created when a story has artifacts to store. It provides a consistent location for story-specific assets.
  - For test scripts or example artifacts within this directory, use a non-`sXXX` prefix (e.g., `example-story-for-testing/` or `run_query_tests.sh`) to avoid confusion with actual story IDs during autocompletion.

## Command-Line Querying Stories

With metadata in YAML frontmatter, stories can be queried directly from the command line.

### Example Queries (\*nix - macOS/Linux)

These examples assume stories are located in `docs/stories/sXXX-slug/story.md`.

**Find stories with status "In Progress":**

```bash
grep -l -E '^status: "In Progress"' docs/stories/s*/story.md | sed -E 's|docs/stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

**Find stories tagged with "design":**
(This regex ensures "design" is matched as a whole tag within the semicolon-delimited list.)

```bash
grep -l -E '^tags: "([^"]*;)*design([^"]*;|")[^"]*"' docs/stories/s*/story.md | sed -E 's|docs/stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

### Example Queries (Windows - PowerShell)

**Find stories with status "In Progress":**

```powershell
Get-ChildItem -Path "docs\stories\s*\story.md" -Recurse | Select-String -Pattern '^status: "In Progress"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

**Find stories tagged with "design":**
(This regex ensures "design" is matched as a whole tag within the semicolon-delimited list.)

```powershell
Get-ChildItem -Path "docs\stories\s*\story.md" -Recurse | Select-String -Pattern '^tags: "([^"]*;)*design([^"]*;|")[^"]*"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

Refer to the `s001-initial-project-setup/`, `s002-design-enhanced-story-structure/`, and `s003-implement-enhanced-story-structure/` directories in this guide for concrete examples of this structure. The design document for this enhanced structure can be found at `s002-design-enhanced-story-structure/artifacts/enhanced-story-structure-design.md`.

## Flexibility

Vibe Tasking is unopinionated. Feel free to adapt the contents of `story.md` (beyond the core frontmatter) or `journal.md`, or add other files to the story directory to best suit your project's workflow and documentation needs. The key is consistency within your team and project regarding the core structure.
