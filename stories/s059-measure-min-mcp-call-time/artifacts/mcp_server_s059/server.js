#!/usr/bin/env node
/**
 * @license
 * Copyright 2025 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  McpError,
  ErrorCode,
} from "@modelcontextprotocol/sdk/types.js";

// In-memory store for ping timestamps
// In-memory store for ping data objects { call_identifier: string, server_timestamp: string }
let pingTimestamps = [];

class PingMcpServer {
  constructor() {
    this.server = new Server(
      {
        name: "s059-ping-server", // Will be used in mcp_settings.json
        version: "0.1.0",
      },
      {
        capabilities: {
          tools: {}, // Resources not needed for this simple server
        },
      }
    );

    this.setupToolHandlers();

    this.server.onerror = (error) => console.error("[MCP Error]", error);
    process.on("SIGINT", async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: "ping_tool",
          description:
            "Records a server UTC timestamp along with a client-provided identifier.",
          inputSchema: {
            type: "object",
            properties: {
              call_identifier: {
                type: "string",
                description:
                  "A unique identifier for the ping call (e.g., client timestamp or sequence number).",
              },
            },
            required: ["call_identifier"],
          },
        },
        {
          name: "report_pings_tool",
          description: "Returns a list of all recorded ping data objects.",
          inputSchema: { type: "object", properties: {} },
        },
        {
          name: "clear_pings_tool",
          description: "Clears all recorded ping data.",
          inputSchema: { type: "object", properties: {} },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const serverTimestamp = new Date().toISOString();
      const args = request.params.arguments || {};

      switch (request.params.name) {
        case "ping_tool":
          if (
            !args.call_identifier ||
            typeof args.call_identifier !== "string"
          ) {
            throw new McpError(
              ErrorCode.InvalidParams,
              "Missing or invalid 'call_identifier' string argument for ping_tool."
            );
          }
          const pingData = {
            call_identifier: args.call_identifier,
            server_timestamp: serverTimestamp,
          };
          pingTimestamps.push(pingData);
          console.log(
            `MCP Server [s059-ping-server]: Received ping_tool call. Identifier: "${args.call_identifier}", Server Timestamp: ${serverTimestamp}. Total pings: ${pingTimestamps.length}`
          );
          return {
            content: [
              {
                type: "text",
                text: JSON.stringify({
                  message:
                    "Ping received, identifier and server timestamp recorded.",
                  call_identifier: args.call_identifier,
                  server_timestamp: serverTimestamp,
                  totalPings: pingTimestamps.length,
                }),
              },
            ],
          };
        case "report_pings_tool":
          console.log(
            `MCP Server [s059-ping-server]: Received report_pings_tool call. Reporting ${pingTimestamps.length} ping data objects.`
          );
          return {
            content: [
              {
                type: "text",
                text: JSON.stringify({ pings: pingTimestamps }), // pings is now an array of objects
              },
            ],
          };
        case "clear_pings_tool":
          const clearedCount = pingTimestamps.length;
          pingTimestamps = [];
          console.log(
            `MCP Server [s059-ping-server]: Received clear_pings_tool call. Cleared ${clearedCount} ping data objects.`
          );
          return {
            content: [
              {
                type: "text",
                text: JSON.stringify({
                  message: "All ping data cleared.",
                  clearedCount: clearedCount,
                }),
              },
            ],
          };
        default:
          throw new McpError(
            ErrorCode.MethodNotFound,
            `Unknown tool: ${request.params.name}`
          );
      }
    });
  }

  async run() {
    const transport = new StdioServerTransport(); // Using Stdio for local execution
    await this.server.connect(transport);
    // Stdio transport doesn't need a port, it communicates over stdin/stdout
    console.error("MCP Ping Server [s059-ping-server] running on stdio.");
  }
}

const server = new PingMcpServer();
server.run().catch(console.error);
