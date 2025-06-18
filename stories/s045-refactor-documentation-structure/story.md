---
id: "s045-refactor-documentation-structure"
title: "Refactor Documentation Structure and Standardize Terminology"
status: "Done"
priority: "High"
tags: "documentation;refactor;organization;terminology;information-architecture"
resolution: "Implemented"
---

# Story: s045 - Refactor Documentation Structure and Standardize Terminology

## Description

**User Story:** As a Vibe Tasking maintainer, I want to refactor the `docs/` directory structure and standardize documentation terminology, so that the documentation is more organized, maintainable, and clearly distinguishes between user-facing articles, AI-facing conceptual guides, and AI-facing executable playbooks.

**Details:**
This story will implement a new information architecture for the project's documentation. Key changes include:

- Establishing clear definitions for documentation types (articles, ai-guides, ai-playbooks, onboarding, reference) in a new glossary.
- Creating new top-level directories:
  - `docs/articles/` (for user-focused content, including the moved `onboarding/` subdirectory).
  - `docs/ai-playbooks/` (for AI executable instructions).
- Restructuring the existing `docs/guides/` directory (to be renamed `docs/ai-guides/`) to differentiate between:
  - AI Guides for VT-Core project maintenance (at the root of `docs/ai-guides/`).
  - AI Guides for general Vibe Tasking framework usage (in a new `docs/ai-guides/vibe-tasking/` subdirectory).
- Migrating all existing documentation files to their new appropriate locations within this structure.
- Ensuring all internal links throughout the documentation are updated to reflect the new file paths.
- Creating or updating `README.md` files for all new and restructured directories to explain their purpose and contents.
- An ADR will be created to document the rationale and final agreed-upon structure.

This refactor aims to improve clarity, discoverability, and maintainability of the Vibe Tasking documentation for both human users and AI assistants.

**Canonical Target Documentation Structure (`docs/` directory):**

```
docs/
├── README.md              # Overview of all documentation
├── adrs/
│   ├── README.md
│   └── adr-XXX-documentation-refactor.md # (To be created as part of this story)
│   └── ...                # Existing ADRs
├── reference/
│   ├── README.md
│   └── glossary.md        # New: For canonical term definitions
│   └── ...                # (e.g., ai-assistant-capabilities.md)
│
├── articles/              # User-focused documentation
│   ├── README.md
│   ├── onboarding/        # Moved from docs/onboarding/
│   │   ├── README.md
│   │   ├── 01-introduction.md
│   │   └── ...            # All current onboarding files
│   ├── ai-collaboration-best-practices.md # Moved from docs/guides/
│   ├── leveraging-project-guides.md     # Moved from docs/guides/
│   ├── using-architecture-decision-records.md # Moved from docs/ai-guides/ (formerly docs/guides/)
│   └── ...                # Other user articles
│
├── ai-playbooks/          # AI: Step-by-step task execution (imperative scripts)
│   ├── README.md
│   └── INSTALLING.md      # Current root INSTALLING.md, moved here
│   └── ...                # (Future: make-installer-zip-playbook.md)
│
└── ai-guides/             # AI: Conceptual/scenario guidance
    ├── README.md          # Defines "ai-guides", explains structure
    │                      # (Does not specifically mention 'vibe-tasking' subdir)
    ├── updating-onboarding-guide.md  # Moved from current docs/ai-guides/ (formerly docs/guides/)
    ├── updating-installing-md-guide.md # Moved from current docs/ai-guides/ (formerly docs/guides/)
    │                                   # (For maintaining VT-Core's INSTALLING.md playbook)
    └── vibe-tasking/      # AI conceptual guides for general Vibe Tasking framework usage
        ├── README.md      # Explains these ai-guides are for general VT framework use
        ├── planning-guide.md            # Moved from current docs/ai-guides/ (formerly docs/guides/)
        ├── working-on-stories-guide.md  # Moved from current docs/ai-guides/ (formerly docs/guides/)
        ├── writing-context-documents.md # Moved from current docs/ai-guides/ (formerly docs/guides/)
        └── handling-command-output-issues.md # Moved from current docs/ai-guides/ (formerly docs/guides/)
```

## Artifacts

- This `story.md` file.
- `journal.md` for this story.
- `docs/adrs/adr-XXX-documentation-refactor.md` (New ADR documenting the decisions for this story - number to be determined).
- `docs/reference/glossary.md` (New or updated glossary with standardized terminology).
- All modified, moved, and newly created documentation files and `README.md` files within the `docs/` directory as per the canonical structure.

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup and Planning Confirmation**

  - [x] **Process:** User confirms the story (`s045`) structure, title, description, canonical target structure, and proposed Checkpoints/ACs accurately reflect the planned work.
  - [x] **Process:** Story status updated to "In Progress", and an initial journal entry is created for `s045`.

- [x] **Checkpoint: Define Terminology and Document Rationale (ADR)**

  - [x] **Documentation:** Create/update `docs/reference/glossary.md` with agreed-upon definitions for "articles," "AI-Playbook," "AI-Guide (AI Conceptual)," "onboarding," "reference," and the distinctions for guide categories (VT-Core maintenance vs. general Vibe Tasking framework).
  - [x] **Process:** User reviews and approves the glossary definitions.
  - [x] **Documentation:** Create `docs/adrs/adr-XXX-documentation-refactor.md` (with appropriate next number) detailing the problem statement, decision drivers, the chosen new documentation structure, and the rationale behind it.
  - [x] **Process:** User reviews and approves the content of the ADR.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Implement New Directory Structure and Core READMEs**

  - [x] **Implementation:** Create the new directory structure within `docs/` as defined in the canonical target structure.
  - [x] **Documentation:** Create or update `README.md` files for all new and significantly restructured directories as specified in the canonical target structure.
  - [x] **Process:** User reviews and approves the new directory structure and the content of these core `README.md` files.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Migrate Documentation Files**

  - [x] **Implementation:** Move all existing files from their current locations (`docs/onboarding/`, `docs/guides/`, root `INSTALLING.md`) to their new correct locations as per the canonical target structure.
  - [x] **Process:** User confirms all files have been migrated to their correct new locations.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Update All Internal Links**

  - [x] **Implementation:** Systematically review all files within the `docs/` directory (and any key root project files like the main `README.md` or `CONTEXT.md`) for internal links referencing moved files.
  - [x] **Implementation:** Update all identified internal links to point to the new correct paths.
  - [x] **Process:** User performs a spot-check or confirms a strategy for verifying link updates.
  - [x] **Process:** Based on user confirmation, all critical links are verified as updated and functional.
  - [x] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the next Checkpoint.

- [x] **Checkpoint: Final Review and Story Closure**
  - [x] **Process:** User confirms all previous Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** User confirms the overall documentation structure is implemented as planned, and the project's documentation is coherent, accessible, and all links are correct.
  - [x] **Process:** Story status for `s045` is updated to "Done", and the `resolution` field is set to "Implemented".
  - [x] **Process:** Journal updated with the final entry for `s045`.
