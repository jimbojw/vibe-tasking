# Design: Enhanced Story Structure for Vibe Tasking

## 1. Introduction

This document outlines the design for an enhanced story structure for the Vibe Tasking framework. This design is an output of story `s002-design-enhanced-story-structure`.

The primary goals of this enhancement are to:

- Improve the machine-readability of story metadata for querying purposes.
- Enable simple and efficient querying of stories directly from the command line using common, cross-platform tools.
- Define a core set of useful metadata fields for tracking and managing stories.
- Maintain the framework's core principles of flexibility, broad compatibility, and minimal reliance on external tooling or complex setups.
- Ensure that metadata is self-contained within each story file, avoiding the need for separate index files and potential synchronization issues.

## 2. Metadata Storage: YAML Frontmatter

Each story's `story.md` file will begin with a YAML frontmatter block. This block will contain structured metadata for that specific story.

### 2.1. Core Metadata Fields

The following core metadata fields are defined:

- **`id`**: (String) A unique identifier for the story. This should ideally match the story's directory slug (e.g., `s001-initial-project-setup`).
- **`title`**: (String) The human-readable title of the story.
- **`status`**: (String) The current status of the story. Recommended values: `"To Do"`, `"In Progress"`, `"Done"`, `"Blocked"`.
- **`priority`**: (String) The priority of the story. Recommended values: `"High"`, `"Medium"`, `"Low"`.
- **`tags`**: (String) A semicolon-separated list of keywords or labels for categorization and filtering (e.g., `"design;feature;ui"`).

### 2.2. Formatting for Queryability

To ensure reliable querying using simple command-line tools like `grep`, the metadata fields intended for querying (`id`, `title`, `status`, `priority`, `tags`) **must** adhere to the following formatting guidelines within the YAML frontmatter:

- Each field and its value must be on a single line.
- String values should be enclosed in double quotes (e.g., `status: "In Progress"`).
- The `tags` field should be a single string with tags separated by semicolons.

**Example Frontmatter:**

```yaml
---
id: "s003-new-feature-x"
title: "Implement New Feature X"
status: "To Do"
priority: "Medium"
tags: "feature;backend;api"
---

# Story: s003 - Implement New Feature X
... (rest of story.md content) ...
```

### 2.3. Exclusion of Date Fields

`created_date` and `updated_date` fields are intentionally excluded from the frontmatter. Vibe Tasking assumes usage with a Version Control System (VCS) like Git. The VCS is the canonical source of truth for all change history and timestamps, making such fields in the frontmatter redundant and prone to discrepancies.

## 3. Command-Line Querying

Stories can be queried directly from the command line by searching the frontmatter of `story.md` files. The story ID is typically the name of the directory containing the `story.md` file.

### 3.1. Querying Mechanism

The primary mechanism involves:

1.  Using a line-based search tool (e.g., `grep` on \*nix, `Select-String` on PowerShell) to find `story.md` files whose frontmatter contains a specific metadata key-value pair.
2.  Extracting the story directory name (which serves as the story ID in this context) from the path of the matched file(s), often using a stream editor like `sed` or PowerShell path manipulation cmdlets.

### 3.2. Example Queries (\*nix - macOS/Linux)

These examples assume stories are located in `docs/stories/sXXX-slug/story.md`.

**Find stories with status "In Progress":**

```bash
grep -l -E '^status: "In Progress"' docs/stories/s*/story.md | sed -E 's|docs/stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

**Find stories with priority "High":**

```bash
grep -l -E '^priority: "High"' docs/stories/s*/story.md | sed -E 's|docs/stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

**Find stories tagged with "design":**
(Note: To match a specific tag like "design" accurately, ensuring it's a whole word within the semicolon-delimited list, a more precise regex is needed.)

```bash
grep -l -E '^tags: "([^"]*;)*design([^"]*;|")[^"]*"' docs/stories/s*/story.md | sed -E 's|docs/stories/(s[0-9]+-[^/]+)/story.md|\1|'
```

### 3.3. Example Queries (Windows - PowerShell)

**Find stories with status "In Progress":**

```powershell
Get-ChildItem -Path "docs\stories\s*\story.md" -Recurse | Select-String -Pattern '^status: "In Progress"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

**Find stories with priority "High":**

```powershell
Get-ChildItem -Path "docs\stories\s*\story.md" -Recurse | Select-String -Pattern '^priority: "High"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

**Find stories tagged with "design":**
(Note: Similar to the \*nix example, a more precise regex is needed for accurate whole-word tag matching in PowerShell's `Select-String`.)

```powershell
Get-ChildItem -Path "docs\stories\s*\story.md" -Recurse | Select-String -Pattern '^tags: "([^"]*;)*design([^"]*;|")[^"]*"' | ForEach-Object { ($_.Path | Split-Path | Split-Path -Leaf) }
```

## 4. Test Artifacts

For testing and exemplifying this querying mechanism, a test script and example story have been created:

- Example Story: `docs/stories/s002-design-enhanced-story-structure/artifacts/example-story-for-testing/story.md`
- Test Script: `docs/stories/s002-design-enhanced-story-structure/artifacts/run_query_tests.sh`

This script validates the `grep` and `sed` commands against the example story. The naming convention for such test artifacts within a story's `artifacts` directory (e.g., `example-story-for-testing`) is chosen to avoid conflicts with actual story ID autocompletion.

## 5. Future Considerations

While the current design focuses on a minimal, robust set of core fields and querying capabilities, future enhancements could include:

- Standardizing more optional metadata fields (e.g., `assignee`, `related_stories`).
- Developing more sophisticated (optional) tooling for advanced reporting or validation, if desired by users, while ensuring the core remains simple and tool-agnostic.
