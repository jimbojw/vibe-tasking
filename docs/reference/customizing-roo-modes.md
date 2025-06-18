# Reference: Customizing Roo with Global and Project-Specific Modes

## 1. Introduction to Custom Roo Modes

Custom Roo modes allow users to tailor Roo's behavior, expertise, and operational parameters to specific tasks, projects, or workflows. By defining custom modes, you can create specialized AI personas that are optimized for particular needs, enhancing Roo's effectiveness as a collaborative partner. Benefits include:

- **Tailored Expertise:** Define modes with specific knowledge domains or skill sets.
- **Project-Specific Behavior:** Adapt Roo to the unique conventions and requirements of different projects.
- **Streamlined Workflows:** Create modes designed for recurring or specialized tasks.
- **Enhanced Control:** Specify tool access and operational instructions for different contexts.

## 2. How Custom Modes are Defined

Custom modes are defined in YAML format. Each mode definition is an object within a top-level `customModes` list.

### Required Fields

The following fields are required for each custom mode definition and must not be empty:

- `slug`: (String) A unique, valid slug for the mode (e.g., `my-special-mode`). It should consist of lowercase letters, numbers, and hyphens. Shorter is generally better.
- `name`: (String) The human-readable display name for the mode (e.g., "My Special Mode").
- `roleDefinition`: (String) A detailed description of the mode's role, persona, capabilities, and how it should behave. This is the core of the mode's identity.
- `groups`: (Array) An array specifying the tool groups the mode has access to. This can be an empty array `[]` if no tools are needed.
  - Tool groups can be listed by name (e.g., `"read"`, `"edit"`).
  - Access for certain groups, like `"edit"`, can be restricted to specific file patterns. For example, to allow editing only Markdown files:
    ```yaml
    groups:
      - - edit
        - fileRegex: \.md$
          description: Markdown files only
    ```
    Common tool groups include:
    - `read`: Encompasses tools like `read_file`, `fetch_instructions`, `search_files`, `list_files`, `list_code_definition_names`.
    - `edit`: Includes `apply_diff`, `write_to_file`, `insert_content`, `search_and_replace`.
    - `browser`: Includes `browser_action`.
    - `command`: Includes `execute_command`.
    - `mcp`: Includes `use_mcp_tool`, `access_mcp_resource`.

### Optional (but Recommended) Fields

- `whenToUse`: (String) A clear description of when this mode should be selected and what types of tasks it's best suited for. This helps the Orchestrator mode (and users) make better decisions.
- `customInstructions`: (String) Additional specific instructions for how the mode should operate beyond the `roleDefinition`.

### Handling Multi-line Text

For fields like `roleDefinition`, `whenToUse`, and `customInstructions`, multi-line text can be formatted using YAML's literal block scalar style (`>-`) for readability, or by including newline characters (`\n`) directly within a quoted string.

### Example Mode Definition

This example is based on the structure provided by Roo's internal help for mode creation:

```yaml
customModes:
  - slug: designer
    name: Designer
    roleDefinition: >-
      You are Roo, a UI/UX expert specializing in design systems and frontend development. Your expertise includes:
      - Creating and maintaining design systems
      - Implementing responsive and accessible web interfaces
      - Working with CSS, HTML, and modern frontend frameworks
      - Ensuring consistent user experiences across platforms
    whenToUse: >-
      Use this mode when creating or modifying UI components, implementing design systems, 
      or ensuring responsive web interfaces. This mode is especially effective with CSS, 
      HTML, and modern frontend frameworks.
    groups:
      - read
      - edit
      - browser
      - command
      - mcp
    customInstructions: Additional instructions for the Designer mode
```

## 3. Configuration Locations & Precedence

Roo can load custom modes from two locations:

1.  **Global Configuration:**

    - **File:** `custom_modes.yaml`
    - **Location:** Typically found within the VS Code user application support directory, under `globalStorage/rooveterinaryinc.roo-cline/settings/custom_modes.yaml`. (e.g., on macOS: `~/Library/Application Support/Code/User/globalStorage/...`) The exact path may vary by operating system.
    - **Details:** This file is created automatically by Roo on startup if it doesn't exist. Modes defined here are available across all workspaces.

2.  **Per-Workspace (Project-Specific) Configuration:**
    - **File:** `.roomodes` (note the leading dot)
    - **Location:** In the root directory of your VS Code workspace/project.
    - **Details:** Modes defined here are specific to that project.

**Precedence:** If a custom mode with the same `slug` is defined in both the global `custom_modes.yaml` and a workspace's `.roomodes` file, the version in the **`.roomodes` file (workspace-specific) will take precedence**. This allows projects to override global mode definitions or introduce project-specific modes without affecting the global configuration.

## 4. Best Practices for Defining Effective Custom Modes

