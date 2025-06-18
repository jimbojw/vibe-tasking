# Vibe Tasking Zip Archive (`vibe-tasking.zip`) Content Specification

This document outlines the proposed contents and directory structure for the `vibe-tasking.zip` distributable archive. The goal is to provide a comprehensive yet minimal set of files for users to easily set up Vibe Tasking in their own projects, guided by an AI assistant using the included `INSTALLING.md` AI-Playbook.

## Top-Level Directory

The zip archive will contain a single top-level directory named `vibe-tasking/`. All specified files and directories will reside within this top-level directory.

## File and Directory Structure within `vibe-tasking/`

```
vibe-tasking/
├── CONTEXT.md                   # Template for project-specific AI context
├── INSTALLING.md                # AI-Playbook for installing Vibe Tasking from this zip
├── README.md                    # README specific to this Vibe Tasking zip package
├── LICENSE                      # Apache License 2.0
└── docs/
    ├── stories/
    │   └── README.md            # Core Vibe Tasking story structure guide
    └── ai-guides/
        ├── README.md            # Copied from VT-Core: docs/ai-guides/README.md
        └── vibe-tasking/
            ├── README.md        # Copied from VT-Core: docs/ai-guides/vibe-tasking/README.md
            └── ...              # All other files from VT-Core: docs/ai-guides/vibe-tasking/*
```

## Details of Key Files:

- **`CONTEXT.md`**:
  - A template file. Users (with AI assistance) will customize this to provide project-specific context to their AI assistants.
- **`INSTALLING.md`**:
  - A new, non-embedding AI-Playbook, sourced from a template within the VT-Core repository (e.g., `docs/ai-playbooks/installing.md_template`).
  - This playbook will guide an AI assistant to intelligently copy or merge the files from this zip into the user's target project directory. It will handle potential existing files and ensure the correct Vibe Tasking structure is established.
- **`README.md` (root of zip content)**:
  - Provides information about this `vibe-tasking.zip` package itself: its purpose, contents, and how to use the `INSTALLING.md` playbook.
- **`LICENSE`**:
  - The standard Apache License 2.0, consistent with the Vibe Tasking project.
- **`docs/stories/README.md`**:
  - The canonical guide explaining the Vibe Tasking story structure, metadata, and conventions. Copied directly from VT-Core.
- **`docs/ai-guides/README.md`**:
  - Copied from VT-Core `docs/ai-guides/README.md`. Provides an overview of the AI Guides.
- **`docs/ai-guides/vibe-tasking/README.md` and other files**:
  - The `README.md` and all other conceptual AI guides from VT-Core `docs/ai-guides/vibe-tasking/` are included. These provide essential understanding for AI assistants helping users with the Vibe Tasking framework (e.g., `planning-guide.md`, `working-on-stories-guide.md`).

## Source of Files

- Files like `LICENSE`, `docs/stories/README.md`, and the contents of `docs/ai-guides/` will be direct copies from the Vibe Tasking Core (VT-Core) repository at the time of zip creation.
- `CONTEXT.md` and the root `README.md` will be specifically crafted for this zip distribution.
- The new `INSTALLING.md` AI-Playbook will be copied from a template in the VT-Core repository (e.g., from `docs/ai-playbooks/installing.md_template`) and included in the zip.

This specification will be used to guide the experimentation and creation of the prototype `vibe-tasking.zip` and the `make-installer-guide.md` AI playbook.
