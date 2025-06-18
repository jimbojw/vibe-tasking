---
id: "s028-add-resolution-field"
title: "Add Resolution Field to Story Frontmatter"
status: "Done"
priority: "High"
tags: "framework-enhancement;story-structure;documentation"
resolution: "Implemented"
---

# Story: s028 - Add Resolution Field to Story Frontmatter

## Description

As a Vibe Tasking user/maintainer, I want to add a `resolution` field to the standard story frontmatter so that the outcome or reason for a story's terminal state can be explicitly documented, aligning with industry best practices and improving clarity.

This enhancement aims to make story metadata more expressive and queryable.

**Key Design Decisions:**

1.  **Field Presence:** The `resolution` field will be added to the YAML frontmatter of `story.md` files and will always be present.
2.  **Default Value:** For active stories (e.g., status "To Do", "In Progress", "Blocked"), the `resolution` will be `"Unresolved"`.
3.  **Proposed `status` Values (to work with `resolution`):**
    - `"To Do"` (resolution: `"Unresolved"`)
    - `"In Progress"` (resolution: `"Unresolved"`)
    - `"Done"` (resolution: set to a success-oriented value like `"Implemented"`, `"Fixed"`, `"Completed"`)
    - `"Closed"` (new status for stories terminated without fulfilling original intent; resolution: set to a non-completion value like `"Obsolete"`, `"Won't Do"`, `"Duplicate"`)
    - `"Blocked"` (resolution: `"Unresolved"`)
4.  **Proposed `resolution` Values:**
    - `"Unresolved"` (Default for active stories)
    - **For `status: "Done"`:**
      - `"Implemented"`
      - `"Fixed"`
      - `"Completed"`
    - **For `status: "Closed"`:**
      - `"Obsolete"`
      - `"Won't Do"`
      - `"Duplicate"`
      - `"Cannot Reproduce"`
      - `"Invalid"`

## Artifacts

- This `story.md` file.
- (During implementation of this story) The updated `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`.
- (During implementation of this story) The updated `INSTALLING.md`.
- (During implementation of this story, if needed) The updated `docs/guides/planning-guide.md`.

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
- [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
- [x] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.
- [x] The proposed `status` and `resolution` values and their interaction are finalized and documented within this story.
- [x] The `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` file is updated to:
  - Define the new `resolution` frontmatter field (always present, string, double-quoted, default `"Unresolved"`).
  - List the recommended `resolution` values.
  - Update the recommended `status` values to include `"Closed"` and clarify interaction with `resolution`.
  - Ensure YAML frontmatter examples in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` reflect the new `resolution` field.
- [x] The `INSTALLING.md` file is updated to synchronize its embedded `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` content with the canonical version, following `docs/guides/updating-installing-md-guide.md`.
- [x] (If deemed necessary during implementation) `docs/guides/planning-guide.md` is updated to instruct AI assistants on how to guide users with the new `status` and `resolution` fields during story creation.
- [ ] (Optional) Example `grep`/`Select-String` queries in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` are reviewed for impact by the new field, and updated or new examples (e.g., querying by resolution) are added if beneficial.
- [x] User confirms the changes to the story structure and documentation are satisfactory before this story (`s028`) is marked "Done".
- [x] **Process:** User confirms the new story structure (directory, `story.md`, `journal.md`) and its initial content accurately reflect the planned work and adhere to the Story Documentation Guide.
