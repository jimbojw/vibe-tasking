---
id: "adr-011"
title: "[Superseded] docs/stories/README.md as Single Source of Truth for Story Structure"
status: "Superseded"
date: "2025-05-30"
tags: "conventions;documentation-standards;stories;ai-interaction;core-concept"
---

# ADR-011: [Superseded] docs/stories/README.md as Single Source of Truth for Story Structure

## Status

This ADR has been **Superseded** by [ADR-024: Refactor Story Documentation into Dedicated AI Guides](adr-024-story-documentation-refactor.md) as of 2025-05-30. The single source of truth for story structure is now `docs/ai-guides/core/stories/stories-structuring-guide.md`.

## Context

For Vibe Tasking to function consistently, especially when AI assistants are involved in creating, parsing, and managing stories, there must be a definitive reference for how stories are structured. This includes directory naming conventions, required files (`story.md`, `journal.md`), YAML frontmatter fields, standard sections within `story.md`, and any other related conventions. Dispersing this information or leaving it ambiguous would lead to inconsistencies and errors.

## Alternatives Considered

1.  **No Single Source of Truth (SOT):** Rely on conventions being described in multiple places (e.g., various guides, onboarding documents, or just implied by examples).

    - _Pros:_ Flexibility in where information is placed.
    - _Cons:_ High risk of conflicting information, outdated instructions, and confusion for both users and AI assistants. Difficult to maintain consistency. AI might pick up incorrect or incomplete conventions.

2.  **Hardcoded Conventions in Tooling (if tooling existed):** If Vibe Tasking involved custom scripts or tools, these tools could enforce the structure.

    - _Pros:_ Strong enforcement.
    - _Cons:_ Violates the "code-free" principle (ADR-001). Makes conventions opaque (hidden in code) rather than explicit. Harder to update conventions without code changes.

3.  **Conventions Defined Only in `CONTEXT.md`:** Place all story structure rules directly within the root `CONTEXT.md` file.
    - _Pros:_ Centralized for AI initial onboarding.
    - _Cons:_ `CONTEXT.md` could become excessively long and detailed, trying to be both an AI onboarding pointer _and_ a comprehensive technical specification. `CONTEXT.md` is intended to be a high-level guide and pointer to more detailed documents.

## Decision

The **`docs/ai-guides/core/stories/stories-structuring-guide.md`** file within a Vibe Tasking project will serve as the **single source of truth (SOT)** for all conventions related to story structure, metadata, and management. (This ADR originally specified `docs/stories/README.md` but has been superseded).

This includes:

- Story directory naming conventions.
- Required files within a story directory (e.g., `story.md`, `journal.md`).
- The exact YAML frontmatter fields for `story.md`, their data types, recommended values (e.g., for `status`, `priority`, `resolution`), and formatting rules (e.g., quoting strings).
- Standard Markdown sections within `story.md` (e.g., Description, Artifacts, Acceptance Criteria).
- Conventions for `journal.md` entries.
- Guidelines for the optional `artifacts/` directory.
- Examples of command-line queries for stories (which rely on the defined frontmatter).

The root `CONTEXT.md` file will explicitly instruct AI assistants to familiarize themselves with `docs/ai-guides/core/stories/stories-structuring-guide.md` as the primary reference for all story-related operations. The setup process is responsible for ensuring this guide and the new lightweight `docs/stories/README.md` (which points to the guides) are correctly established.

> **Note:** The AI-assisted setup process via `INSTALLING.md` mentioned here has been superseded by [`adr-022-retire-ai-playbooks-concept.md`](adr-022-retire-ai-playbooks-concept.md:1). The creation of the story guides and the updated `docs/stories/README.md` is handled by the new installation/setup mechanism.

## Consequences

### Positive

- **Clarity and Consistency:** Provides one definitive place for all users and AI assistants to find story structure rules, minimizing ambiguity and ensuring consistency.
- **Maintainability:** When story conventions evolve, only this one file needs to be updated to reflect the new standard.
- **Effective AI Collaboration:** AI assistants can be reliably directed to this SOT to understand how to create, parse, query, or modify stories correctly.
- **Authoritative Reference:** Serves as the go-to document for any questions about story formatting or metadata.
- **Facilitates Onboarding:** New users or AI sessions can quickly get up to speed on story conventions by reviewing this single document.

### Negative

- **Central Point of Failure (if poorly maintained):** If `docs/ai-guides/core/stories/stories-structuring-guide.md` is inaccurate, outdated, or unclear, it will negatively impact all story-related activities. Diligent maintenance is crucial.
- **Requires AI to Read and Adhere:** The effectiveness relies on AI assistants being instructed to (and capable of) reading and adhering to the conventions in this document.
- **Potential for Length:** As the framework evolves, the `stories-structuring-guide.md` could become lengthy, requiring good internal organization. (This was a concern for the old `docs/stories/README.md`, now addressed by splitting into focused guides).

This decision establishes a clear, maintainable, and authoritative reference point for the most critical structural element of Vibe Tasking, which is essential for reliable user and AI interaction with stories.
