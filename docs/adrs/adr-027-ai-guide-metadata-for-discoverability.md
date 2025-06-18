---
id: "adr-027"
title: "Adopt YAML Frontmatter for AI Guide Discoverability"
status: "Proposed"
date: "2025-05-30"
tags: "ai-guides;metadata;discoverability;workflow;yaml"
---

# ADR-027: Adopt YAML Frontmatter for AI Guide Discoverability

## Context

Currently, AI assistants and users must either remember the available AI guides or rely on hints within the main `CONTEXT.md` file. This approach is not scalable as the number of AI guides grows. It becomes increasingly difficult for an AI assistant to efficiently and accurately identify the most relevant guide for a user's specific task or query. This can lead to suboptimal AI assistance, wasted time, or the AI failing to leverage existing documented knowledge.

The Vibe Tasking project aims to make AI-assistant collaboration as effective as possible. A key part of this is ensuring that AI assistants can easily find and understand the purpose of instructional documents like AI Guides.

## Alternatives Considered (Optional)

### Alternative 1: Enhanced `CONTEXT.md`

- **Description:** Continue to manually curate and update `CONTEXT.md` with more detailed descriptions and trigger phrases for each AI guide.
- **Pros:**
  - No structural change to individual AI guide files.
- **Cons:**
  - Becomes increasingly unwieldy and difficult to maintain as the number of guides grows.
  - Still relies on a central, manually updated file which can become a bottleneck.
  - Less flexible for programmatic discovery by AI assistants.

### Alternative 2: Full-Text Search by AI

- **Description:** Rely on AI assistants to perform full-text searches across all AI guides to determine relevance.
- **Pros:**
  - No changes needed to guide structure.
- **Cons:**
  - Can be slow and computationally expensive for the AI.
  - Relevance matching based on full text can be imprecise and may miss nuances or require significant prompting to narrow down.
  - Does not provide a quick, structured way to grasp a guide's core purpose.

## Decision

We will adopt a minimal YAML frontmatter block at the beginning of every AI Guide file (`ai-guides/**/*.md`, excluding templates). This frontmatter will provide structured metadata to improve the discoverability and understanding of each guide's purpose.

The standard YAML frontmatter for AI Guides will include the following fields:

- `id`: (String, Required) A unique identifier for the guide, typically derived from its filename (e.g., for `ai-guides-collaborative-designing-guide.md`, the id would be `ai-guides-collaborative-designing`).
- `title`: (String, Required) The full H1 title of the guide as it appears in the document (e.g., "Guide: Collaboratively Designing and Authoring AI Guides").
- `usage`: (String, Required) A concise (1-2 sentences) description of when this guide should be consulted or used. This field is critical for enabling AI assistants to quickly determine the guide's relevance to a user's task. Example: "Use this guide when assisting a user in creating a new AI Guide to ensure it meets project standards for structure, content, and collaborative design."
- `tags`: (String, Optional) A semicolon-separated list of relevant keywords or concepts that can further aid in searching and categorization (e.g., "authoring;collaboration;standards;template").

This frontmatter must be placed at the very beginning of the Markdown file to allow for easy parsing by simple command-line tools (e.g., `head`, `grep`).

This decision complements the existing naming convention for AI Guides as specified in [`adr-023-standardize-ai-guides-naming.md`](adr-023-standardize-ai-guides-naming.md:1).

## Consequences

### Positive

- **Improved Discoverability:** AI assistants can programmatically list all AI guides and parse their `usage` field to quickly identify relevant guides for a user's query or task. This can be achieved with simple shell commands (e.g., `find ... -exec head ...`, `grep`).
- **Enhanced AI Efficiency:** Assistants can more accurately and rapidly suggest or use the correct guide, reducing guesswork and improving the quality of assistance.
- **Scalability:** The system becomes more scalable as new guides are added; their purpose is immediately machine-readable.
- **Consistency:** Ensures all AI guides have a standard way of declaring their purpose.
- **Reduced Reliance on `CONTEXT.md`:** `CONTEXT.md` can be simplified to provide meta-guidance on _how_ to find relevant guides, rather than listing them all explicitly.

### Negative

- **Backfill Effort:** Existing AI guides will need to be updated to include this new frontmatter (addressed in story `s066-backfill-ai-guide-frontmatter`).
- **Maintenance Overhead:** Authors of new AI guides must remember to include and correctly populate the frontmatter. This will be mitigated by updating the AI guide template and authoring guides.

## Links / References

- [`adr-023-standardize-ai-guides-naming.md`](adr-023-standardize-ai-guides-naming.md:1)
- Story `s065-enhance-ai-guide-discoverability` (this ADR is an artifact of this story)
- Story `s066-backfill-ai-guide-frontmatter` (follow-up story)
