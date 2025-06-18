---
id: "adr-029-lightweight-story-type"
title: "Lightweight Story Type"
status: "Proposed"
date: "2025-06-08"
tags: "story-structure;process;template;lightweight-story"
---

# ADR-029: Lightweight Story Type

## Context

Vibe Tasking stories, as currently defined by [`story.template.md`](../../../ai-guides/core/stories/story.template.md) and the [`stories-structuring-guide.md`](../../../ai-guides/core/stories/stories-structuring-guide.md), involve a multi-checkpoint structure. This structure is robust for complex tasks but introduces overhead for very simple, single-focus tasks that essentially have one primary acceptance criterion (AC). For example, a task to "update a single sentence in a README" or "fix a typo in a configuration file" might not warrant the full checkpoint protocol.

This overhead includes:

- Defining multiple process-oriented checkpoints (Initial Setup, Work Phase, Final Review).
- AI assistants performing the full Checkpoint Review Protocol for each.

The goal is to introduce a "lightweight story" type to streamline the process for such simple tasks while retaining core Vibe Tasking principles like clear ACs, journaling, and explicit user approval.

## Alternatives Considered

### Alternative 1: No Change (Use Full Story Structure for All Tasks)

- **Description:** Continue using the existing full story structure for all tasks, regardless of complexity.
- **Pros:**
  - Maximum consistency in process.
  - No new templates or guidance needed.
- **Cons:**
  - Process overhead for very simple tasks can feel disproportionate.
  - May discourage creation of stories for minor items due to perceived effort.

### Alternative 2: Ad-hoc Simplification by Users/AI

- **Description:** Allow users or AI assistants to informally simplify the story process on a case-by-case basis without a formal "lightweight" type.
- **Pros:**
  - Flexibility.
- **Cons:**
  - Inconsistency in how simple tasks are handled.
  - Lack of clear guidance for AI assistants on when and how to simplify.
  - Potential for missed steps or unclear completion status.
  - Harder to track or query for "simple" tasks systematically.

### Alternative 3: Rely Entirely on Inbox Method

- **Description:** Utilize the Inbox method (see [`adr-028-inbox-capture-mechanism.md`](adr-028-inbox-capture-mechanism.md) and [`../../../ai-guides/contrib/inbox-capturing-guide.md`](../../../ai-guides/contrib/inbox-capturing-guide.md)) for all simple tasks, without creating any story structure.
- **Pros:**
  - Minimal process for capturing emergent tasks.
- **Cons:**
  - No persistent record of the task's description, ACs, or steps taken beyond git commit messages.
  - No opportunity to evolve the task with additional ACs if it becomes more complex.
  - Less visibility and trackability compared to even a lightweight story.

## Decision

We will introduce a new "Lightweight Story" type to the Vibe Tasking framework.

Key characteristics of a Lightweight Story:

1.  **Tagging Convention and Planning Considerations:**
    - **Structural Definition:** Lightweight stories are fundamentally defined by their single "Combined Checkpoint" structure (detailed in point 3 below).
    - **Optional `lightweight` Tag:** For subsequent categorization and discovery, a story planned as lightweight _may_ include a specific tag, such as `lightweight`, within its `tags` field (e.g., `tags: "fix;lightweight"`).
      - This tag is applied after planning and serves to easily identify these stories (e.g., for users wanting to find all lightweight tasks).
    - **"Lightweight" Intent During Planning:** The _request_ or _intent_ to create a "lightweight" story during the planning phase signals to an AI assistant (guided by the [`stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md)) to:
      - Consider using the lightweight story template.
      - Assess if the task's scope is genuinely suitable for a single-checkpoint, streamlined approach.
      - If the scope appears too broad or complex for a single checkpoint, the AI should advise the user that a full story structure would be more appropriate.
2.  **Template:** A new template, `stories/lightweight-story.template.md`, will be created.
3.  **Structure:**
    - It will retain the standard `story.md` frontmatter.
    - It will feature a single, "Combined Checkpoint" for all substantive work and process steps. This checkpoint will still include ACs for:
      - Initial status update and journal entry.
      - Defining the single core task/AC.
      - User confirmation of the core task.
      - Performing the core task.
      - User review and approval of the completed task.
      - Final journal update and status update to "Done"/"Closed".
    - The AI-led retrospective will still be performed.
4.  **Guidance:**
    - [`ai-guides/core/stories/stories-planning-guide.md`](../../../ai-guides/core/stories/stories-planning-guide.md) will be updated to guide AI assistants on when to suggest or use a lightweight story (e.g., for tasks with a single, clear deliverable or AC).
    - [`ai-guides/core/stories/stories-structuring-guide.md`](../../../ai-guides/core/stories/stories-structuring-guide.md) will be updated to document this new story type and its template.

This approach aims to balance process reduction with the need for clear definition, tracking, and AI guidance.

## Consequences

### Positive

- Reduced process overhead for simple, single-AC tasks.
- Faster creation and completion of stories for minor items.
- Clearer distinction between complex and simple work items.
- Maintained consistency through a dedicated template and guidance.
- AI assistants will have explicit instructions on handling these simpler tasks.

### Negative

- Introduction of a new story type adds a small amount of complexity to the overall framework (another template, more guidance to maintain).
- Potential for initial confusion if the criteria for using a lightweight story are not clearly defined or understood.
- Requires updates to multiple core guidance documents.
