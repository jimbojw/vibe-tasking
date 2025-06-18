# Journal: s032 - ADR: Document Vibe Tasking as Code-Free and Establish ADR Directory

## 2025-05-19T16:28:33Z

- Story created during a planning session.
- The goal is to:
  1. Establish `docs/adrs/` for ADRs, including a `README.md` for that directory.
  2. Link `docs/adrs/README.md` from the main `docs/README.md`.
  3. Create an ADR in `docs/adrs/` (as `adr-001-code-free-framework.md`) formalizing the decision that Vibe Tasking is a code-free framework.
- Key rationale for the "code-free" ADR: This approach provides resilience against changes in natural language documentation (e.g., `CONTEXT.md`, `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`) and avoids the brittleness of hardcoded string parsing. This enhances maintainability and adaptability as instructional context evolves.
- User feedback incorporated to place ADRs in `docs/adrs/` instead of story artifacts.

## 2025-05-19T16:30:46Z

- Created `docs/adrs/README.md` to explain the purpose and structure of ADRs.
- Created `docs/adrs/adr-001-code-free-framework.md` documenting the "code-free" decision for Vibe Tasking.
- Updated `docs/README.md` to include a link to the new `docs/adrs/` directory and its README.
- All planned files for establishing the ADR directory and the initial ADR have been created.

## 2025-05-19T16:33:07Z

- Based on user feedback, the ADR convention was updated to include YAML frontmatter.
- Fields chosen: `id`, `title`, `status`, `date`, `tags`.
- Updated `docs/adrs/README.md` to document the new frontmatter convention.
- Updated `docs/adrs/adr-001-code-free-framework.md` to include the specified YAML frontmatter.

## 2025-05-19T16:33:57Z

- Removed superfluous "## Status" Markdown heading from `docs/adrs/adr-001-code-free-framework.md` as status is covered by YAML frontmatter.
- Updated `docs/adrs/README.md` to remove the recommendation for a separate Markdown status heading in the ADR body.

## 2025-05-19T16:39:34Z

- As an addendum to this story, created a new guide: `docs/guides/using-architecture-decision-records.md`.
- This guide explains how ADRs are used in this project and how they can be an optional add-on to Vibe Tasking.
- Updated `docs/guides/README.md` to link to the new guide.

## 2025-05-19T16:41:26Z

- Per user feedback, removed the direct link to `using-architecture-decision-records.md` from the list of example explanatory guides in `docs/guides/README.md`.
- Discussed adding a convention to `CONTEXT.md` to instruct AI assistants against auto-linking new guides in README files.

## 2025-05-19T16:43:01Z

- Added a "Note on Discoverability" to `docs/guides/README.md` to clarify that individual guides should not be linked directly from this README, as per user instruction.

## 2025-05-19T16:44:15Z

- Marked all Acceptance Criteria in `docs/stories/s032-adr-code-free-project/story.md` as complete ([x]).
