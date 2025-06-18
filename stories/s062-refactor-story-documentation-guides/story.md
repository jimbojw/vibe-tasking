---
id: "s062-refactor-story-documentation-guides"
title: "Refactor Story Documentation into Dedicated AI Guides under docs/ai-guides/vibe-tasking/stories/"
status: "Done"
priority: "Medium"
tags: "documentation;stories;ai-guides;refactor;adr"
resolution: "Implemented"
---

# Story: s062-refactor-story-documentation-guides - Refactor Story Documentation into Dedicated AI Guides under docs/ai-guides/vibe-tasking/stories/

## Description

Currently, information about Vibe Tasking story structure, planning, and working processes is spread across `docs/stories/README.md` and various AI guides. This story aims to refactor and consolidate this documentation into a dedicated set of AI guides located under `docs/ai-guides/vibe-tasking/stories/`. This will improve organization, clarity, and maintainability of story-related guidance. An ADR will be created to document this decision. The existing `docs/stories/README.md` will be updated to be a lightweight pointer to these new guides.

## Artifacts

- ADR (to be created): `../../adrs/adr-024-story-documentation-refactor.md`
- New Structuring Guide (to be created): `../../ai-guides/vibe-tasking/stories/stories-structuring-guide.md`
- New/Updated Planning Guide (to be created/updated): `../../ai-guides/vibe-tasking/stories/stories-planning-guide.md`
- New/Updated Working Guide (to be created/updated): `../../ai-guides/vibe-tasking/stories/stories-working-guide.md`
- Moved Story Template (to be moved): `../../ai-guides/vibe-tasking/stories/story.template.md`
- Moved Journal Template (to be moved): `../../ai-guides/vibe-tasking/stories/journal.template.md`
- Existing `docs/stories/README.md` (to be updated)
- Existing `docs/ai-guides/vibe-tasking/stories-planning-guide.md` (source for new planning guide)
- Existing `docs/ai-guides/vibe-tasking/stories-working-guide.md` (source for new working guide)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Author ADR for Story Documentation Refactor**

  - [x] Collaboratively draft an ADR for the decision to refactor story documentation into dedicated AI guides under `docs/ai-guides/vibe-tasking/stories/`.
  - [x] ADR to follow `../../ai-guides/adr.template.md` and conventions in `../../ai-guides/adrs-writing-guide.md`.
  - [x] ADR clearly states the context (current scattered documentation), decision (consolidate into new guides at the new location), considered options (e.g., keeping current structure, alternative locations), and consequences (improved organization, clearer AI guidance, potential link maintenance).
  - [x] User approves the ADR content and its status is set (e.g., "Accepted").
  - [x] ADR saved to `../../adrs/adr-024-story-documentation-refactor.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Plan New Guide Structure & Content Migration**

  - [x] Define the precise content to be moved from the current `../../stories/README.md` to the new guides.
  - [x] Outline the structure and key sections for the new `../../ai-guides/vibe-tasking/stories/stories-structuring-guide.md`.
  - [x] Outline the structure and key sections for the new `../../ai-guides/vibe-tasking/stories/stories-planning-guide.md` (this will likely involve migrating and potentially refining content from the existing `../../ai-guides/vibe-tasking/stories-planning-guide.md` to this new, more specific location).
  - [x] Outline the structure and key sections for the new `../../ai-guides/vibe-tasking/stories/stories-working-guide.md` (similarly, migrating/refining content from the existing `../../ai-guides/vibe-tasking/stories-working-guide.md`).
  - [x] Define the content for the new, lightweight `../../stories/README.md`, which will primarily point to these new guides.
  - [x] User confirms the documentation plan and new guide outlines.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Create New AI Guides in `docs/ai-guides/vibe-tasking/stories/`**

  - [x] Create `../../ai-guides/vibe-tasking/stories/stories-structuring-guide.md` with planned content.
  - [x] Create (or move and update) `../../ai-guides/vibe-tasking/stories/stories-planning-guide.md` with planned content.
  - [x] Create (or move and update) `../../ai-guides/vibe-tasking/stories/stories-working-guide.md` with planned content.
  - [x] Ensure the original top-level planning and working guides (if moved) are either replaced with pointers or appropriately deprecated/archived if their distinct purpose is superseded.
  - [x] Move `docs/stories/story.template.md` to `../../ai-guides/vibe-tasking/stories/story.template.md`.
  - [x] Move `docs/stories/journal.template.md` to `../../ai-guides/vibe-tasking/stories/journal.template.md`.
  - [x] Update all references to `story.template.md` and `journal.template.md` in the three new guides (`stories-structuring-guide.md`, `stories-planning-guide.md`, `stories-working-guide.md`) to point to their new location.
  - [x] User reviews and approves the content of the new/updated AI guides and the moved templates in their new location.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Update `docs/stories/README.md`**

  - [x] Update `../../stories/README.md` to be a lightweight descriptor, primarily linking to the new AI guides in `../../ai-guides/vibe-tasking/stories/`. (e.g. `stories-structuring-guide.md`)
  - [x] User reviews and approves the updated `../../stories/README.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Review and Update Cross-References**

  - [x] Construct a grep command to search all relevant project files (e.g., `*.md` in `docs/`, `CONTEXT.md`) for links to `docs/stories/README.md` and the old paths of planning/working guides.
  - [x] Execute the grep command, redirecting its output to a file in `./.tmp_ai_output/` (e.g., `./.tmp_ai_output/s062_cross_references.txt`).
  - [x] Read and analyze the `./.tmp_ai_output/s062_cross_references.txt` file to identify all files needing updates.
  - [x] For each identified file, update the links to point to the new guide locations under `docs/ai-guides/vibe-tasking/stories/` (e.g. `stories-structuring-guide.md`).
  - [x] User confirms all relevant cross-references are updated by reviewing the changes and/or the updated `s062_cross_references.txt` (if it's useful to re-run grep to confirm no old links remain).
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [x] **Process:** Journal updated.
  - [x] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
