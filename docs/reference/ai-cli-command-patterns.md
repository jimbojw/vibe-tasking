# AI-Assisted CLI Command Patterns & Behaviors

This document outlines common patterns, user experience considerations, and best practices when using AI assistants to execute command-line interface (CLI) commands. These notes are generally applicable across different AI assistant UXes (like Roo Code, Cline, Cursor, etc.) that support a command execution tool.

## The "Apparent Hang" with Interactive Commands

A common and potentially confusing user experience can occur when an AI assistant executes a command that unexpectedly requires interactive user input.

### The User Experience Problem

1.  The user approves a command execution proposed by the AI assistant.
2.  The AI's chat interface shows a "running" or "spinner" state, indicating the command is in progress.
3.  The command, however, has presented an interactive prompt in the underlying terminal (e.g., `[Y/n]`, a password prompt, etc.).
4.  From the user's perspective in the chat UI, the AI assistant appears to be "hung" or unresponsive. The AI's UX is waiting for a command completion signal from the terminal, but the command itself is blocked, silently waiting for user input.
5.  Resolution requires the user to recognize the situation, switch focus to the terminal window, provide the necessary input, and then the AI's workflow can resume.

### Guidance

- **For Users:** If an AI assistant seems to be stuck on a command execution step, **always check the associated terminal window for an interactive prompt.**
- **For AI Assistants:** Be mindful that seemingly simple commands may have interactive prompts. When possible, construct commands to be explicitly non-interactive.

## Pattern: Non-Interactive File Deletion

A prime example of unexpected interactivity is using `rm` with wildcards in certain shells.

- **Problem:** In some shells (e.g., `zsh`), a command like `rm ./.tmp_ai_output/*` may trigger an interactive confirmation prompt, even when the `-f` (force) flag is used. This will cause the "apparent hang" described above.
- **Recommended Pattern:** For reliable, non-interactive deletion of files within a directory, the `find` command is the recommended alternative.

  ```bash
  # This command finds all items of type 'f' (file) within the specified
  # directory and executes the -delete action on them. It is non-interactive.
  find ./.tmp_ai_output/ -type f -delete
  ```

This pattern is detailed further in the [`command-output-issues-handling-guide.md`](../../ai-guides/contrib/command-output-issues-handling-guide.md).
