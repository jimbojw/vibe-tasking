# Guide: Designing and Using CONTEXT Documents

**Primary Audience:** Human User (to understand how to create and use `CONTEXT.md` files). The AI Assistant benefits from well-structured `CONTEXT.md` files provided by the user.

This guide explains the purpose, design, and usage of `CONTEXT.md` files (or similarly named initial context documents) within the Vibe Tasking project. These documents are intended to be provided to AI assistants at the beginning of a chat session to quickly orient them to essential project information.

## Purpose of CONTEXT Documents

The primary goal of a `CONTEXT.md` file is to save time and ensure AI assistants have foundational knowledge about the project from the outset. By directing the AI to read key introductory documents, we can:

- Reduce repetitive explanations.
- Ensure consistent understanding of core project concepts, structures, and conventions.
- Enable the AI to provide more relevant and accurate assistance more quickly.
- Streamline the onboarding process for the AI in each new session.

## Key Information to Include

A `CONTEXT.md` file should be concise and direct the AI to the most critical high-level documentation. Typically, this includes:

1.  **A Clear Welcome/Instruction:** A brief statement explaining the purpose of the `CONTEXT.md` file itself.
2.  **Pointers to Core Project Documentation:**
    - **Overall Project README:** This provides the broadest overview of the project, its goals, and its general structure (e.g., the main `README.md` in the repository root).
    - **Specific Convention Guides:** If the project has detailed guides for critical processes (like how user stories are documented), these should also be referenced (e.g., `docs/stories/README.md` for Vibe Tasking).
3.  **Expected Action:** Clearly state that the AI should read these documents before proceeding.

## Example: `CONTEXT.md` for Vibe Tasking

The `CONTEXT.md` file located in the root of the Vibe Tasking repository serves as a good example:

```markdown
# AI Assistant Onboarding Instructions for Vibe Tasking Project

Welcome! To effectively assist with tasks related to the Vibe Tasking project, it is crucial that you first familiarize yourself with its core documentation.

Please begin by carefully reading and understanding the content of the following two files in this repository:

1.  **Main Project Overview:**

    - **File:** `README.md`
    - **Purpose:** This file provides a high-level understanding of the Vibe Tasking framework, its goals, key features, and overall project structure.

2.  **Story Documentation Guide:**
    - **File:** `docs/stories/README.md`
    - **Purpose:** This guide details the specific conventions, structure, and methodology for how user stories (development tasks) are documented and managed within this project. Understanding this is essential for working with any tasks related to story creation, modification, or querying.

Reviewing these documents thoroughly at the start of our session will ensure you have the necessary foundational knowledge to provide relevant, accurate, and efficient assistance.

Thank you for reviewing this initial context.
```

_(Note: The content of the example above should reflect the actual `CONTEXT.md` file in the repository. If `CONTEXT.md` is updated, this guide may also need to be updated to reflect the changes.)_

## User Workflow: Initiating a Session with CONTEXT.md

To effectively use the `CONTEXT.md` file at the start of a new chat session with an AI assistant, follow these steps:

1.  **Prepare the AI's Initial Context:**

    - **Goal:** Ensure that only `CONTEXT.md` (or other specifically intended initial files) are in the AI's immediate context when the session begins. This prevents the AI from being distracted or confused by irrelevant open files.
    - **Be Aware of Assistant Behavior:** Different AI assistants handle initial context differently:
      - Some (like **Gemini Code Assist**) may automatically include all currently open editor tabs as context. **Action:** Close all unrelated tabs, leaving only `CONTEXT.md` open if necessary.
      - Others (like **Cursor AI**) might automatically use the content of the currently focused editor tab. **Action:** Check which file is focused and remove it from the AI's context panel if it's not `CONTEXT.md`.
      - Assistants like **Cline** typically only use files explicitly mentioned or provided by the user in the chat prompt.
      - For other assistants (e.g., Copilot), observe their behavior and manage the initial set of files provided to their context accordingly.
    - The key is to start with a clean slate, focused on `CONTEXT.md`.

2.  **Submit `CONTEXT.md` as the First Prompt:**

    - In the chat interface with your AI assistant, type `@CONTEXT.md` (or use autocompletion, e.g., `@CON` then Enter if available).
    - Send this as your very first message.
    - This action typically provides the AI with the full content of `CONTEXT.md` and signals that it should process this file first.

3.  **Allow the AI to Process:**
    - The AI should then read the instructions within `CONTEXT.md`.
    - As per the example `CONTEXT.md` for this project, it will then proceed to read the main project `README.md` and the `docs/stories/README.md` to gain foundational knowledge.

Following these steps helps ensure the AI assistant starts with the correct, focused understanding of the project, leading to more efficient and relevant collaboration.

## Best Practices for CONTEXT Documents

- **Keep it Short:** The `CONTEXT.md` itself should be brief. Its main job is to point to more comprehensive documents.
- **Use Clear File Paths:** Ensure the paths to the referenced documents are accurate and easy for the AI to locate.
- **Focus on Foundational Knowledge:** Only include references to documents that provide essential, high-level context. Avoid linking to highly specific or transient information.
- **Review Periodically:** As the project evolves, review the `CONTEXT.md` to ensure it still points to the most relevant and up-to-date introductory materials.

By implementing a well-structured `CONTEXT.md` file, we can significantly improve the efficiency and effectiveness of our interactions with AI assistants.
