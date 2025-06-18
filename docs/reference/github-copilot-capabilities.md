# GitHub Copilot Capabilities

- **Type:** Plugin
- **Developer:** GitHub / OpenAI / Microsoft
- **Homepage:** https://copilot.github.com/

---

## Context Inclusion

- **Active Editor Context:** Copilot primarily uses the content of the currently open file and the immediate code around the cursor to generate suggestions.
- **Open Files:** May leverage content from other open files in the editor, especially in Copilot Chat (if enabled).
- **Project Awareness:** Has some awareness of the broader project, such as file structure and other files in the workspace, but this is more limited compared to assistants like Cursor AI or Cline.
- **Conversation History:** In Copilot Chat, maintains context from the current chat session to provide more relevant answers.
- **Explicit File Inclusion:** Does not allow explicit user control over which files are included in the AI context beyond what is open or selected.

## Command Execution

- **No Direct Command Execution:** Copilot does not have the ability to execute shell or terminal commands on the user's system.
- **Command Suggestion:** Can generate shell commands, scripts, and code snippets in response to user prompts, but the user must copy and run these commands manually.
- **Copilot Chat (Preview):** In some environments (e.g., VS Code with Copilot Chat), may offer clickable "Run in Terminal" buttons for suggested commands, but actual execution is always user-initiated.

## MCP Server Support (Preview)

- **Model Context Protocol (MCP):** GitHub Copilot in VS Code (version 1.99+) offers preview support for MCP, an open standard allowing AI models to interact with external tools and services.
- **Tool Interaction:** Through MCP servers, Copilot's agent mode can invoke tools for tasks like file operations, accessing databases, or calling APIs.
- **Configuration:** MCP servers can be configured via workspace (`.vscode/mcp.json`) or user settings.
- **Further Information:** For detailed setup and usage, refer to the official [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

## Other Notable Features

- **Code Completion:** Provides real-time code suggestions as you type, including entire lines or blocks of code.
- **Copilot Chat:** Offers a conversational interface for asking questions, generating code, explaining code, and more (available in supported IDEs).
- **Multi-Language Support:** Works with a wide range of programming languages and frameworks.
- **Documentation Assistance:** Can generate comments, docstrings, and documentation snippets.
- **Test Generation:** Can suggest unit tests and test cases for existing code.
- **Natural Language Interface:** Accepts natural language prompts for code generation and explanation.
- **No Direct File System Access:** Cannot read or write arbitrary files in the project outside of the current editor context.
- **No Model Selection:** Users cannot select or change the underlying AI model.
- **No Direct Web Search:** Does not have built-in web search or browsing capabilities.
