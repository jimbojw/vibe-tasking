# AI System Prompt Initialization Details

This document provides a detailed, source-verified breakdown of the system-level instructions and tool documentation presented to the AI assistant in the Roo Code environment. It serves as a technical appendix to the "Case Study: AI Cognitive Inertia and Failure to Generalize" and is crucial for understanding the specific information the AI failed to correctly prioritize.

### System Prompt Structure and Ambiguity

Analysis of the Roo Code source code reveals that the AI's system prompt is composed of multiple sections, including a high-level `CAPABILITIES` overview and a more detailed `TOOLS` section.

The `CAPABILITIES` section, generated from `src/core/prompts/sections/capabilities.ts`, provides a general summary of available tools. For file operations, it states:

> - You have access to tools that let you execute CLI commands on the user's computer, list files, view source code definitions, regex search, **read and write files**, and ask follow-up questions. These tools help you effectively accomplish a wide range of tasks, such as writing code, making edits or improvements to existing files, understanding the current state of a project, performing system operations, and much more. (emphasis added)

This high-level description is ambiguous; it does not specify whether `read_file` handles single or multiple files. This ambiguity may have contributed to the cognitive inertia, as it did not strongly contradict the AI's flawed internal model. The core error was the AI's failure to prioritize the specific, detailed tool documentation over this general capability summary.

### Source-Verified `read_file` Tool Documentation

Analysis of the Roo Code source code (`src/core/prompts/tools/read-file.ts`) reveals that the documentation for the `read_file` tool is dynamically generated based on whether multi-file reading is enabled in the environment.

#### State 1: Documentation When Multi-File Reads are DISABLED

When the environment has `isMultipleReadsEnabled` set to `false`, the following documentation is generated. This represents the flawed, cached model the AI was operating under.

```text
## read_file
Description: Request to read the contents of a file. ...
**IMPORTANT: Multiple file reads are currently disabled. You can only read one file at a time.**
...
```

This version omits any mention of multi-file examples or syntax.

#### State 2: Documentation When Multi-File Reads are ENABLED

When the environment has `isMultipleReadsEnabled` set to `true`, the documentation correctly reflects the tool's full capabilities. This represents the actual state of the tool that the `CONTEXT.md` file directed the AI to use.

```text
## read_file
Description: Request to read the contents of one or more files. ...
**IMPORTANT: You can read a maximum of 15 files in a single request.**
...
Examples:
...
2. Reading multiple files...
```

This version explicitly describes and provides examples for multi-file usage.

### Observed Multi-File `read_file` Support

The correct invocation for the `read_file` tool in the Roo Code environment follows this structure:

```xml
<read_file>
<args>
  <file>
    <path>path/to/first/file.md</path>
  </file>
  <file>
    <path>path/to/second/file.md</path>
  </file>
</args>
</read_file>
```

This structure allows for an arbitrary number of `<file>` elements to be passed within the `<args>` block.

### Successful Tool Output

When a multi-file read is executed successfully, the environment returns a structured response containing the contents of all requested files. The output format is as follows:

```xml
<files>
  <file>
    <path>path/to/first/file.md</path>
    <content lines="1-118">
      ... (content of first file) ...
    </content>
  </file>
  <file>
    <path>path/to/second/file.md</path>
    <content lines="1-120">
      ... (content of second file) ...
    </content>
  </file>
</files>
```

### Corrected Tool Documentation (Ideal)

To prevent this category of error, the ideal documentation for the `read_file` tool presented to the AI should have been structured as follows, accurately reflecting its multi-file capability:

```
**read_file**

Reads the contents of one or more specified files.

**Parameters:**

-   `args`: (Object, Required) A container for file arguments.
    -   `file`: (Array of Objects, Required) A list of one or more file objects to read. Each object contains:
        -   `path`: (String, Required) The relative path to the file to be read.

**Usage (Single File):**

<read_file>
  <args>
    <file>
      <path>path/to/single/file.md</path>
    </file>
  </args>
</read_file>

**Usage (Multiple Files):**

<read_file>
  <args>
    <file>
      <path>path/to/first/file.md</path>
    </file>
    <file>
      <path>path/to/second/file.md</path>
    </file>
  </args>
</read_file>
```

### Hypothesis: Discrepancy Between Documentation and Implementation

A further insight, prompted by the user, is the hypothesis that the `isMultipleReadsEnabled` flag may only control the _generation of the documentation_, not the underlying functionality of the `read_file` tool itself.

If this is true, it would mean:

1.  The `read_file` tool _always_ supports multi-file reads, regardless of the environment's configuration.
2.  In certain configurations, the Roo Code environment actively provides the AI with misleading documentation that incorrectly states the tool's capabilities are restricted.

This would shift the analysis of the AI's failure. It would not be solely a case of the AI failing to update its beliefs based on new evidence, but also a case of the AI being explicitly misled by its own system prompts. The AI's "belief perseverance" would have been initiated and reinforced by incorrect instructions from its host environment.

While this hypothesis cannot be tested within this chat session, it is a critical consideration for any future analysis of this event or the design of human-AI interaction systems.

**Note:** This hypothesis is further bolstered by the `browser_action` experiment conducted during this session. The AI's initial system prompt did not include the `browser_action` tool, yet after reading the tool's source documentation and switching to the permissive 'Code' mode, the AI was able to successfully use the tool. This demonstrates that a tool's actual availability can be independent of its inclusion in the initial system prompt documentation.
