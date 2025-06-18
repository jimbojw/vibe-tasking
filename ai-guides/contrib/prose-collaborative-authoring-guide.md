---
id: "prose-collaborative-authoring"
title: "Guide: Collaborative Concise Prose Authoring"
usage: "Use this guide when assisting a user with prose writing to ensure the output is consistent, concise, and incorporates iterative feedback effectively."
tags: "prose;writing;authoring;collaboration;conciseness;style;feedback"
---

# Guide: Collaborative Concise Prose Authoring

**(Primary Audience: AI Assistant (for drafting and refining prose collaboratively with a user, focusing on conciseness and iterative improvement).)**

## Introduction

This guide outlines key principles and practices for an AI assistant when collaboratively authoring prose—text meant primarily for human readers—with a user. It emphasizes achieving conciseness and effectively incorporating iterative feedback.

Following these guidelines will equip you to produce clear, direct, and user-aligned content. This enhances readability for end-users and establishes you as a more effective, adaptive writing partner.

## Core Principles for Collaborative Concise Prose

To effectively assist a user in producing clear, concise, and accurate prose, adhere to the following core principles.

### 1. Prioritize Conciseness and Clarity

Strive for direct language and eliminate unnecessary wordiness. Embrace the principle famously advocated by Strunk and White: 'omit needless words.' Your goal is to help the user convey their message clearly and efficiently.

- **Use Shorter Sentences:** Break down complex sentences into simpler ones.
- **Reduce Adverbs and Adjectives:** Only use modifiers that add essential meaning.
- **Trim Supporting Clauses:** If a clause doesn't add critical information, consider removing or rephrasing it.
- **Focus on Precision:** Choose words that convey exact meaning.
- **Example of Conciseness:**
  - **Less Concise:** "It is often the case that developers find that the Agile methodologies, which are designed to be flexible, offer a significant amount of value when they are applied to the somewhat unpredictable domain of AI development."
  - **More Concise:** "Agile methodologies, designed for flexibility, offer significant value in the unpredictable domain of AI development."

### 2. Embrace Iterative Refinement

Understand that the first draft is rarely the final one. Collaborative writing is an iterative process. Key aspects of this include:

- **Prefer Direct Edits to Files:** Once a course of action is clear (e.g., after an outline is approved or a specific change is discussed), directly apply your drafted prose or modifications to the relevant file. Users often find it easier to review concrete changes within the document context.
- **User-Controlled Approval:** Be aware that AI assistant UIs (such as Roo Code) typically provide users with granular control over how AI-suggested edits are integrated into files (e.g., requiring explicit approval or enabling auto-approve). Your direct edits will be subject to this user-managed workflow.
- **Interpret Rejections as Feedback:** If a user rejects an edit you have applied, treat this as significant feedback. It may signal a misunderstanding of the requirement or a preference for a different approach. In such cases, use tools like `ask_followup_question` to seek clarification before re-attempting the edit or proceeding with related changes.
- **View All Modifications as Iteration:** Both AI-applied edits and any subsequent modifications made directly by the user are integral parts of the iterative cycle that leads to the final, polished document.

### 3. Value and Learn from User Feedback

The user is the ultimate authority on the content and style. Pay close attention to their feedback, especially direct edits.

- **Direct Edits as Guidance:** When a user directly modifies your drafted text, these edits are strong indicators of their preferred style, tone, and terminology. Analyze these changes.
- **Adapt Your Style:** Proactively adjust your subsequent drafts to align with the user's demonstrated preferences. For instance, if the user consistently shortens your sentences or removes certain phrases, adopt that pattern.
- **Confirm Understanding:** If feedback is unclear, ask for clarification to ensure your revisions will meet their expectations.
- **Handle Potential Out-of-Band Edits Carefully:** Be aware that users might edit files directly while you are processing a request or waiting for a follow-up. Current AI UIs may not always notify you of these out-of-band changes. While re-reading a file before every modification is generally too aggressive, **if the user mentions they have made edits, or if they report that your changes have overwritten theirs, you MUST then re-read the file before applying further edits.** This ensures you are working with the absolute latest version and respecting all user contributions.

### 4. Ensure Clarity on Technical Terms and Style Conventions

Maintain consistency and accuracy in the use of technical terms and stylistic elements.

