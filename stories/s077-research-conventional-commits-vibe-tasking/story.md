---
id: "s077-research-conventional-commits-vibe-tasking"
title: "Research and Define Conventional Commit Prefixes for Vibe Tasking"
status: "To Do"
priority: "Medium"
tags: "conventional-commits;git;versioning;workflow;research;design;vibe-strategist"
resolution: "Unresolved"
---

# Story: s077-research-conventional-commits-vibe-tasking - Research and Define Conventional Commit Prefixes for Vibe Tasking

## Description

As a Vibe Tasking maintainer, I want to research and define a Conventional Commits-like prefix nomenclature tailored for Vibe Tasking workflows, so that commits can be categorized meaningfully, distinguishing between framework changes and typical project activities (like story creation or AI-Guide updates) which may not impact SemVer.

Background:

- Conventional Commits (e.g., `docs:`, `feat:`, `fix:`) are often used with tools like `semantic-release` to infer version changes.
- Vibe Tasking involves frequent commits for various documentation and workflow management tasks (e.g., creating stories, updating AI-Guides, journaling progress) that are distinct from code changes that would typically affect a host project's semantic version.
- A tailored prefix system would help clarify the nature of Vibe Tasking-related commits.
- The Vibe Strategist mode may be useful for brainstorming and refining these conventions.

## Artifacts

- `artifacts/s077-conventional-commits-research.md` (To be created: Research on Conventional Commits and their applicability)
- `artifacts/s077-vibe-tasking-commit-prefixes.md` (To be created: Proposed prefix nomenclature for Vibe Tasking)
- (Potentially) `docs/adrs/adr-XXX-vibe-tasking-commit-conventions.md` (To be created if an ADR is needed)
- (Potentially) A new AI-Guide for Vibe Tasking commit conventions.

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

- [ ] **Checkpoint: Research Conventional Commits & Vibe Tasking Needs**

  - [ ] Research the Conventional Commits specification and common usage patterns.
  - [ ] Analyze typical commit types within a Vibe Tasking workflow (e.g., new story, update story ACs, journal entry, new/update AI-Guide, new/update ADR, documentation changes, framework code changes if any).
  - [ ] Identify how standard Conventional Commit prefixes might align or misalign with Vibe Tasking commit types, especially concerning SemVer implications for a host project.
  - [ ] Analyze recent project commit history for any existing informal commit message conventions (e.g., `docs(guide): ...`, `docs(story): ...`) and consider them as input.
  - [ ] Document findings in `artifacts/s077-conventional-commits-research.md`.
  - [ ] User reviews research findings.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Design Vibe Tasking Commit Prefix Nomenclature**

  - [ ] Based on research, design a set of commit prefixes tailored for Vibe Tasking.
  - [ ] Prefixes should clearly distinguish between:
    - Changes to the Vibe Tasking framework itself (which might warrant a SemVer bump of Vibe Tasking).
    - Routine Vibe Tasking activities within a host project (e.g., `story:`, `journal:`, `ai-guide:`) that generally should not affect the host project's SemVer.
  - [ ] Consider if scopes (e.g., `story(s001):`) are applicable or useful.
  - [ ] Document the proposed prefixes, their meanings, and usage guidelines in `artifacts/s077-vibe-tasking-commit-prefixes.md`.
  - [ ] (Optional) If the decision is significant, draft an ADR for the new commit conventions.
  - [ ] (Optional) Consider if a new AI-Guide is needed to explain these conventions to AI assistants.
  - [ ] User reviews and approves the proposed nomenclature.
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
