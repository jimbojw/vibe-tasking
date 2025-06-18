---
id: "s027-validate-installing-md-with-windsurf"
title: "Validate INSTALLING.md (New Install & Upgrade) with Windsurf"
status: "Closed"
priority: "Medium"
tags: "validation;testing;installing.md;windsurf;codeium;ai-capabilities"
resolution: "Obsolete"
---

# Story: s027 - Validate INSTALLING.md (New Install & Upgrade) with Windsurf

## Description

As a project maintainer, I want to validate both the "New Installation" and "Upgrade Existing Installation" paths of the `INSTALLING.md` AI playbook using Windsurf (Codeium Cascade), by following the steps outlined in the `docs/guides/validating-installing-md-playbook.md` guide (once created by story s022).

This validation will verify Windsurf's ability to:

1. Correctly self-assess and report its capabilities.
2. Perform a new installation of Vibe Tasking in a clean repository.
3. Perform an upgrade of an existing Vibe Tasking setup.

Testing the "merge" functionality for `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` during upgrade is out of scope for this story.
An artifact documenting these validation paths and behavioral findings will be created. Insights from this validation may also lead to suggestions for tweaking `INSTALLING.md` for better performance.

## Acceptance Criteria

- [ ] **Checkpoint: Initial Story Setup**
  - [ ] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is appended to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete before proceeding with substantive work Checkpoints.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'New Installation Path Validation (Windsurf)' Checkpoint.
- [ ] **Checkpoint: New Installation Path Validation (Windsurf)**
  - [ ] The `docs/guides/validating-installing-md-playbook.md` (from s022) is reviewed and used as the primary procedure for this validation.
  - [ ] A validation session is conducted with Windsurf using `INSTALLING.md` (Path 1) in a clean test repository.
  - [ ] Windsurf's capability self-assessment is verified as accurate (reporting full capabilities).
  - [ ] All steps for new installation (directory creation, file population, example story) are verified as per the validation guide.
  - [ ] **Process:** All ACs within this 'New Installation Path Validation (Windsurf)' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'New Installation Path Validation (Windsurf)' Checkpoint and any significant decisions made within it.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Upgrade Path Validation (Windsurf)**
  - [ ] A separate test repository is prepared with a standard existing Vibe Tasking setup.
  - [ ] A validation session is conducted with Windsurf using `INSTALLING.md` (Path 2) in this pre-configured repository.
  - [ ] Windsurf's capability self-assessment is verified.
  - [ ] Windsurf's handling of existing `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` and `CONTEXT.md` (excluding merge for `stories/README.md`) is verified as per the validation guide.
  - [ ] Windsurf's handling of optional directory creation (`docs/guides/`, `docs/reference/`) is verified.
  - [ ] **Process:** All ACs within this 'Upgrade Path Validation (Windsurf)' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Upgrade Path Validation (Windsurf)' Checkpoint and any significant decisions made within it.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Documentation and Review**
  - [ ] An artifact (e.g., `artifacts/windsurf-installing-md-validation.md`) is created, detailing observations and behavioral findings for both validation paths.
  - [ ] Based on observations, any potential tweaks to `INSTALLING.md` to improve its performance with Windsurf are identified and documented (either as part of the validation artifact or as a separate note/follow-up task).
  - [ ] User confirms the validation tests have been thoroughly executed and documented.
  - [ ] **Process:** All ACs within this 'Documentation and Review' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Documentation and Review' Checkpoint and any significant decisions made within it.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.
- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" (or other terminal status) and `resolution` field is set appropriately.
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
