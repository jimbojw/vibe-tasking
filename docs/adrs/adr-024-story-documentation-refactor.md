---
id: "adr-024-story-documentation-refactor"
title: "Refactor Story Documentation into Dedicated AI Guides"
status: "Accepted"
date: "2025-05-30"
tags: "documentation;stories;ai-guides;refactor"
---

# ADR-024: Refactor Story Documentation into Dedicated AI Guides

## Context

Current Vibe Tasking documentation for story structure, planning, and working processes is primarily located in `docs/stories/README.md`. Some related guidance also existed in general AI guides at `docs/ai-guides/core/stories-planning-guide.md` and `docs/ai-guides/core/stories-working-guide.md`.

This distributed approach can make it harder for users and AI assistants to find comprehensive, focused information on story-related procedures. The `docs/stories/README.md` has become quite large and covers too many aspects beyond a simple overview of the stories directory.

## Alternatives Considered

### Alternative 1: Keep Current Structure

- **Description:** Maintain the existing documentation layout.
- **Pros:**
  - No immediate effort required.
- **Cons:**
  - Does not address the discoverability and focus issues.
  - `docs/stories/README.md` remains overly dense.

### Alternative 2: Enhance `docs/stories/README.md` with Better Internal Linking

- **Description:** Restructure `docs/stories/README.md` with a clearer table of contents and internal links, but keep all content within that file.
- **Pros:**
  - Some improvement in navigation within the single file.
- **Cons:**
  - File remains very large.
  - Does not align with the pattern of using `docs/ai-guides/` for detailed procedural instructions for AI.

## Decision

Refactor story-related documentation into a set of dedicated AI guides. These new guides will be located in a new subdirectory: `docs/ai-guides/core/stories/`.

The new guides will cover:

- Story Structuring (naming, core files, templates, artifacts)
- Story Planning (AI-assisted co-authoring, requirements, template adherence)
- Story Working (AI progression, user feedback, checkpoint management)

Content from the existing `docs/stories/README.md` will be migrated to these new guides. Content from the (now removed) `docs/ai-guides/core/stories-planning-guide.md` and `docs/ai-guides/core/stories-working-guide.md` has been reviewed, refined, and migrated into the new, more specifically scoped guides: `docs/ai-guides/core/stories/stories-planning-guide.md` and `docs/ai-guides/core/stories/stories-working-guide.md` respectively. The original top-level files have been removed.

The `docs/stories/README.md` will be updated to become a lightweight overview of the `docs/stories/` directory, primarily linking to the new, detailed guides.

Additionally, the core story template files (`story.template.md` and `journal.template.md`) will be moved from `docs/stories/` to `docs/ai-guides/core/stories/` to co-locate them with the guides that describe their usage.

## Consequences

### Positive

- Improved organization and discoverability of story-related documentation.
- Clearer, more focused guides for users and AI assistants on specific aspects of story management.
- Aligns story-related procedural guides with the established `docs/ai-guides/` structure.
- `docs/stories/README.md` becomes more concise and serves its primary purpose as an overview of the story directory.
- Story templates (`story.template.md`, `journal.template.md`) are co-located with their primary usage guides in `docs/ai-guides/core/stories/`, improving discoverability and adherence to the sibling template convention.

### Negative

- Requires effort to create new guides and migrate content.
- Requires updating cross-references in other documents to point to the new guide and template locations.
- Potential for temporary confusion if users are accustomed to the old structure, though this should be mitigated by clear linking.
