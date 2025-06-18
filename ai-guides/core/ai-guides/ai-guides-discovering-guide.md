---
id: "ai-guides-discovering-guide"
title: "Guide: Indexing, Discovering, and Using AI Guides"
usage: "Use this guide to understand how an AI assistant can become aware of all available AI Guides (by building an AI Guide Index via a shell command) and then dynamically consult this index to find and use relevant guides for specific tasks. This is particularly important for discovering guides within Git submodules."
tags: "ai-guides;discovery;indexing;awareness;shell-command;submodules;usage;context;workflow;guide-index;path-usage"
---

# Guide: Indexing, Discovering, and Using AI Guides

**(Primary Audience: AI Assistant (to understand and execute the standard process for building an inventory of AI Guides and then finding and using relevant ones).)**

## Introduction

This guide details the standard process an AI assistant **MUST** follow. **The first action upon understanding this guide is to build the AI Guide Index** (an inventory of available AI Guides and their purposes). Subsequently, you will dynamically consult this index to identify and use the most relevant guide(s) for specific user tasks or requests.

The AI Guide Index is a crucial in-memory, recallable knowledge base of available AI Guides' `relative_path` and `usage_string`. Building this index correctly, especially to include guides within Git submodules, is the **immediate foundational step.** Subsequently, this guide explains how to leverage that index effectively.

Adhering to this comprehensive process ensures that you leverage the full and evolving suite of AI Guides, providing accurate and contextually appropriate assistance.

## Building Your AI Guide Index

The primary goal of this section is to ensure you, the AI assistant, can reliably discover all available AI Guides within the project and understand their intended `usage`. This knowledge is foundational for providing relevant assistance.

### Why This Approach for Indexing?

Standard file listing tools or environment information available to AI assistants (e.g., `list_files`, or details in `environment_details`) may not always consistently reveal files within Git submodules (often located in directories like `vendor/`). (The specific limitations of such tools are further detailed in [../../../docs/reference/roo-code-capabilities.md](../../../docs/reference/roo-code-capabilities.md:0).) Shell commands, such as `find` (for Linux/macOS) or `Get-ChildItem` (for PowerShell on Windows), however, can reliably traverse these submodule directories from the project root.

By executing a specific shell command detailed below, you can obtain a comprehensive list of AI Guides and their `usage` strings. Once you understand this output, you effectively possess an **AI Guide Index**—an in-memory, recallable mapping from each guide's `relative_path` to its `usage_string`. This index is what equips you to effectively discover and use guides as described later in this document.

This section focuses on _how_ to obtain this vital information to form your AI Guide Index, emphasizing that the ability to recall and use this path-to-usage mapping is key, rather than adherence to a specific internal data structure.

### Step 1: Execute the Guide Indexing Command

**Upon first reading and understanding this guide, and when run from the project root directory,** execute the following shell command to build your initial AI Guide Index. This command will find all relevant `*-guide.md` files within any `ai-guides/` directory structure (excluding story artifacts and templates), sort them, and output their relative path and extracted `usage` string on a single line per guide. Executing this command from the project root ensures all relevant `*-guide.md` files are found, including those within submodules.

**For Linux/macOS (bash/zsh):**

```bash
find . -type d -path "*/stories/s[0-9][0-9][0-9]-*" -prune -o -type f -name "*-guide.md" -path "*/ai-guides/*" ! -name "*.template.md" -exec sh -c 'filepath="$1"; usage_value=$(grep -m 1 "^usage: " "$filepath" | sed -e '\''s/^usage:\s*//'\''); echo "$filepath:$usage_value"' _ {} \; | sort
```

**For Windows (PowerShell):**

```powershell
Get-ChildItem -Path . -Recurse -File -Filter "*-guide.md" |
Where-Object { $_.FullName -like "*/ai-guides/*" -and $_.FullName -notlike "*/stories/s[0-9][0-9][0-9]-*/*" -and $_.Name -notlike "*.template.md" } |
Sort-Object FullName |
ForEach-Object {
    $filepath = $_.FullName
    # Get relative path from the current location (project root)
    $relativepath = (Resolve-Path -Path $filepath -Relative).TrimStart(".\")

    # Try to get the first line matching "usage: "
    # Select-String returns a MatchInfo object, we want the Line property
    $usageLineObject = Get-Content -Path $filepath -TotalCount 20 | Select-String -Pattern "^usage: " -First 1

    $usage_value = ""
    if ($usageLineObject) {
        $usage_value = $usageLineObject.Line -replace "^usage:\s*" # Remove "usage: " prefix
    }

    Write-Output "$relativepath:$usage_value"
}
```

