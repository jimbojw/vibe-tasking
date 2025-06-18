# Using Architecture Decision Records (ADRs) with Vibe Tasking

While Architecture Decision Records (ADRs) are not a mandatory component of the core Vibe Tasking framework, they can be a valuable complementary practice for projects that wish to formally document significant architectural choices. This guide explains how ADRs are utilized within _this specific Vibe Tasking project_ and how you might consider using them.

## What are ADRs?

An Architecture Decision Record (ADR) is a short document that captures an important architectural decision, its rationale, and its consequences. The goal is to create a historical log of key design choices, making it easier for the team (including AI assistants and future contributors) to understand why the system is built the way it is.

For a detailed explanation of the ADR format and conventions used in this project, please see the [ADRs Directory README](../../adrs/README.md). To help create new ADRs consistently, we use a standard [ADR Template (`ai-guides/contrib/adrs/adr.template.md`)](../../ai-guides/adr.template.md). For guidance on collaboratively authoring ADRs with AI assistance, refer to the [Guide for Writing ADRs (`ai-guides/contrib/adrs/adrs-writing-guide.md`)](../../ai-guides/adrs-writing-guide.md).

## ADRs as an Optional "Add-on" to Vibe Tasking

Vibe Tasking itself is designed to be lightweight and code-free, focusing on Markdown-based stories and context files. It functions perfectly well without a formal ADR process.

However, for projects that grow in complexity or involve multiple contributors, explicitly documenting architectural decisions can provide significant benefits:

- **Clarity and Shared Understanding:** Ensures everyone understands the reasons behind major design choices.
- **Onboarding:** Helps new team members get up to speed on the project's architecture.
- **Consistency:** Promotes more deliberate and consistent decision-making.
- **Avoiding "Oral Tradition":** Prevents critical architectural knowledge from being lost if team members leave.

In this project, we use the `docs/adrs/` directory to store our ADRs. This is a convention we've adopted, not a requirement imposed by Vibe Tasking.

## When Might You Use ADRs in Your Vibe Tasking Project?

Consider adopting ADRs if:

- Your project involves non-trivial architectural decisions (e.g., choosing a specific technology, a structural pattern for your documentation, a key integration point).
- You anticipate needing to explain these decisions to others in the future.
- You want to maintain a clear record of why certain paths were chosen over alternatives.

## How ADRs Complement Vibe Tasking Stories

- **Stories Drive Work:** Vibe Tasking stories (`story.md`) define tasks, including those that might lead to an architectural decision (e.g., a research story to investigate options, or a design story to propose a solution).
- **ADRs Document Decisions:** If a story results in a significant architectural decision, that decision can be formally captured in an ADR. The story itself might then link to the ADR as an artifact.

For example, story `s032-adr-code-free-project` in this repository led to the creation of `adr-001-code-free-framework.md`, which documents why Vibe Tasking itself is a code-free framework.

## Conclusion

ADRs are a useful tool for software and documentation architecture. While not a core part of Vibe Tasking, they can be seamlessly integrated as an optional practice to enhance project clarity and maintain a record of important design choices. If you choose to use them, establishing a clear location (like `docs/adrs/`) and a consistent format (see our [ADRs Directory README](../../adrs/README.md)) is recommended.
