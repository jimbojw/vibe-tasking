---
id: "adr-020"
title: "Standardize Authoring of User Articles and Tutorials"
status: "Proposed" # Proposed | Accepted | Deprecated | Superseded
date: "2025-05-23"
tags: "documentation;templates;articles;tutorials;ai-guide;standards;authoring"
---

# ADR-020: Standardize Authoring of User Articles and Tutorials

## Context

User-facing documentation, specifically standalone articles and multi-part tutorial series, needs consistent structure, formatting, and quality to be effective. As AI assistants are increasingly involved in drafting such content, clear guidelines and templates are essential to ensure they can assist productively and adhere to project standards. Currently, there's a lack of formalized guidance and templates for these specific document types.

This ADR addresses the need to:

- Define standard structures for articles and tutorials.
- Provide AI assistants with clear instructions on how to help create these documents.
- Establish reusable templates to streamline the authoring process.

## Decision

We will establish a standardized approach for authoring user articles and multi-part tutorials by creating dedicated AI guides and document templates.

1.  **AI Guides:**

    - **`docs/ai-guides/contrib/articles/articles-writing-guide.md`**: An AI guide detailing the collaborative process and standards for creating standalone articles.
    - **`docs/ai-guides/contrib/tutorials/tutorials-writing-guide.md`**: An AI guide detailing the collaborative process and standards for creating multi-part tutorial series, including their `README.md` overview and individual parts.
    - These guides will instruct AI assistants on structure, content, tone, formatting, use of templates, and collaborative best practices, following the principles in `docs/ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`.

2.  **Document Templates:**

    - **`docs/ai-guides/contrib/articles/article.template.md`**: A template for standalone articles.
      - Key features: No YAML frontmatter, `# Guide: {{TITLE}}` format, `**(Primary Audience: ...)**` declaration, standard sections (Introduction, Body, optional Conclusion/Related Links).
    - **`docs/ai-guides/contrib/tutorials/tutorial-series-readme.template.md`**: A template for the main `README.md` of a tutorial series.
      - Key features: Series title, introduction, numbered list of parts with descriptions and links (`./{{PART_FILENAME}}.md`), concluding link to the first part. No YAML frontmatter.
    - **`docs/ai-guides/contrib/tutorials/tutorial-part.template.md`**: A template for individual parts of a tutorial series.
      - Key features: Numbered title (`# XX - {{TITLE}}`), introductory signposting paragraph (with "Up" link to `./`, "Previous" and "Next" links), top navigation table (with `◀`, `▶` arrows), `---` separator, main content sections, concluding signposting paragraph ("Next Steps"), and a bottom navigation table mirroring the top one. No YAML frontmatter.
    - These templates will be created following `docs/ai-guides/core/template-files-working-guide.md` and placed as siblings to their respective AI guides, as per `docs/adrs/adr-019-adopt-sibling-template-convention.md`.

3.  **Directory Structure for Tutorial Assets:**
    - The AI guide and templates specific to multi-part tutorials will be grouped in `docs/ai-guides/contrib/tutorials/`.

## Consequences

### Positive

- **Improved Consistency:** Articles and tutorials will have a more uniform structure and style, enhancing user experience.
- **Enhanced Quality:** Clear guidelines and templates will help maintain a higher standard of documentation.
- **Increased Efficiency:** Streamlines the authoring process for both humans and AI assistants.
- **Better AI Collaboration:** Provides AI assistants with explicit instructions, reducing guesswork and improving their contributions.
- **Clear Standards:** Formalizes previously unstated or inconsistently applied conventions.

### Negative

- **Initial Effort:** Requires time to create and refine the initial set of guides and templates.
- **Maintenance Overhead:** Guides and templates will need to be kept up-to-date as project conventions evolve.
- **Learning Curve:** Users and AI assistants will need to become familiar with these new assets and how to use them.

## Next Steps

- Finalize and approve the content of the AI guides and templates mentioned.
- Update any relevant higher-level documentation (e.g., main project `README.md` or `docs/README.md`) to reference these new standards if appropriate.
- Ensure AI assistants are primed with these new guides when tasked with article or tutorial creation.
