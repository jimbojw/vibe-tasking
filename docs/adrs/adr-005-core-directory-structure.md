---
id: "adr-005"
title: "Core Directory Structure for Vibe Tasking Projects"
status: "Accepted"
date: "2025-05-19"
tags: "project-structure;documentation-organization;conventions;core-concept"
---

# ADR-005: Core Directory Structure for Vibe Tasking Projects

## Context

To ensure consistency, discoverability, and a clear separation of concerns for Vibe Tasking artifacts within a user's project, a standardized core directory structure is beneficial. This structure needs to be logical for both human users and AI assistants navigating the project. It should also accommodate the primary types of documents Vibe Tasking relies on.

## Alternatives Considered

1.  **Flat Structure:** Place all Vibe Tasking files (stories, guides, context) in a single top-level directory (e.g., `.vibes/` or `vibes/`).

    - _Pros:_ Simple for very small projects.
    - _Cons:_ Becomes disorganized quickly as the number of files grows. Hard to distinguish between different types of documents (e.g., stories vs. guides).

2.  **User-Defined Structure:** Allow users to define any directory structure they prefer, with Vibe Tasking tools or AI needing to be configured or explicitly told where to find things.

    - _Pros:_ Maximum flexibility for users.
    - _Cons:_ No consistency across projects using Vibe Tasking. Makes it difficult for AI assistants (especially those pre-trained or broadly familiar with Vibe Tasking conventions) to reliably locate key files like `CONTEXT.md` or the stories directory. Increases setup and configuration burden.

3.  **Highly Nested/Granular Structure:** Create many deeply nested subdirectories for different categories or states of documents.
    - _Pros:_ Very fine-grained organization.
    - _Cons:_ Can lead to overly complex paths and make navigation cumbersome. May be overkill for many projects.

## Decision

Vibe Tasking will promote a standard core directory structure, typically rooted within a `docs/` directory in the user's project, along with key files at the project root. The recommended structure is:

- **Project Root:**
  - `CONTEXT.md`: Primary AI onboarding and context file.
  - `INSTALLING.md`: AI playbook for installing/setting up Vibe Tasking in a new project.
    > **Note:** The concept of `INSTALLING.md` as an AI playbook for setup has been superseded by [`adr-022-retire-ai-playbooks-concept.md`](adr-022-retire-ai-playbooks-concept.md:1).
- **`docs/` (or a similar user-chosen top-level documentation directory):**
  - `README.md`: Overview of the project's documentation.
  - `stories/`: Contains all Vibe Tasking stories.
    - `README.md`: The canonical Story Documentation Guide.
    - `sXXX-slug/`: Directory for an individual story.
      - `story.md`
      - `journal.md`
      - `artifacts/` (optional)
  - `guides/`: For project-specific instructional guides.
    - `README.md`: Overview of guides.
  - `reference/`: For project-specific reference material.
    - `README.md`: Overview of reference material.
  - `adrs/` (as adopted by this project): For Architecture Decision Records.
    - `README.md`: Overview of ADRs.
  - `onboarding/` (primarily for the Vibe Tasking framework project itself, to guide users on Vibe Tasking):
    - `README.md`
    - `01-introduction.md`, etc.

While the top-level `docs/` directory is a common convention, users could adapt this (e.g., to `.docs/` or `project_docs/`) as long as the relative structure within it (especially for `stories/` and its `README.md`) and the location of root `CONTEXT.md` are maintained or clearly communicated to AI assistants.

## Consequences

### Positive

- **Consistency:** Provides a predictable structure across projects using Vibe Tasking, making it easier for users and AI assistants to navigate.
- **Discoverability:** Key files and document types are found in expected locations.
- **Separation of Concerns:** Different types of documentation (stories, guides, reference) are logically grouped.
- **Scalability:** The structure can accommodate a growing number of stories and documents.
- **AI Friendliness:** A consistent structure helps AI assistants locate and understand the purpose of different files more reliably.

### Negative

- **Prescriptive:** Some users might prefer a different organizational scheme. However, the core elements (`CONTEXT.md`, `docs/ai-guides/core/stories/stories-structuring-guide.md`, and the `stories/sXXX-slug/` pattern) are crucial for Vibe Tasking's operation with AI.
- **Initial Setup:** Requires creating these directories, though this is typically automated by the AI during the `INSTALLING.md` process.
  > **Note:** The AI-automated setup via `INSTALLING.md` mentioned here has been superseded by [`adr-022-retire-ai-playbooks-concept.md`](adr-022-retire-ai-playbooks-concept.md:1).

This decision aims to balance providing a clear, effective standard structure with allowing some flexibility for project-specific needs, while ensuring core components are consistently located for optimal AI interaction.
