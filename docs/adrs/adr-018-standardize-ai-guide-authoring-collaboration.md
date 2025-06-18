---
id: "adr-018"
title: "Standardize AI Guide Authoring and Collaborative Design Process"
status: "Accepted"
date: "2025-05-23"
tags: "ai-guide;standards;collaboration;process;template;authoring"
deciders: "User (via AI assistant interaction)"
consulted: "AI Assistant (Cline)"
informed: "Project Maintainers, AI Assistants"
---

# ADR-018: Standardize AI Guide Authoring and Collaborative Design Process

## Context

As the Vibe Tasking project grows, the number of AI-Guides—documents intended to instruct AI assistants on how to perform tasks or understand concepts—is increasing. To ensure consistency, clarity, and effectiveness of these guides, and to leverage the AI assistant as a true partner in their creation, a standardized approach to both their structure and the collaborative process of their design is needed.

Currently, while general Markdown best practices are followed, there isn't a specific, documented standard for:

- The collaborative process an AI assistant should follow when helping a user design a new AI-Guide.
- The precise structure and content expectations for AI-Guides (e.g., imperative voice, audience declaration, use of templates).
- A readily available template for creating new AI-Guides.

This lack of standardization could lead to inconsistent guide quality, AI misunderstandings, and inefficient use of user and AI time during guide creation.

**Decision Drivers:**

- Need for consistent quality and structure across all AI-Guides.
- Desire to maximize AI assistant effectiveness by providing clear, unambiguous instructions.
- Importance of leveraging the AI assistant's capabilities as a thinking partner in the guide design process, not just a scribe.
- Need for a reusable template to speed up the creation of new AI-Guides.
- Alignment with the Vibe Tasking ethos of strong user-AI collaboration.

## Alternatives Considered

### Alternative 1: No explicit standard

- **Description:** Rely on general best practices and individual AI/user discretion.
- **Pros:** No upfront effort.
- **Cons:** High risk of inconsistency, poor quality guides, inefficient collaboration.

### Alternative 2: Standardize only file structure/formatting

- **Description:** Define a template and formatting rules, but don't explicitly guide the collaborative design process.
- **Pros:** Ensures structural consistency.
- **Cons:** Misses the significant benefit of guiding the AI's role in the collaborative _design_ of the guide content, which is crucial for effectiveness.

### Alternative 3: Standardize both collaborative design process and file structure/formatting

- **Description:** Create a comprehensive guide for AI assistants on how to help users design and write AI-Guides, and provide a corresponding file template.
- **Pros:** Addresses both the "what" (structure) and the "how" (collaborative design) for creating effective AI-Guides. Maximizes benefits of user-AI partnership.
- **Cons:** Highest initial effort, but expected to yield the best long-term results.

## Decision

It was decided to **Standardize both collaborative design process and file structure/formatting (Option 3)**.

This will be achieved by:

1.  **Creating a new AI-Guide:** `docs/ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`. This guide will instruct AI assistants on:
    - How to collaboratively engage with a user to understand the intent and scope of a new AI-Guide.
    - How to leverage AI expertise in structuring the new guide and identifying potential issues.
    - How to assist in collaboratively drafting and refining content.
    - The standard structure, formatting, voice, and content requirements for all AI-Guides.
2.  **Creating a new AI-Guide template:** `docs/ai-guides/core/ai-guides/ai-guide.template.md`. This template will provide a standardized starting point for new AI-Guides, incorporating placeholders for common sections.
3.  **Updating existing AI-Guides:** Over time, existing AI-Guides will be reviewed and aligned with the structural and formatting standards outlined in `ai-guides-collaborative-designing-guide.md`. (This alignment is covered by other ACs in story `s052`).

## Consequences

### Positive

- Improved consistency and quality of AI-Guides.
- Enhanced clarity for AI assistants consuming these guides.
- More effective and efficient collaboration between users and AI assistants during the guide creation process.
- AI assistants are empowered to be more proactive partners in guide design.
- Faster creation of new AI-Guides due to the template and clear standards.
- Reinforces the Vibe Tasking ethos of strong user-AI partnership.

### Negative

- Initial effort required to create the new guide and template.
- Effort required to align existing guides to the new standard over time.

## Links / References

- `docs/ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md` (The new standard and process guide)
- `docs/ai-guides/core/ai-guides/ai-guide.template.md` (The new template)
- `docs/stories/s052-codify-apply-ai-guide-standards/story.md` (The story driving this decision)
