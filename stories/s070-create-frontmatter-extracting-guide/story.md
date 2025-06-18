---
id: "s070-create-frontmatter-extracting-guide"
title: "Create AI Guide: Extracting YAML Frontmatter"
status: "To Do"
priority: "Medium"
tags: "documentation;ai-guide;frontmatter;extraction;cli;lightweight"
resolution: "Unresolved"
---

# Story: s070-create-frontmatter-extracting-guide - Create AI Guide: Extracting YAML Frontmatter

## Description

As a Vibe Tasking user or AI assistant, I want a dedicated AI Guide that details common methods for extracting YAML frontmatter from files, particularly story files, so that this process can be performed efficiently and consistently, especially when using command-line tools. This guide should include examples for Linux/macOS and considerations for Windows.

## Artifacts

- New AI Guide: [`ai-guides/core/frontmatter-extracting-guide.md`](ai-guides/core/frontmatter-extracting-guide.md:0) (to be created)
- Updated: [`ai-guides/core/stories/stories-discovering-guide.md`](ai-guides/core/stories/stories-discovering-guide.md:0)
- (Potentially) Updated: [`ai-guides/core/ai-guides/ai-guides-discovering-guide.md`](ai-guides/core/ai-guides/ai-guides-discovering-guide.md:0)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [ ] **Process:** The '[`stories-working-guide.md`](ai-guides/core/stories/stories-working-guide.md:0)' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the 'Core Task' AC below is accurate, complete, and suitable for a lightweight story.
  - [ ] **Core Task:** A new AI Guide, [`ai-guides/core/frontmatter-extracting-guide.md`](ai-guides/core/frontmatter-extracting-guide.md:0), is created, detailing:
    - [ ] The purpose and benefits of efficiently extracting YAML frontmatter.
    - [ ] At least one reliable command-line method (e.g., using `awk` as explored: `awk '/^---$/{if(flag==1){flag=0}else{flag=1}; next} flag==1'`) for extracting frontmatter content from single or multiple files for Linux/macOS.
    - [ ] Examples of how to use the chosen method(s) with `find` and `xargs` for batch processing.
    - [ ] Discussion and illustrative examples for adapting or finding equivalent commands for Windows (e.g., using PowerShell `Select-String`, `Get-Content` with regex, or `ForEach-Object`).
    - [ ] Guidance on handling the output (e.g., direct use by AI, redirection to temporary files, adding separators between outputs from multiple files).
  - [ ] [`ai-guides/core/stories/stories-discovering-guide.md`](ai-guides/core/stories/stories-discovering-guide.md:0) is updated to reference the new [`ai-guides/core/frontmatter-extracting-guide.md`](ai-guides/core/frontmatter-extracting-guide.md:0) for detailed frontmatter extraction techniques, potentially simplifying its own examples.
  - [ ] Consideration is given to referencing the new guide in [`ai-guides/core/ai-guides/ai-guides-discovering-guide.md`](ai-guides/core/ai-guides/ai-guides-discovering-guide.md:0), and an update is made if deemed appropriate and beneficial for AI guide discovery processes.
  - [ ] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [ ] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
