---
id: "adr-006"
title: "Story File and Directory Structure"
status: "Accepted"
date: "2025-05-19"
tags: "project-structure;stories;conventions;documentation-organization"
---

# ADR-006: Story File and Directory Structure

## Context

Vibe Tasking stories represent individual units of work. To keep information related to a single story organized, encapsulated, and easily accessible, a clear and consistent file and directory structure for each story is necessary. This structure should support the main story definition, its ongoing log of activities, and any associated files.

## Alternatives Considered

1.  **Single File per Story:** Store all information for a story (definition, journal, links to artifacts) within a single large Markdown file.

    - _Pros:_ Simplest in terms of file count.
    - _Cons:_ Can become very long and difficult to navigate. Hard to separate the core definition from the chronological journal. Managing embedded or linked binary artifacts becomes messy.

2.  **No Prescribed Structure within Story Directory:** Allow users to place any files they want within a story's directory without specific names like `story.md` or `journal.md`.

    - _Pros:_ Maximum flexibility.
    - _Cons:_ Lack of consistency makes it hard for users and AI assistants to reliably find the main story definition or its log. Difficult to automate processes or build tooling around.

3.  **Flat Structure for All Story Files:** Place all `story.md` files in one directory, all `journal.md` files in another, etc.
    - _Pros:_ Groups files by type.
    - _Cons:_ Disassociates a story's definition from its journal and artifacts, making it harder to see all context for a single story in one place. Navigation becomes more complex.

## Decision

Each Vibe Tasking story will reside in its own dedicated directory, named using the `sXXX-descriptive-slug` convention (e.g., `docs/stories/s001-initial-setup/`). Within this directory, the following standard file structure will be used:

- **`story.md` (Required):** The main Markdown file detailing the user story. It must begin with YAML frontmatter for metadata, followed by sections for Description, Artifacts (links), and Acceptance Criteria. This is the canonical definition of the task.
- **`journal.md` (Required):** A Markdown file containing a chronological log of progress, updates, decisions, discussions, and notes related to the story over time.
- **`artifacts/` (Optional Directory):** A subdirectory created only if the story has actual files (e.g., images, small data files, scripts, text snippets) associated with it. This provides a consistent location for story-specific assets.

## Consequences

### Positive

- **Encapsulation:** All information directly related to a single story is grouped together in one place.
- **Clear Separation of Concerns:**
  - `story.md` provides the "what and why" (definition and criteria).
  - `journal.md` provides the "how and when" (chronological progress).
  - `artifacts/` stores the "outputs or inputs" (associated files).
- **Navigability:** Easy for users and AI assistants to locate the specific components of any given story.
- **Consistency:** A standard structure across all stories simplifies understanding and tooling.
- **Scalability:** The `artifacts/` directory provides a clean way to manage multiple associated files without cluttering the main story directory.

### Negative

- **Directory Overhead:** Creates a directory for every story, which might seem like overhead for very small, trivial tasks (though such tasks might not always warrant a full Vibe Tasking story).
- **Prescriptive Naming:** Requires adherence to the `story.md` and `journal.md` naming convention.

This decision prioritizes clear organization, encapsulation of story-related information, and ease of navigation for both humans and AI assistants.
