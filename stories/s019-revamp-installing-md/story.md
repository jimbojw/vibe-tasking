---
id: "s019-revamp-installing-md"
title: "Revamp INSTALLING.md with Prerequisites Check and Upgrade Path"
status: "Done"
priority: "High"
tags: "documentation;installation;playbook;ai-instructions;upgrade;prerequisites"
---

# Story: s019 - Revamp INSTALLING.md with Prerequisites Check and Upgrade Path

## Description

This story is to significantly enhance the `INSTALLING.md` AI playbook. The goal is to make the Vibe Tasking adoption process more robust, user-friendly, and adaptable to different AI assistant capabilities and existing project states.

The `INSTALLING.md` file will be restructured into three main sections:

1.  **Prerequisites Check:**

    - The AI assistant executing the playbook will be instructed to perform a self-assessment of its capabilities, specifically:
      - Ability to read arbitrary named files (e.g., Cline's `read_file`).
      - Ability to execute terminal commands (e.g., Cline's `execute_command`).
    - The AI will report these capabilities (and their implications for the Vibe Tasking experience) to the user.
    - The AI will then ask the user to confirm if they wish to proceed with the installation/upgrade.

2.  **Installation / Upgrade Instructions:**

    - **New Installation:** For projects without an existing Vibe Tasking setup, this path involves creating the standard directory structure (`docs/stories/`, `docs/guides/`, `docs/reference/`) and populating essential files (`docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, project root `CONTEXT.MD`) using the default content provided in Section 3 of `INSTALLING.md`.
    - **Upgrade Path (for AIs with file-reading capabilities):** For projects with an existing Vibe Tasking setup, this path involves:
      - Reading the user's current `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and `CONTEXT.MD`.
      - Comparing them against the new default versions provided in Section 3 of `INSTALLING.md`.
      - Identifying significant user customizations (e.g., additional YAML fields in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, substantially different `CONTEXT.MD` instructions) that might be overwritten.
      - Presenting these potential conflicts/overwrites to the user and asking for guidance (e.g., overwrite with new default, keep existing file, attempt to merge). The default behavior, if no significant customizations are detected or if the user agrees, should be to overwrite with the new defaults.
      - Providing heuristics to the AI on what might constitute an "important detail" to preserve.

3.  **Default File Content Reference:**
    - This section will contain the complete, up-to-date, verbatim content for default files like `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and a new project `CONTEXT.MD`. This content must be meticulously maintained and synchronized with the canonical versions in this (Vibe Tasking) repository.

The overall clarity and step-by-step nature of the instructions in `INSTALLING.md` must be suitable for an AI assistant to follow reliably.

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter immediately upon starting work on this story.
- [x] **Process:** An initial journal entry is added to journal.md for this story, noting that work has commenced.
- [x] **Process:** The journal.md for this story is kept up-to-date with entries detailing progress, decisions, and any issues encountered throughout the execution of this story.
- [x] The `INSTALLING.md` file is restructured into three distinct, clearly titled sections: "1. Prerequisites Check", "2. Installation / Upgrade Instructions", and "3. Default File Content Reference".
- [x] **Section 1 (Prerequisites Check) in `INSTALLING.md`:**
  - [x] Contains clear instructions for the AI assistant to self-assess its capabilities for arbitrary file reading and command execution.
  - [x] Instructs the AI to inform the user about its capabilities and their impact on the Vibe Tasking experience.
  - [x] Instructs the AI to ask the user for confirmation to proceed before starting installation/upgrade.
- [x] **Section 2 (Installation / Upgrade Instructions) in `INSTALLING.md`:**
  - [x] Clearly distinguishes between "New Installation" and "Upgrade" paths.
  - [x] "New Installation" path accurately details directory creation and copying of default file content from Section 3.
  - [x] "Upgrade" path is explicitly marked as requiring file-reading capabilities.
  - [x] "Upgrade" path includes instructions for the AI to:
    - Read existing `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and `CONTEXT.MD` in the user's project.
    - Compare these with the defaults in Section 3 of `INSTALLING.md`.
    - Identify potential user customizations or significant data loss if overwritten.
    - Provide heuristics/examples of what to look for (e.g., extra YAML fields, substantially different `CONTEXT.MD`).
    - Clearly present findings to the user and ask for guidance on how to proceed (overwrite, keep, attempt merge), with a sensible default (e.g., overwrite if no major customizations detected).
- [x] **Section 3 (Default File Content Reference) in `INSTALLING.md`:**
  - [x] Contains the complete, accurate, and up-to-date verbatim content for the canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (from this Vibe Tasking project).
  - [x] Contains the complete, accurate, and up-to-date verbatim content for a new project's `CONTEXT.MD` (from this Vibe Tasking project).
- [x] The overall language, structure, and detail level of `INSTALLING.md` are suitable for an AI assistant to reliably execute the playbook.
- [x] User confirms satisfaction with the revamped `INSTALLING.md`.
- [x] This story (s019) is documented with its story.md and journal.md (reflecting completion of all above ACs), and then its status is marked as "Done" in the frontmatter.
