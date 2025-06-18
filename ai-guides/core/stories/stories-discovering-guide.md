---
id: "stories-discovering-guide"
title: "Guide: Discovering Vibe Tasking Stories"
usage: "Use this guide to understand the standard methods and best practices for discovering, filtering, and presenting existing Vibe Tasking stories based on various criteria."
tags: "stories;discovery;filtering;querying;frontmatter;cli"
---

# Guide: Discovering Vibe Tasking Stories

**(Primary Audience: AI Assistant (to understand and execute standard methods for finding, filtering, and presenting Vibe Tasking stories).)**

## Introduction

This guide details the standard methods and best practices for AI assistants to discover, filter, and present existing Vibe Tasking stories. Adhering to these guidelines will enable you to efficiently locate relevant stories based on user queries and provide clear information about their status and content. This capability is crucial for tasks such as reporting on project progress, finding specific work items, or helping users manage their backlog.

## Understanding Story Location and Structure

Before attempting to discover stories, ensure you are familiar with their standard location and structure:

- **Location:** All Vibe Tasking stories reside within individual subdirectories under the main `stories/` directory in the project root.
- **Directory Naming:** Each story directory follows the `sXXX-descriptive-slug` convention (e.g., `s001-initial-project-setup`).
- **Core File:** The primary definition of a story is contained within a `story.md` file inside its respective directory.

For comprehensive details on story structure, naming conventions, and `story.md` content (including YAML frontmatter), you **MUST** refer to the **[Guide: Structuring Vibe Tasking Stories](stories-structuring-guide.md)**.

## Methods for Story Discovery

### 1. Listing Story Directories

The first step in discovering stories is typically to list the contents of the `stories/` directory. This will give you a list of all story slugs.

- You can achieve this programmatically using file system listing capabilities appropriate to your environment.

### 2. Accessing `story.md` Files

Once you have a list of story directories (slugs), you can access the `story.md` file within each relevant directory. **However, for filtering or initial assessment, avoid reading the entire file content.** Instead, prioritize methods that extract only the necessary information, such as the YAML frontmatter, using targeted command-line tools (see below). Reading full files should typically only occur after a story has been identified as highly relevant.

- Path to a story file: `stories/[story-slug]/story.md`

### 3. Parsing YAML Frontmatter

The YAML frontmatter at the beginning of each `story.md` file contains crucial metadata for filtering and understanding the story. You **MUST** parse this frontmatter to extract relevant fields. Key fields include:

- `id`: Unique identifier (e.g., `"s001-initial-project-setup"`)
- `title`: Human-readable title (e.g., `"Initial Project Setup"`)
- `status`: Current workflow status (e.g., `"To Do"`, `"In Progress"`, `"Done"`)
- `priority`: Story priority (e.g., `"High"`, `"Medium"`, `"Low"`)
- `tags`: Semicolon-separated list of keywords (e.g., `"design;feature;ui"`)
- `resolution`: Outcome for terminal states (e.g., `"Implemented"`, `"Obsolete"`)

## Filtering and Querying Stories

Based on user requests, you will often need to filter stories.

### 1. Filtering by Frontmatter Fields

The most common method is to filter based on the values extracted from the YAML frontmatter.

- **Example User Request:** "Find all stories that are 'In Progress'."
- **Action:** List story directories, read each `story.md`, parse frontmatter, and identify stories where the `status` field is `"In Progress"`.

### 2. Using Command-Line Tools (If Available and Permitted)

If you have the capability to execute shell commands and it is appropriate for the task, tools like `grep` or `rg` (ripgrep) are **highly recommended and preferred** for efficiently querying frontmatter across multiple files, rather than reading each file individually.

#### Example Queries (\*nix - macOS/Linux)

These examples assume stories are located in `stories/sXXX-slug/story.md`.

**Find stories with status "In Progress":**

```bash
grep -l -E '^status: "In Progress"' stories/s*/story.md | sed -E 's|stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

**Fetch frontmatter of stories with status "To Do" (extracting content between `---` delimiters and adding a `---` separator after each):**

```bash
grep -l -E '^status: "To Do"' stories/s*/story.md | xargs -I {} sh -c "awk '/^---$/{if(flag==1){flag=0}else{flag=1}; next} flag==1' '{}' && echo '---'"
```

**Note:** This command first uses `grep -l` to find files containing `status: "To Do"`. Then, for each found file, `xargs` executes a shell command (`sh -c "..."`). This shell command uses `awk` to print lines that are strictly _between_ the `---` frontmatter delimiters (i.e., the frontmatter content itself, excluding the `---` lines). After the `awk` command processes a file, `&& echo '---'` appends a `---` line, serving as a visual separator between the frontmatter outputs of different files. This method precisely extracts the frontmatter content.

**Find stories tagged with "design":**
(This regex ensures "design" is matched as a whole tag within the semicolon-delimited list.)

```bash
grep -l -E '^tags: "([^"]*;)*design([^"]*;|")[^"]*"' stories/s*/story.md | sed -E 's|stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

#### Example Queries (Windows - PowerShell)

**Find stories with status "In Progress":**

```powershell
Get-ChildItem -Path "stories\s*\story.md" -Recurse | Select-String -Pattern '^status: "In Progress"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

**Find stories tagged with "design":**
(This regex ensures "design" is matched as a whole tag within the semicolon-delimited list.)

```powershell
Get-ChildItem -Path "stories\s*\story.md" -Recurse | Select-String -Pattern '^tags: "([^"]*;)*design([^"]*;|")[^"]*"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

Refer to the `s001-initial-project-setup/`, `s002-design-enhanced-story-structure/`, and `s003-implement-enhanced-story-structure/` directories in `stories/` for concrete examples of story structure.

**Important:** When using command-line tools:

- Ensure your commands are targeted and efficient.
- Clearly explain to the user what command you intend to run and why.
- Process the output of the command to extract the necessary information before presenting it.

### 3. Searching Within Story Content (Advanced)

For more complex queries, users might ask to find stories containing specific keywords within their title, description, or acceptance criteria.

- This typically involves reading the full content of `story.md` files (after any initial frontmatter filtering) and performing text searches.
- Command-line tools can also be used for this (e.g., `rg "keyword" stories/`).

## Presenting Discovered Stories

When presenting discovered stories to the user:

- **Be Clear and Concise:** Provide enough information for the user to identify the relevant stories.
- **Common Formats:**
  - A list of story titles with their status and priority.
  - Include the story ID/slug for easy reference.
  - Provide direct links to the `story.md` files if appropriate (e.g., `[s001-initial-project-setup](stories/s001-initial-project-setup/story.md)`).
- **Handle Large Result Sets:** If many stories match a query, consider:
  - Summarizing the count.
  - Asking the user if they want to see all results or apply further filters.
  - Presenting a subset (e.g., the first 5-10) and offering to show more.

## Best Practices

- **Confirm User Intent:** Before performing broad or complex searches, clarify the user's criteria to ensure you're looking for the right information.
- **Prioritize Efficient Frontmatter Extraction:** For structured data like status or priority, always prefer filtering by extracting YAML frontmatter using command-line tools (as shown in examples) rather than reading full `story.md` files. This significantly improves efficiency and reduces unnecessary data processing.
- **Inform User of Method:** Briefly let the user know how you are attempting to find the stories (e.g., "I will search the frontmatter of all stories for status 'To Do'.").

## Conclusion

By understanding story structure, leveraging frontmatter metadata, and applying appropriate filtering techniques (including command-line tools where applicable), you can effectively discover and present Vibe Tasking stories. This skill is essential for assisting users with project management, task tracking, and maintaining an overview of development work.
