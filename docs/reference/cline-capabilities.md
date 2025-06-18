# Cline Capabilities

- **Type:** Plugin (VS Code Extension)
- **Developer:** Cline
- **Homepage:** https://cline.bot/

---

Cline is an AI assistant that operates within a dedicated VS Code extension. A key characteristic of Cline is its modal operation, switching between "Plan Mode" for discussion and strategy, and "Act Mode" for tool execution and task implementation.

**Note on Modal Equivalence:** Functionally, Cline's Plan/Act model is similar to Cursor AI's modal approach. Cline's **Act Mode** (focused on tool execution and task implementation) is comparable to Cursor AI's **Agent Mode**, while Cline's **Plan Mode** (focused on discussion, strategy, and planning) is comparable to Cursor AI's **Ask Mode / General Chat** behavior.

## Context Inclusion

- **Initial Task Context:** Receives initial task instructions, which may include file content.
- **Environment Details:** Automatically receives `environment_details` with each user message, including:
  - VSCode Visible Files
  - VSCode Open Tabs
  - Current Time
  - Current Working Directory File Listing
  - Context Window Usage
  - Current Mode (Act/Plan)
  - System Information (OS, Shell, Home Directory)
  - Actively Running Terminals (if any)
  - Connected MCP Servers (if any)
- **Tool Outputs:** Receives the results of tool executions (e.g., `read_file` content, `execute_command` output if streamed, `list_files` results, `search_files` results, `browser_action` screenshots and logs).
- **User Messages:** All user messages and conversation history contribute to context.
- **File Content via `read_file`:** Can explicitly read file contents.
- **MCP Resources:** Can access resources provided by MCP servers via `access_mcp_resource`.

## Command Execution

- **`execute_command` Tool:** Can execute arbitrary CLI commands on the user's system.
  - Requires user approval for potentially impactful commands.
  - Commands are executed in the current working directory (`/Users/jimbo/checkouts/vibe-tasking`) unless `cd` is prepended.
  - Can run interactive and long-running commands.

## Other Notable Features

- **File System Operations:**
  - `read_file`: Read file content.
  - `write_to_file`: Create or overwrite files.
  - `replace_in_file`: Make targeted edits to existing files.
  - `list_files`: List directory contents (recursively or top-level).
  - `search_files`: Perform regex searches across files.
- **Code Analysis:**
  - `list_code_definition_names`: List top-level code definitions in a directory.
- **Browser Interaction:**
  - `browser_action`: Launch, click, type, scroll, and close a Puppeteer-controlled browser. Receives screenshots and console logs.
- **User Interaction:**
  - `ask_followup_question`: Ask clarifying questions with optional multiple-choice answers.
- **Task Management:**
  - `attempt_completion`: Signal task completion.
  - `new_task`: Create a new task with preloaded context.
- **MCP Integration:**
  - `use_mcp_tool`: Execute tools provided by connected MCP servers.
  - `access_mcp_resource`: Access data from MCP servers.
  - `load_mcp_documentation`: Load documentation for creating MCP servers.
- **Planning Mode:**
  - `plan_mode_respond`: Engage in conversational planning with the user.
- **Vision Capabilities:** Can analyze images provided by the user.
- **Direct Backend Connections:** Allows direct connection to various AI model backends (e.g., directly to Google's Gemini models via API key), as opposed to routing through an intermediary service.
