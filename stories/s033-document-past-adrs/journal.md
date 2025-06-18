# Journal: s033 - Document Past Architectural Decisions as ADRs

## 2025-05-19T16:52:05Z

- Story created to identify and document past architectural decisions for the Vibe Tasking framework.
- **Type:** Research & Design.
- **Goal:** Improve project understanding and maintainability by explicitly recording the rationale and consequences of foundational choices.
- Initial research phase involved reviewing `README.md` and `docs/onboarding/` documentation.
- A list of potential past architectural decisions was identified. This list has now been moved into the Description section of `story.md` for this story (`s033-document-past-adrs`).
- Next steps will involve selecting a subset of these decisions from the `story.md` to document as ADRs within this story.

## 2025-05-19T16:55:21Z

- User initiated work on this story.
- Updated status to "In Progress" in `story.md` frontmatter.
- Checked off the first Acceptance Criterion in `story.md`.
- Awaiting user review of the potential ADR list in `story.md` and suggestions for changes/selection.

## 2025-05-19T16:59:05Z

- Based on user feedback, the following ADRs were selected and drafted:
  - `docs/adrs/adr-002-markdown-syntax.md`: Documenting the decision to use Markdown as the primary syntax. Rationale: AI and human readability.
  - `docs/adrs/adr-003-yaml-frontmatter.md`: Documenting the decision to use YAML frontmatter for structured metadata in stories and ADRs. Rationale: More structured than pure Markdown, AI/human readable, CLI queryable.
- The AC "The list of potential past architectural decisions (now included in this story's Description) is reviewed." is now considered complete.
- The AC "A specific subset of these past decisions is selected for documentation as ADRs within the scope of this story." is now considered complete.

## 2025-05-19T17:08:57Z

- Updated `docs/adrs/README.md` to include a comprehensive example template for ADRs.
- The new template makes "Alternatives Considered" a required section and lists "Assumptions," "Constraints," "Risks," "Further Discussion / Open Issues," and "References" as optional sections.
- This change standardizes and enhances the ADR format for the project.

## 2025-05-19T17:12:07Z

- Retrofitted existing ADRs to align with the updated template:
  - Added "Alternatives Considered" section to `docs/adrs/adr-001-code-free-framework.md`.
  - Added "Alternatives Considered" section to `docs/adrs/adr-002-markdown-syntax.md`.
  - Added "Alternatives Considered" section to `docs/adrs/adr-003-yaml-frontmatter.md`.
- No optional sections were deemed immediately necessary for these existing ADRs during this pass.

## 2025-05-19T17:18:53Z

- Drafted `docs/adrs/adr-004-repository-integrated.md` to document the decision for Vibe Tasking to be a repository-integrated framework.

## 2025-05-19T17:24:16Z

- Drafted `docs/adrs/adr-005-core-directory-structure.md` to document the decision on the standard Vibe Tasking directory structure.

## 2025-05-19T17:25:32Z

- Drafted `docs/adrs/adr-006-story-file-structure.md` to document the decision on the `story.md`/`journal.md`/`artifacts/` structure per story.

## 2025-05-19T17:27:02Z

- Drafted `docs/adrs/adr-007-agnostic-framework-design.md` to document the decision for Vibe Tasking to be broadly agnostic (OS, IDE, VCS, AI).

## 2025-05-19T17:27:43Z

- Drafted `docs/adrs/adr-008-ai-assisted-setup.md` to document the decision for an AI-assisted setup process via `INSTALLING.md`.

## 2025-05-19T17:28:25Z

- Drafted `docs/adrs/adr-009-ai-assisted-planning.md` to document the decision for a collaborative, AI-assisted story planning process.

## 2025-05-19T17:29:08Z

- Drafted `docs/adrs/adr-010-root-context-md.md` to document the decision to use a root `CONTEXT.md` file for AI onboarding.

## 2025-05-19T17:29:50Z

- Drafted `docs/adrs/adr-011-story-readme-sot.md` to document the decision for `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` to be the Single Source of Truth for story structure.

## 2025-05-19T17:30:33Z

- Drafted `docs/adrs/adr-012-journaling-practice.md` to document the decision to use `journal.md` for story context and history.

## 2025-05-19T17:31:21Z

- Drafted `docs/adrs/adr-013-structured-onboarding.md` to document the decision to provide a structured onboarding guide for the Vibe Tasking framework.

## 2025-05-19T17:32:02Z

- Drafted `docs/adrs/adr-014-process-acceptance-criteria.md` to document the decision to include standard "Process" ACs in stories.
- This completes the drafting of all identified ADRs for this story.

## 2025-05-19T17:32:43Z

- All Acceptance Criteria in `story.md` have been marked as complete.
- Story status updated to "Done" and resolution to "Implemented" in `story.md`.
- This story is now complete.
