---
id: "s051-design-story-dependency-tracking"
title: "Design Story Dependency Tracking in Frontmatter"
status: "To Do"
priority: "High"
tags: "research;design;story-format;dependencies;yaml;adr"
resolution: "Unresolved"
---

# Story: s051 - Design Story Dependency Tracking in Frontmatter

## Description

**User Story:** As a Vibe Tasking user, I want to formally define and track dependencies between stories directly in their YAML frontmatter, so that I can easily query which stories are blocked by others and which stories are unblocked upon a story's completion, improving project planning and visibility.

**Details:** This story involves researching, designing, and potentially implementing a standardized way to declare story dependencies within the `story.md` YAML frontmatter. Currently, dependencies are often noted informally in the story's "Details" or "Acceptance Criteria" sections. Formalizing this in the frontmatter will enable better tooling and automated analysis.

The research should consider:

- **Syntax:** How to represent dependencies.
  - Standard YAML practice suggests using an array for a list of values associated with a single key, e.g., `depends_on: ["s001", "s002"]`.
  - The research should confirm that duplicate keys (e.g., multiple `depends_on:` lines) are not suitable for accumulating a list of dependencies in YAML, as parsers typically only honor the last instance of a duplicate key.
  - Example of preferred array notation: `depends_on: ["s001", "s002"]` (meaning this story requires s001 and s002 to be complete).
  - Example for `blocks`: `blocks: ["s005", "s006"]` (meaning this story, when complete, unblocks s005 and s006 - potentially a derived or explicitly stated relationship).
- **Types of Dependencies:** While various types exist (e.g., "blocks", "is_blocked_by", "relates_to"), the initial focus might be on a "depends_on" relationship.
- **Interaction with `status: Blocked`:** The proposed dependency mechanism should align with or potentially supersede the current informal practice of setting `status: "Blocked"` and `resolution: "Pending completion of sNNN"`. For instance, if a story `sXYZ` has `depends_on: ["sABC"]`, it implies `sXYZ` is blocked if `sABC` is not "Done" or "Closed". The system should ideally make the `status: "Blocked"` more programmatically determinable or manageable through these dependency fields.
- **Queryability:** How these fields (using array notation) would be queried.
  - This includes developing robust `grep` / regex patterns for finding specific items within YAML arrays.
  - It should also consider and compare the ease/reliability of using `grep` versus YAML-aware CLI tools (e.g., `yq`) or simple scripts for more complex dependency queries (e.g., "find all stories that depend on s001 AND s002").
  - The goal is to find practical ways to query, for example, all stories blocked by a specific story, or all stories that unblock others.
- **Pros and Cons:**
  - Pros: Improved visibility of task relationships, better planning, potential for automated dependency graph generation, clearer indication of what's unblocked, more systematic handling of "Blocked" status.
  - Cons: Increased frontmatter complexity, potential for circular dependencies if not managed, effort to backport to existing stories.
- **Impact on `ai-guides/core/stories/stories-structuring-guide.md`:** The story documentation guide will need updating if a new field is adopted.

The outcome of this story will be a decision on whether and how to implement this. If the decision is to proceed, an ADR will be created, and `ai-guides/core/stories/stories-structuring-guide.md` will be updated. A follow-up decision on backporting this to existing "To Do" stories will also be made.

## Artifacts

- This `story.md` file.
- Research notes on dependency tracking options.
- Potentially an ADR (if a change is adopted).
- Updated `ai-guides/core/stories/stories-structuring-guide.md` (if a change is adopted).

## Acceptance Criteria

- [ ] **Checkpoint: Initial Story Setup**
  - [ ] **Process:** Story status is updated to "In Progress".
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms ACs.
  - [ ] A plan for researching dependency representation options is defined.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Research and Option Analysis' Checkpoint.
- [ ] **Checkpoint: Research and Option Analysis**
  - [ ] Different syntaxes for representing `depends_on` (and potentially `blocks` or `relates_to`) in YAML frontmatter are researched and documented.
  - [ ] The interaction between proposed dependency fields and the existing `status: "Blocked"` / `resolution: "Pending..."` pattern is analyzed, aiming for a more integrated solution.
  - [ ] Examples of how these new fields could be queried using CLI tools are developed (e.g., to find stories blocked by `sNNN`, or stories that `sNNN` depends on).
  - [ ] Pros and cons of adopting formal dependency tracking are analyzed and documented.
  - [ ] A recommendation for a specific syntax (or a decision not to proceed) is formulated.
  - [ ] User reviews the research, analysis, and recommendation.
  - [ ] **Process:** All ACs in this Checkpoint complete, journal updated, user approval to proceed.
- [ ] **Checkpoint: Decision & ADR (If Applicable)**
  - [ ] A final decision is made on whether to implement formal dependency tracking in frontmatter.
  - [ ] If the decision is to proceed:
    - [ ] An Architecture Decision Record (ADR) is drafted, detailing the chosen syntax, its interaction with story statuses (especially "Blocked"), rationale, and implications.
    - [ ] User reviews and approves the ADR.
    - [ ] The ADR is finalized and saved in `docs/adrs/`.
  - [ ] If the decision is not to proceed, the rationale is documented in this story's journal.
  - [ ] **Process:** All ACs in this Checkpoint complete, journal updated, user approval to proceed.
- [ ] **Checkpoint: Update Core Documentation (If Applicable)**
  - [ ] If a new dependency field is adopted, `ai-guides/core/stories/stories-structuring-guide.md` (the canonical source for story structure) is updated to include the new field(s) in the YAML frontmatter specification, along with examples, guidance on its use with `status: "Blocked"`, and query guidance.
  - [ ] `ai-guides/core/stories/stories-planning-guide.md` is reviewed and updated if it contains or references frontmatter examples that would become outdated.
  - [ ] A general review of `docs/articles/` (especially those in `docs/articles/onboarding/`) is conducted to identify and update any illustrative frontmatter examples that might conflict with the new standard.
  - [ ] User reviews and approves all documentation changes.
  - [ ] **Process:** All ACs in this Checkpoint complete, journal updated, user approval to proceed.
- [ ] **Checkpoint: Backporting Strategy & Execution (If Applicable)**
  - [ ] A decision is made on whether to backport the new dependency field(s) to existing open "To Do" and "Blocked" stories.
  - [ ] If backporting is approved:
    - [ ] A list of stories requiring updates is identified.
    - [ ] The new dependency field(s) are added to the identified stories.
    - [ ] User reviews the backported changes.
  - [ ] If backporting is not approved, the rationale is documented in the journal.
  - [ ] **Process:** All ACs in this Checkpoint complete, journal updated, user approval to proceed.
- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and ACs are complete.
  - [ ] **Process:** Story status updated to "Done", resolution set (e.g., "Implemented" or "Decision Documented").
  - [ ] **Process:** All ACs in this Checkpoint complete, journal updated.
