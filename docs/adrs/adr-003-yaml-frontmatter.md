---
id: "adr-003"
title: "Use YAML Frontmatter for Structured Metadata"
status: "Accepted"
date: "2025-05-19"
tags: "metadata;syntax;stories;adrs;queryability;parsing"
---

# ADR-003: Use YAML Frontmatter for Structured Metadata

## Context

While Markdown (see ADR-002) is the primary syntax for Vibe Tasking documents due to its readability and AI compatibility, it lacks a standardized way to embed structured metadata directly within the document that is easily machine-parsable for tasks like querying, filtering, or status tracking. Relying solely on parsing Markdown content for this metadata can be brittle.

We need a way to include key metadata fields (e.g., ID, title, status, priority, tags) for stories and ADRs themselves in a consistent, easily parsable format that complements the main Markdown content.

## Alternatives Considered

1.  **No Explicit Metadata Block / Parse from Markdown:** Attempt to extract metadata by parsing conventions within the main Markdown body (e.g., specific heading formats or keyword lines).

    - _Pros:_ Keeps everything strictly within Markdown syntax.
    - _Cons:_ Very brittle; minor changes to wording or formatting could break parsing. Complex to implement reliably with simple tools. Less explicit for human readers to identify metadata fields.

2.  **Custom Delimited Metadata Block (Non-YAML):** Use custom delimiters and a custom key-value format within a block.

    - _Pros:_ Could be tailored exactly to needs.
    - _Cons:_ Lacks standard tooling for parsing and validation that YAML offers. AI assistants might be less familiar with a custom format. Adds cognitive overhead for users to learn the custom syntax.

3.  **JSON Frontmatter:** Use JSON within the `---` delimiters instead of YAML.

    - _Pros:_ JSON is widely supported and strictly defined.
    - _Cons:_ Less human-readable than YAML for simple key-value lists (more quotes, commas, braces). Can be more cumbersome for manual editing.

4.  **Separate Metadata Files:** Store metadata in separate files (e.g., a JSON or CSV file per story/ADR, or a central manifest file).
    - _Pros:_ Completely separates metadata from content, potentially easier for bulk processing by some tools.
    - _Cons:_ Disassociates metadata from the content it describes, making it harder to manage and keep synchronized. Increases the number of files per story/ADR. Less convenient for AI assistants to process as a single unit of context.

## Decision

Vibe Tasking documents that require structured metadata, specifically **stories (`story.md`)** and **ADRs (`docs/adrs/*.md`)**, will use **YAML frontmatter** at the beginning of the file.

The frontmatter block will be delimited by triple-dashed lines (`---`). Inside this block, metadata will be defined as key-value pairs in YAML format.

Key requirements for this YAML frontmatter:

- Each field and its value must be on a single line.
- All string values for core metadata fields must be enclosed in double quotes to ensure consistent parsing, especially by simpler command-line tools.

## Consequences

### Positive

- **Structured Metadata:** Provides a clear, structured way to define essential metadata separate from the narrative content.
- **Machine Readability & Queryability:** YAML is easily parsed by a wide variety of tools, including simple command-line utilities (like `grep`, `sed`, `awk` with appropriate regex) and more sophisticated parsers in various programming languages. This facilitates querying and filtering of stories/ADRs based on metadata fields.
- **Human Readability:** YAML is designed to be human-readable, especially for simple key-value structures.
- **AI Compatibility:** AI assistants can readily understand and generate YAML, making it easy to collaborate on metadata creation and updates.
- **Consistency:** Enforces a consistent way to specify metadata across all stories and ADRs.
- **Complements Markdown:** Allows Markdown to be used for its strength (narrative content) while offloading structured data to a more suitable format within the same file.

### Negative

- **Slightly Increased Complexity:** Introduces a second syntax (YAML) alongside Markdown, though YAML for simple key-value pairs is straightforward.
- **Adherence Required:** The benefits rely on consistent adherence to the frontmatter format (e.g., quoting strings, one field per line). Deviations could break parsing for simpler tools.
- **Not a Database Replacement:** While good for embedding metadata, it's not a substitute for a full database if highly complex querying or relational data management is needed (which is outside Vibe Tasking's core scope).

This decision balances the need for structured, queryable metadata with the desire to maintain overall simplicity and readability within the Vibe Tasking framework.
