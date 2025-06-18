---
id: "s066-backfill-ai-guide-frontmatter"
title: "Backfill YAML Frontmatter into Existing AI Guides"
status: "Done" # Was Blocked by s065
priority: "Medium"
tags: "ai-guides;documentation;maintenance;backfill"
resolution: "Implemented"
---

# Story: s066-backfill-ai-guide-frontmatter - Backfill YAML Frontmatter into Existing AI Guides

## Description

This story is to add the YAML frontmatter, defined in story `s065-enhance-ai-guide-discoverability`, to all existing AI Guide documents (`ai-guides/**/*.md`, excluding templates). This will ensure all guides have consistent metadata, particularly the "purpose" or "usage_context" field, making them programmatically discoverable and their intended use clear.

**This story is blocked by the completion of `s065-enhance-ai-guide-discoverability`**, as it depends on the finalized frontmatter structure and updated AI guide template/authoring guidance from that story.

As a Vibe Tasking maintainer, I want all existing AI Guides to have the standard YAML frontmatter, so that they are consistently structured and their purposes can be programmatically determined.

## Artifacts

- Dependency: [`stories/s065-enhance-ai-guide-discoverability/story.md`](../s065-enhance-ai-guide-discoverability/story.md)
- Reference ADR (to be created in s065): `docs/adrs/adr-027-ai-guide-metadata-for-discoverability.md` (Expected path)
- Reference Guide (to be updated in s065): [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md)
- Reference Template (to be updated in s065): [`ai-guides/core/ai-guides/ai-guide.template.md`](../../ai-guides/core/ai-guides/ai-guide.template.md)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work (after s065 is complete).
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Identify Existing AI Guides**

  - [x] **Action:** Delete the outdated guide: `ai-guides/contrib/updating-onboarding-guide.md`.
  - [x] **Verification:** User confirms the file `ai-guides/contrib/updating-onboarding-guide.md` has been deleted.
  - [x] **Action:** Generate a list of all remaining AI Guide files (`ai-guides/**/*.md`) that require frontmatter backfilling. This list should exclude template files (e.g., `*.template.md`) and the deleted guide.
  - [x] **Verification:** The generated list is reviewed and confirmed by the user to be complete and accurate.
  - [x] **Process:** All ACs within this 'Identify Existing AI Guides' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Backfill YAML Frontmatter**

  - [x] **Action:** For each AI Guide identified in the previous checkpoint:
    - [x] Add the standard YAML frontmatter block as defined by the updated [`ai-guide.template.md`](../../ai-guides/core/ai-guides/ai-guide.template.md) (from s065).
    - [x] Populate the `id` field (e.g., derived from filename or existing H1 title, ensuring uniqueness if necessary).
    - [x] Populate the `title` field (typically from the guide's H1 title).
    - [x] Populate the `status` field (e.g., `"Accepted"` or as appropriate for a guide document).
    - [x] Populate the `tags` field with relevant keywords.
    - [x] Populate the `resolution` field (e.g., `"Unresolved"` or as appropriate for a guide document).
    - [x] Critically, populate the `usage` field (as finalized in s065) with a concise and accurate description of when the guide should be used. This will likely require careful reading and summarization of each guide's purpose.
  - [x] **Action:** Create `ai-guides/contrib/README.md` to provide an overview of the `contrib` guides.
  - [x] **Process:** All ACs within this 'Backfill YAML Frontmatter' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint, noting any challenges or interesting findings during the backfill.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Verification of Backfill**

  - [x] **Verification:** All identified AI Guides now contain the standard YAML frontmatter.
  - [x] **Verification:** A sample programmatic check (e.g., using `grep` or a small script) is performed to confirm that the `usage` field is present and populated in all backfilled guides. The results of this check are presented to the user.
  - [x] **Process:** All ACs within this 'Verification of Backfill' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
