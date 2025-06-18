# Cursor AI Capabilities

- **Type:** Standalone IDE (VS Code Fork)
- **Developer:** Anysphere Inc.
- **Homepage:** https://cursor.sh/

---

Cursor AI allows for model selection, but its connections are typically intermediated by Cursor's backend, unlike Cline's direct connection capability. While users can opt out of having their content used for training, the passthrough via Cursor's backend is a characteristic of its architecture.

Cursor Chat (previously "Composer") operates with different modes:

  **Note on Modal Equivalence:** Functionally, Cursor's modal approach is similar to Cline's Plan/Act model. Cursor's **Agent Mode** is comparable to Cline's **Act Mode** (focused on tool execution and task implementation), while Cursor's **Ask Mode / General Chat** behavior is comparable to Cline's **Plan Mode** (focused on discussion, strategy, and planning).

- **Agent Mode:** The default and most autonomous mode. Designed to handle complex coding tasks with minimal guidance.
  - Autonomously explores the codebase, reads documentation, browses the web, edits files, and runs terminal commands.
  - Capabilities include:
    - `codebase_search`: Semantically search the codebase.
    - `read_file`: Read specific files or parts of files.
    - `edit_file`: Propose and apply code changes.
    - `file_search`: Find files by name.
    - `list_dir`: List contents of directories.
    - `run_terminal_cmd`: Execute terminal commands.
    - `grep_search`: Perform regex-based searches in files.
    - `delete_file`: Delete files.
    - `reapply`: Request a smarter model to reapply a previous edit.
    - `web_search`: Search the web for information.
  - Aims to make codebase-wide changes.
- **Ask Mode:** Used to get explanations and answers about the codebase and to plan out features with the AI.
- **Manual Mode:** For making focused edits using only the context explicitly provided by the user.
- **Custom Modes:** Users can create custom modes to suit specific workflows.
- Modes can be switched using a mode picker or a keyboard shortcut (e.g., `⌘K`).

## Context Inclusion

- **Agent Mode:** Dynamically gathers context by:
  - Exploring the codebase using `codebase_search` and `file_search`.
  - Reading specific files with `read_file`.
  - Listing directory contents with `list_dir`.
  - Accessing external information via `web_search`.
- **Manual Mode:** Uses only context provided by the user.
- General context can also be influenced by attached files and selected code snippets in the IDE.

## Command Execution

- **Agent Mode:** Can run terminal commands using the `run_terminal_cmd` tool. User approval is required before execution.
- **General Chat:** Can provide terminal command suggestions for the user to execute manually.

## Other Notable Features

- Model selection available (e.g., Claude variants, GPT models), though intermediated by Cursor's backend.
- Sidebar interface for Chat.
- Integrated diff views for proposed code changes.
- Ability to interact with linter results and suggest fixes.
- Can be explicitly directed to consult specific files or documentation.

## Available Tools (Self-Reported by Agent)

The following tools are directly available to the Cursor AI agent:

- `codebase_search(query: str, explanation: str | None = None, target_directories: list[str] | None = None)`: Find relevant code snippets.
- `read_file(target_file: str, start_line_one_indexed: int, end_line_one_indexed_inclusive: int, should_read_entire_file: bool, explanation: str | None = None)`: Read file contents.
- `run_terminal_cmd(command: str, is_background: bool, explanation: str | None = None)`: Propose a terminal command for execution.
- `list_dir(relative_workspace_path: str, explanation: str | None = None)`: List directory contents.
- `grep_search(query: str, case_sensitive: bool | None = None, exclude_pattern: str | None = None, explanation: str | None = None, include_pattern: str | None = None)`: Perform regex searches.
- `edit_file(target_file: str, code_edit: str, instructions: str)`: Propose file edits or create new files.
- `file_search(query: str, explanation: str)`: Fuzzy search for files by path.
- `delete_file(target_file: str, explanation: str | None = None)`: Delete a file.
- `reapply(target_file: str)`: Request a smarter model to reapply the last edit to a file if the diff was not as expected.
- `web_search(search_term: str, explanation: str | None = None)`: Search the web.
