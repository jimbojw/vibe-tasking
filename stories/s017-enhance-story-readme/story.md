---
id: "s017-enhance-story-readme"
title: "Enhance Story README with Process ACs and Planning Guide Insights"
status: "Done"
priority: "Medium"
tags: "documentation;stories;readme;best-practice;acceptance-criteria;planning"
---

# Story: s017 - Enhance Story README with Process ACs and Planning Guide Insights

## Description

This story aims to update the canonical `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` to further improve the Vibe Tasking story creation and execution process. The changes will include:

1.  Codifying standard process steps (updating status to "In Progress", initial journaling, ongoing journaling) as leading Acceptance Criteria for all new stories.
2.  Reviewing the guidance on Acceptance Criteria for Research, Design, and Implementation stories currently in `docs/guides/planning-guide.md` and incorporating relevant parts into `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` to make it a more complete, standalone reference.
3.  Updating the example journal entry in `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` to use a full timestamp (date and time) to encourage more precise logging.

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter immediately upon starting work on this story.
- [x] **Process:** An initial journal entry is added to journal.md for this story, noting that work has commenced.
- [x] **Process:** The journal.md for this story is kept up-to-date with entries detailing progress, decisions, and any issues encountered throughout the execution of this story.
- [x] The "Story Directory Structure" section in docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md, under the "5. Acceptance Criteria" subsection, is updated to recommend including standard process-related ACs (updating status, initial journaling, ongoing journaling) as the _first_ items in any new story's AC list.
- [x] The "Story Directory Structure" section in docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md, under the "5. Acceptance Criteria" subsection, is enhanced with a general note advising that Acceptance Criteria should be tailored to the nature of the story (e.g., Research, Design, Implementation) and briefly mentioning the typical focus of ACs for such types (e.g., documented findings for Research, specifications for Design, working features for Implementation). This note will not directly link to docs/guides/planning-guide.md.
- [x] The example initial journal entry within docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md (under the `journal.md` description) is updated to show a full timestamp including both date and time (e.g., YYYY-MM-DDTHH:MM:SSZ or similar ISO 8601 format).
- [x] The `INSTALLING.md` file is updated to reflect all changes made to `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` by re-synchronizing its embedded "CONTENT FOR docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md" section, following the procedure in `docs/guides/updating-installing-md-guide.md`.
- [x] User confirms satisfaction with all updates to docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md and INSTALLING.md.
- [x] This story (s017) is documented with its story.md and journal.md (reflecting completion of all above ACs), and then its status is marked as "Done" in the frontmatter.
