# Draft: AI-Led Retrospective Process & Prompts

This document outlines the key steps and prompts for an AI assistant to lead a story retrospective. The process emphasizes AI-driven analysis and suggestions, followed by an opportunity for user input and action. This content is intended for incorporation into `ai-guides/core/stories/stories-working-guide.md`.

## AI-Led Retrospective Process Steps:

1.  **AI Internal Reflection & Suggestion Generation:**

    - (Internal AI Step) After all substantive story ACs are complete, the AI analyzes the story's execution. Aspects to consider include:
      - Tool usage efficacy and any difficulties.
      - Patterns in user feedback, corrections, or clarifications.
      - Clarity and completeness of the original story description and ACs.
      - Effectiveness of any consulted AI-Guides (gaps, ambiguities).
      - Overall conversational flow and collaboration smoothness.
    - (Internal AI Step) Based on this analysis, the AI formulates 1-3 specific, actionable suggestions for process improvement (targeting Vibe Tasking core, project-specific guides, story templates, or general collaboration patterns).

2.  **AI Journals Its Suggestions:**

    - The AI appends its formulated suggestions to the `journal.md` of the completed story. Each suggestion should be clearly articulated.
      - _Journal Entry Example Snippet:_
        ```
        - AI Retrospective Suggestions:
          1.  Suggestion: Consider creating an AI-Guide for [specific task] due to [observation during story].
          2.  Suggestion: The story template for [type of story] could be enhanced by adding an AC for [missing check/step].
          3.  Suggestion: When using [tool_name], adopting [alternative approach] might improve efficiency because [reasoning].
        ```

3.  **AI Presents Suggestions to User & Invites Feedback:**

    - **AI Dialogue Starter:**
      "Okay, we've completed the main work for story `[Story ID] - [Story Title]`.
      I've taken a moment to reflect on how it went and have jotted down a few suggestions for potential process improvements in the story's `journal.md`.

      Here's a summary of what I noted:

      1.  `[AI Suggestion 1 (concise summary)]`
      2.  `[AI Suggestion 2 (concise summary)]`
      3.  `[AI Suggestion 3 (concise summary, if applicable)]`

      Do any of these resonate with you, or would you like to discuss them further? Perhaps convert any into new stories or update existing guides?

      Also, I'd be happy to hear any of your own reflections on this story – what went well from your perspective, or what could have been better?"

4.  **Capture User's Reflections (If Offered):**

    - If the user provides their own retrospective thoughts or feedback on the AI's suggestions, the AI summarizes these and appends them to the `journal.md` as well.
      - _Journal Entry Example Snippet (User Feedback):_
        ```
        - User Retrospective Feedback:
          - User agreed with AI suggestion #1 and suggested creating a new story for it.
          - User noted that [specific aspect of the story] was particularly smooth.
          - User felt that [another aspect] could be improved by [user's idea].
        ```

5.  **Conclude Retrospective:**
    - AI confirms with the user if there's anything else to discuss for this retrospective before moving to final story closure.
    - **AI Dialogue Closer:** "Thanks for that feedback! I've added your thoughts to the journal. Is there anything else for this retrospective, or are we ready to proceed with the final closure steps for the story?"
