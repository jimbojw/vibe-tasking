# AI-Playbook: Install Vibe Tasking from Zip Archive

**Objective:** To set up the Vibe Tasking framework in the user's target project using the files contained within this archive.

**Prequisites for AI Assistant:**

- You have access to file system operations (read, write, copy, list directories).
- The user has specified a target project directory where Vibe Tasking should be installed.
- This `INSTALLING.md` file and all other accompanying files and directories (e.g., `CONTEXT.md`, `docs/`) are present in your current working directory (assumed to be the root of the unzipped `vibe-tasking` archive).

**Steps:**

1.  **Confirm Target Directory:**

    - Ask the user to confirm the absolute path to their target project directory if not already provided.
    - Let this be `TARGET_PROJECT_ROOT`.

2.  **Copy `CONTEXT.md`:**

    - Copy the `CONTEXT.md` file from this archive's root to `TARGET_PROJECT_ROOT/CONTEXT.md`.
    - Inform the user that they will need to customize this `CONTEXT.md` later with their project-specific details.

3.  **Create `docs/` Directory Structure in Target:**

    - In `TARGET_PROJECT_ROOT`, create the directory `docs/` if it doesn't exist.
    - In `TARGET_PROJECT_ROOT/docs/`, create the directory `stories/` if it doesn't exist.
    - In `TARGET_PROJECT_ROOT/docs/`, create the directory `ai-guides/` if it doesn't exist.
    - In `TARGET_PROJECT_ROOT/docs/ai-guides/`, create the directory `vibe-tasking/` if it doesn't exist.

4.  **Copy Core Vibe Tasking Documentation:**

    - Copy `docs/stories/README.md` from this archive to `TARGET_PROJECT_ROOT/docs/stories/README.md`.
    - Copy `docs/ai-guides/README.md` from this archive to `TARGET_PROJECT_ROOT/docs/ai-guides/README.md`.
    - Copy all files and subdirectories from `docs/ai-guides/vibe-tasking/` in this archive to `TARGET_PROJECT_ROOT/docs/ai-guides/vibe-tasking/`.

5.  **Copy `LICENSE`:**

    - Copy the `LICENSE` file from this archive's root to `TARGET_PROJECT_ROOT/LICENSE`.

6.  **Copy Root `README.md` (Optional but Recommended):**

    - The `README.md` file in this archive's root is specific to the zip package.
    - You can optionally copy it to `TARGET_PROJECT_ROOT/VIBE_TASKING_README.md` or similar, so the user has a reference to this installation package.

7.  **Verification (Optional):**

    - List the key files and directories created in `TARGET_PROJECT_ROOT` to confirm the setup.
      - `TARGET_PROJECT_ROOT/CONTEXT.md`
      - `TARGET_PROJECT_ROOT/docs/stories/README.md`
      - `TARGET_PROJECT_ROOT/docs/ai-guides/README.md`
      - `TARGET_PROJECT_ROOT/docs/ai-guides/vibe-tasking/` (and its contents)

8.  **Inform User of Completion:**
    - Notify the user that the Vibe Tasking files have been installed into their project.
    - Remind them to:
      - Customize `TARGET_PROJECT_ROOT/CONTEXT.md`.
      - Review `TARGET_PROJECT_ROOT/docs/stories/README.md` to understand story structure.
      - Consult the guides in `TARGET_PROJECT_ROOT/docs/ai-guides/vibe-tasking/` for usage.

This playbook provides a basic installation. Advanced scenarios like merging with existing files or handling conflicts are out of scope for this initial version and should be handled with user guidance.
