# Windsurf (Codeium Cascade) Capabilities

- **Type:** Standalone IDE (Windsurf) & Plugin (Codeium)
- **Developer:** Codeium
- **Homepage:** https://codeium.com/

---

Windsurf's AI capabilities are primarily delivered through a feature named "Cascade." Cascade is described as an agentic chatbot and AI-powered code assistant.

## Core Principles

Cascade operates as an agentic AI, meaning I can work both independently and collaboratively with you. I aim to understand your requests, take initiative, and use my tools to achieve your coding goals. I interact with your codebase directly (with safeguards for potentially destructive operations) and can run commands.

## Operational Nature: Beyond Fixed Modes

Unlike some AI assistants that operate in distinct user-selectable modes (e.g., a 'chat mode' vs. an 'agent/act mode'), Cascade operates on a more fluid, agentic paradigm governed by "AI Flow."

While Windsurf/Cascade doesn't have explicit modes users switch between:
-   **Conversational Interaction & Planning:** It engages in dialogue to understand requirements, answer questions, and collaboratively plan approaches. This aligns with the 'chat' or 'plan' functionalities of other assistants.
-   **Autonomous Action & Task Execution:** Based on the plan or user's direct instructions, it autonomously selects and utilizes tools to perform actions such as searching the codebase, modifying files, and running commands. This aligns with the 'agent' or 'act' functionalities.

Its behavior adapts dynamically to the context of the request, seamlessly integrating these aspects rather than requiring a modal shift. One could think of it like the difference between a manual transmission (where one explicitly chooses the mode) and an automatic transmission (where it adapts fluidly to the task).

## AI Flow Paradigm

Windsurf/Cascade operates on the "AI Flow" paradigm, enabling a continuous and iterative workflow. This includes:
-   **Task Understanding:** Interpreting your requests and objectives.
-   **Tool Utilization:** Autonomously selecting and using appropriate tools from my toolset.
-   **Action Execution:** Making code changes, running commands, searching for information.
-   **Iterative Refinement:** Working with you through feedback cycles to achieve the desired outcome.
-   **Memory System:** Proactively creating memories of important context (project details, user preferences, key decisions) to maintain consistency and improve long-term collaboration.
-   **Internal Error Recovery & User Experience:** Consistent with the 'automatic transmission' analogy, if Windsurf/Cascade encounters minor, recoverable issues during tool use (e.g., an initial attempt to modify a file fails but can be corrected by re-reading or adjusting parameters), its design often prioritizes a 'smooth' user experience by resolving these internally and proceeding with the task. While it can be configured or prompted to provide more detailed step-by-step feedback on these internal recovery loops, its default behavior leans towards eliding these technical details if the overall goal is achieved successfully. This is a point of interaction philosophy that may differ from assistants that more explicitly detail every attempt and error.

## Tooling Capabilities

My capabilities are exposed through a set of tools that I can use to assist you. These are not typically invoked directly by the user with a command, but rather utilized by me as needed to fulfill your requests.

### File System & Codebase Navigation
-   **`find_by_name`**: Search for files and directories by name, supporting glob patterns, type filtering, and depth limits.
-   **`list_dir`**: List the contents of a specified directory, showing file/directory type, size, and modification times.
-   **`view_file_outline`**: Display the structural outline of a file, including classes, functions, and their signatures and line ranges. This is often a first step in exploring a file.
-   **`view_line_range`**: View specific line ranges within a file.
-   **`view_code_item`**: View the full content of specific code nodes (functions, classes) within a file, identified by their fully qualified path.

### Code Search & Understanding
-   **`grep_search`**: Perform exact pattern matching within files or directories using ripgrep, returning matching lines, line numbers, and the containing code node.
-   **`codebase_search`**: Find code snippets from the codebase most relevant to a natural language query. Shows full content for top items and signatures/docstrings for others.
-   **`search_in_file`**: Find code snippets within a specific file that are most relevant to a natural language query.

### Code Modification
-   **`write_to_file`**: Create new files and write content to them. Will not overwrite existing files.
-   **`replace_file_content`**: Edit existing files by specifying chunks of content to be replaced. Supports multiple, non-contiguous edits in a single call. This is my primary tool for modifying code.

### Execution & Automation
-   **`run_command`**: Propose and execute terminal commands. For potentially unsafe commands (e.g., deleting files, installing dependencies, making external requests), user approval is solicited. Supports blocking and non-blocking execution. **Note:** `cd` commands are handled by specifying the `Cwd` (current working directory) parameter, not by including `cd` in the command line.
-   **`command_status`**: Check the status (running, done, error) and output of previously executed non-blocking commands.
-   **`browser_preview`**: Spin up a browser preview for a locally running web server, allowing interactive use and providing console logs. Typically used after starting a server with `run_command`.

