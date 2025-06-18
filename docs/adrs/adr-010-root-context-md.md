---
id: "adr-010"
title: "Use of Root CONTEXT.md for AI Onboarding"
status: "Accepted"
date: "2025-05-19"
tags: "ai-interaction;onboarding;context-management;conventions;core-concept"
---

# ADR-010: Use of Root CONTEXT.md for AI Onboarding

## Context

For an AI assistant to effectively collaborate on a project using Vibe Tasking (or any project, really), it needs initial grounding information. This includes understanding the project's purpose, key architectural elements, coding standards, and crucial Vibe Tasking conventions (like where to find the `docs/ai-guides/core/stories/stories-structuring-guide.md`). Providing this context at the beginning of each new AI session is vital for relevant and accurate AI contributions.

## Alternatives Considered

1.  **No Standard Context File:** Rely on users to manually provide necessary context at the start of each AI session through conversational prompts.

    - _Pros:_ Maximum flexibility for users in what context they provide.
    - _Cons:_ Inconsistent context provision. Prone to users forgetting critical information. Time-consuming for users to repeat context. AI might not receive all necessary pointers, leading to suboptimal performance or misunderstandings.

2.  **Embedding All Context in Every Story:** Attempt to include all global project context within each individual `story.md` file.

    - _Pros:_ Ensures context is always with the task.
    - _Cons:_ Highly redundant. Bloats story files. Makes global context updates very difficult (requires editing every story). Not suitable for overarching project information.

3.  **Project-Specific AI Configuration Files (if supported by AI tool):** Rely on AI tools that might have their own project-specific configuration mechanisms for pre-loading context.
    - _Pros:_ Could be powerful if the AI tool offers robust features.
    - _Cons:_ Ties Vibe Tasking's context mechanism to specific AI tools, violating the "agnostic framework" principle (ADR-007). Not all AI assistants or IDE integrations support such custom configurations.

## Decision

Vibe Tasking will promote the use of a **single, standardized `CONTEXT.md` file located at the root of the user's project.**

This `CONTEXT.md` file serves as the primary onboarding document for AI assistants. Its purpose is to:

- Provide a concise overview of the project.
- Instruct the AI on essential Vibe Tasking conventions, primarily by pointing it to the `docs/ai-guides/core/stories/stories-structuring-guide.md` (the SOT for story structure) and potentially other key guides like `docs/guides/planning-guide.md`.
- Link to other critical project-specific documentation (e.g., main project `README.md`, architectural diagrams, coding standards).
- Set expectations for AI behavior and collaboration within the project.

Users are responsible for creating and maintaining their project's `CONTEXT.md`. The AI-assisted setup process (`INSTALLING.md`) will create an initial `CONTEXT.md` template that users should then customize.

> **Note:** The AI-assisted setup process via `INSTALLING.md` mentioned here has been superseded by [`adr-022-retire-ai-playbooks-concept.md`](adr-022-retire-ai-playbooks-concept.md:1). The creation of an initial `CONTEXT.md` template will need to be handled by the new installation/setup mechanism.

## Consequences

### Positive

- **Consistent AI Onboarding:** Provides a standard mechanism for giving AI assistants initial project context.
- **Centralized Core Instructions:** Key pointers and instructions for AI are in one place, making them easier to manage and update.
- **Reduced Redundancy:** Avoids repeating common instructions in every AI interaction or story file.
- **Improved AI Performance:** A well-crafted `CONTEXT.md` helps the AI understand the project and its conventions better, leading to more relevant and accurate assistance.
- **User Empowerment:** Gives users direct control over how AI is primed for their specific project.
- **Tool Agnostic:** Relies on a simple Markdown file, which any AI capable of reading files can process.

### Negative

- **User Responsibility:** The effectiveness of `CONTEXT.md` depends on the user creating and maintaining it properly. An outdated or poorly written `CONTEXT.md` can be detrimental.
- **AI Must Process It:** Users (or automated workflows) must ensure the AI processes `CONTEXT.md` at the start of relevant sessions.
- **Not a Replacement for Dynamic Context:** `CONTEXT.md` provides initial, relatively static context. Dynamic, task-specific context will still come from individual `story.md` files and ongoing conversation.
- **Potential for Overload:** If `CONTEXT.md` becomes too long or tries to include too much detail (instead of linking to details), it could be less effective or exceed AI context window limits for some interactions. Brevity and linking are key.

This decision establishes a simple yet powerful convention for managing the initial context provided to AI assistants, aligning with Vibe Tasking's principles of clarity and effective user-AI collaboration.
