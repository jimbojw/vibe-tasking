---
id: "s043-research-zip-installer-path"
title: "Research Alternative Zip-Based Installation Path"
status: "Closed"
priority: "Medium"
tags: "research;installation;packaging;automation;playbook"
resolution: "Superseded by s046"
---

# Story: s043 - Research Alternative Zip-Based Installation Path

## Description

**User Story:** As a Vibe Tasking maintainer, I want to research a method for creating a distributable zip archive (`vibe-tasking.zip`) via an AI playbook (`make-installer-guide.md`), so that the Vibe Tasking installation process becomes more robust, easier to maintain, and can include a comprehensive set of initial project files and guides.

**Details:**
The current `INSTALLING.md` approach, which embeds file content directly, faces challenges:

1.  Updating embedded content (especially `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`) via `docs/ai-guides/updating-installing-md-guide.md` is becoming fragile.
2.  It omits other valuable guides (e.g., `docs/ai-guides/vibe-tasking/stories/stories-planning-guide.md`, `docs/ai-guides/vibe-tasking/stories/stories-working-guide.md`) that would benefit new users.

This research story aims to:

- Define the contents and structure of an ideal `vibe-tasking.zip` distributable. This zip will include a new, leaner `INSTALLING.md` that relies on the presence of other files within the unzipped package rather than embedding them.
- Experiment with and document a reliable procedure for an AI assistant (using tools like `execute_command` or by generating temporary shell scripts) to create this `vibe-tasking.zip`.
- Codify this procedure into a new AI playbook, tentatively named `make-installer-guide.md`.

The ultimate goal is to produce a well-documented research outcome, including a draft of `make-installer-guide.md`, that can inform a subsequent Design or Implementation story.

## Artifacts

- This `story.md` file.
- `journal.md` for this story.
- (To be created) `artifacts/zip-content-specification.md` - Document defining the contents and structure of `vibe-tasking.zip`.
- (To be created) `artifacts/zip-creation-experiments.md` - Log of experiments, steps taken, and outcomes in creating the prototype zip.
- (To be created) `artifacts/draft-make-installer-guide.md` - The draft AI playbook.
- (To be created) `artifacts/prototype-vibe-tasking.zip` - An example of the target zip file.

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup and Confirmation**

  - [x] **Process:** User confirms the new story structure (directory, `story.md`, `journal.md`) and its initial content (title, description, proposed Checkpoints and ACs) accurately reflect the planned work and adhere to the Story Documentation Guide.

  - [x] **Checkpoint: Define Target `vibe-tasking.zip` Contents and Structure**

  - [x] **Research:** Identify essential files for a minimal Vibe Tasking setup (e.g., root `CONTEXT.md`, `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`, a new non-embedding `INSTALLING.md`).
  - [x] **Research & Specification:** Specify that the zip will include a `docs/ai-guides/` directory structure. This will contain `docs/ai-guides/README.md` (from VT-Core) and a `docs/ai-guides/vibe-tasking/` subdirectory. The `vibe-tasking/` subdirectory will include its own `README.md` (from VT-Core `docs/ai-guides/vibe-tasking/README.md`) and all other files from VT-Core `docs/ai-guides/vibe-tasking/`, as per `adr-017-documentation-refactor.md`.
  - [x] **Research & Specification:** Specify that the `vibe-tasking.zip` will have a single top-level directory (e.g., `vibe-tasking/`) containing a `docs/` subdirectory, which in turn houses the `ai-guides/` structure (e.g., `vibe-tasking/docs/ai-guides/README.md`). Also, clarify that the zip will include a root `CONTEXT.md`, `README.md` (for the zip package), `LICENSE`, `CONTRIBUTING.md` (template), and a new, non-embedding `INSTALLING.md` (AI-Playbook) at the top level of the zip's content (e.g., `vibe-tasking/CONTEXT.md`). The `docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md` will also be included under `vibe-tasking/docs/ai-guides/vibe-tasking/stories/stories-structuring-guide.md`.
  - [x] **Documentation:** Document the proposed contents and structure in `artifacts/zip-content-specification.md`.
  - [x] **Process:** User reviews and confirms the proposed zip contents and structure.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Experiment with `vibe-tasking.zip` Creation and Validation**

  - [x] **Experimentation:** Based on the specification, create a prototype `vibe-tasking.zip` file. This may involve manually creating a temporary, non-embedding `INSTALLING.md` for inclusion.
  - [x] **Validation:** Test the prototype by:
    - [x] Unzipping the `vibe-tasking.zip` into a test directory.
    - [x] Simulating an AI assistant following the new (non-embedding) `INSTALLING.md` from the unzipped package to set up a Vibe Tasking structure in the test directory.
    - [x] Verifying that the resulting setup is correct and functional.
  - [x] **Documentation:** Document the detailed steps taken to create the functional prototype zip, the content of the non-embedding `INSTALLING.md` used, and the results of the validation test in `artifacts/zip-creation-experiments.md`.
  - [ ] **Iteration:** Iterate on the zip contents, the non-embedding `INSTALLING.md`, and the creation process until a reliable and functional outcome is achieved.
  - [ ] **Process:** User confirms the prototype `vibe-tasking.zip` and its associated installation process are functional and the creation steps are well-understood.
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Draft `make-installer-guide.md` AI Playbook**

  - [ ] **Drafting:** Based on the successful zip creation experiments, draft the `make-installer-guide.md` AI playbook.
  - [ ] **Content:** The playbook must clearly instruct an AI assistant on how to:
    - [ ] Identify and gather all specified source files from the Vibe Tasking repository.
    - [ ] Create the necessary directory structure for the zip package.
    - [ ] Copy the source files into the correct locations within this structure.
    - [ ] Create the `vibe-tasking.zip` file containing this structure.
    - [ ] (Optional) Include instructions for the AI on how to perform a basic verification of the created zip file.
  - [ ] **Storage:** The draft `make-installer-guide.md` is saved as `artifacts/draft-make-installer-guide.md`.
  - [ ] **Process:** User reviews the draft `make-installer-guide.md` for clarity, completeness, and feasibility for an AI assistant.
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [ ] **Checkpoint: Final Research Summary and Review**

  - [ ] **Documentation:** Consolidate all research findings:
    - [ ] The final `artifacts/zip-content-specification.md`.
    - [ ] The final `artifacts/zip-creation-experiments.md` (summarizing the successful method).
    - [ ] The final `artifacts/draft-make-installer-guide.md`.
    - [ ] An example `artifacts/prototype-vibe-tasking.zip`.
  - [ ] **Documentation:** Document any identified limitations, potential issues, or future considerations for this new installation path.
  - [ ] **Process:** User confirms the research findings are comprehensive, clearly presented, and the `draft-make-installer-guide.md` provides a solid basis for a future implementation.
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to 'Final Story Closure'.

- [ ] **Checkpoint: Final Story Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [ ] **Process:** Story status is updated to "Done" and `resolution` field is set to "Completed".
  - [ ] **Process:** All ACs within this 'Final Story Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Story Closure' Checkpoint and the story's overall completion.