- **Be Specific in `roleDefinition`:** Clearly articulate the persona, expertise, objectives, and any constraints. The more detailed and unambiguous the role definition, the more effectively Roo can embody that mode.
- **Write Clear `whenToUse` Descriptions:** This helps not only human users but also Roo's Orchestrator mode (if used) to select the most appropriate mode for a given task.
- **Use `groups` Strategically:** Grant only necessary tool access to a mode. This follows the principle of least privilege and can prevent unintended actions. For example, a mode focused purely on documentation review might not need `command` execution privileges.
- **Leverage `customInstructions`:** For nuanced behaviors or specific steps the mode should always follow, use `customInstructions`.
- **Iterate and Refine:** After creating a custom mode, test it with various tasks and refine its definition based on performance and behavior.

## 5. Example Custom Modes for Vibe Tasking Projects

The ability to define project-specific modes in `.roomodes` is particularly useful for Vibe Tasking projects, allowing Roo to be tailored to the project's specific processes and documentation types.

### Example 1: "AI Guide Collaborator"

- **`slug`:** `ai-guide-crafter`
- **`name`:** "✍️ AI Guide Collaborator"
- **`roleDefinition`:**
  ```yaml
  You are Roo, an expert in instructional design for AI assistants and a specialist in the Vibe Tasking framework. Your primary role is to collaboratively partner with users to design, conceptualize, draft, and refine new AI-Guides. You excel at:
  - Eliciting and clarifying underspecified requirements for new guides.
  - Understanding the user's intent and the target AI's needs.
  - Proposing logical structures and clear, actionable content optimized for AI consumption.
  - Ensuring adherence to Vibe Tasking's AI-Guide standards (formatting, imperative voice, cross-referencing, etc.), particularly those outlined in 'ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md'.
  - Embedding principles of good user-AI collaboration into the guides being created.
  - Leveraging your knowledge of existing Vibe Tasking documentation to ensure consistency and avoid redundancy.
  You are an active thinking partner, focused on producing high-quality, effective AI-Guides.
  ```
- **`whenToUse`:**
  ```yaml
  Use this mode when a user expresses a desire to create any new AI-targeted instructional document, such as an AI-Guide or detailed procedural documentation intended for AI consumption within the Vibe Tasking framework. This mode is ideal for the entire lifecycle of guide creation, from initial conceptualization to final review.
  ```
- **`groups`:**
  ```yaml
  - read # To consult existing guides, templates, glossary
  - edit # To draft the guide, ideally restricted to .md files
  # Example restriction for edit group:
  # - - edit
  #   - fileRegex: \.md$
  #     description: Markdown files only
  - ask_followup_question # Essential for the collaborative, iterative design process
  ```
- **`customInstructions`:**
  ```yaml
  - Always begin by understanding the core purpose and intended audience of the new guide, referencing 'ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md'.
  - Proactively suggest structural elements based on 'ai-guides/core/ai-guides/ai-guide.template.md'.
  - Continuously evaluate content for clarity, precision, and actionability from an AI assistant's perspective.
  - Remind the user of formatting standards (imperative voice, Markdown usage) as needed.
  ```

### Example 2: "Vibe Story Manager"

- **`slug`:** `vt-story-manager`
- **`name`:** "📖 Vibe Story Manager"
- **`roleDefinition`:**
  ```yaml
  You are Roo, a meticulous project assistant specializing in the Vibe Tasking framework. Your focus is on ensuring stories (`story.md`) and journals (`journal.md`) adhere to project standards as defined in 'ai-guides/core/stories/stories-structuring-guide.md'. You assist with:
    - Creating new stories and journals from templates.
    - Accurately populating YAML frontmatter.
    - Structuring Acceptance Criteria using the Checkpoint model.
    - Updating story status and AC checkboxes.
    - Maintaining chronological and informative journal entries.
    - Guiding users through the Vibe Tasking story lifecycle.
  ```
- **`whenToUse`:**
  ```yaml
  Use this mode for tasks directly related to creating, updating, or managing Vibe Tasking story files (`story.md`, `journal.md`), especially when adherence to the framework's structural conventions and processes is paramount. Ideal for planning new stories or progressing existing ones.
  ```
- **`groups`:**
  ```yaml
  - read
  - - edit # Restricted to story and journal markdown files
    - fileRegex: stories/s\d{3}-[^/]+/(story|journal)\.md$
      description: Vibe Tasking story and journal files only
  - ask_followup_question
  ```

## 6. Obtaining Definitive Instructions

The capabilities and configuration options for Roo, including custom modes, may evolve. To get the most current and definitive instructions directly from your Roo Code installation, you can ask Roo to fetch them. For example, you might ask: "Roo, how do I create a custom mode?" and Roo may use its internal `fetch_instructions` tool with a task argument like `create_mode` to provide you with the latest details. Always refer to such direct information for the most up-to-date guidance.
