---
id: "adr-016"
title: "Use ASCII-Art for Diagrams"
status: "Accepted"
date: "2025-05-20"
tags: "adr;documentation;diagrams;ascii-art"
---

# ADR-016: Use ASCII-Art for Diagrams

## Context

The Vibe Tasking project requires a method for embedding diagrams within its documentation, including ADRs and story descriptions. Key considerations for choosing a diagramming method include:

- **Direct Viewability:** Diagrams should be easily viewable directly in plain text environments, version control diffs, and code editors without requiring special rendering or plugins.
- **Version Control Friendliness:** The diagram format should be text-based to allow for meaningful diffs and versioning.
- **Tooling Simplicity:** The method should align with the principles of `adr-001-code-free-framework.md`, minimizing external dependencies or build steps.
- **Current Git Hosting Limitations:** The primary Git hosting platform used for this project does not natively render complex diagramming languages like Mermaid. Implementing client-side or build-step rendering for Mermaid would introduce complexity counter to ADR-001.
- **AI Assistant Compatibility:** The chosen format should ideally be interpretable and potentially updatable by AI assistants.

## Alternatives Considered

1.  **Mermaid:**

    - _Pros:_ Rich, structured diagramming syntax; can produce complex and visually appealing diagrams; text-based and version controllable.
    - _Cons:_ Requires rendering capabilities not natively supported by the current Git host; integrating rendering would add build complexity or reliance on browser extensions, violating ADR-001 principles; AI assistants may not universally support generating or updating complex Mermaid syntax accurately without specific fine-tuning or tools.

2.  **Embedded Images (e.g., PNG, JPG, SVG):**

    - _Pros:_ Can produce highly detailed and visually rich diagrams; SVGs are text-based and scalable.
    - _Cons:_
      - PNG/JPG are binary formats, making diffs meaningless and increasing repository size.
      - SVGs, while text-based, can be very complex, making manual diffs and edits challenging.
      - Both typically require external tools to create and edit, increasing workflow friction.
      - Binary images (PNG/JPG) generally have poor support for interpretation or modification by AI assistants. SVGs might be parsable but complex for AI to manipulate reliably.
      - Not directly viewable in all plain text environments.

3.  **ASCII-Art / Text-Based Diagrams:**
    - _Pros:_ Directly viewable in any text editor, terminal, or version control interface; inherently text-based, making diffs and versioning straightforward; no external dependencies or build steps required; aligns perfectly with `adr-001-code-free-framework.md`; generally well-understood and can be created/edited by AI assistants.
    - _Cons:_ Can be more time-consuming to create and maintain for complex diagrams; visual fidelity is limited compared to graphical formats; may become unwieldy for very large or intricate diagrams.

## Decision

The decision is to use **ASCII-art** for diagrams within the Vibe Tasking project documentation.

This includes diagrams in ADRs, story descriptions, guides, and any other Markdown-based documentation where visual representation is beneficial. Tools that facilitate ASCII-art creation (e.g., online editors, text editor plugins) can be used, but the final output must be plain text ASCII characters.

## Consequences

### Positive Consequences

- **Maximum Viewability & Accessibility:** Diagrams are viewable everywhere text can be displayed, without needing special tools or rendering.
- **No Build/Tooling Overhead:** Aligns with the "code-free" and "zero-build" principles of the Vibe Tasking framework (ADR-001).
- **Excellent Version Control Integration:** Changes to diagrams are easily tracked and diffed.
- **Simplicity:** Easy for humans and AI assistants to read and potentially modify.
- **Platform Independence:** Works across all operating systems and text editors.

### Negative Consequences

- **Limited Visual Fidelity:** ASCII-art cannot achieve the same level of visual polish or complexity as graphical diagramming tools or languages like Mermaid.
- **Creation/Maintenance Effort:** Creating and maintaining complex diagrams in ASCII-art can be more laborious than using dedicated diagramming software.
- **Scalability for Complexity:** Very large or intricate diagrams might be difficult to represent clearly and maintainably in ASCII-art.

### Future Considerations

This decision can be revisited and potentially superseded by a new ADR if:

- The primary Git hosting platform introduces native, server-side rendering for a suitable text-based diagramming language (e.g., Mermaid).
- The trade-offs change significantly due to advancements in AI capabilities for diagram generation/manipulation in other formats.
