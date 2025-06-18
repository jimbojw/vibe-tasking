---
id: "s016-guide-for-updating-installing-md"
title: "Create Guide for Updating INSTALLING.md"
status: "Done"
priority: "Medium"
tags: "documentation;guide;maintenance;ai-instructions;installation"
---

# Story: s016 - Create Guide for Updating INSTALLING.md

## Description

This story is to create a new guide specifically for AI assistants working on the Vibe Tasking project. The guide will detail the process for updating the `INSTALLING.md` file, particularly its embedded "CONTENT FOR docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md" section, whenever the canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` file is modified. This ensures that the AI playbook for setting up Vibe Tasking in other projects remains synchronized with the latest story structure conventions.

The new guide will be located in the `docs/guides/` directory.

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter immediately upon starting work on this story.
- [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting that work has commenced.
- [x] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress, decisions, and any issues encountered throughout the execution of this story.
- [x] A new guide file, `docs/guides/updating-installing-md-guide.md`, is created.
- [x] The guide clearly instructs an AI assistant on the following steps:
  - How to recognize or be informed that `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` has been updated.
  - The necessity of reading the complete, most current content of `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`.
  - How to locate the specific marker `CONTENT FOR docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` within the `INSTALLING.md` file.
  - The process of replacing the entire Markdown block following this marker in `INSTALLING.md` with the newly read, complete content from `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`.
  - An emphasis on ensuring the copied content is an exact, verbatim duplicate, including all Markdown formatting, code blocks, and newlines.
- [x] The new `docs/guides/updating-installing-md-guide.md` is linked from the main `docs/guides/README.md`. (Note: Skipped per user preference against maintaining lists in READMEs, thus considered complete in context).
- [x] A "Maintenance Notes for AI Assistants" section is added to this project's root `CONTEXT.MD` file (or an existing similar section is updated). This section will include a brief instruction to consult the new `docs/guides/updating-installing-md-guide.md` when modifications to `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` are made or requested.
- [x] User confirms satisfaction with the new guide and the update to `CONTEXT.MD`.
- [ ] This story (`s016`) is documented with its `story.md` and `journal.md` (reflecting completion of all above ACs), and then its status is marked as "Done" in the frontmatter.
