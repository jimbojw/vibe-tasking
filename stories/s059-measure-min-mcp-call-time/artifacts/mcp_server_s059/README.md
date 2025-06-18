# Minimal MCP Server for s059

This directory contains a minimal Node.js MCP-compliant server designed for story s059 to measure MCP call timings. It uses the `@modelcontextprotocol/sdk` and communicates via Stdio.

## Files

- `package.json`: Defines dependencies (including `@modelcontextprotocol/sdk`) and a start script.
- `server.js`: The MCP server implementation.
- `.gitignore`: Ignores `node_modules` and log files.

## Setup

1.  **Install Dependencies:**
    Navigate to this directory (`docs/stories/s059-measure-min-mcp-call-time/artifacts/mcp_server_s059/`) in your terminal and run:
    ```bash
    npm install
    ```

## Running the Server (for direct testing or if not managed by MCP settings)

1.  **Start the Server:**
    From this directory, run:

    ```bash
    npm start
    ```

    Or directly:

    ```bash
    node server.js
    ```

    The server will log to stderr that it's "MCP Ping Server [s059-ping-server] running on stdio."

2.  **Running as a Background Process (Linux/macOS):**
    To run the server in the background for manual testing (if not relying on MCP settings to manage it):

    ```bash
    node server.js &
    ```

    Note the PID (Process ID) that is output by the shell. The `mcp_server.pid` file will also be created by the `execute_command` used in the story.

3.  **Finding the Process ID (PID):**
    If you need to find the PID later:

    ```bash
    ps aux | grep "node server.js"
    ```

    Look for the process related to this `server.js` file.

4.  **Stopping the Server:**
    - If running in the foreground, press `Ctrl+C` in the terminal.
    - If running in the background, use the PID:
      ```bash
      kill <PID>
      ```
      (Replace `<PID>` with the actual Process ID).

## MCP Tools Provided

When registered with an MCP manager (e.g., in `mcp_settings.json`), this server (named `s059-ping-server`) provides the following tools, callable via `use_mcp_tool`:

- **`ping_tool`**

  - **Description:** Records a server UTC timestamp along with a client-provided identifier.
  - **Input Schema:**
    ```json
    {
      "type": "object",
      "properties": {
        "call_identifier": {
          "type": "string",
          "description": "A unique identifier for the ping call (e.g., client timestamp or sequence number)."
        }
      },
      "required": ["call_identifier"]
    }
    ```
  - **Output:** JSON string: `{ "message": "Ping received, identifier and server timestamp recorded.", "call_identifier": "client_provided_id", "server_timestamp": "YYYY-MM-DDTHH:MM:SS.sssZ", "totalPings": count }`

- **`report_pings_tool`**

  - **Description:** Returns a list of all recorded ping data objects. Each object contains `call_identifier` and `server_timestamp`.
  - **Input Schema:** Empty object `{}`.
  - **Output:** JSON string: `{ "pings": [{"call_identifier": "id1", "server_timestamp": "ts1"}, {"call_identifier": "id2", "server_timestamp": "ts2"}, ...] }`

- **`clear_pings_tool`**
  - **Description:** Clears all recorded ping data objects.
  - **Input Schema:** Empty object `{}`.
  - **Output:** JSON string: `{ "message": "All ping data cleared.", "clearedCount": count }`

## Registration in MCP Settings

To use this server with `use_mcp_tool`, it needs to be added to your MCP settings file (e.g., `/Users/jimbo/Library/Application Support/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/mcp_settings.json`).

Example configuration:

```json
{
  "mcpServers": {
    "s059-ping-server": {
      "command": "node",
      "args": [
        "/full/path/to/docs/stories/s059-measure-min-mcp-call-time/artifacts/mcp_server_s059/server.js"
      ],
      "disabled": false,
      "alwaysAllow": []
    }
    // ... other servers
  }
}
```

**Note:** Replace `/full/path/to/` with the actual absolute path to the `server.js` file in your workspace.
