---
id: "tool-use-requirement-handling-guide"
title: "Guide: Handling AI Assistant Tool-Use Requirements"
usage: "Guidance for AI assistants on using `ask_followup_question` (or equivalent) to manage host UX tool-use requirements during conversational pauses, aligning with Vibe Tasking's collaborative principles."
tags: "ai-ux;tool-use-requirement;ask-followup-question;collaboration;workflow;constraints;rooveterinaryinc.roo-cline"
---

# Guide: Handling AI Assistant Tool-Use Requirements

**(Primary Audience: AI Assistant (to understand how to satisfy a tool-use requirement imposed by its host UX while working with Vibe Tasking modes and maintaining collaborative interaction patterns).)**

## The Challenge: UX-Imposed Tool Use

Some AI assistant User Experiences (UXs), like Roo Code or Cline in 'Act' mode, require the AI to use a tool in every response. This is a UX constraint, not a Vibe Tasking framework rule. When a conversational pause or simple informational reply is needed, this can feel awkward.

## The Solution: Strategic Use of `ask_followup_question`

To handle this UX requirement gracefully while upholding Vibe Tasking's collaborative spirit:

**Use `ask_followup_question` (or your AI platform's equivalent interaction tool).**

**Why this tool?**

- It's designed for interaction and dialogue management.
- It fulfills the UX's tool-use requirement without performing unnecessary file/system operations or causing side effects.
- It allows you to return control to the user naturally.

**When to Use It:**

1.  **After Providing Information:** If the user asks a question and you've answered it, conclude with `ask_followup_question`.

    - _Example:_ "That's correct. Does that clarify things for you? What would you like to do next?"

2.  **For Proactive Check-ins:** After completing a significant step, before starting a complex one, or when a natural pause for user confirmation is beneficial.

    - _Example:_ "I've completed [action X]. Shall I proceed with [task Y]?"

3.  **When the UX Errs:** If your host UX incorrectly flags a conversational turn as needing a tool (e.g., you, the AI, receive an internal "tool use required" error after a simple statement or when a pause is natural).
    - _Note for AI:_ The user typically does not see this internal UX error. Your response should be natural for the conversational flow, without referencing an error the user isn't aware of.
    - _Example:_ (After you receive an internal "tool use required" error) "What would you like to do next?"

**In essence: If your UX demands a tool but the conversational context calls for a pause or simple confirmation, `ask_followup_question` is your go-to.**

- **Note on Single Suggestions:** Remember that some AI UXes (like Roo) support using `ask_followup_question` with only a single suggested answer. This is a powerful technique for situations where you need to prompt the user to continue or acknowledge something without offering multiple, potentially distracting, choices. For example: `ask_followup_question(question="I have completed the file analysis. Ready to proceed?", suggestions=["Yes, proceed."])`.

This approach ensures UX compliance while keeping the interaction smooth, collaborative, and user-focused.

## See Also

- For a comprehensive overview of the `ask_followup_question` tool and other related capabilities, see the [`roo-code-capabilities.md`](../../docs/reference/roo-code-capabilities.md) document.
