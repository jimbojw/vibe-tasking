---
id: "s090-create-article-why-not-manually-edit-ai-code"
title: "Create Article: Why Not Manually Edit AI-Generated Code"
status: "Done"
priority: "Medium"
tags: "lightweight;article;documentation"
resolution: "Implemented"
---

# Story: s090-create-article-why-not-manually-edit-ai-code - Create Article: Why Not Manually Edit AI-Generated Code

## Description

This story is to create a new article for the `docs/articles/` directory. The article will address the reasons why developers should avoid manually editing AI-generated code, even for seemingly minor changes.

The core arguments to be presented are:

- Focusing on immediate, personal speed by manually editing is a "wrong question."
- The correct perspective is to consider what is faster and more maintainable for all future users and AI interactions over time.
- The article will use a metaphor: an expert Java developer _could_ manually patch bytecode if a compiler error occurs, but the correct engineering solution is to _fix the compiler_ if the error persists.
- In AI-assisted software engineering, the natural language specifications, context, and acceptance criteria provided to the AI are the primary "code." Source code files are downstream artifacts.
- If an AI assistant consistently errs, the developer's role is to "fix the compiler" by improving the inputs to the AI. Vibe Tasking, with its emphasis on AI Guides, facilitates this.

The article should be produced with AI assistance, leveraging relevant AI Guides for article writing.

## Artifacts

- [x] New article: `docs/articles/why-not-manually-edit-ai-generated-code.md`

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Combined - Story Execution and Closure**

  - [x] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Core Task:** A new article titled 'Why Not Manually Edit AI-Generated Code' (or similar, to be finalized during drafting) is created in `docs/articles/why-not-manually-edit-ai-generated-code.md`. The article clearly articulates the arguments against manual edits of AI-generated code, using the suggested Java compiler/bytecode metaphor, and emphasizes improving AI inputs (e.g., AI Guides) as the correct long-term strategy. The article is well-structured, follows project documentation standards (consulting `ai-guides/contrib/articles/articles-writing-guide.md`), and has been reviewed for clarity and accuracy.
  - [x] **Process:** User reviews and approves the completion of the 'Core Task' and any related sub-tasks.
  - [x] **Process (Retrospective):** AI performs an internal reflection on the completed story, analyzing its execution.
  - [x] **Process (Retrospective):** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [x] **Process (Retrospective):** AI briefly lists its journaled suggestions to the user and asks if it's okay to proceed with story closure. (User may optionally provide feedback or create inbox items for suggestions at this point).
  - [x] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [x] **Process:** All ACs within this 'Combined - Story Execution and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint and the story's overall completion.
