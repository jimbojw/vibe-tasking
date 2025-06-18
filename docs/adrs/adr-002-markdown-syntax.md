---
id: "adr-002"
title: "Use Markdown as Primary Syntax for Vibe Tasking Documents"
status: "Accepted"
date: "2025-05-19"
tags: "syntax;documentation-format;core-concept;readability;ai-compatibility"
---

# ADR-002: Use Markdown as Primary Syntax for Vibe Tasking Documents

## Context

Vibe Tasking aims to be a lightweight, accessible, and AI-friendly framework for managing development tasks and project documentation. A fundamental decision is the choice of syntax for all its core documents, including stories (`story.md`, `journal.md`), guides, and context files. The chosen syntax needs to be easy for humans to read and write, and equally easy for AI assistants to parse and understand.

Alternatives could include plain text, more structured formats like XML/JSON, or proprietary formats.

## Alternatives Considered

1.  **Plain Text (.txt):**

    - _Pros:_ Maximum simplicity, universally compatible.
    - _Cons:_ Lacks any structuring capability for headings, lists, code blocks, emphasis, or links, making complex documents hard to read and navigate. No standard way to indicate semantic meaning.

2.  **Structured Data Formats (e.g., XML, JSON):**

    - _Pros:_ Excellent for machine readability and complex data structures. Strong validation capabilities.
    - _Cons:_ Not human-friendly for writing or reading narrative documentation. Verbose. High learning curve for non-developers. AI generation can be overly complex.

3.  **Rich Text Formats (e.g., RTF, DOCX):**

    - _Pros:_ WYSIWYG editing, rich formatting options.
    - _Cons:_ Binary formats are not version-control friendly (diffs are meaningless). Often tied to specific software. Less accessible for AI parsing and generation compared to plain text or Markdown.

4.  **Other Lightweight Markup Languages (e.g., AsciiDoc, reStructuredText):**
    - _Pros:_ Often more powerful and feature-rich than Markdown (e.g., better support for includes, complex tables, admonitions).
    - _Cons:_ Steeper learning curve than Markdown. Smaller user base and less ubiquitous tool support. Potentially less familiar to a broad range of AI models.

## Decision

Vibe Tasking will use **Markdown** as the primary syntax for all its user-facing and AI-consumed documentation.

This includes:

- Story definitions (`story.md`)
- Journal entries (`journal.md`)
- Guides (`docs/guides/`)
- Onboarding documents (`docs/onboarding/`)
- Context files (`CONTEXT.md`)
- ADRs themselves (`docs/adrs/`)

While YAML frontmatter is used for metadata (see ADR-003), the main body of all these documents will be Markdown.

## Consequences

### Positive

- **Human Readability:** Markdown is designed to be easily readable in its raw form and renders cleanly into HTML for display.
- **AI Compatibility:** AI assistants, particularly LLMs, are extensively trained on Markdown content and can parse, understand, and generate it effectively.
- **Simplicity:** The syntax is simple and has a low learning curve for users.
- **Wide Tool Support:** A vast ecosystem of editors, linters, previewers, and converters support Markdown.
- **Version Control Friendly:** Markdown files are plain text, making them ideal for version control systems like Git (easy diffing and merging).
- **Portability:** Documents are not tied to specific proprietary software.
- **Extensibility (within limits):** While the core is simple, Markdown can be extended with features like tables, code blocks, etc., which are useful for technical documentation.

### Negative

- **Limited Structure:** Markdown is less structured than formats like XML or JSON. While this is a benefit for simplicity, complex data relationships can be harder to represent purely in Markdown. (This is partly mitigated by using YAML frontmatter for metadata).
- **Flavor Variations:** Different Markdown parsers might have slight variations in how they interpret certain edge cases, though common standards (like CommonMark) alleviate this.
- **Not Ideal for All Data Types:** While excellent for narrative text and code, Markdown is not a replacement for databases or highly structured data storage.

This decision prioritizes human and AI readability, simplicity, and broad compatibility, aligning with Vibe Tasking's core goals.
