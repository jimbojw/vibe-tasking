# Content Migration Plan & New docs/stories/README.md Content

## I. Content to be moved from `docs/stories/README.md`:

1.  **To `stories-structuring-guide.md`:**

    - Section: "Story Directory Naming Convention" (lines 5-15 of original `docs/stories/README.md`)
    - Section: "Story Directory Structure" (lines 17-90 of original `docs/stories/README.md`) - Details `story.md` (frontmatter, title, description, artifacts, ACs/Checkpoints), `journal.md`, and `artifacts/` directory.
    - Section: "Core Story Templates" (lines 129-137 of original `docs/stories/README.md`)
    - Section: "Flexibility" (lines 138-140 of original `docs/stories/README.md`)

2.  **To `stories-planning-guide.md` (or a potential new "Story Querying Guide"):**
    - Section: "Command-Line Querying Stories" (lines 91-127 of original `docs/stories/README.md`)

## II. Proposed Content for new lightweight `docs/stories/README.md`:

```markdown
# Vibe Tasking - Stories

This directory (`docs/stories`) is where user stories and their associated artifacts for the Vibe Tasking project itself are documented. It also serves as a living example of how the Vibe Tasking framework can be used.

## Understanding Vibe Tasking Stories

Detailed guidance on how Vibe Tasking stories are structured, planned, and worked on can be found in the following dedicated AI Guides:

- **Structuring Stories:** For details on story directory naming, `story.md` and `journal.md` file structure, YAML frontmatter, acceptance criteria, and the use of `story.template.md` and `journal.template.md`, please refer to the **[Story Structuring Guide](../ai-guides/vibe-tasking/stories/stories-structuring-guide.md)**.
- **Planning Stories:** For guidance on how AI assistants help plan and create new stories, including identifying story types and defining acceptance criteria, see the **[Story Planning Guide](../ai-guides/vibe-tasking/stories/stories-planning-guide.md)**.
- **Working on Stories:** For protocols on how AI assistants progress through stories, manage checkpoints, and update story status, consult the **[Story Working Guide](../ai-guides/vibe-tasking/stories/stories-working-guide.md)**.

## Core Story Templates

The core templates for creating new stories will be co-located with the story guides under `docs/ai-guides/vibe-tasking/stories/`:

- [`story.template.md`](../ai-guides/vibe-tasking/stories/story.template.md)
- [`journal.template.md`](../ai-guides/vibe-tasking/stories/journal.template.md)

Refer to the **[Story Structuring Guide](../ai-guides/vibe-tasking/stories/stories-structuring-guide.md)** for detailed instructions on using these templates.
```
