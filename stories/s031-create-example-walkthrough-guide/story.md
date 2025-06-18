---
id: "s031-create-example-walkthrough-guide"
title: "Create Example Walkthrough Guide"
status: "Done"
priority: "Medium"
tags: "documentation;onboarding;tutorial;example"
resolution: "Completed"
---

# Story: s031 - Create Example Walkthrough Guide

## Description

As a new Vibe Tasking user, I want a step-by-step example walkthrough of a typical Vibe Tasking session so I can see the framework in action and better understand the user-AI interaction for planning and executing a story.

This story involves creating a new guide document, likely `docs/onboarding/05-example-walkthrough.md`, that provides a scripted example of:

1.  A user initiating planning for a task with an AI assistant.
2.  The AI helping to define and create the `story.md` and `journal.md` for a new Vibe Tasking story.
3.  The user then instructing the AI to begin work on that newly created story.
4.  A brief illustration of the AI assisting with an acceptance criterion and updating the journal.

The walkthrough should include example user prompts and AI responses/actions.

## Acceptance Criteria

- [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
- [ ] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
- [ ] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.
- [ ] A new guide file (e.g., `docs/onboarding/05-example-walkthrough.md`) is created.
- [ ] The new guide contains a clear, step-by-step scripted example of a Vibe Tasking session, covering story planning and initial work execution.
- [ ] The example includes illustrative user prompts and AI assistant responses/actions.
- [ ] The `docs/onboarding/README.md` is updated to include this new guide in its list and recommended reading order.
- [ ] The `docs/onboarding/04-working-with-stories.md` guide is updated to link to this new walkthrough as a practical example.
- [x] User confirms the new example walkthrough guide is clear, helpful, and accurately represents a typical Vibe Tasking workflow.
- [x] **Process:** User confirms the new story structure (directory, `story.md`, `journal.md`) for _this_ story (`s031`) and its initial content accurately reflect the planned work and adhere to the Story Documentation Guide.
