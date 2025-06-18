---
id: "adr-015"
title: "Enhancing AI Compliance for Acceptance Criteria Updates"
status: "Accepted"
date: "2025-05-20"
tags: "process;ai-collaboration;acceptance-criteria;story-management;checkpoint"
---

# ADR-015: Enhancing AI Compliance for Acceptance Criteria Updates

## Context

A core tenet of the Vibe Tasking framework is the meticulous tracking of progress against clearly defined Acceptance Criteria (ACs) within each `story.md` file. It has been observed that AI assistants, while generally capable of performing the tasks outlined in ACs, sometimes fail to consistently mark these ACs as complete (e.g., by changing `- [ ]` to `- [x]`) in the `story.md` file. This oversight can lead to:

- Inaccurate representation of true story progress.
- Increased cognitive load on the user to manually track and update ACs.
- Potential for rework if an AI (or user) mistakenly believes an AC is still pending.

This ADR addresses the need for a more robust process to ensure AI assistants reliably update ACs.

## Alternatives Considered

1.  **No Change (Rely on User Diligence):** Continue with the current state, where the user is primarily responsible for noticing and correcting missed AC updates.

    - _Pros:_ No change to existing processes or documentation.
    - _Cons:_ Does not solve the underlying problem; maintains user burden.

2.  **In-line `story.md` Instruction Only:** Add a prominent instruction directly within the `story.md` template (via `docs/ai-guides/core/stories/stories-structuring-guide.md`) reminding the AI to update ACs.

    - _Pros:_ High visibility for the AI at the point of action.
    - _Cons:_ Might be overlooked; adds slight boilerplate to all stories.

3.  **Dedicated Guide via `CONTEXT.md` Only:** Create a new guide for "working on stories" and use `CONTEXT.md` to direct the AI to read it. This guide would detail the AC update procedure.

    - _Pros:_ Allows for comprehensive instructions on story execution best practices.
    - _Cons:_ Indirect reminder; AI must recall and apply guide content.

4.  **User-Initiated AC Update Commands Only:** Require the user to explicitly command the AI to mark specific ACs as complete.

    - _Pros:_ Very explicit; ensures user control.
    - _Cons:_ Significantly increases user burden; makes the process more manual.

5.  **Initial Hybrid Approach:** Combine in-line prompts, a dedicated guide, and new process ACs. (This was the state before introducing "Checkpoints").
6.  **Chosen "Checkpoint" Model (Evolved Hybrid):** Introduce a formal "Checkpoint" structure within `story.md` AC lists. Top-level Checkpoints define mandatory pause-and-ask points for AI assistants, with detailed ACs nested under them. This is layered with the in-line prompts, a dedicated guide, and process ACs.

## Decision

The Vibe Tasking project will adopt an evolved multi-layered approach, centered around a "Checkpoint" model, to enhance AI compliance with updating Acceptance Criteria and managing interaction flow. This solution consists of:

1.  **"Checkpoint" Structure in `story.md`:**
    - Acceptance Criteria lists will be structured with top-level "Checkpoints" (e.g., bolded items) that represent major phases or logical groupings of work.
    - Detailed, checkable Acceptance Criteria (ACs) will be nested under these Checkpoints (or can be standalone top-level items if simple).
    - This structure will be defined in `docs/ai-guides/core/stories/stories-structuring-guide.md`.
2.  **Mandatory AI Pause Protocol:**
    - Upon completion of all nested ACs for a Checkpoint, the AI assistant **MUST** pause its work on the story.
    - It must then perform the **Checkpoint Review Protocol** (defined below and detailed in the `working-on-stories-guide.md`) for all ACs within the just-completed Checkpoint.
    - Following user confirmation of those ACs, the AI **MUST** explicitly ask the user for approval to proceed to the _next_ Checkpoint (e.g., using an `ask_followup_question` tool if available, or for assistants like Windsurf/Cascade, engaging in natural language dialogue which inherently includes this pause and query).
3.  **In-line `story.md` Prompt for Marking ACs:** An explicit instruction will remain in the `docs/ai-guides/core/stories/stories-structuring-guide.md` template, reminding the AI to mark individual (nested) ACs as complete (`- [x]`).
4.  **Checkpoint Review Protocol Application & Process AC:** A standard "Process" AC will be added to the `docs/ai-guides/core/stories/stories-structuring-guide.md` template. This AC will reinforce the AI's responsibility to have applied the **Checkpoint Review Protocol** upon the completion of each Checkpoint. The protocol involves the AI summarizing completed ACs within the Checkpoint and obtaining user confirmation before those ACs are marked as complete and before asking to proceed to the next Checkpoint.
5.  **Dedicated Guide (`docs/guides/working-on-stories-guide.md`):** This guide will be created/updated to:
    - Detail the "Checkpoint" structure and the mandatory "pause and ask to proceed to next Checkpoint" protocol.
    - Detail the **Checkpoint Review Protocol** itself, including using tools like `ask_followup_question` (or for assistants like Windsurf/Cascade, their natural language dialogue and `suggested_responses` tool where appropriate) for the review and for asking to proceed.
    - Provide specific guidance for modal AI assistants (like Cline) on how Checkpoints map to their "task" or work cycle concepts.
    - Reinforce general best practices (journaling, status updates).
6.  **`docs/guides/planning-guide.md` Update:** This guide will be updated to instruct users and AIs on how to structure new stories using the Checkpoint model.
7.  **`CONTEXT.md` Update:** The root `CONTEXT.md` will direct AI assistants to consult the `docs/guides/working-on-stories-guide.md`.

## Consequences

### Positive

- **Increased Reliability:** The multi-layered prompts and explicit responsibilities are expected to significantly increase the likelihood of AI assistants correctly updating ACs.
- **Clearer AI Responsibilities:** The new process AC and guide clearly define the AI's role in the AC update process, including initiating reviews with the user.
- **Improved Progress Tracking:** More accurately updated ACs will lead to a clearer real-time view of story progress.
- **Dedicated Guidance Document:** The new guide provides a centralized place for best practices related to AI collaboration during story work, including nuanced advice for different AI types.
- **Reduced User Burden (Potentially):** While the review protocol involves user confirmation, the AI initiating this review should be less burdensome than the user having to constantly monitor and correct ACs.

### Negative

- **Minor Boilerplate Increase:** The in-line prompt and new process AC will add a small amount of text to each `story.md` file.
- **Potential for Slight Increase in User Interaction:** The AI-initiated review protocol requires user confirmation. However, this is intended to be a quick verification step.
- **Complexity of Implementation:** This change touches multiple key documents (`docs/ai-guides/core/stories/stories-structuring-guide.md`, `CONTEXT.md`, `INSTALLING.md`) and requires a new guide and ADR.
  > **Note:** The reference to `INSTALLING.md` here is historical. The AI-assisted setup via `INSTALLING.md` has been superseded by adr-022-retire-ai-playbooks-concept.md.

### Future Considerations

- The effectiveness of this new process, particularly the AI-initiated review protocol and its impact on user workflow, should be monitored.
- If AI assistants continue to struggle with AC updates despite these measures, or if the user burden for confirmation proves too high, this decision may need to be revisited and the protocol adjusted.
