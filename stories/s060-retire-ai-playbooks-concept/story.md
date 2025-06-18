---
id: "s060-retire-ai-playbooks-concept"
title: "Retire AI-Playbooks Concept"
status: "Done"
priority: "Medium"
tags: "refactor;documentation;ai-playbook;cleanup"
resolution: "Implemented"
---

# Story: s060 - Retire AI-Playbooks Concept

## Description

As a Vibe Tasking maintainer, I want to retire the `ai-playbooks` concept and remove all associated files and references from the project, so that the documentation is streamlined and reflects current architectural decisions.

**Details:**
The `ai-playbooks` concept is considered outmoded or premature for the current state of the Vibe Tasking project. This story will manage the systematic removal of this concept.

This involves:

1.  Removing the primary playbook file: [`docs/ai-playbooks/INSTALLING.md`](docs/ai-playbooks/INSTALLING.md:1).
2.  Deleting related guide files, specifically [`docs/ai-guides/updating-installing-md-guide.md`](docs/ai-guides/updating-installing-md-guide.md:1).
3.  Searching for and removing all textual references to "ai-playbook(s)" and the `INSTALLING.md` file throughout the project.
4.  Deleting the entire [`docs/ai-playbooks/`](docs/ai-playbooks/) directory.
5.  Searching for and removing any remaining references to the `docs/ai-playbooks/` directory path.
6.  Updating story [`s046-create-writing-ai-playbooks-guide`](docs/stories/s046-create-writing-ai-playbooks-guide/story.md:2) to `status: "Closed"` and `resolution: "Obsolete"`.

## Artifacts

- This `story.md` and `journal.md`.
- Story [`s046-create-writing-ai-playbooks-guide/story.md`](docs/stories/s046-create-writing-ai-playbooks-guide/story.md:2) (to be updated).

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Update Story s046**

  - [x] **File Edit:** Modify [`docs/stories/s046-create-writing-ai-playbooks-guide/story.md`](docs/stories/s046-create-writing-ai-playbooks-guide/story.md:2) frontmatter:
    - Set `status: "Closed"`
    - Set `resolution: "Obsolete"`
  - [x] **Process:** User confirms story [`s046`](docs/stories/s046-create-writing-ai-playbooks-guide/story.md:2) is correctly updated.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Create ADR for Retiring AI-Playbooks' Checkpoint.

- [x] **Checkpoint: Create ADR for Retiring AI-Playbooks**

  - [x] **Drafting:** Create a new ADR file, tentatively named `docs/adrs/adr-022-retire-ai-playbooks-concept.md`.
    - The ADR should state the decision to retire the `ai-playbooks` concept and the associated `INSTALLING.md`.
    - It should explain the rationale (e.g., concept considered outmoded/premature, streamlining documentation, plans for alternative installation approach).
    - It must explicitly supersede [`docs/adrs/adr-008-ai-assisted-setup.md`](docs/adrs/adr-008-ai-assisted-setup.md:1).
    - It should identify and list other ADRs affected by this change (e.g., [`adr-005`](docs/adrs/adr-005-core-directory-structure.md:1), [`adr-010`](docs/adrs/adr-010-root-context-md.md:1), [`adr-011`](docs/adrs/adr-011-story-readme-sot.md:1), [`adr-013`](docs/adrs/adr-013-structured-onboarding.md:1), [`adr-015`](docs/adrs/adr-015-enhancing-ac-update-compliance.md:1), [`adr-017`](docs/adrs/adr-017-documentation-refactor.md:1)) and specify how they are impacted (e.g., sections becoming obsolete).
    - It should outline the impact of this decision, including the new (likely manual or to-be-defined) installation/setup process.
  - [x] **Review:** User reviews and approves the content of the new ADR.
  - [x] **Status Update (New ADR):** Update the status of the new ADR to "Accepted" in its frontmatter.
  - [x] **Status Update (Old ADRs):** Update the status of [`docs/adrs/adr-008-ai-assisted-setup.md`](docs/adrs/adr-008-ai-assisted-setup.md:1) to "Superseded by adr-022" (or the final new ADR ID) in its frontmatter. For other affected ADRs, add notes or update statuses as appropriate to reflect that parts are superseded or context has changed.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Update Onboarding Installation Document' Checkpoint.

- [x] **Checkpoint: Remove Core Playbook Files**

  - [x] **File Deletion:** Delete [`docs/ai-playbooks/INSTALLING.md`](docs/ai-playbooks/INSTALLING.md:1).
  - [x] **File Deletion:** Delete [`docs/ai-guides/updating-installing-md-guide.md`](docs/ai-guides/updating-installing-md-guide.md:1).
  - [x] **Process:** User confirms files have been deleted.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Remove Textual References' Checkpoint.

- [x] **Checkpoint: Update Onboarding Installation Document**

  - [x] **Identify Document:** Confirm the primary installation guide is [`docs/articles/onboarding/03-installation.md`](docs/articles/onboarding/03-installation.md:1).
  - [x] **Content Review:** Analyze the current content of [`docs/articles/onboarding/03-installation.md`](docs/articles/onboarding/03-installation.md:1) to identify all references to `INSTALLING.md` and the AI-assisted setup process.
  - [x] **Content Update:**
    - Remove sections detailing the use of `INSTALLING.md` with an AI assistant.
    - Replace these sections with placeholder content indicating that the AI-assisted setup is currently deprecated and new installation instructions are forthcoming.
    - Ensure any direct links to `INSTALLING.md` are removed.
  - [x] **Review:** User reviews and approves the changes to [`docs/articles/onboarding/03-installation.md`](docs/articles/onboarding/03-installation.md:1).
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Remove Core Playbook Files' Checkpoint.

- [x] **Checkpoint: Remove Textual References**

  - [x] **Search & Replace:** Search all project files (primarily `.md`) for references to:
    - "ai-playbook" (and its plural form)
    - "INSTALLING.md" (specifically the one in `docs/ai-playbooks/`)
    - The path `docs/ai-playbooks/`
  - [x] **Content Update:** Remove or rephrase found references appropriately. This may involve removing links, sentences, or entire sections.
  - [x] **Process:** User reviews and confirms all identified textual references have been appropriately addressed.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Delete `ai-playbooks` Directory' Checkpoint.

- [x] **Checkpoint: Delete `ai-playbooks` Directory**

  - [x] **Directory Deletion:** Delete the entire [`docs/ai-playbooks/`](docs/ai-playbooks/) directory.
  - [x] **Process:** User confirms the directory has been deleted.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Final Review and Closure' Checkpoint.

- [x] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set to "Implemented" in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
