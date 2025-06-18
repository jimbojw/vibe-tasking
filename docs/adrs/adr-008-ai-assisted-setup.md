---
id: "adr-008"
title: "AI-Assisted Setup via INSTALLING.md Playbook"
status: "Superseded by [adr-022](adr-022-retire-ai-playbooks-concept.md)"
date: "2025-05-28"
tags: "installation;automation;ai-interaction;onboarding;process"
---

# ADR-008: AI-Assisted Setup via INSTALLING.md Playbook

## Context

Setting up the Vibe Tasking directory structure and initial files (like `CONTEXT.md`, `docs/ai-guides/core/stories/stories-structuring-guide.md`) in a user's project needs to be straightforward and minimize manual effort. The process should ideally leverage the capabilities of AI assistants, which are central to the Vibe Tasking workflow.

## Alternatives Considered

1.  **Manual Setup Guide for Users:** Provide detailed step-by-step instructions for users to manually create all directories and files.

    - _Pros:_ Gives users full control. No reliance on AI capabilities for setup.
    - _Cons:_ Prone to human error (typos, incorrect file placement). Tedious and time-consuming for users. Does not showcase or leverage AI collaboration from the outset.

2.  **Project Template/Scaffolding Tool:** Provide a downloadable template or a command-line tool that scaffolds the initial Vibe Tasking structure.

    - _Pros:_ Consistent setup. Reduces manual effort.
    - _Cons:_ Requires users to download and potentially run external tools or manage template files. Adds a layer of tooling outside the core AI interaction model. May require updates to the scaffolder if the core structure evolves.

3.  **Interactive AI Setup without Playbook:** Instruct users to ask their AI to create the structure piece by piece through a series of conversational prompts.
    - _Pros:_ Uses AI.
    - _Cons:_ Relies heavily on the AI's interpretation of multiple, potentially ambiguous prompts. Less reliable and repeatable than a structured playbook. Can be slow if many steps are involved.

## Decision

Vibe Tasking installation will be primarily **AI-assisted, guided by a dedicated `INSTALLING.md` file** (referred to as an "AI Playbook").

This `INSTALLING.md` file, located at the root of the Vibe Tasking framework distribution, contains explicit, step-by-step instructions _for an AI assistant_ to perform the initial setup. Users copy the content of `INSTALLING.md` and provide it as a prompt to their AI assistant within their project context. The AI then executes these instructions (creating directories, files, and initial content).

## Consequences

### Positive

- **Simplicity for Users:** Users only need to copy-paste the `INSTALLING.md` content to their AI.
- **Leverages AI Capabilities:** Utilizes the AI's ability to understand instructions and perform file system operations (if the AI assistant has such capabilities, like Cline).
- **Consistency and Reliability:** A detailed playbook for the AI reduces the chance of errors compared to manual setup or purely conversational AI setup.
- **Introduces AI Collaboration Early:** Demonstrates the Vibe Tasking model of user-AI partnership from the very beginning.
- **Maintainability of Setup Process:** The setup process is defined in a single, version-controlled Markdown file (`INSTALLING.md`). Updates to the setup process involve updating this one file.
- **Flexibility for AI:** While providing explicit steps, the natural language format allows different AI assistants to interpret and execute the setup according to their specific capabilities.

### Negative

- **Dependency on AI Capabilities:** Relies on the AI assistant being able to understand and execute the instructions in `INSTALLING.md`, including file creation/modification. Assistants without these capabilities would require the user to perform the steps manually, guided by the AI.
- **Clarity of `INSTALLING.md` is Crucial:** The playbook must be extremely clear and unambiguous to ensure correct execution by various AI assistants.
- **Initial `INSTALLING.md` Creation:** Requires careful crafting of this playbook document.

This decision prioritizes ease of use for end-users, leverages the core strength of AI assistants in the Vibe Tasking philosophy, and provides a maintainable and consistent setup mechanism.
