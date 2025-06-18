---
id: "s009-how-to-use-vibe-tasking-guide"
title: "Create 'How to Use Vibe Tasking' Guide"
status: "Done"
priority: "High"
tags: "documentation;guide;onboarding"
---

# Story: s009 - Create 'How to Use Vibe Tasking' Guide

## Description

As a potential adopter of Vibe Tasking, I want a clear guide on how to set up and use the Vibe Tasking methodology in my own new or existing project so that I can quickly get started with repository-integrated story management.

**Details:**

Currently, this project serves as an _example_ of Vibe Tasking, but it lacks explicit instructions for others to adopt it. This story is about creating a new guide document (e.g., `docs/guides/how-to-use-vibe-tasking.md`) that covers:

- **Introduction:** Briefly reiterate what Vibe Tasking is and its benefits.
- **Setting up in a New Project:**
  - Recommended directory structure (e.g., creating `docs/stories/`).
  - Copying or creating a `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` (the Story Documentation Guide).
  - Creating your first story (directory, `story.md` with frontmatter, `journal.md`).
- **Adopting in an Existing Project:**
  - Similar steps to a new project, but considerations for integrating with existing documentation or workflows.
- **Core Concepts:**
  - Explanation of `story.md`, `journal.md`, and `artifacts/`.
  - Importance and structure of YAML frontmatter.
- **Customization:** Emphasize flexibility and encourage adapting conventions.
- **Tips for Success:** (e.g., consistency, linking artifacts, using journal effectively).

## Artifacts

- **Superseded Guide:** `docs/guides/how-to-use-vibe-tasking.md` (The AI playbook content from this guide, created as part of story s009, has been moved to `INSTALLING.md` and this file deleted as part of story s011).
- **New AI Playbook Location:** [`INSTALLING.md`](../../ai-playbooks/INSTALLING.md) (This file now contains the AI playbook for setting up Vibe Tasking in other projects).
- [Journal for this story](journal.md)

## Acceptance Criteria

- [x] A new guide document (e.g., `how-to-use-vibe-tasking.md`) is created, likely within the `docs/guides/` directory.
- [x] The guide covers setting up Vibe Tasking in both new and existing projects.
- [x] The guide explains the core components and conventions (story directories, `story.md`, `journal.md`, frontmatter).
- [x] The guide emphasizes the flexibility of Vibe Tasking.
- [x] The guide is clear, concise, and actionable for a new user.
- [x] The main `docs/guides/README.md` is updated to list the new guide.
