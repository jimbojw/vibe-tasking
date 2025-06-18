---
id: "s087-research-random-numbers-guide"
title: "Research and Document CLI-Based Random Number Generation Guide"
status: "Done"
priority: "Medium"
tags: "research;documentation;ai-guide;cli;random-numbers;prng;contrib-guide"
resolution: "Implemented"
---

# Story: s087-research-random-numbers-guide - Research and Document CLI-Based Random Number Generation Guide

## Description

As a Vibe Tasking user or AI developer, I want to research, vet, and document reliable command-line interface (CLI) methods for generating random numbers, so that AI assistants can be guided to use these tools when prompted to produce random numbers, rather than "making them up." This will ensure more transparent and verifiable randomness, especially for tasks like simulating dice rolls (e.g., for story [`s076-design-ai-farkle-guide`](../s076-design-ai-farkle-guide/story.md)).

This story will involve:

- Reviewing, testing, and potentially expanding upon the provided draft documentation which discusses tools like `shuf` (Linux), `jot` (macOS), `bash $RANDOM`, and `/dev/urandom` pipelines.
- Verifying OS compatibility, command syntax, output formats, and any potential biases (e.g., modulo bias).
- Codifying these findings into a new AI Guide: `ai-guides/contrib/random-numbers-generating-guide.md`.
- The guide will instruct AI assistants on how to choose and use appropriate CLI tools for random number generation based on OS, the number of values needed, the required range, and fairness considerations.

## Artifacts

- [`ai-guides/contrib/random-numbers-generating-guide.md`](../../../../ai-guides/contrib/random-numbers-generating-guide.md) (To be created: The new AI Guide)
- `artifacts/draft-cli-random-number-generation.md` (A copy of the initial draft documentation provided by the user for reference and refinement)
- `artifacts/cli-random-tool-testing-log.md` (A log of commands tested, outputs observed, and any issues or confirmations)
- [`stories/s076-design-ai-farkle-guide/story.md`](../s076-design-ai-farkle-guide/story.md) (Context for dice rolling use case)

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] **Checkpoint: Initial Story Setup**

  - [x] **Process:** The '`stories-working-guide.md`' AI Guide has been consulted for current best practices.
  - [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** The initial draft documentation provided by the user is saved to `artifacts/draft-cli-random-number-generation.md`.
  - [x] **Process:** User confirms the overall Acceptance Criteria list for this story is accurate and complete.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Research & Vet CLI Random Number Generation Methods**

  - [x] Review and test `shuf` command on a Linux environment (if available, or based on documentation):
    - Verify syntax for generating N numbers in range 1-6 (e.g., `shuf -i 1-6 -n X`).
    - Confirm output format (one number per line).
    - Document findings in `artifacts/cli-random-tool-testing-log.md`.
  - [x] Review and test `jot` command on a macOS environment (if available, or based on documentation):
    - Verify syntax for generating N numbers in range 1-6 (e.g., `jot -r X 1 6`).
    - Confirm output format.
    - Document findings in `artifacts/cli-random-tool-testing-log.md`.
  - [x] Review and test `bash $RANDOM` method on a compatible \*nix environment:
    - Verify loop syntax for generating N numbers in range 1-6 (e.g., `for i in {1..X}; do echo $((RANDOM % 6 + 1)); done`).
    - Confirm output format and note modulo bias.
    - Document findings in `artifacts/cli-random-tool-testing-log.md`.
  - [x] Review and test `/dev/urandom` pipeline method on a compatible \*nix environment:
    - Verify syntax (e.g., `xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c X`).
    - Confirm output format (single string vs. newlines with `grep -o .`).
    - Note its bias-free nature.
    - Document findings in `artifacts/cli-random-tool-testing-log.md`.
  - [x] Research or test if these tools can generate a single random number within a generic range (e.g., 1-25).
  - [x] User reviews the documented findings and test results.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Draft `random-numbers-generating-guide.md`**

  - [x] **Process:** The [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md) is consulted.
  - [x] Based on the vetted methods from the research phase and the initial draft (`artifacts/draft-cli-random-number-generation.md`), draft the content for `ai-guides/contrib/random-numbers-generating-guide.md`.
  - [x] The guide clearly explains why using programmatic/CLI methods for randomness is preferred over AI "making up" numbers.
  - [x] The guide details each vetted CLI method (`shuf`, `jot`, `$RANDOM`, `/dev/urandom` pipeline):
    - Target OS/environment.
    - Command syntax with clear examples for common use cases (e.g., single number in a range, multiple dice rolls).
    - Explanation of command components.
    - Expected output format.
    - Pros, cons, and any relevant notes (e.g., modulo bias, fairness).
  - [x] The guide provides clear advice to an AI assistant on how to choose the appropriate method based on the user's OS (if known) and the specific requirements of the random number generation task.
  - [x] The guide includes a summary table (similar to the one in the draft) for quick reference.
  - [x] User reviews the drafted `random-numbers-generating-guide.md`.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Test and Refine the Guide**

  - [x] The AI assistant (this instance or a new one) is given scenarios requiring random number generation (e.g., "roll 3 dice on Linux", "pick a random number between 1 and 50 on macOS", "generate 4 fair dice rolls universally"). (User confirmed guide effectiveness out-of-band)
  - [x] The AI assistant attempts to select and use a CLI command _strictly following only the instructions in the newly drafted `ai-guides/contrib/random-numbers-generating-guide.md`_. (User confirmed guide effectiveness out-of-band)
  - [x] The AI presents the chosen command and, if executable by the testing setup, its output. (User confirmed guide effectiveness out-of-band)
  - [x] User evaluates the AI's choice of command and its generated command syntax for correctness based on the guide. (User confirmed guide effectiveness out-of-band)
  - [x] Any ambiguities, errors, or areas for improvement in the guide are identified. (User confirmed guide effectiveness out-of-band, deferring further refinement)
  - [x] The `random-numbers-generating-guide.md` is iteratively refined based on this testing feedback. (User confirmed guide effectiveness out-of-band, deferring further refinement)
  - [x] User confirms the guide is effective and enables an AI to correctly choose and formulate commands for random number generation. (Confirmed out-of-band)
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete. (Skipped detailed in-chat testing per user request)
  - [ ] **Process:** Journal updated.
  - [ ] **Process:** User approval obtained to proceed.

- [ ] **Checkpoint: Story Review and Retrospective**

  - [x] **Process:** AI performs an internal reflection on the completed story.
  - [x] **Process:** AI appends its 1-3 specific, actionable suggestions for process improvement to the `journal.md`.
  - [x] **Process:** AI presents a summary of its journaled suggestions to the user.
  - [x] **Process:** AI invites the user to provide their own retrospective feedback.
  - [x] **Process:** AI appends a summary of the user's feedback (if any) to the `journal.md`. (User confirmed no additional feedback for journal beyond inbox items).
  - [x] **Process:** AI confirms with the user that the retrospective discussion is complete.

- [ ] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set appropriately.
  - [x] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete.
  - [ ] **Process:** Journal updated.
