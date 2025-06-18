---
id: "s029-refactor-onboarding-documentation"
title: "Refactor Onboarding Documentation into an Onboarding Subdirectory"
status: "Done"
priority: "Medium"
tags: "documentation;refactor;user-guide;onboarding"
resolution: "Implemented"
---

# Story: s029 - Refactor Onboarding Documentation into an Onboarding Subdirectory

## Description

As a Vibe Tasking user, I want the initial onboarding and usage documentation to be structured into a clear, sequential guide within a dedicated `docs/onboarding/` subdirectory, with focused topics, so that I can more easily learn how to use Vibe Tasking and find specific information.

This story involves refactoring the content currently in `docs/guides/beginners-guide.md` into a new set of guides within the `docs/onboarding/` directory.

**Proposed New Structure within `docs/onboarding/`:**

1.  `README.md`: Overview of the onboarding guide sections and their recommended reading order.
2.  `01-introduction.md`: Covers core Vibe Tasking concepts, benefits, and the typical project directory structure.
3.  `02-installation.md`: A user-facing guide on installing Vibe Tasking, explaining how to use the `INSTALLING.md` AI playbook.
4.  `03-planning-stories.md`: A focused guide on the collaborative story planning process with an AI assistant.
5.  `04-working-with-stories.md`: A guide on how to explore/query existing stories and how to initiate work on a story with an AI assistant.

_(The exact filenames, numbering, and content breakdown can be finalized during the implementation of this story.)_

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
- [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
- [x] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.
- [x] The new subdirectory `docs/onboarding/` is created.
- [x] A `README.md` file is created within the `docs/onboarding/` subdirectory, introducing the guide and its sections.
- [x] Content from the existing `docs/guides/beginners-guide.md` is refactored and migrated into the new, focused guide files within `docs/onboarding/` (e.g., `01-introduction.md`, `02-installation.md`, etc.).
  - [x] Content for `01-introduction.md` created/migrated.
  - [x] Content for `02-installation.md` created/migrated.
  - [x] Content for `03-planning-stories.md` created/migrated.
  - [x] Content for `04-working-with-stories.md` created/migrated.
- [x] The original `docs/guides/beginners-guide.md` file is deleted.
- [x] All internal links within the Vibe Tasking project that previously pointed to `docs/guides/beginners-guide.md` are identified and updated to point to the relevant new guide(s) or the `docs/onboarding/README.md`. This includes (but may not be limited to):
  - Project root `README.md`.
  - `INSTALLING.md` (if it references `beginners-guide.md`).
  - `CONTEXT.md` (if it references `beginners-guide.md`).
  - Other files in `docs/guides/` or `docs/stories/` if they currently link to `beginners-guide.md`.
- [x] The main `docs/README.md` is updated to list and describe the new `docs/onboarding/` subdirectory and its purpose.
- [x] The `docs/guides/README.md` is reviewed and updated if necessary to reflect any changes in its scope (e.g., to clarify its focus now that `onboarding/` handles beginner topics).
- [x] User confirms the new documentation structure, content, and link updates are satisfactory.
- [x] **Process:** User confirms the new story structure (directory, `story.md`, `journal.md`) for _this_ story (`s029`) and its initial content accurately reflect the planned work and adhere to the Story Documentation Guide.
