---
id: "articles-writing-guide"
title: "Guide: Collaboratively Authoring Standalone Articles"
usage: "Use this guide when assisting a user in collaboratively conceptualizing, drafting, structuring, and refining standalone technical articles, typically for the docs/articles/ directory."
tags: "articles;documentation;authoring;collaboration;user-focused"
---

# Guide: Collaboratively Authoring Standalone Articles

**(Primary Audience: AI Assistant (for assisting users in collaboratively conceptualizing, drafting, structuring, and refining standalone articles for the Vibe Tasking project).)**

## Introduction

This guide outlines how to effectively collaborate with a user to create standalone technical articles, typically located in the `docs/articles/` directory. Standalone articles are user-focused documents that explain concepts, offer guidance, or discuss best practices. Your role is to be an active partner in thinking through the article's purpose, structure, and content, ensuring it's clear, well-structured, informative, and adheres to project conventions.

Refer to `docs/reference/glossary.md` for the definition of an "Article." The standard template for articles is `ai-guides/contrib/articles/article.template.md`.

## Core Principles for Collaborative Article Authoring

1.  **User-Centric Focus:** The primary goal is to help the user articulate their knowledge and achieve their communication objectives for the article.
2.  **Leverage the Template:** Use `ai-guides/contrib/articles/article.template.md` as a starting point, but be flexible in adapting it to the user's specific needs for the article.
3.  **Iterative Development:** Article creation is a process of discussion, drafting, and refinement with the user.
4.  **Adherence to Key Conventions:** While the template provides detailed structure, ensure high-level project conventions (like title format and no YAML frontmatter) are followed.

## Phase 1: Collaborative Article Conceptualization

Your first step is to help the user clarify their vision for the article.

### Understanding the Article's Intent

Prompt the user with questions to understand the core purpose:

- "What is the main goal of this article? What should the reader know or be able to do after reading it?"
- "Who is the primary target audience for this article? (e.g., new users, experienced developers, non-technical stakeholders?)"
- "What are the 2-3 most critical pieces of information or key takeaways this article must convey?"
- "Does this article relate to or build upon any existing documents in the project?"
- "What working title do you have in mind for this article?"

### Discussing Structure and Scope

Based on the user's intent, discuss a potential structure:

- **Suggest High-Level Sections:** "Based on what you've said, perhaps we could structure it with sections like Introduction, [Key Concept 1], [Key Concept 2], and a Conclusion. Does that sound right?"
- **Define Scope:** "What specific topics should we ensure are covered? Are there any related topics we should intentionally exclude to keep this article focused?"
- **Consider Visuals or Examples:** "Would any diagrams, code snippets, or examples help illustrate the points in this article?"

## Phase 2: Leveraging the Article Template

Once a general concept is formed, introduce the standard article template.

1.  **Introduce the Template:**

    - "We can use the standard article template at `ai-guides/contrib/articles/article.template.md` as a starting point for the structure."
    - Briefly explain that the template provides placeholders for common sections like the title, primary audience, introduction, body sections, and optional conclusion/related links.
    - Refer to `ai-guides/core/template-files-working-guide.md` for general guidance on how you (the AI) should use templates.

2.  **Populate Initial Fields:**
    - Based on the conceptualization phase, help the user populate the initial fields of the template, such as the `{{ARTICLE_TITLE}}` and `{{AUDIENCE_DESCRIPTION}}`.

## Phase 3: Collaborative Content Drafting and Refinement

This is an iterative process of writing and refining content with the user.

1.  **Draft Section by Section:**

    - Work through the article section by section, using the populated template as a guide.
    - "Let's start with the Introduction. What are the main points we want to cover there?"
    - Offer to draft initial content for sections based on the user's input and your understanding.

2.  **Focus on Clarity and User Needs:**

    - **Articulate Ideas:** Help the user express their ideas clearly and concisely. For more detailed guidance on achieving conciseness and collaborating effectively on prose, refer to the [Guide: Collaborative Concise Prose Authoring](../prose-collaborative-authoring-guide.md).
    - **Ensure Understanding:** "Does this paragraph accurately capture what you mean here?"
    - **Suggest Enhancements:** "Perhaps an example here would be helpful?" or "Could we break this complex idea into a bulleted list?"

- **Recommend a Brevity Pass:** For articles with significant prose, suggest a dedicated 'brevity pass' after the initial draft (e.g., applying principles from 'Strunk & White'). This can help sharpen focus and improve readability, as observed to be effective (e.g., story s090).

3.  **Maintain Vibe Tasking Style:**
    - **Tone:** Encourage an informative, advisory, and user-focused tone.
    - **Linking:** Suggest links to other relevant Vibe Tasking documents where appropriate (e.g., glossary terms, related guides or articles).
    - **Formatting Reminders:** Gently guide the user on standard Markdown formatting (headings, lists, bold/italics, backticks for literals) to ensure readability and consistency, as outlined in the template's comments.

## Phase 4: Key Article Conventions (AI Checkpoints)

While the template covers most formatting, as an AI assistant, you **MUST** ensure these high-level conventions for standalone articles are met:

1.  **No YAML Frontmatter:** Confirm that no YAML frontmatter is added to the article.
2.  **Title Format:** Ensure the main title is a level 1 Markdown heading (`#`) and generally follows the `# Guide: Descriptive Article Title` format.
3.  **Primary Audience Declaration:** Verify the `**(Primary Audience: ...)**` declaration is present immediately after the title.

## Phase 5: Review and Finalization

1.  **Encourage User Review:** Once a complete draft is ready, prompt the user to review it thoroughly for accuracy, completeness, flow, and tone.
2.  **Incorporate Feedback:** Assist the user in making any necessary revisions based on their review.
3.  **Final Check:** Perform a final check against the key conventions before considering the article complete.

By following this collaborative approach, you can significantly aid users in producing high-quality, effective standalone articles that enrich the Vibe Tasking project's knowledge base.
