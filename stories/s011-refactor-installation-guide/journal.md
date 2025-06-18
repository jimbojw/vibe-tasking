# Journal: s011 - Refactor Installation Guide, Update Context, and Enhance Journaling Guidance

## 2025-05-16T21:42:39-0400

- Story `s011` created to address documentation clarity, synchronization, and long-term maintenance, plus enhancing guidance on initial journal entries.
- **Issues Identified:**
  1.  The guide `docs/guides/how-to-use-vibe-tasking.md` is more accurately an "installation guide."
  2.  The content of `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` embedded within `how-to-use-vibe-tasking.md` became outdated after `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` was updated in story `s010`.
  3.  A mechanism is needed to remind AI assistants working on this Vibe Tasking project to maintain synchronization between these files.
  4.  Guidance should be added to `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` about using the initial journal entry to capture context from the story drafting phase.
- **Planned Actions (for future execution of this story):**
  1.  Rename `docs/guides/how-to-use-vibe-tasking.md` to `docs/guides/installation-guide.md`.
  2.  Update internal links (e.g., in `docs/guides/README.md`).
  3.  Update `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` to include the "Tip for Initial Journal Entry."
  4.  Synchronize the embedded `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` content within the (renamed) installation guide to include all recent updates (from `s010` and from step 3 of this story).
  5.  Update this project's root `CONTEXT.md` with a special instruction for AI assistants regarding this synchronization.
- This story file (`story.md`) and this initial journal entry created. The actual implementation of the changes described above will occur when this story (`s011`) is prioritized and executed.

## 2025-05-18T11:59:00-0400 (Approximate time of discussion)

- Discussion with user to refine the scope and direction of story `s011`.
- **Key Changes to Plan:**
  - A new file, `INSTALLING.md`, will be created at the project root. This file will contain the AI assistant playbook for setting up Vibe Tasking in _other_ projects (content to be sourced from the AI instructions in the old `docs/guides/how-to-use-vibe-tasking.md`).
  - The existing `docs/guides/how-to-use-vibe-tasking.md` file will be deleted entirely.
  - The `docs/guides/beginners-guide.md` will be updated to link to the new `INSTALLING.md` file. This guide is primarily for external users adopting Vibe Tasking.
  - The canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` will still be updated with the "Tip for Initial Journal Entry" as originally planned.
  - **Correction:** The project's root `CONTEXT.MD` will _not_ be modified as part of this story. Its current instruction to read `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` is correct for AI assistants working _within this project_. `INSTALLING.md` is for external adoption.
- The `story.md` for `s011` will be updated to reflect these revised objectives and acceptance criteria.

## 2025-05-19T03:24:00-0400 (Approximate time of execution)

- **Execution of s011:**
  - Updated `docs/stories/s011-refactor-installation-guide/story.md` to reflect the revised plan and set status to "In Progress".
  - Added "Tip for Initial Journal Entry" to the canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`.
  - Created `INSTALLING.md` at the project root, populating it with the AI playbook from the old `docs/guides/how-to-use-vibe-tasking.md` and ensuring its embedded `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` content was synchronized with the canonical version (including the new journal tip).
  - Deleted `docs/guides/how-to-use-vibe-tasking.md`.
  - Updated `docs/guides/beginners-guide.md` to link to the new `INSTALLING.md`.
  - Updated `docs/guides/README.md` to remove the link to the deleted `how-to-use-vibe-tasking.md`.
  - Updated `docs/stories/s009-how-to-use-vibe-tasking-guide/journal.md` and `docs/stories/s009-how-to-use-vibe-tasking-guide/story.md` to reflect that `how-to-use-vibe-tasking.md` was superseded by `INSTALLING.md`.
  - Addressed user feedback: Removed an obsolete note about `## Status` from `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and re-synchronized this change into `INSTALLING.md`.
- All planned changes for story `s011` are now complete. Awaiting final user confirmation before marking as "Done".
