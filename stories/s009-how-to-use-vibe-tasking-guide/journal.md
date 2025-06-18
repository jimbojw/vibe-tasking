# Journal: s009 - Create 'How to Use Vibe Tasking' Guide

## 2025-05-16T21:06:39-0400

- Story initiated. Discussed the core philosophy and approach for creating the "How to Use Vibe Tasking" guide.
- Key insights from project owner (user):
  - **Natural Language as Code:** In the Vibe Coding paradigm, Vibe Tasking's documentation (stories, guides) functions as a form of high-level source code. These natural language specifications are "compiled" or interpreted by LLMs into executable actions or traditional code. The programmer's role evolves to crafting these precise specifications and managing context.
  - **"How to Use" Guide as an AI Playbook:** The `how-to-use-vibe-tasking.md` guide should be structured as a direct set of instructions (a "playbook") that a user can provide to their AI assistant. The AI would then use this playbook to automate the setup of Vibe Tasking in a new project.
  - **Single-Document Structure for the Guide:** The guide will be a single document. It will contain an introductory section for the human user, followed by a clearly demarcated section with explicit, copy-pasteable instructions for the AI assistant. This is preferred over separate documents for user and AI.
  - **AI-Driven `CONTEXT.md` Creation:** The playbook will include instructions for the user's AI to create an initial `CONTEXT.md` file in the new project. This `CONTEXT.md` will guide future AI sessions to understand the Vibe Tasking structure (e.g., by pointing them to the newly created `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`).
  - **Envisioned Workflow:**
    1. User discovers Vibe Tasking and the "how-to" guide.
    2. User copies the AI instruction portion of the guide into their AI assistant's chat.
    3. The AI assistant processes the instructions and sets up the Vibe Tasking directory structure and essential files (e.g., `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, initial `CONTEXT.md`).
- Plan:
  1. Create this journal entry. (This step)
  2. AI (Cline) to re-read key project documents (`README.md`, `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, `CONTEXT.md`). (Completed prior to this journal entry during planning phase)
  3. AI (Cline) to draft `docs/guides/how-to-use-vibe-tasking.md` as a playbook.
  4. AI (Cline) to draft updates for `docs/guides/README.md`.
  5. User to review drafts. (Skipping detailed draft review in chat, will review actual file).
  6. Implement file creation/updates in ACT MODE.
  7. Update `s009/story.md` and this journal.

## 2025-05-16T21:10:56-0400

- Created `docs/guides/how-to-use-vibe-tasking.md` playbook.
- Updated `docs/guides/README.md` to link to the new guide.
- Updated `story.md` for this story (s009) to "Done", updated artifacts, and checked off acceptance criteria.
- Story s009 is now complete.

## 2025-05-19T03:21:00-0400 (Approximate time of s011 execution)

- **Note for Historical Context (re: Story s011):** The guide `docs/guides/how-to-use-vibe-tasking.md`, created as part of this story (s009), is being superseded.
- Its AI playbook content is being moved to a new root-level file `INSTALLING.md`.
- The user-facing introductory content of `docs/guides/how-to-use-vibe-tasking.md` is considered covered by `docs/guides/beginners-guide.md`.
- Consequently, `docs/guides/how-to-use-vibe-tasking.md` will be deleted as part of story `s011-refactor-installation-guide`.
- The `docs/guides/beginners-guide.md` and other relevant links will be updated to point to `INSTALLING.md`.
