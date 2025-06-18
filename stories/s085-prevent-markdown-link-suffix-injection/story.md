---
id: "s085-prevent-markdown-link-suffix-injection"
title: "Investigate and Prevent AI Markdown Link Suffix Injection"
status: "To Do"
priority: "Medium"
tags: "ai-behavior;markdown;links;documentation;bug"
resolution: "Unresolved"
---

# Story: s085-prevent-markdown-link-suffix-injection - Investigate and Prevent AI Markdown Link Suffix Injection

## Description

As a user of Vibe Tasking, I want AI assistants to generate correct Markdown links without erroneous colon-number suffixes (e.g., `:0`, `:1`), so that links in documentation are functional and maintain the integrity of the project's knowledge base.

This story involves:

1.  Investigating the root cause of why AI assistants sometimes inject these breaking characters into Markdown links.
2.  Developing and implementing appropriately-placed guidance (e.g., in core AI-Guides or system prompt considerations) to explicitly forbid this practice and ensure links are generated correctly.

## Artifacts

- [`inbox/2025-06-10-investigate-and-prevent-ai-markdown-link-suffix-injection.md`](inbox/2025-06-10-investigate-and-prevent-ai-markdown-link-suffix-injection.md:0) (Original inbox item)
- (Potential) New or updated AI-Guide(s) or system prompt notes.
- (Potential) Research notes on AI behavior.

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [ ] **Process:** AI has consulted `stories-working-guide.md` and `stories-structuring-guide.md` for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** AI has performed spot grooming (consulting `stories-spot-grooming-guide.md`) and assisted in reviewing/confirming AC validity and completeness.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Investigation of Root Cause**

  - [ ] Research conducted to understand potential reasons for AI assistants injecting colon-number suffixes into Markdown links.
  - [ ] Possible causes documented (e.g., training data artifacts, misinterpretation of context, tool interactions).
  - [ ] A summary of findings is recorded in the journal or as an artifact.
  - [ ] **Process:** All ACs within this 'Investigation of Root Cause' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Investigation of Root Cause' Checkpoint and any significant decisions made within it.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Develop and Implement Prevention Guidance**

  - [ ] Based on investigation findings, appropriate guidance is drafted to instruct AI assistants to avoid link suffix injection.
  - [ ] Determine the best location(s) for this guidance (e.g., a new AI-Guide, updates to existing AI-Guides, considerations for system prompts).
  - [ ] New AI-Guide(s) created or existing ones updated with the new guidance.
  - [ ] (If applicable) Notes or recommendations for system prompt adjustments are documented.
  - [ ] User reviews and approves the drafted guidance and its placement.
  - [ ] **Process:** All ACs within this 'Develop and Implement Prevention Guidance' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [ ] **Process:** AI performs an internal reflection on the completed story, analyzing its execution.
  - [ ] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [ ] **Process:** AI invites the user to provide their own retrospective feedback and discusses any suggestions.
  - [ ] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [ ] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status like "Closed") and `resolution` field is set appropriately in this `story.md`'s frontmatter.
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
