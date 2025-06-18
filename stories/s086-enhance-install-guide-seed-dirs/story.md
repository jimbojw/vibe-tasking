---
id: "s086-enhance-install-guide-seed-dirs"
title: "Enhance Install Guide to Seed stories/ and ai-guides/ Dirs with READMEs"
status: "To Do"
priority: "Medium"
tags: "installation;setup;documentation;ai-guides;stories;lightweight"
resolution: "Unresolved"
---

# Story: s086-enhance-install-guide-seed-dirs - Enhance Install Guide to Seed stories/ and ai-guides/ Dirs with READMEs

## Description

As a user installing Vibe Tasking, I want the AI-assisted installation process to automatically create the initial `stories/` and `ai-guides/` directories in my host project, each populated with a basic `README.md` file, so that my project has a more complete and user-friendly starting structure for Vibe Tasking.

This involves updating the [`INSTALL_VIBE_TASKING.md`](INSTALL_VIBE_TASKING.md:0) guide to instruct the AI assistant performing the installation to:

1.  Create the `stories/` directory.
2.  Create an `ai-guides/` directory.
3.  Add a `README.md` to `stories/` with specific boilerplate content.
4.  Add a `README.md` to `ai-guides/` with specific boilerplate content.
    The boilerplate content for these READMEs will be defined and inlined within the `INSTALL_VIBE_TASKING.md` guide itself.

## Artifacts

- [`INSTALL_VIBE_TASKING.md`](INSTALL_VIBE_TASKING.md:0) (The primary file to be modified)
- [`inbox/2025-06-10-update-install-guide-to-create-stories-aiguides-dirs-with-readmes.md`](inbox/2025-06-10-update-install-guide-to-create-stories-aiguides-dirs-with-readmes.md:0) (Original inbox item)
- [`artifacts/host-project-stories-README.md`](stories/s086-enhance-install-guide-seed-dirs/artifacts/host-project-stories-README.md:0) (Draft README for host project `stories/` dir)
- [`artifacts/host-project-ai-guides-README.md`](stories/s086-enhance-install-guide-seed-dirs/artifacts/host-project-ai-guides-README.md:0) (Draft README for host project `ai-guides/` dir)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** AI has performed spot grooming (consulting `stories-spot-grooming-guide.md`) and assisted in reviewing/confirming AC validity and completeness (especially the 'Core Task' AC).
  - [ ] **Process:** User confirms the 'Core Task' AC below is accurate, complete, and suitable for a lightweight story.
  - [ ] **Core Task:** The [`INSTALL_VIBE_TASKING.md`](INSTALL_VIBE_TASKING.md:0) guide is updated to include:
    - Instructions for the AI assistant to create `stories/` and `ai-guides/` directories in the host project during installation.
    - Inlined boilerplate content for a `README.md` file to be placed in the new `stories/` directory.
    - Inlined boilerplate content for a `README.md` file to be placed in the new `ai-guides/` directory.
    - Instructions for the AI assistant to write these `README.md` files.
  - [ ] **Core Task:** The updated installation process (as if run by an AI following the revised guide) is tested, and it successfully creates the `stories/` and `ai-guides/` directories with their respective `README.md` files containing the correct boilerplate.
  - [ ] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [ ] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