As an AI Assistant, you should determine the user's operating system and use the appropriate command.

### Step 2: Understanding and Utilizing the Command Output

Each line in this output directly provides you with the **`relative_path`** to an AI Guide and its **`usage_string`**.
The output from the command will be a sorted list of lines, where each line follows the format:
`[relative_path]:[usage_string]`

For example:
`./path/to/guide.md:"Usage string with original quotes"`
`./path/to/another-guide.md:Usage string without original quotes if not quoted in file`

This command output itself is the foundation of your AI Guide Index. By internalizing this information—that is, being able to recall the `relative_path` and corresponding `usage_string` for each guide listed—you "have an index." When a user initiates a task, you can then consult this index (your in-memory understanding of the guides) to identify potentially relevant guides by their `usage_string`s, as detailed in the next section.

## Process for Discovering and Using Relevant Guides (Leveraging Your Built AI Guide Index)

Once you have **initially built your AI Guide Index as instructed upon first reading this guide, and subsequently refreshed it as needed,** you **MUST** follow these steps each time you start a new user task/request, or when the evolving context suggests a new guide might be beneficial.

### Step 1: Understand User Intent and Task Context

- First, ensure you have a clear understanding of the user's current goal, task, or question.
- Determine if the user's request pertains to a broad category of work (e.g., story implementation, bug fixing, documentation writing, general assistance).

### Step 2: Consult Your AI Guide Index

- Based on the user's intent and the task category, **consult your AI Guide Index** (the in-memory understanding of guide paths and usage strings you built).
- Iterate through the guides in your index. For each guide, primarily use its `usage_string` to determine relevance to the current task.
- If multiple guides have potentially relevant `usage_string`s and further disambiguation is needed _before_ reading the full files, you may need to read the first few lines (i.e., the frontmatter) of these candidate guides (using their `relative_path` from your index) to inspect their `title` or `tags`.

### Step 3: Present Findings (If Necessary)

- If multiple guides seem potentially relevant (based on `usage_string` from your index and optionally a quick frontmatter check for titles/tags), or if you want to confirm your selection, present your findings to the user.
  > "Based on your request to [user's task], I found these AI Guides that might be helpful:
  >
  > - `[relative_path/to/guide1.md]`: [Usage of Guide 1]
  > - `[relative_path/to/guide2.md]`: [Usage of Guide 2]
  >   (If you've also read titles for clarity, you can add: e.g., "The first one is titled '[Title of Guide 1]'")
  >
  >   Which one would you like me to consult, or shall I proceed with the most relevant one?"
- If one guide is clearly the most relevant based on its `usage_string` (from your index):
  > "I'll consult the guide at `[relative_path/to/guide.md]`, as its usage description, '[Usage of Guide]', seems most relevant to [user's task]."

### Step 4: Consult Selected Guide(s) and Apply Precedence

- Using the `relative_path` from the selected guide's entry in your AI Guide Index, read the full content of the AI Guide file(s).
- **Apply Precedence if Multiple Relevant Guides Exist:**
  - **Identify Guide Origins:** When your AI Guide Index (built as described earlier in this guide) returns multiple relevant guides for a task, determine if they originate from the host project (e.g., `ai-guides/...`) or a submodule (e.g., `vendor/some-submodule/ai-guides/...`). The `relative_path` in your index will indicate this.
  - **Host Project Precedence:** If relevant guides are found in both the host project and a submodule (like `vendor/vibe-tasking/`), and there is a direct conflict in their instructions, the guidance from the **host project's guide takes precedence.**
  - **Intelligent Merging:** Even when one guide takes precedence, strive to intelligently merge non-conflicting information, advice, or context from all relevant guides. The goal is to provide the most comprehensive and accurate assistance.
  - **Single Source:** If only one relevant guide is found, or all relevant guides are from the same source (e.g., all from the submodule), follow that guidance directly.
- Follow the instructions, principles, and best practices detailed within the consulted guide(s), applying precedence rules as described above, to assist the user or complete the task.

## Conclusion

By consistently following this comprehensive approach—first building your AI Guide Index using the specified shell command, and then leveraging that index to discover and consult relevant guides—you will be able to effectively utilize the full suite of available guidance. This ensures your actions are informed by the latest project conventions and best practices, particularly when navigating projects with Git submodules where other discovery methods might be incomplete.
