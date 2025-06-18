---
id: "adr-012"
title: "Use of journal.md for Story Context and History"
status: "Accepted"
date: "2025-05-19"
tags: "stories;documentation-practices;context-management;auditability;process"
---

# ADR-012: Use of journal.md for Story Context and History

## Context

During the lifecycle of a Vibe Tasking story, numerous events occur: work commences, progress is made, decisions are taken, issues are encountered, discussions happen, and eventually, the story is completed or closed. The main `story.md` file defines the task but is not suitable for capturing this dynamic, chronological flow of information. A dedicated mechanism is needed to log these activities for context recovery, auditability, and knowledge sharing.

## Alternatives Considered

1.  **No Formal Journal:** Rely on commit messages, chat logs, or memory to reconstruct a story's history.

    - _Pros:_ No extra files to maintain.
    - _Cons:_ Highly unreliable. Commit messages are often too brief or not directly tied to story-specific decisions. Chat logs are ephemeral and hard to search. Memory is fallible. Context is easily lost, especially for older stories or when team members change.

2.  **Embedding Journal Entries in `story.md`:** Add a "Journal" section within the `story.md` file itself.

    - _Pros:_ Keeps all information in one file.
    - _Cons:_ Can make `story.md` excessively long and cluttered, mixing the static definition of the story with its dynamic history. Harder to quickly see the latest updates without scrolling through the entire definition.

3.  **External Logging Tool:** Use a separate issue tracker or project management tool's comment system for logging story progress.
    - _Pros:_ Dedicated tools often have rich features for comments, notifications, etc.
    - _Cons:_ Creates a disconnect from the repository-integrated Vibe Tasking artifacts (ADR-004). Information is not version-controlled with the story definition. May require an internet connection or access to a separate system.

## Decision

Each Vibe Tasking story will include a dedicated **`journal.md`** file within its directory. This Markdown file will serve as a chronological log for all significant events, progress, updates, decisions, discussions, and notes related to that specific story.

Key characteristics of `journal.md` usage:

- Entries should be timestamped (e.g., `## YYYY-MM-DDTHH:MM:SSZ`).
- Content should be concise but informative, detailing what happened or was decided.
- It should be updated contemporaneously as work progresses or events occur.
- Both users and AI assistants are responsible for contributing to the journal (e.g., AI noting it has started work, user logging a key decision after a discussion).

## Consequences

### Positive

- **Context Recovery:** Provides a reliable way to quickly understand the history and current state of a story, especially when resuming work after a pause or for new team members/AI sessions.
- **Auditability:** Creates a traceable record of a story's lifecycle.
- **Knowledge Persistence:** Captures valuable context, rationale for decisions, and solutions to problems encountered during the story's execution.
- **Improved Collaboration:** Serves as a shared log that all participants (human and AI) can refer to.
- **Supports Asynchronous Work:** Allows team members to catch up on progress made by others.
- **Version Controlled History:** Like all Vibe Tasking files, the journal is version controlled.

### Negative

- **Requires Discipline:** The value of `journal.md` depends on consistent and timely updates by users and AI. If neglected, it loses its utility.
- **Potential for Verbosity:** If entries are too detailed or frequent for minor updates, the journal could become noisy, though this is a matter of convention and judgment.
- **Manual Effort (to some extent):** While AI can make entries for its actions, users need to remember to log their own decisions or offline discussions.

This decision prioritizes robust context management and historical tracking within the repository-integrated, text-based philosophy of Vibe Tasking.
