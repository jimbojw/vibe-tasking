---
id: "s082-periodic-review-generating-guide"
title: "Design AI Guide for Generating Periodic Review Reports"
status: "To Do"
priority: "Medium"
tags: "ai-guide;design;reporting;git-history;contrib;documentation"
resolution: "Unresolved"
---

# Story: s082-periodic-review-generating-guide - Design AI Guide for Generating Periodic Review Reports

## Description

As a Vibe Tasking user/maintainer, I want an AI Guide that instructs an AI assistant on how to generate periodic review reports, so that project progress and activities can be summarized effectively.

This new `contrib` feature will involve:

- The AI assistant analyzing Git history (commit messages) over a specified period (e.g., "last week", "year to date").
- The AI assistant collecting data from progressed stories and their journals within that period.
- Generating a report, potentially based on a defined template.
- Storing the generated report in a standardized location (e.g., `docs/reports/`).
- Updating the main `README.md` to list "Periodic Review Reports" as a new `contrib` feature.

## Artifacts

- `ai-guides/contrib/reporting/periodic-review-generating-guide.md` (To be created: The new AI Guide)
- `artifacts/s082-report-template-design.md` (To be created: Design/template for the report structure)
- `docs/reports/` (To be created or confirmed as the storage location for generated reports)
- [`README.md`](../../../README.md) (To be updated to include this new contrib feature)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [ ] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [ ] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Design Report Content and Process**

  - [ ] Define the key data points to be included in a periodic review report (e.g., commit summaries, stories started/completed, key journal highlights).
  - [ ] Design a template or structure for the report in `artifacts/s082-report-template-design.md`.
  - [ ] Determine the process for an AI to gather the necessary data (e.g., Git commands, file parsing strategies for stories/journals). This should include considering:
    - Strategies for progressive summarization of large texts (e.g., summarizing `journal.md` files into terse blobs, potentially storing these intermediate summaries).
    - The potential use of the `new_task` tool for delegating summarization or data extraction sub-tasks that don't require full chat context.
  - [ ] Decide on a standardized location for storing generated reports (e.g., `docs/reports/`) and ensure this directory is created if it doesn't exist (perhaps with a `.gitignore` or `README.md`).
  - [ ] User reviews and approves the report design and data gathering process.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Draft Periodic Review Generating AI Guide**

  - [ ] **Process:** The [`ai-guides-collaborative-designing-guide.md`](../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) has been consulted.
  - [ ] Draft the `ai-guides/contrib/reporting/periodic-review-generating-guide.md`.
  - [ ] The guide instructs the AI on how to:
    - Prompt the user for the desired reporting period.
    - Execute commands to get Git log data for the period.
    - Identify and parse relevant story files and journal entries from the period.
    - Synthesize the collected data into the defined report template/structure.
    - Save the generated report to the designated location (e.g., `docs/reports/`).
  - [ ] User reviews the draft AI Guide.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Update Main README.md**

  - [ ] Add "Periodic Review Reports" to the "Optional Contributed Features" section in the main [`README.md`](../../../README.md).
  - [ ] Briefly describe its purpose and benefit, noting that an AI-Guide exists to instruct AIs on generating these reports.
  - [ ] User reviews and approves the `README.md` update.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Test the AI Guide (Implementation)**

  - [ ] User attempts to have an AI assistant generate a periodic review report for a sample period, strictly following the new `periodic-review-generating-guide.md`.
  - [ ] The generated report's accuracy, completeness, and adherence to the designed template are evaluated.
  - [ ] Any issues or ambiguities in the guide are identified and the guide is iteratively refined.
  - [ ] User confirms the guide is effective.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [ ] **Process:** AI performs an internal reflection on the completed story.
  - [ ] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [ ] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [ ] **Process:** AI invites the user to provide their own retrospective feedback.
  - [ ] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`.
  - [ ] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" and `resolution` field is set appropriately.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
