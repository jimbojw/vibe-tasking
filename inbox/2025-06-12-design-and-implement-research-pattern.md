# Design and Implement a "Research" Pattern for Vibe Tasking

This is a proposal for a major new feature in the Vibe Tasking framework: a formal pattern for handling long-running, open-ended research questions. This will likely require at least two stories to implement.

## Phase 1: Refactor Journaling into a Standalone Component

1.  **Decouple `journal.md`:** Abstract the concept of a `journal.md` file from its current role as a story-only artifact. Define it as a general-purpose, append-only logging component.
2.  **Create a `journaling-guide.md`:** Author a new core AI-Guide that details the standard process for creating and appending timestamped entries to any `journal.md` file.
3.  **Update Story Guides:** Refactor the existing story-related guides (`stories-working-guide.md`, etc.) to depend on this new, standalone journaling guide.

## Phase 2: Implement the Research Pattern

1.  **Create `docs/research/` Directory:** Establish a new top-level directory for housing research logs.
2.  **Define Research Structure:**
    - Each research topic will get its own directory, prefixed with `rXXX-` (e.g., `docs/research/r001-overcoming-strong-priors/`).
    - Each directory will contain:
      - A main `research.md` file (name to be confirmed) to describe the research question, sub-questions, and links to relevant context. This file will have YAML frontmatter for discoverability.
      - A `journal.md` file for logging findings, experiments, and insights chronologically, following the new standalone journaling guide.

- An `artifacts/` directory, to be created on-demand when there are specific experimental scripts, data files, or other materials to store.

3.  **Create Research AI-Guides:** Create a new `ai-guides/contrib/research/` subdirectory with a full suite of guides to make the pattern operational for AI assistants:
    - `research-starting-guide.md`: For creating a new research log.
    - `research-discovering-guide.md`: For building an index of all research logs using `find`.
    - `research-logging-guide.md`: For handling user cues to log new findings to a specific research journal.
    - `research-closing-guide.md`: For reviewing, summarizing, and formally closing a research topic.
4.  **Author an ADR:** Create an Architecture Decision Record to formally document the introduction of this new "Research" pattern into the Vibe Tasking framework.

5.  **Update Onboarding Guide:** Make the new Research pattern discoverable by adding a reference to it in the primary user onboarding guide.
