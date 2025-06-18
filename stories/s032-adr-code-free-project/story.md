---
id: "s032-adr-code-free-project"
title: "ADR: Document Vibe Tasking as Code-Free and Establish ADR Directory"
status: "Done"
priority: "Medium"
tags: "adr;design;documentation;core-concept;project-structure"
resolution: "Implemented"
---

# Story: s032 - ADR: Document Vibe Tasking as Code-Free and Establish ADR Directory

## Description

As a project maintainer, I want to:

1.  Establish a dedicated directory `docs/adrs/` for storing Architecture Decision Records (ADRs).
2.  Create an initial ADR within this new directory that formally documents the decision for Vibe Tasking to be a "code-free" framework, explaining its rationale and benefits.

The core decision for the ADR is that Vibe Tasking relies on structured Markdown files and natural language conventions rather than executable code for its core operations and AI interaction. This makes the framework resilient to changes in instructional documents (like `CONTEXT.md` or `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`) and avoids the brittleness associated with hardcoded strings or programmatic parsing of natural language.

## Artifacts

- [ADR Directory README](docs/adrs/README.md) (to be created)
- [ADR: Code-Free Framework](docs/adrs/adr-001-code-free-framework.md) (to be created)
- `docs/README.md` (to be updated)

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.
- [x] **Process:** An initial journal entry is added to journal.md for this story, noting work has commenced.
- [x] **Process:** The journal.md for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.
- [x] The `docs/adrs/` directory is created.
- [x] A `README.md` file is created in `docs/adrs/` explaining the purpose and structure of ADRs within the Vibe Tasking project.
- [x] The main `docs/README.md` file is updated to include a link to the `docs/adrs/README.md` guide.
- [x] An ADR document is created at `docs/adrs/adr-001-code-free-framework.md` documenting the "code-free" decision.
- [x] The ADR clearly states the decision to keep Vibe Tasking a code-free framework.
- [x] The ADR explains the primary rationale: resilience to changes in natural language documentation and avoidance of brittle, hardcoded parsing logic.
- [x] The ADR outlines the benefits, such as flexibility, easier maintenance of instructional context for AI, and reduced susceptibility to breakage from evolving natural language in key documents.
- [x] Alternative approaches (e.g., a script-based or tool-dependent framework) and why they were not chosen are briefly considered and documented in the ADR.
- [x] The ADR follows a standard ADR format (e.g., including sections for Status, Context, Decision, Consequences).
- [x] User confirms the new story structure (directory, `story.md`, `journal.md`) and its initial content accurately reflect the planned work and adhere to the Story Documentation Guide.
- [x] User confirms the `docs/adrs/` directory and its `README.md` are correctly set up.
- [x] User confirms the link in `docs/README.md` is correct.
- [x] User confirms the created ADR document (`docs/adrs/adr-001-code-free-framework.md`) is clear, complete, and accurately captures the decision and its rationale.
