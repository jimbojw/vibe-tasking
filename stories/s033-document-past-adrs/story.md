---
id: "s033-document-past-adrs"
title: "Document Past Architectural Decisions as ADRs"
status: "Done"
priority: "Medium"
tags: "adr;documentation;research;design;project-history"
resolution: "Implemented"
---

# Story: s033 - Document Past Architectural Decisions as ADRs

## Description

As a project maintainer, I want to identify and document significant past architectural decisions for the Vibe Tasking framework as ADRs. This will ensure that the rationale and consequences of these foundational choices are explicitly recorded, improving project understanding and maintainability.

This story involves reviewing previously made architectural choices, selecting a subset for documentation, and then drafting the corresponding ADR files.

The following potential past decisions have been identified for consideration (derived from review of `README.md` and `docs/onboarding/` documentation, excluding the already documented `adr-001-code-free-framework.md`):

1.  **ADR-MD-Syntax:** Using Markdown as the primary syntax.
2.  **ADR-Repo-Integrated:** Framework being repository-integrated.
3.  **ADR-Core-Dirs:** The standard Vibe Tasking directory structure (e.g., `docs/stories/`, `CONTEXT.md`).
4.  **ADR-Story-Structure:** The `story.md`/`journal.md`/`artifacts/` structure per story.
5.  **ADR-Story-Frontmatter:** Using YAML frontmatter and specific fields for stories.
6.  **ADR-Agnostic-Framework:** Designing Vibe Tasking to be OS, IDE, VCS, and AI model agnostic.
7.  **ADR-AI-Assisted-Setup:** The AI-driven installation process via `INSTALLING.md`.
8.  **ADR-AI-Assisted-Planning:** The collaborative AI-driven story planning process.
9.  **ADR-Context-MD-Usage:** Employing a root `CONTEXT.md` for AI onboarding.
10. **ADR-Story-Readme-SOT:** Designating `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` as the single source of truth for story structure.
11. **ADR-Journaling-Practice:** The practice of maintaining `journal.md` for context and history.
12. **ADR-Onboarding-Process:** Providing a structured onboarding guide for the Vibe Tasking framework itself.
13. **ADR-Process-ACs:** Including standard "Process" acceptance criteria in stories.

## Artifacts

- This `story.md` and `journal.md`.
- New ADR files to be created in `docs/adrs/`.
- (Potentially) Updates to `docs/adrs/README.md` if any conventions are refined.

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
- [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
- [x] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.
- [x] The list of potential past architectural decisions (now included in this story's Description) is reviewed.
- [x] A specific subset of these past decisions is selected for documentation as ADRs within the scope of this story.
- [x] For each selected decision:
  - [x] A new ADR file is created in the `docs/adrs/` directory (e.g., `adr-002-decision-name.md`).
  - [x] The ADR includes appropriate YAML frontmatter (id, title, status, date, tags).
  - [x] The ADR content clearly outlines the Context, Decision, and Consequences.
- [x] User confirms the selection of ADRs to be created.
- [x] User confirms the content and format of each newly created ADR.
- [x] User confirms the new story structure (directory, `story.md`, `journal.md`) and its initial content accurately reflect the planned work and adhere to the Story Documentation Guide.
