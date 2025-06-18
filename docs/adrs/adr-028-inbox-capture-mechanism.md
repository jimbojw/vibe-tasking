---
id: "adr-028"
title: "Adopt Top-Level Inbox Directory for Emergent Thought Capture"
status: "Proposed"
date: "2025-06-08"
tags: "inbox;capture;gtd;workflow;process;s068"
deciders: "Vibe Tasking Maintainers (via s068)"
consulted: "AI Assistant (Roo)"
informed: "All Vibe Tasking Users and Contributors"
---

# ADR-028: Adopt Top-Level Inbox Directory for Emergent Thought Capture

## Context

During focused work on Vibe Tasking stories, users and AI assistants frequently encounter emergent thoughts, ideas, ancillary tasks, or potential improvements that are not directly within the scope of the current task. Without a dedicated, low-friction capture mechanism, these "open loops" can:

- Be forgotten if not immediately acted upon.
- Disrupt the current task flow if the user/AI attempts to address them prematurely.
- Lead to informal, inconsistent capture methods (e.g., mental notes, scratchpads, unrelated story comments).

This aligns with the "Capture" principle of David Allen's "Getting Things Done" (GTD) methodology, which emphasizes getting all commitments and ideas out of one's head and into a trusted external system. Story `s068-define-inbox-capture-mechanism` was initiated to design such a mechanism for Vibe Tasking.

The key requirements for this mechanism are:

- **Low Friction:** Easy and quick to use for both humans and AI.
- **Reliable Capture:** Ensures items are not lost.
- **Individual Item Integrity:** Each captured item should be distinct for later processing.
- **Vibe Tasking Alignment:** Should fit naturally within the existing file-based, Markdown-centric framework.

## Alternatives Considered

### Alternative 1: Single `INBOX.md` File

- **Description:** Use a single Markdown file (e.g., `INBOX.md` at the project root or in `docs/`) to which all captured thoughts are appended.
- **Pros:**
  - Simple concept, single point of entry.
- **Cons:**
  - Potential for merge conflicts if multiple users/AIs append simultaneously (less of an issue in typical single-user + AI Vibe Tasking, but a structural concern).
  - Processing individual items from a long, single file can be cumbersome.
  - AI interaction for appending requires careful file manipulation to avoid overwriting.
  - Less clean separation of individual thoughts for later conversion into distinct stories or tasks.

### Alternative 2: Using Story `journal.md` or `artifacts/` of the _Current_ Story

- **Description:** Capture emergent thoughts directly within the `journal.md` or an artifact file of the story being worked on when the thought arises.
- **Pros:**
  - Context is immediately co-located.
- **Cons:**
  - Thoughts might not be relevant to the current story and could get lost or become hard to find later if they need to be processed independently.
  - Clutters the journal or artifacts of a specific story with items that might belong elsewhere or become their own stories.
  - No centralized "inbox" to review all captured emergent items across the project.

## Decision

It is decided to adopt a new top-level directory named `inbox/` at the project root as the dedicated mechanism for capturing emergent thoughts within Vibe Tasking.

Each captured item will be a separate Markdown (`.md`) file within this `inbox/` directory.

The specifics of this mechanism are detailed in [`stories/s068-define-inbox-capture-mechanism/artifacts/proposed_mechanism.md`](../../stories/s068-define-inbox-capture-mechanism/artifacts/proposed_mechanism.md). Key aspects include:

1.  **Location:** `inbox/` at the project root. A `README.md` file will be placed within `inbox/` to describe its purpose, optionally link to relevant guides, and explicitly state that it **MUST NOT** contain an index of inbox items.
2.  **Capture Method:** One `.md` file per captured item.
3.  **File Naming Convention:** `YYYY-MM-DD-descriptive-slug.md` (e.g., `2025-06-08-create-adr-for-guide-discovery.md`). The date is UTC.
4.  **Content of Inbox Items:** The content of each `.md` file is simply the raw captured thought, idea, or task. No specific internal structure (like YAML frontmatter) is prescribed, prioritizing low-friction capture. Context, if needed, can be part of the raw text.

## Consequences

### Positive

- **Low-Friction Capture:** Creating a new small file is a straightforward operation for AI assistants and users.
- **Clear Separation:** Emergent thoughts are kept separate from active story work, maintaining focus.
- **Individual Item Processing:** Each captured item is a distinct file, making it easy to list, review, and process individually (e.g., delete, archive, or convert into a new story as planned in `s069`).
- **Centralized Collection:** All "open loops" are gathered in one known location.
- **VCS Integration:** Inbox items are version-controlled like any other project file.
- **Alignment with GTD:** Directly implements the "Capture" and "Inbox" concepts.

### Negative

- **Directory Proliferation:** The `inbox/` directory could accumulate many small files if not regularly processed. (This is mitigated by the planned `s069-design-implement-inbox-processing` story).
- **Process Adherence:** Relies on users and AI assistants consistently using this mechanism. An AI Guide (`ai-guides/contrib/inbox-capturing-guide.md` as proposed in `s068`) will be crucial.
- **Initial Setup:** Requires creation of the `inbox/` directory and its `README.md`.

## Links / References

- [`stories/s068-define-inbox-capture-mechanism/story.md`](../../stories/s068-define-inbox-capture-mechanism/story.md) (Driving story for this decision)
- [`stories/s068-define-inbox-capture-mechanism/artifacts/proposed_mechanism.md`](../../stories/s068-define-inbox-capture-mechanism/artifacts/proposed_mechanism.md) (Detailed proposal for the inbox mechanism)
- [`stories/s068-define-inbox-capture-mechanism/artifacts/gtd_principles.md`](../../stories/s068-define-inbox-capture-mechanism/artifacts/gtd_principles.md) (GTD principles informing this decision)
- [`stories/s069-design-implement-inbox-processing/story.md`](../../stories/s069-design-implement-inbox-processing/story.md) (Planned follow-up story for processing inbox items)
