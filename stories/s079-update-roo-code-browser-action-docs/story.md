---
id: "s079-update-roo-code-browser-action-docs"
title: "Update Roo Code Browser Action Docs and Create AI Capabilities Guide"
status: "To Do"
priority: "Medium"
tags: "documentation;ai-assistant-capabilities;roo-code;browser-action;ai-guide;design"
resolution: "Unresolved"
---

# Story: s079-update-roo-code-browser-action-docs - Update Roo Code Browser Action Docs and Create AI Capabilities Guide

## Description

As a Vibe Tasking maintainer, I want to update the documentation for Roo Code's `browser_action` tool to reflect its conditional availability and create a new AI Guide for assistants to explain their capabilities, so that user expectations are better managed and AIs can clearly communicate their limitations.

Background:
Roo Code's `browser_action` tool is only available with specific AI models (e.g., Claude 3.5 Sonnet, 3.7 Sonnet variants) that have been officially trained and validated by their providers for computer use capabilities. This is not a Roo Code-specific limitation but rather reflects the capabilities released by model providers. The tool is excluded from the system prompt when unavailable to save tokens and prevent unsupported actions. This story aims to clarify this in Vibe Tasking documentation and provide guidance for AIs to explain such limitations. (See GitHub issue #4455 for more context).

Tasks:

1.  Update [`docs/reference/ai-assistant-capabilities.md`](../../../../docs/reference/ai-assistant-capabilities.md) to mention the model dependency for Roo Code's `browser_action` tool.
2.  Update [`docs/reference/roo-code-capabilities.md`](../../../../docs/reference/roo-code-capabilities.md) to detail _when_ the `browser_action` tool is available (e.g., specific Claude Sonnet models) and briefly explain the rationale (provider validation for computer use).
3.  Design and draft a new "AI Assistant Capabilities Guide" (e.g., in `ai-guides/core/reference/`) to help AIs explain their capabilities or limitations, especially when there's a mismatch with user expectations.

## Artifacts

- [`docs/reference/ai-assistant-capabilities.md`](../../../../docs/reference/ai-assistant-capabilities.md) (To be updated)
- [`docs/reference/roo-code-capabilities.md`](../../../../docs/reference/roo-code-capabilities.md) (To be updated)
- `ai-guides/core/reference/ai-assistant-capabilities-explaining-guide.md` (To be created: New AI Guide)
- [Roo Code Docs - Using Browser Use](https://docs.roocode.com/features/browser-use#using-browser-use) (External reference)
- [GitHub Issue: RooCodeInc/Roo-Code#4455](https://github.com/RooCodeInc/Roo-Code/issues/4455) (Context for `browser_action` availability)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Update Existing Roo Code Documentation**

  - [ ] [`docs/reference/ai-assistant-capabilities.md`](../../../../docs/reference/ai-assistant-capabilities.md) is updated to note the conditional availability (model dependency) of Roo Code's `browser_action` tool.
  - [ ] [`docs/reference/roo-code-capabilities.md`](../../../../docs/reference/roo-code-capabilities.md) is updated to clearly detail that the `browser_action` tool is available only with specific models (Claude Sonnet 3.5 or 3.7) and briefly explains the rationale (provider validation for computer use).
  - [ ] Test and document whether Cline (using `gemini-2.5-pro` as backend) can perform `browser_action`. Update `cline-capabilities.md` and `ai-assistant-capabilities.md` tables accordingly.
  - [ ] User reviews and approves the documentation updates.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Design and Draft AI Assistant Capabilities Explaining Guide**

  - [ ] **Process:** The [`ai-guides-collaborative-designing-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) has been consulted.
  - [ ] A new AI Guide, `ai-guides/core/reference/ai-assistant-capabilities-explaining-guide.md`, is drafted.
  - [ ] The guide's `usage` string is: "This guide should be consulted by an AI assistant when the user asks about AI assistant capabilities, especially when there seems to be a mismatch between user expectations and the AI assistant's own internal assessment of its capabilities for a given tool or action."
  - [ ] The guide instructs AI assistants on how to:
    - Clearly explain their general capabilities.
    - Address user queries about specific tool availability or limitations.
    - Manage user expectations when a requested action cannot be performed due to capability constraints (e.g., tool not available in current mode, model limitations).
    - Proactively inform users about conditional tool availability if relevant to the user's request.
  - [ ] User reviews the draft "AI Assistant Capabilities Explaining Guide".
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [ ] **Process:** AI performs an internal reflection on the completed story.
  - [ ] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [ ] **Process:** AI invites the user to provide their own retrospective feedback.
  - [ ] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [ ] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" and `resolution` field is set appropriately.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
