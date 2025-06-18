# Proposed Inbox Mechanism for Vibe Tasking

This document outlines the proposed mechanism for capturing emergent thoughts, ideas, or ancillary tasks within the Vibe Tasking project, inspired by GTD principles.

## 1. Inbox Location

- A new top-level directory named `inbox/` will be created at the root of the Vibe Tasking project.
  - A `README.md` file will be placed within `inbox/`. Its purpose is to:
    - Ensure the directory is preserved by Git even when empty.
    - Briefly describe the purpose of the `inbox/` directory (for capturing emergent thoughts).
    - Optionally, link to relevant AI Guides (e.g., `inbox-capturing-guide.md`, `inbox-processing-guide.md`).
    - Crucially, this `README.md` **MUST NOT** contain an index or list of the inbox items themselves, as such lists are prone to becoming outdated.
- **Rationale:** This provides a clear, dedicated, and easily discoverable location for all captured items, separate from active stories or core documentation. The `README.md` offers guidance and preserves the directory.

## 2. Capture Method

- Each distinct thought, idea, or task captured will be stored as an individual Markdown (`.md`) file within the `inbox/` directory.
- **Rationale:**
  - Ensures each item can be processed, archived, or deleted independently.
  - Aligns with Vibe Tasking's file-centric approach to managing information.
  - Avoids potential complexities or merge conflicts associated with appending to a single shared file, especially when an AI assistant is performing the capture.
  - Simplifies listing, counting, and managing individual inbox items.

## 3. File Naming Convention

Captured items will use the following filename convention:

`YYYY-MM-DD-descriptive-slug.md`

- **`YYYY-MM-DD`**: The UTC date when the item was captured (e.g., `2025-06-08`).
  - This provides a default chronological sorting order by day.
  - AI assistants may need to execute a system command (e.g., `date -u +%Y-%m-%d` on Linux/macOS or its equivalent on Windows) to obtain this date.
- **`descriptive-slug`**: A descriptive, kebab-case slug derived from the content of the thought or provided by the user/AI (e.g., `improve-readme-linking-for-clarity`, `research-alternative-library-for-feature-x`, `create-adr-for-ai-guide-discovery-mechanism`).
  - This provides a quick human-readable hint about the item's content. Uniqueness for a given day will rely on the descriptiveness of this slug.
- **`.md`**: Standard Markdown file extension.

- **Example Filename:** `2025-06-08-create-adr-for-guide-discovery.md`

## 4. Content of Inbox Items

The content of each inbox `.md` file is simply the raw captured thought, idea, or task description. No specific internal structure (like YAML frontmatter or prescribed sections) is mandated for the content of these files.

- **Rationale:**
  - Maximizes low-friction capture. The primary goal is to get the thought recorded quickly without concern for formatting.
  - The date-stamped and descriptive filename provides the primary metadata for later review and processing.
  - If additional context (like the story active during capture) is crucial, it can be included naturally within the raw text of the captured thought.
  - Future needs for more structured inbox items can be addressed as a separate enhancement if proven necessary.

## Summary of Design Goals

This proposed mechanism aims to be:

- **Low-Friction:** Easy and quick for both users and AI assistants to use.
- **Reliable:** Ensures thoughts are captured in a persistent, reviewable format.
- **Organized:** Keeps inbox items separate and individually manageable.
- **Vibe Tasking Aligned:** Leverages Markdown files and a simple directory structure.
- **Processable:** Structured in a way that facilitates a future "inbox processing" workflow (as anticipated by story `s069`).
