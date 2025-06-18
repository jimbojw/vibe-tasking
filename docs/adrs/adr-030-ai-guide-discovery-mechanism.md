---
id: "adr-030"
title: "AI Guide Discovery Mechanism"
status: "Proposed"
date: "2025-06-10"
tags: "ai-guides;discovery;indexing;shell-command;cli;architecture"
---

# ADR-030: AI Guide Discovery Mechanism

## Context

Vibe Tasking relies on AI assistants having access to a comprehensive suite of AI Guides to provide accurate and contextually relevant assistance. These guides can reside directly in the host project or within Git submodules (e.g., the Vibe Tasking framework itself in `vendor/`).

The primary challenge is ensuring that AI assistants can reliably discover _all_ available AI Guides, irrespective of their location within the project structure, particularly when standard file listing capabilities of AI assistants might not consistently traverse or reveal files within Git submodules. An incomplete understanding of available guides would limit the AI's effectiveness.

This ADR documents the decision for the standard mechanism by which AI assistants build an "AI Guide Index"—an inventory of available guides and their intended usage.

## Alternatives Considered

### Alternative 1: Standard AI File Listing Tools

- **Description:** Relying on the AI assistant's built-in file system listing capabilities (e.g., `list_files` tool, or information from `environment_details`).
- **Pros:**
  - Simple to invoke; uses existing AI toolset.
  - No external command execution required.
- **Cons:**
  - May not consistently or reliably discover files within Git submodules. This limitation can lead to an incomplete AI Guide Index. (As noted in the [AI Guide Discovery Process](ai-guides/core/ai-guides/ai-guides-discovering-guide.md:1), which references potential limitations detailed in `docs/reference/roo-code-capabilities.md`).
  - Might require reading full file lists, which could be inefficient for large projects.

### Alternative 2: Project-Specific Indexing Script

- **Description:** Developing and maintaining a dedicated script (e.g., Python, Node.js) within the Vibe Tasking project to scan for AI Guides and output an index (e.g., in JSON format).
- **Pros:**
  - Could provide a more robust and customizable indexing solution.
  - Output could be in a structured format, potentially easier for AIs to parse directly.
  - Could incorporate more complex logic for guide validation or metadata extraction.
- **Cons:**
  - Adds a development and maintenance burden for this new script.
  - Introduces a dependency on a specific scripting language interpreter being available in the user's environment.
  - May be overly complex for the fundamental task of path and usage string discovery.
  - Violates the ethos of [`adr-001-code-free-framework.md`](adr-001-code-free-framework.md:1) by introducing a script for maintenance, even if internal, which goes against the principle of minimizing code dependencies.

### Alternative 3: Manually Maintained Index File

- **Description:** Maintaining a dedicated index file (e.g., as a table or bulleted list within `ai-guides/README.md` or a separate `ai-guides-index.md`) that lists all AI Guides and their usage. The AI assistant would read this single file to build its index.
- **Pros:**
- Potentially very fast discovery for the AI, as it only needs to read one pre-compiled file.
- Simple for humans to read and understand the list of available guides.
- **Cons:**
- **(Minor) Index Maintenance:** The index file would require manual updates whenever guides are added, removed, or their usage strings change. While this could be partially scripted (e.g., via a dedicated AI Guide for index updates using CLI tools), it still introduces a maintenance step.
- **(Major) Host Project Discovery Problem:** This method does not inherently solve the problem of discovering AI Guides located in the host project when Vibe Tasking (or other guide libraries) are used as Git submodules. The index would cover guides within its own scope (e.g., Vibe Tasking's core guides), but host project guides would either need their own separate index or would still require a dynamic discovery process.
- **(Future Scalability) Multi-Submodule Issue:** If future projects adopt a pattern of providing AI Guide libraries via Git submodules, each such submodule would face the same discoverability challenge. The current Vibe Tasking `CONTEXT.md` includes a directive to load the `ai-guides-discovering-guide.md` (which uses shell commands), but this specific bootstrapping doesn't scale to arbitrary new submodules that might also be invisible to standard AI file listing tools.

## Decision

The chosen mechanism for AI Guide discovery is for the AI assistant to execute specific shell commands, tailored to the user's operating system (Linux/macOS or Windows). These commands are detailed in the [`ai-guides/core/ai-guides/ai-guides-discovering-guide.md`](../../ai-guides/core/ai-guides/ai-guides-discovering-guide.md:1).

Specifically:

1.  **Command Execution:** The AI executes a `find` (Linux/macOS) or `Get-ChildItem` (Windows PowerShell) command.
2.  **Scope:** These commands search for all `*-guide.md` files located within any `ai-guides/` directory structure, while excluding specific paths like story artifacts (`stories/sXXX-*/...`) and template files (`*.template.md`).
3.  **Metadata Extraction:** The commands extract the `usage: "..."` string from the YAML frontmatter of each discovered guide file.
4.  **Output Format:** The output is a list of lines, with each line containing `[relative_path]:[usage_string]`.
5.  **Index Creation:** The AI assistant uses this output to build an in-memory "AI Guide Index," mapping guide paths to their usage descriptions.

**Rationale:**

- **Submodule Traversal:** Shell commands like `find` and `Get-ChildItem` reliably traverse directory structures, including Git submodules, ensuring all guides are found.
- **Common Utilities:** These commands leverage standard, widely available shell utilities, minimizing new dependencies.
- **Simplicity for AI:** The process is relatively straightforward for an AI assistant to execute and parse the output, given the defined format.
- **Efficiency:** Targeted `grep` (or `Select-String`) within the shell commands allows for efficient extraction of the `usage` string without reading entire files initially.
- **Avoids New Dependencies:** This approach avoids adding a project-specific script and its associated language interpreter dependencies for this core discovery function.

## Consequences

### Positive

- **Comprehensive Discovery:** Ensures a complete inventory of AI Guides, including those within submodules.
- **Effective Indexing:** Allows AI assistants to build an effective in-memory index of available guidance, mapping paths to usage strings.
- **Improved AI Performance:** Leads to more accurate and contextually aware AI assistance by providing access to all relevant guides.
- **Standardization:** Provides a consistent, documented method for AI Guide discovery across different AI assistant implementations.

### Negative

- **Shell Capability Dependency:** Relies on the AI assistant possessing the capability to execute shell commands.
- **OS-Specific Commands:** Requires the AI assistant to correctly identify the user's operating system and use the appropriate command variant.
- **Frontmatter Parsing Fragility:** The extraction of the `usage:` string using `grep`/`sed` or PowerShell equivalents is dependent on the specific format of the frontmatter. Significant, uncoordinated changes to the `usage:` line format could break the extraction logic.
- **In-Memory Index:** The AI Guide Index is typically built in the AI's memory for the current session. It may need to be rebuilt or refreshed if the set of available guides changes significantly or upon starting new AI sessions (as per the process in the discovery guide).
- **Command Complexity:** The shell commands themselves are somewhat complex and could be prone to errors if modified without understanding their components.

## Links / References

- [`ai-guides/core/ai-guides/ai-guides-discovering-guide.md`](../../ai-guides/core/ai-guides/ai-guides-discovering-guide.md) (Defines the discovery process and commands)
- [`docs/reference/roo-code-capabilities.md`](../reference/roo-code-capabilities.md) (Referenced in the discovery guide regarding potential limitations of other file listing methods)
