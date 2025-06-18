---
id: "s011-refactor-installation-guide"
title: "Create INSTALLING.md, Update Story Template, and Refine Related Guides"
status: "Done"
priority: "High"
tags: "documentation;refactor;maintenance;journaling;best-practice;installation"
---

# Story: s011 - Create INSTALLING.md, Update Story Template, and Refine Related Guides

## Description

This story refines the Vibe Tasking documentation to improve clarity for users wishing to adopt the Vibe Tasking methodology in their own projects, and enhances internal best practices for story creation.

Key changes include:

1.  **Create `INSTALLING.md`:** A new file named `INSTALLING.md` will be created at the project root. This file will serve as an AI assistant playbook, containing detailed instructions for setting up the Vibe Tasking framework in a new or existing project. The content for this playbook will be sourced from the AI instruction section of the now-obsolete `docs/guides/how-to-use-vibe-tasking.md`.
2.  **Update `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (Canonical Story Template):** The canonical story template will be enhanced by adding a "Tip for Initial Journal Entry." This tip will recommend using the first journal entry of a new story to capture important context, discussions, or decisions made during the story drafting phase, ensuring this valuable information is preserved.
3.  **Update `docs/guides/beginners-guide.md`:** This guide, which is primarily for users external to this specific Vibe Tasking project who wish to adopt the methodology, will be updated. The existing link that (incorrectly) points to a non-existent installation guide will be changed to point to the new `INSTALLING.md` at the project root.
4.  **Delete Obsolete Guide:** The file `docs/guides/how-to-use-vibe-tasking.md` will be deleted as its AI playbook content is moved to `INSTALLING.md` and its user-facing introductory content is sufficiently covered by `docs/guides/beginners-guide.md`.
5.  **Ensure Content Synchronization:** The embedded "CONTENT FOR docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md" section within the new `INSTALLING.md` must be an exact, up-to-date copy of the canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (including the new "Tip for Initial Journal Entry").

This story does _not_ involve changes to the root `CONTEXT.MD` file, as its current guidance for AI assistants working _within this project_ (pointing them to `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`) remains correct.

## Acceptance Criteria

- [ ] A new file `INSTALLING.md` is created at the project root, containing the AI assistant installation playbook (sourced from the old `docs/guides/how-to-use-vibe-tasking.md`).
- [ ] The embedded "CONTENT FOR docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md" section within the new `INSTALLING.md` is verified and updated to exactly match the current, enhanced content of the canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (including the new "Tip for Initial Journal Entry").
- [ ] The file `docs/guides/how-to-use-vibe-tasking.md` is deleted.
- [ ] The link in `docs/guides/beginners-guide.md` that previously pointed to a non-existent installation guide is updated to point to the new `INSTALLING.md` at the project root.
- [ ] The canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` is updated to include a "Tip for Initial Journal Entry" under its `journal.md` description, advising the use of the first journal entry for capturing story drafting context.
- [ ] Any other internal links within the project that previously pointed to `docs/guides/how-to-use-vibe-tasking.md` (e.g., in `docs/guides/README.md`) are updated appropriately (e.g., removed or retargeted if a general installation concept is still relevant elsewhere).
- [ ] User confirms satisfaction with all changes made in this story.
- [ ] This story (`s011`) is documented with its `story.md` and `journal.md` (reflecting these changes and their execution), and then marked as "Done".