- **Confirm Terminology:** For specialized terms or jargon (e.g., `Scrum Master`, `Product Owner`), confirm the user's preferred capitalization and usage. Strive for consistency once established.
- **Use Quotation Marks Appropriately:** Reserve double quotation marks for literal quotations from other works or individuals. Avoid using them for emphasis or to highlight a term being defined (bolding or italics are often more appropriate for the latter, depending on context).

### 5. Utilize Outlines for Structure

Before drafting substantial prose sections, collaborate with the user on an outline.

- **Draft Outlines Directly in Documents:** When appropriate, draft the proposed outline directly into the target document using standard Markdown list formatting. This allows the user to see and approve the structure in context.
- **Use Meta-Direction (Optional):** You can include brief, _italicized notes_ within or alongside the in-document outline to indicate it's a placeholder (e.g., _Outline: Key points for this section..._ or _This outline will be expanded into full prose._).
- **Seek User Approval of In-Document Outline:** Always ensure the user reviews and approves the in-document outline before you proceed to replace it with detailed prose. This helps prevent extensive rewrites.

## Applying the Principles in Practice (Workflow & Examples)

These principles are best understood through a typical collaborative workflow. The creation of the "[Agile Reimagined: Applying Timeless Principles to AI-Centric Development](../../docs/articles/agile-ai-development.md)" article serves as a practical case study for this process.

A general workflow often includes these iterative steps:

1.  **Conceptualization and Outlining:**

    - **AI Assistant:** Helps the user clarify the document's purpose, audience, and key messages (as detailed in the "Guide: Collaboratively Designing and Authoring AI Guides").
    - **AI Assistant:** Proposes an initial outline for the document structure.
    - **User:** Reviews, refines, and approves the outline.
    - _Example:_ For the "Agile Reimagined" article, we first defined its goals and then collaboratively developed a section-by-section outline.

2.  **Iterative Drafting of Sections:**

    - **AI Assistant:** Drafts a specific section based on the approved outline, focusing on conciseness and clarity from the start.
    - **User:** Reviews the draft, providing feedback. This feedback can range from minor wording tweaks to requests for significant additions, clarifications, or stylistic changes. The user may also make direct edits to the content.
    - _Example:_ Initial drafts for sections like "Agile Fundamentals Revisited" were provided, and the user then suggested changes, such as splitting paragraphs, adding diagrams, and refining terminology.

3.  **Incorporating Feedback and Learning:**

    - **AI Assistant:** Carefully incorporates all user feedback and direct edits.
    - **AI Assistant:** Analyzes the nature of the edits (e.g., preference for shorter sentences, specific terminology, removal of adverbs) to adapt its style for subsequent drafts. This is key to "learning from user feedback."
    - _Example:_ User feedback on the initial Introduction for the "Agile Reimagined" article emphasized a more concise style, which was then applied to subsequent sections.

4.  **Handling Specific Elements (e.g., Diagrams, Technical Terms):**

    - **AI Assistant:** When elements like diagrams are needed, consults relevant guides (e.g., the "ASCII-Art Diagrams Authoring Guide") and proposes a draft.
    - **User:** Reviews and refines these specific elements.
    - **AI Assistant:** Confirms preferred usage for technical terms as they arise.
    - _Example:_ We collaboratively designed and refined both the Waterfall and Agile loop diagrams, ensuring they followed project guidelines and user preferences.

5.  **Review and Finalization:**
    - **AI Assistant:** Once all sections are drafted and iteratively refined, presents the complete document.
    - **User:** Conducts a final review.
    - **AI Assistant:** Makes any final adjustments.

This iterative loop of outlining, drafting, user feedback/editing, and AI adaptation, all while prioritizing conciseness and clarity, forms the core of effective collaborative prose authoring.

## Conclusion

By consistently applying the principles outlined in this guide—prioritizing conciseness, embracing iterative refinement, valuing user feedback, ensuring clarity on terms and style, and utilizing outlines—an AI assistant can significantly enhance its effectiveness as a collaborative prose author. The ultimate goal is to produce clear, user-focused documentation efficiently and to become an increasingly adaptive and insightful partner in the writing process. Adherence to these practices will lead to higher quality prose and a more productive user-AI collaboration.
