---
id: "python-script-dry-run-guide"
title: "Guide: Using Python Scripts with Dry Runs for Programmable Tasks"
usage: "Use this guide for the standard practice of using ad-hoc Python scripts with a --dry-run mechanism to perform and preview programmable tasks like bulk file modifications or cross-reference updates."
tags: "python;scripting;dry-run;automation;safety;workflow"
---

# Guide: Using Python Scripts with Dry Runs for Programmable Tasks

**(Primary Audience: AI Assistant)**

## Introduction

This guide outlines the standard practice for using ad-hoc Python scripts to perform project-wide programmable tasks, such as bulk file modifications or cross-reference updates. A key aspect of this practice is the mandatory use of a `--dry-run` (or similar) mechanism to preview changes and confirm script behavior with the user before any actual modifications are made. This ensures safety, accuracy, and user confidence.

## Core Process: Scripting with Dry Run Confirmation

When a task is identified as suitable for an ad-hoc Python script (e.g., updating multiple files, complex text replacements across the project, or manipulating YAML frontmatter in bulk):

1.  **Script Design and Suggestion:**

    - Propose the use of a Python script to automate the task.
    - Design the script to accept a `--dry-run` flag that enables it to output what it _would_ do, without actually making changes.
    - If the script modifies files, it should clearly indicate which files would be affected and what changes would be made during a dry run.

2.  **Initial Execution (Dry Run):**

    - **Always** execute the script with the `--dry-run` flag first.
    - Pipe both standard output and standard error to a versioned file in the story's `artifacts/` directory (e.g., `dry_run_output_v1.txt`, `dry_run_output_v2.txt`). This allows for tracking multiple iterations as the script is refined.
    - Example: `python your_script.py --dry-run [other_arguments] > artifacts/dry_run_output_v1.txt 2>&1`

3.  **Output Review and User Confirmation:**

    - Present the output of the dry run to the user. This output should be clear and allow the user to verify the intended actions of the script.
    - Explicitly ask the user to review the dry run output and confirm if the script is behaving as expected and if it's safe to proceed with the actual execution.
    - Example prompt: "The dry run produced the following output: [show output]. Does this look correct? May I proceed with the actual execution?"

4.  **Actual Execution (Live Run):**

    - Only after receiving explicit user confirmation, execute the script _without_ the `--dry-run` flag to perform the actual modifications.
    - Pipe both standard output and standard error to a versioned file in the story's `artifacts/` directory (e.g., `live_run_output_v1.txt`).
    - Example: `python your_script.py [other_arguments] > artifacts/live_run_output_v1.txt 2>&1`

5.  **Post-Execution Verification (Optional but Recommended):**
    - If feasible, suggest a way to verify the changes after the live run (e.g., checking a few modified files, running a specific check command).

## Handling Command Output

Executing scripts and capturing their output (especially for dry runs) is critical. You may encounter situations where command output is not immediately visible or accessible.

- Refer to the **[Guide: Handling Command Output Issues with AI Assistants](command-output-issues-handling-guide.md)** for detailed strategies on reliably obtaining command output, including using temporary files for redirection if direct capture fails. This is particularly important for ensuring both you and the user can inspect the results of a dry run.

## Key Principles

- **Safety First:** The dry run step is mandatory to prevent unintended widespread changes.
- **User Confirmation is Crucial:** Never proceed with a live run without explicit user approval based on the dry run output.
- **Clarity in Output:** Ensure the dry run output is understandable and clearly shows intended actions.
- **Idempotency (Ideal):** If possible, design scripts to be idempotent, meaning running them multiple times has the same effect as running them once. This is not strictly related to dry runs but is a good practice for such scripts.

## Conclusion

By consistently applying the dry run methodology for ad-hoc Python scripts, AI assistants can perform complex, project-wide tasks with greater safety and accuracy. This collaborative approach, involving user confirmation at critical steps, builds trust and ensures that automated changes align with user intent.
