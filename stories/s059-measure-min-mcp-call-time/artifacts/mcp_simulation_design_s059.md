# MCP Simulation Design for s059

This document outlines the parameters, MCP server details, simulation procedure, and data collection for story s059.

## 1. Simulation Parameters

- **Number of MCP Calls:** 30 iterations.
- **AI Assistant:** Roo Code (Code Mode).
- **AI Model:** gemini-2.5-pro-preview-05-06.
- **MCP Server:** Custom minimal Node.js server (details below).

## 2. MCP Server Details

- **Location:** [`./mcp_server_s059/`](./mcp_server_s059/.placeholder)
- **Implementation:** Node.js with `@modelcontextprotocol/sdk` (Stdio transport).
- **Setup and Running:** See [`./mcp_server_s059/README.md`](./mcp_server_s059/README.md:1).
- **Key Tools for Simulation (via `use_mcp_tool` with server_name "s059-ping-server"):**
  - `ping_tool`: Records a server timestamp along with a client-provided identifier.
  - `report_pings_tool`: Returns all recorded ping data objects.
  - `clear_pings_tool`: Clears all recorded ping data.

## 3. Simulation Procedure (AI-Led)

The AI assistant will perform the following steps:

1.  **Install MCP Server Dependencies (if not already done):**

    - Command: `npm install`
    - Working Directory: `docs/stories/s059-measure-min-mcp-call-time/artifacts/mcp_server_s059`

2.  **Start the MCP Server:**

    - The server should be managed via MCP settings (e.g., in `.roo/mcp.json` or `.vscode/mcp.json`). Ensure "s059-ping-server" is enabled.
    - If manual start is needed for some reason:
      - Command: `node server.js`
      - Working Directory: `docs/stories/s059-measure-min-mcp-call-time/artifacts/mcp_server_s059`

3.  **Iterative MCP Calls (30 times):**
    For each step `N` from 1 to 30:

    - **Action:** Call the MCP server's `ping_tool`.
    - **Tool:** `use_mcp_tool`
    - **Parameters for `use_mcp_tool`:**
      - `server_name`: "s059-ping-server"
      - `tool_name`: "ping_tool"
      - `arguments`: `{ "call_identifier": "ping-[N]" }` (e.g., "ping-1", "ping-2", or AI's current timestamp string)
    - **Data to Record:**
      - `call_number` (N)
      - `client_call_identifier` sent (e.g., "ping-[N]")
      - Start time of the `use_mcp_tool` call (AI-side).
      - End time of the `use_mcp_tool` call (AI-side).
      - Duration of the `use_mcp_tool` call (AI-side, or calculated).
      - `server_timestamp` from the `ping_tool`'s JSON response.
      - `call_identifier` from the `ping_tool`'s JSON response (should match what was sent).

4.  **Report Pings:**

    - **Action:** Call the MCP server's `report_pings_tool`.
    - **Tool:** `use_mcp_tool`
    - **Parameters:** `server_name`: "s059-ping-server", `tool_name`: "report_pings_tool", `arguments`: `{}`
    - **Data to Record:** The full list of ping data objects returned by the server. This serves as a verification.

5.  **Clear Pings:**

    - **Action:** Call the MCP server's `clear_pings_tool`.
    - **Tool:** `use_mcp_tool`
    - **Parameters:** `server_name`: "s059-ping-server", `tool_name`: "clear_pings_tool", `arguments`: `{}`

6.  **Stop the MCP Server:**
    - Ensure the MCP server "s059-ping-server" is disabled in MCP settings if it was started via settings.
    - If started manually for testing, stop it (e.g., `Ctrl+C` or `kill` if backgrounded).

## 4. Data Collection and CSV Structure

- All AI interactions, `use_mcp_tool` calls (parameters and results), AI-reported timings, and MCP server responses must be logged meticulously during the simulation.
- This log will be parsed into `artifacts/mcp_simulation_data_s059.csv`.
- **CSV Columns (Revised):**
  1.  `call_number`: (Integer) The simulation call number (1 to 30 for pings).
  2.  `mcp_tool_name`: (String) e.g., "ping_tool".
  3.  `client_call_identifier`: (String) The identifier sent by the AI (e.g., "ping-N" or client timestamp).
  4.  `ai_call_start_time_iso`: (String) ISO 8601 timestamp of `use_mcp_tool` call start (from AI log).
  5.  `ai_call_end_time_iso`: (String) ISO 8601 timestamp of `use_mcp_tool` call end (from AI log).
  6.  `ai_call_duration_ms`: (Integer) Duration in milliseconds (from AI log or calculated).
  7.  `server_response_call_identifier`: (String) The `call_identifier` from the `ping_tool`'s JSON response.
  8.  `server_reported_timestamp`: (String) The `server_timestamp` from the `ping_tool`'s JSON response.

## 5. Note on Tool Repetition

- The previous attempt at this simulation encountered a tool repetition limit. This revised design, by sending a unique `call_identifier` with each `ping_tool` call, aims to make each invocation distinct, potentially bypassing this limit. This will be a key aspect to observe during the new simulation run.
