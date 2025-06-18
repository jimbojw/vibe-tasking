# Journal: s019 - Revamp INSTALLING.md with Prerequisites Check and Upgrade Path

## 2025-05-19T05:03:00-0400

- Story `s019` created.
- **Purpose:** To significantly enhance the `INSTALLING.md` AI playbook.
- **Key Enhancements:**
  1.  Restructure `INSTALLING.md` into three main sections: "Prerequisites Check", "Installation / Upgrade Instructions", and "Default File Content Reference".
  2.  **Prerequisites Check:** Instruct the AI assistant to self-assess its capabilities (file reading, command execution), report to the user, and ask for confirmation to proceed.
  3.  **Installation / Upgrade Instructions:**
      - Maintain the current "New Installation" path.
      - Add an "Upgrade Path" for AIs with file-reading: This involves reading existing user files (`docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, `CONTEXT.MD`), comparing them to new defaults, identifying user customizations, and interactively guiding the user through overwrite/merge decisions.
  4.  **Default File Content Reference:** Ensure this section contains accurate, up-to-date verbatim content for default files.
- The goal is to make Vibe Tasking adoption more robust, user-friendly, and adaptable.

## 2025-05-19T05:04:00-0400

- Work commenced on story `s019`.
- Status updated to "In Progress" in `story.md` and first AC marked.
- This journal entry created to log the start of work and satisfy the second AC.
- Next step: Read the current `INSTALLING.md` to prepare for restructuring and content additions.

## 2025-05-19T05:13:00-0400

- Read the existing `INSTALLING.md`.
- Completely rewrote `INSTALLING.md` to implement the new three-section structure:
  1.  **Prerequisites Check:** Added instructions for AI self-assessment of capabilities (file reading, command execution), reporting to the user, and asking for confirmation to proceed.
  2.  **Installation / Upgrade Instructions:**
      - Delineated "New Installation" and "Upgrade Existing Installation" paths.
      - The "New Installation" path retains the original steps for directory and default file creation.
      - The "Upgrade Path" (marked as requiring file-reading) now includes steps for reading existing user files (`docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, `CONTEXT.MD`), comparing them to new defaults, identifying potential user customizations (with heuristics), and interactively guiding the user through overwrite/merge decisions.
  3.  **Default File Content Reference:** This section now explicitly holds the verbatim content for `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and a new project `CONTEXT.MD`, sourced from the current Vibe Tasking project.
- Ensured the language and detail are appropriate for an AI assistant playbook.
- Corrected casing for `CONTEXT.md` references within `INSTALLING.md` based on user feedback.
- Refined wording in `INSTALLING.md` (Path 2, for AI lacking file-read capability) to avoid telling the human user to refer to "Section 3", instead instructing the AI to provide defaults "from my current instructions".
- Further refined the "Upgrade `CONTEXT.md`" subsection in `INSTALLING.md` based on user feedback:
  - Emphasized that `CONTEXT.md` is highly likely to be customized.
  - Changed the primary goal of the upgrade for `CONTEXT.md` to ensuring the essential Vibe Tasking instruction (to read `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`) is present and correct.
  - Made the default action for a customized `CONTEXT.md` (that already contains a similar Vibe Tasking instruction) to _not_ make changes, preserving user customizations, rather than defaulting to overwrite. The AI should still offer to show the default if the user is interested.
- The `INSTALLING.md` now reflects the comprehensive plan discussed and all feedback incorporated.

## 2025-05-19T05:29:00-0400

- Based on user query, reviewed `docs/guides/updating-installing-md-guide.md`.
- Updated this guide to include instructions for synchronizing both embedded `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and the new project `CONTEXT.md` content within `INSTALLING.md`, aligning it with the new structure of `INSTALLING.md`.
- Further clarified in `docs/guides/updating-installing-md-guide.md` that the "CONTENT FOR new project CONTEXT.md" in `INSTALLING.md` is a _generic template_ and not a direct mirror of this project's specific `CONTEXT.MD`.
- Corrected `docs/guides/updating-installing-md-guide.md` by removing the now-redundant Section B ("Synchronizing New Project `CONTEXT.md` Content"), as the `CONTEXT.md` template within `INSTALLING.md` does not have an external canonical source in this project for direct synchronization. Changes to that template would be direct edits to `INSTALLING.md` itself.
