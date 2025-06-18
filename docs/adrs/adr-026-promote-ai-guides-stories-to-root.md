---
id: "adr-026"
title: "Promote ai-guides and stories Directories to Project Root"
status: "Accepted"
date: "2025-05-30"
tags: "directory-structure;refactor;ai-guides;stories;organization"
---

# ADR-026: Promote ai-guides and stories Directories to Project Root

## Context

The Vibe Tasking project currently houses key documentation directories, `ai-guides` and `stories`, within the `docs/` subdirectory (i.e., `docs/ai-guides/` and `docs/stories/`). While `docs/` serves as a general container for all documentation, the `ai-guides` and `stories` directories are fundamental to the Vibe Tasking framework's operation and daily use by both humans and AI assistants.

Their current nested location can:

- Slightly obscure their top-level importance within the project structure.
- Lead to longer relative paths when linking to/from them from other parts of the project, particularly from the root or other top-level directories.

This ADR proposes a structural change to elevate their visibility and simplify pathing.

## Alternatives Considered (Optional)

### Alternative 1: Keep Current Structure

- **Description:** Maintain `ai-guides` and `stories` within the `docs/` directory.
- **Pros:**
  - No changes required, no risk of breaking links or workflows.
  - All documentation remains consolidated under a single `docs/` top-level directory.
- **Cons:**
  - Does not address the desire to signal the higher importance of these specific directories.
  - Path lengths remain longer.

### Alternative 2: Create Symbolic Links at Root

- **Description:** Keep the directories physically within `docs/` but create symbolic links to them at the project root (e.g., `ai-guides -> docs/ai-guides`).
- **Pros:**
  - Provides shorter access paths from the root.
  - Physical location remains unchanged, potentially simpler for some existing tooling that expects them under `docs/`.
- **Cons:**
  - Introduces symbolic links, which can sometimes cause confusion or issues across different operating systems or with certain tools.
  - Does not fully address the "visibility/importance" aspect as clearly as a physical move.
  - Link updating within Markdown files would still be complex, as relative links from within the actual `docs/ai-guides` and `docs/stories` would still be based on their physical location.

## Decision

We will move the `docs/ai-guides` directory to the project root as `ai-guides/`.
We will move the `docs/stories` directory to the project root as `stories/`.

This decision aims to:

1.  **Elevate Visibility:** Clearly signal the first-class importance of these directories within the Vibe Tasking framework.
2.  **Simplify Paths:** Make it easier and more intuitive to reference content within these directories from across the project.
3.  **Improve Organization and Specificity:** Reflect their core role more directly in the project's top-level structure. This change also enhances purpose alignment:
    - `ai-guides/` at the root will specifically house guides intended primarily for AI assistants, increasing their isolation and specificity.
    - `stories/` at the root will house the structured story subdirectories, aligning better with their unique operational nature distinct from general documentation.
    - The remaining `docs/` directory will then more clearly serve general audience documentation (for users and/or AI assistants).

This change will necessitate updating all internal Markdown links throughout the repository that reference the old paths. A Python script will be developed and used to perform this update in a controlled manner (with a dry-run capability) to ensure accuracy and minimize disruption. This script will be similar in nature to the one used in story `s063-refactor-ai-guides-structure`.

## Consequences

### Positive

- Improved project clarity and organization, reflecting the central role of `ai-guides` and `stories`.
- Shorter and more intuitive paths for accessing and linking to content within these directories.
- Reinforces their status as core components of the Vibe Tasking framework.
- Enhanced purpose alignment for directories: `ai-guides/` for AI-specific guides, `stories/` for operational story units, and `docs/` for general audience documentation.

### Negative

- Requires a one-time effort to move directories and update all internal links.
- Potential for broken links if the update script is not comprehensive or if manual links are missed. This risk will be mitigated by careful script development, a dry-run, and spot-checking.
- Users and AI assistants will need to adapt to the new paths.
