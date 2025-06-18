---
id: "adr-014"
title: "Inclusion of Standard Process Acceptance Criteria in Stories"
status: "Accepted"
date: "2025-05-19"
tags: "stories;conventions;process;acceptance-criteria;quality"
---

# ADR-014: Inclusion of Standard Process Acceptance Criteria in Stories

## Context

Vibe Tasking stories rely on Acceptance Criteria (ACs) to define what "done" means for a task. While most ACs are specific to the story's deliverables, certain process-related actions are consistently required for good Vibe Tasking hygiene, such as updating the story's status and maintaining its journal. If these process steps are not explicitly listed, they might be overlooked.

## Alternatives Considered

1.  **No Explicit Process ACs:** Assume users and AI assistants will remember to perform standard process steps (like updating status or journal) without them being listed in every story's ACs.

    - _Pros:_ Shorter AC lists in `story.md`.
    - _Cons:_ High risk of these crucial process steps being forgotten, leading to outdated story metadata and incomplete journals. Less explicit guidance for AI.

2.  **Process Steps Documented Elsewhere Only:** Document the standard process steps in a general guide (like `docs/ai-guides/core/stories/stories-structuring-guide.md` or a "Working with Stories" guide) but do not repeat them in individual story ACs.

    - _Pros:_ Avoids repetition in each `story.md`.
    - _Cons:_ Users and AI might not always refer back to the general guide when focused on a specific story. Less immediate reminder within the context of the task at hand.

3.  **Automated Process Updates (if tooling existed):** If Vibe Tasking had dedicated tooling, some process steps (like updating status when work begins) could potentially be automated.
    - _Pros:_ Ensures consistency for automatable steps.
    - _Cons:_ Violates "code-free" principle (ADR-001). Not all process steps (e.g., "journal kept up-to-date") are easily automatable.

## Decision

Vibe Tasking stories **should include a set of standard "Process" Acceptance Criteria** at the beginning of their AC list. These process ACs serve as explicit reminders for essential Vibe Tasking hygiene.

Recommended standard process ACs (as also mentioned in `docs/ai-guides/core/stories/stories-structuring-guide.md`):

- `- [ ] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.`
- `- [ ] **Process:** An initial journal entry is added to journal.md for this story, noting work has commenced.`
- `- [ ] **Process:** The journal.md for this story is kept up-to-date with entries detailing progress and decisions *as they are made*.`
  (And potentially others related to completion, like updating status to "Done" and filling in `resolution`).

These are included directly in each `story.md` to ensure they are highly visible during story execution.

## Consequences

### Positive

- **Increased Consistency:** Helps ensure that standard Vibe Tasking processes (status updates, journaling) are followed more consistently.
- **Clear Reminders:** Acts as an immediate checklist for users and AI assistants working on a story.
- **Improved Story Hygiene:** Leads to more accurate story metadata and more complete, contemporaneous journal entries.
- **Better Training for AI:** Explicitly listing these steps helps reinforce expected AI behavior when interacting with stories.
- **Enhanced Auditability:** When these ACs are checked off, it provides a clearer audit trail of process adherence.

### Negative

- **Repetition in `story.md`:** These standard ACs will be repeated in every story, adding a few lines to each `story.md` file.
- **Manual Checking:** Still requires users or AI to manually check off these ACs (though AI can be instructed to do so for its own actions).

This decision prioritizes the benefits of explicit reminders and consistent process adherence over the minor cost of repeating a few standard ACs in each story.
