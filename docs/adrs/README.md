# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) for the Vibe Tasking project.

## What is an ADR?

An ADR is a short document that captures a significant architectural decision made along with its context and consequences. ADRs are immutable; once recorded, they are not changed, only superseded by a new ADR if a decision is revisited.

## Purpose

- **Documentation:** To record key architectural decisions and the reasoning behind them.
- **Communication:** To share these decisions with the team and stakeholders.
- **Onboarding:** To help new team members understand the architectural evolution of the project.
- **Consistency:** To ensure that decisions are made consciously and consistently.

## Format

Each ADR **must** begin with a YAML frontmatter block for metadata, followed by the Markdown content. This aligns with the Vibe Tasking story format and enhances queryability. ADR filenames are typically numbered sequentially and include a brief descriptive slug (e.g., `adr-001-code-free-framework.md`).

For the standard structure and content of an ADR, please refer to the official [ADR Template (`ai-guides/contrib/adrs/adr.template.md`)](../../ai-guides/contrib/adrs/adr.template.md). This template should be used as the starting point for all new ADRs.

**Key Formatting Notes for YAML Frontmatter:**

- Each field and its value must be on a single line.
- All string values within the frontmatter (for `id`, `title`, `status`, `tags`) should be enclosed in double quotes to ensure consistent parsing.
- The `date` should be in `YYYY-MM-DD` format.
- `tags` should be a semicolon-separated list.

**Required Content Sections:**

- **Context**
- **Alternatives Considered**
- **Decision**
- **Consequences**

The optional sections should be used as needed to provide comprehensive documentation for more complex decisions.

## Authoring New ADRs

To ensure consistency and leverage AI collaboration effectively, new ADRs should be created using the [ADR Template (`ai-guides/contrib/adrs/adr.template.md`)](../../ai-guides/contrib/adrs/adr.template.md). AI assistants can help you through this process, guided by the instructions in [Collaboratively Writing Architecture Decision Records (`ai-guides/contrib/adrs/adrs-writing-guide.md`)](../../ai-guides/contrib/adrs/adrs-writing-guide.md). This formalized approach, established by [ADR-021](./adr-021-formalize-adr-authoring-process.md), helps maintain quality and clarity in our architectural documentation.

## When to Write an ADR

Consider writing an ADR for:

- Decisions that have a significant impact on the architecture.
- Decisions that are not obvious or have non-trivial trade-offs.
- Decisions that are likely to be questioned or revisited in the future.
- Decisions that introduce new technologies, patterns, or significant changes to existing ones.

By maintaining a log of ADRs, we create a valuable historical record of our architectural journey.