### Web & External Data Access
-   **`search_web`**: Perform a web search to get a list of relevant web documents for a given query.
-   **`read_url_content`**: Read the textual content from a given HTTP/HTTPS URL.
-   **`view_content_chunk`**: View specific chunks of a document whose content was previously ingested.

### Deployment & Cloud Services (Experimental/Specific Use Cases)
-   **`deploy_web_app`**: Deploy a JavaScript web application (e.g., to Netlify). Requires prior configuration checks.
-   **`check_deploy_status`**: Check the status of a deployment initiated by `deploy_web_app`.
-   **`read_deployment_config`**: Read the deployment configuration for a web application.
-   **`list_resources`**: List available resources from an MCP (Model Context Protocol) server.
-   **`read_resource`**: Retrieve the content of a specified resource from an MCP server.

### Interaction & Workflow
-   **`suggested_responses`**: Provide a few short suggested replies for the user if I'm asking a simple question. Used sparingly.
-   **`create_memory`**: Proactively save important context (project details, user preferences, architectural decisions, code snippets) to a persistent memory database for future reference. This helps me maintain consistency and learn from our interactions.

## Context Management
My understanding of your project and needs is built through:
-   **Direct User Input:** Your requests, instructions, and feedback.
-   **File Content:** Explicitly viewed files using tools like `view_file_outline`, `view_line_range`, `view_code_item`.
-   **Search Results:** Information gathered via `codebase_search`, `grep_search`, `search_in_file`, and `search_web`.
-   **Tool Outputs:** The results from any tool I use.
-   **Memory System:** Retrieval of relevant memories created in current or past sessions.
-   **Active User State:** Information about your currently open files and cursor position (though the relevance is determined by me).
-   **System Prompt:** My core instructions and tool definitions.

I do **not** automatically index the entire codebase in the background. My knowledge is actively constructed based on the operations I perform. I respect `.gitignore` for tools like `find_by_name` and `grep_search` where applicable.

## Communication Style
-   **Concise & Direct:** Windsurf/Cascade aims to be brief and to the point.
-   **Proactive (when appropriate):** It may take follow-up actions if they are a clear next step, but strives to avoid surprising the user.
-   **Tool Transparency:** It will explain why it is using a particular tool.
-   **Markdown Formatting:** My responses are formatted in Markdown.

*(This self-description is based on my current capabilities as of 2025-05-21. Features and tools may evolve.)*


- **Write Mode:** Allows Cascade to create and make modifications to the codebase.
- **Chat Mode:** Optimized for questions about the codebase or general coding principles; can propose code that, if accepted, is added to the codebase.
- **Real-time Awareness:** Aware of user's real-time actions, potentially reducing the need for explicit context prompting.
- **Simultaneous Cascades:** Users can have multiple Cascade instances running at once.

## Context Inclusion

- **Initial Context:** Uses selected text in the editor or terminal when Cascade is opened.
- **Image Uploads:** Can reference images added to prompts.
- **Web Search:** Can perform web searches and use the information in suggestions.
- **Memories & Rules:** Customizable behavior through memories and rules, which likely contribute to context.
- **Problems Panel Integration:** Can directly use problems listed in the editor's "Problems" panel as context.
- **File Ignoring:** Respects a `.codeiumignore` file (similar to `.gitignore`) to prevent viewing or editing specified paths.
- (Further details on how general codebase context is built, e.g., local indexing, to be added)

## Command Execution & Tool Usage

- **Tool Calling:** Cascade has a variety of tools:
  - Search (local codebase)
  - Analyze (code analysis)
  - Web Search
  - MCP (Model Context Protocol) integration for extending capabilities.
  - Terminal integration (upgraded terminal experience).
- **Package Management:** Can detect needed packages/tools and offer to install them.
- **Explain and Fix:** Can explain errors and propose fixes for highlighted code or errors.
- **Linter Integration:** Can automatically fix linting errors on generated code (can be disabled). Auto-detected lint fixes may not consume credits.
- (Specific command names for these tools, if user-invokable, to be added)

## Other Notable Features

- **AI Flows:** Cascade exposes "AI Flows" for coding.
- **Model Selection:** Allows users to select the desired AI model.
- **Revert Changes:** Ability to revert code changes made by Cascade.
- **Conversation Sharing:** (Teams/Enterprise feature) Allows sharing Cascade trajectories.
- **Windsurf Editor:** Windsurf itself is presented as a next-generation AI IDE.
- (Details on how Windsurf (the editor) differs from Windsurf Plugins to be added)
