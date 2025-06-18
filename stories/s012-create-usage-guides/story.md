---
id: "s012-create-usage-guides"
title: "Create Vibe Tasking Usage Guide(s)"
status: "Closed"
priority: "High"
tags: "documentation;guide;best-practice;ai-collaboration"
resolution: "Obsolete"
---

# Story: s012 - Create Vibe Tasking Usage Guide(s)

## Description

While the `installation-guide.md` covers setting up Vibe Tasking, users also need comprehensive guidance on _how to effectively use_ the framework for day-to-day development and AI collaboration. This story is to create one or more new usage guides to address this need.

The usage guide(s) should cover, but are not necessarily limited to:

**1. Tactical Usage:** - Best practices for initiating AI chat sessions using the project's `CONTEXT.md`. - Effective journaling in `journal.md`: what to include, level of detail, using timestamps. - Managing and linking artifacts in the `artifacts/` directory and `story.md`. - Crafting effective `story.md` content: clear descriptions, actionable acceptance criteria (referencing the note in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`), and well-defined user story formats. - Tips for iterative refinement of stories with AI.

**2. Strategic Usage:** - Structuring Vibe Tasking stories for different phases of work (e.g., research, design, implementation, testing) to align AI contributions and focus. - Leveraging Vibe Tasking for managing larger features or epics (e.g., by linking related stories). - Broader principles for effective AI collaboration within the Vibe Tasking framework (e.g., context management, iterative prompting, the "Curiosity, Empathy, Humility" model from the main `README.md`). - How Vibe Tasking aids in context recovery and maintaining momentum across multiple AI sessions.

The output of this story will be one or more new guide documents in the `docs/guides/` directory. The decision on whether to create a single comprehensive usage guide or separate tactical and strategic guides can be made during the implementation of this story.

## Acceptance Criteria

- [ ] At least one new usage guide document is created in the `docs/guides/` directory (e.g., `tactical-vibe-tasking-guide.md`, `strategic-vibe-tasking-guide.md`, or a combined `vibe-tasking-usage-guide.md`).
- [ ] The created guide(s) comprehensively cover key aspects of tactical Vibe Tasking usage as outlined in the description.
- [ ] The created guide(s) comprehensively cover key aspects of strategic Vibe Tasking usage as outlined in the description.
- [ ] The new guide(s) are clearly written, actionable, and provide valuable insights for users looking to maximize their effectiveness with Vibe Tasking.
- [ ] The new guide(s) are linked from the main `docs/guides/README.md`.
- [ ] User confirms satisfaction with the content, structure, and completeness of the new usage guide(s).
- [ ] This story (`s012`) is documented with its `story.md` and `journal.md`, and then marked as "Done".
