# Roo Code Capabilities

- **Type:** Mode within the Roo AI Assistant
- **Developer:** RooCodeInc
- **Homepage:** https://github.com/RooCodeInc/Roo-Code

---

Roo Code is an AI-powered **autonomous coding agent** and a specialized mode of the Roo AI assistant. It's designed for direct code manipulation, file system operations, command execution, and task automation. When in "💻 Code" mode, Roo acts as a highly skilled software engineer, leveraging a comprehensive set of tools to interact with the development environment and help you build software more efficiently.

## Operational Approach

Roo Code operates with a distinct methodology designed for clarity, user control, and robustness:

- **Step-by-Step Execution:** Complex tasks are broken down into smaller, logical steps. Each step is typically performed by a single tool use.
- **User Confirmation and Oversight:** Users are informed of the intended action (tool use) before execution and receive the result afterward. This allows for continuous oversight and intervention if needed.
- **Tool-Driven Actions:** All significant actions are performed via explicit tools (e.g., [`read_file`](#file-system-operations), [`apply_diff`](#file-system-operations), [`execute_command`](#command-execution)). This makes the AI's operations transparent.
- **Iterative Refinement:** The workflow is inherently iterative. Each step builds upon the confirmed success of the previous one, allowing for adjustments and corrections along the way.
- **Error Management:** The incremental nature of changes makes it easier to identify, isolate, and recover from any errors or misapplications of tools, ensuring file integrity.

### Synergy with Structured Frameworks

The operational characteristics of Roo Code make it particularly well-suited for interacting with structured, documentation-centric frameworks like Vibe Tasking. Key aspects of this synergy include:

- **Procedural Adherence:** Roo Code's step-by-step, tool-driven nature aligns well with frameworks that require AI assistants to follow specific protocols, use templates, and update structured documents (e.g., Markdown files with frontmatter, checklists).
- **Checkpoint Management:** The emphasis on user confirmation after each significant action (or "Checkpoint" in Vibe Tasking terminology) is a core strength. Roo Code can use tools like [`ask_followup_question`](#user-interaction) to manage these pauses and ensure user alignment before proceeding, as often mandated by such frameworks.
- **Transparent Task Execution:** The explicit use of tools for all file operations, command execution, and information retrieval provides the transparency needed for users to trust and verify AI actions within a defined workflow.
- **Contextual Grounding:** Roo Code's ability to read specific documents on demand allows it to be effectively "grounded" in the context provided by framework documents (e.g., story details, procedural guides, templates), enhancing accuracy and relevance.

## What Roo Code Can Do

Based on its core design, Roo Code can:

- 🚀 **Generate Code** from natural language descriptions
- 🔧 **Refactor & Debug** existing code
- 📝 **Write & Update** documentation
- 🤔 **Answer Questions** about your codebase (often by switching to or utilizing "Ask" mode capabilities)
- 🔄 **Automate** repetitive tasks
- 🏗️ **Create** new files and projects
- 🌐 **Automate browser actions** (see Browser Interaction section below)
- 🔌 **Integrate** with OpenAI-compatible or custom APIs/models (primarily via MCP)
- 🎭 **Adapt** its “personality” and capabilities through [Custom Modes](https://docs.roocode.com/advanced-usage/custom-modes) (facilitated by `fetch_instructions` for mode creation).

## Context Inclusion

Roo Code mode operates with a rich contextual understanding derived from:

- **Initial Task Context:** User-provided instructions and any initial file content.
- **Environment Details:** Automatically received with each user message, including:
  - VSCode Visible Files (provides file paths; content requires `read_file`)
  - VSCode Open Tabs (provides file paths; content requires `read_file`)
  - Current Time
  - Current Workspace Directory File Listing (recursive on task start)
    - **Note:** This initial listing may omit the contents of Git submodule directories.
  - Current Context Size (Tokens)
  - Current Cost
  - Current Mode (and its capabilities/restrictions)
  - System Information (OS, Shell, Home Directory)
  - Actively Running Terminals (if any)
  - Connected MCP Servers (if any)
- **Tool Outputs:** Results from executed tools, such as file content from `read_file`, command output from `execute_command`, search results from `search_files`, etc.
- **User Messages:** The ongoing conversation history.
- **File Content via `read_file`:** Can explicitly read the full or partial content of any file.
- **MCP Resources:** Can access data and documentation from connected Model Context Protocol (MCP) servers.

## Core Capabilities & Tools

Roo Code mode utilizes the following tools to perform tasks:

### File System Operations

- **`read_file`**: Reads the content of one or more specified files. It is most efficient to read all known relevant files in a single operation.
  - **Multi-File Reading:** To read multiple files at once, include a separate `<file>` element for each path within the `<args>` block. This is the preferred method when multiple files are known to be required for a task.
  - **Example (Multi-File Read):**
    ```xml
    <read_file>
      <args>
        <file>
          <path>src/main.ts</path>
        </file>
        <file>
          <path>src/utils.ts</path>
        </file>
        <file>
          <path>README.md</path>
        </file>
      </args>
    </read_file>
    ```
  - **Note on AI Knowledge vs. Documentation:** An AI assistant's internal knowledge or system prompts may occasionally contain outdated information about tool capabilities. For instance, an assistant might believe `read_file` only supports single-file reads. However, as confirmed during a game of Sparkle (June 2025), this documentation is correct: `read_file` **does** support multi-file reading, and it is the preferred method. This documentation should always be considered the definitive source of truth for tool usage.
- **`write_to_file`**: Creates new files or completely overwrites existing files with new content. It will automatically create any parent directories in the specified path if they do not already exist.
- **`apply_diff`**: Applies one or more line-based changes (additions, deletions, modifications) to an existing file.
  - **Multiple Operations:** You can perform several distinct search-and-replace operations in a single call by providing multiple `<<<<<<< SEARCH...>>>>>>> REPLACE` blocks within the `<diff>` tag.
  - **Mastery Guide:** For detailed best practices, troubleshooting, and advanced usage, consult the [`apply-diff-mastering-guide.md`](../../ai-guides/contrib/apply-diff-mastering-guide.md).
- **`insert_content`**: Inserts blocks of text at a specified line number in an existing file.
  - **Appending:** To append content to the end of a file, use `line: 0`.
- **`search_and_replace`**: Performs text or regex-based search and replace operations within files.
- **`list_files`**: Lists files and directories within a specified path, with an option for recursive listing.
  - **Submodule Interaction Notes:**
    - When listing the project root (`.`), `list_files` may omit Git submodule parent directories (e.g., `vendor/`).
    - When `recursive:true` is used on a submodule's parent directory (e.g., `list_files vendor/ recursive:true`), it lists the submodule's root directory (e.g., `vibe-tasking/`) but does not recurse into the submodule's contents.
    - Even if `list_files recursive:true` targets a path _directly inside_ a submodule (e.g., `vendor/vibe-tasking/ai-guides/`), it appears to only list the immediate contents (first-level files and directories) and does not fully recurse into deeper subdirectories within that submodule path.
- **`search_files`**: Performs a regex search across files in a specified directory, providing context-rich results. This tool searches for patterns or specific content across multiple files, displaying each match with encapsulating context. The `path` parameter specifies the directory to search, which will be searched recursively.
  - **Parameters:**
    - `path`: (required) The directory to search in.
    - `regex`: (required) The regex pattern.
    - `file_pattern`: (optional) Glob pattern to filter files (e.g., `*.ts`). Defaults to `*` (all files).
  - **Usage Note for Recursive Search:** When performing a recursive search:
    - Set the `path` parameter to the top-level directory you want to search within.
    - Set the `file_pattern` parameter to a simple filename glob (e.g., `*.md`, `requirements.txt`). Avoid including directory components or complex path wildcards (like `docs/*/*.md` or `s*/story.md`) in `file_pattern` if `path` is already targeting the parent directory for recursion, as this can lead to incomplete or no results. The tool handles recursion based on the `path` parameter.
    - **Submodule Interaction & Result Limitation Notes:**
      - `search_files` _does_ traverse into Git submodule directories.
      - However, it may not return an exhaustive list of all matching files from within submodules, especially if the number of actual matches is large (e.g., observed returning ~10-27 matches when `find` command identified >200). This suggests potential internal result limiting or filtering.
      - The exact number of results from broad queries within submodules may show slight variability between identical calls.

### Code Analysis

- **`list_code_definition_names`**: Lists definition names (classes, functions, methods, etc.) from source code in a file or directory.

### Command Execution

- **`execute_command`**: Executes arbitrary CLI commands.
  - User approval may be implicitly or explicitly required.
  - Commands run in the workspace's default terminal or a specified working directory if `cd` is used.
  - Supports interactive and long-running commands. For important behavioral notes and best practices regarding command execution, see [`ai-cli-command-patterns.md`](./ai-cli-command-patterns.md).

### Browser Interaction

- **`browser_action`**: Launches and controls a headless browser to perform actions like navigating to URLs, clicking elements, typing text, and extracting content or screenshots. This is useful for web scraping, testing web applications, or interacting with web-based tools.
  - **Model Availability Note:** As of this writing, this tool is only enabled for use with Claude 3.5 and Claude 3.7 models. It will not be available as a tool for other models.

### User Interaction

- **`ask_followup_question`**: Asks the user clarifying questions, often providing suggested answers to expedite the process.
  - **Usage Notes:**
    - It is possible to provide only a single suggested answer, which can be useful for pacing or forcing a specific confirmation.
    - Markdown formatting is supported within the `<question>` content.
    - Markdown formatting is **not** supported within the `<suggest>` content.

### Task Management & Workflow

- **`attempt_completion`**: Signals that Roo believes the current task or sub-task is complete, presenting the result.
- **`new_task`**: Initiates a new, separate chat session to handle a sub-task, often in a different mode.
  - **UX Behavior:** This action opens a new, top-level chat window for the sub-task. The original ("host") chat session will pause, displaying a waiting or progress state, until the new task chat is completed or closed by the user.
  - **Context Inheritance:** The new task **does not** automatically inherit the conversational or file context from the host chat. Its initial context is defined _solely_ by the `message` parameter provided in the tool call. To provide file context to the new task, file paths must be explicitly referenced within the `message` string (e.g., "Please summarize the following document: @path/to/file.md"). The new task will then need to process this message and read the file itself.
- **`switch_mode`**: Requests a switch to a different operational mode.
  - **Usage Notes:**
    - This can be used to switch to any available mode, including standard modes (e.g., "Code", "Architect") and project-specific custom modes (e.g., "Vibe Strategist").
    - The primary reason to switch is to adopt the most appropriate persona, capabilities, and file permissions for the task at hand (e.g., switching to "Architect" for high-level planning before switching to "Code" for implementation, or switching to "Vibe Strategist" for meta-level analysis of the project's workflow).

### MCP (Model Context Protocol) Integration

- **`use_mcp_tool`**: Executes tools provided by connected MCP servers.
- **`access_mcp_resource`**: Accesses data resources exposed by MCP servers.
- **`fetch_instructions`**: Retrieves detailed instructions for complex or specialized tasks, such as creating new MCP (Model Context Protocol) servers or defining new [Custom Modes](https://docs.roocode.com/advanced-usage/custom-modes).

### Vision Capabilities

- Roo can analyze images provided by the user within the chat interface, incorporating visual information into its understanding and responses.

---

_This document outlines the primary capabilities of Roo in "Code" mode. As Roo and the Vibe Tasking framework evolve, these capabilities may be updated._
