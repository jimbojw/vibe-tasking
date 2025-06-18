---
id: "stories-working-guide"
title: "Guide: Working on Vibe Tasking Stories"
usage: "This guide MUST be consulted when a user initiates work on any Vibe Tasking story (e.g., 'Let's work on story sXYZ'). It outlines essential procedures for story progression, including status updates, AC management, journaling, and the mandatory Checkpoint Review Protocol."
tags: "stories;workflow;acceptance-criteria;checkpoints;journaling;collaboration"
---

# Guide: Working on Vibe Tasking Stories

**(Primary Audience: AI Assistant (to understand and implement best practices when actively working on a Vibe Tasking story). The Human User benefits from the AI's adherence to these practices.)**

This guide details best practices and required protocols for AI assistants when actively engaged in "working on" or "progressing" a Vibe Tasking story. Adherence to these guidelines ensures clear communication, accurate progress tracking, and effective collaboration.

## Core Responsibilities During Story Work

When a user instructs you to begin work on a Vibe Tasking story (e.g., "Let's work on s042-implement-new-feature"), you **MUST** adhere to the following:

0.  **Understand Story Structure:** Before proceeding with any other steps, you **MUST** first consult the **[Guide: Structuring Vibe Tasking Stories](stories-structuring-guide.md)** to ensure you have a full understanding of the standard story file structure and conventions.

1.  **Understand the Story:** Thoroughly read the `story.md` file, paying close attention to its `Description` and all `Acceptance Criteria (ACs)`. (Refer to the **[Story Structuring Guide](stories-structuring-guide.md)** for details on `story.md` content.)
2.  **Update Story Status:** Immediately update the story's `status` in its `story.md` frontmatter from `"To Do"` to `"In Progress"`.
3.  **Journal Entry for Commencing Work:** Append a new entry to the story's `journal.md` (or create the file with this entry if it doesn't already exist) noting that work has commenced. **Entries MUST follow the format specified in [`journal.template.md`](journal.template.md), starting with a `## YYYY-MM-DDTHH:MM:SSZ` timestamp heading followed by bulleted content.** Include any initial thoughts or clarifications.
    **Note on Appending to `journal.md`:**
    When appending entries to `journal.md`, AI assistants should use methods that add content to the end of the file without overwriting existing content.

    - For AI assistants like **Roo** (or similar assistants with direct file manipulation tools), this can be achieved using a tool like `insert_content` with the `line` parameter set to `0`. For example, conceptually: `insert_content into 'path/to/journal.md' at line 0 with '## YYYY-MM-DDTHH:MM:SSZ\n\n- Your bulleted journal entry content here.'`. **Always refer to [`journal.template.md`](journal.template.md) for the precise formatting.**
    - For AI assistants that primarily use shell commands, appending can be done using the shell's append redirect operator (e.g., `echo "YOUR JOURNAL ENTRY HERE" >> path/to/journal.md` on Linux/macOS or `Add-Content -Path "path\to\journal.md" -Value "YOUR JOURNAL ENTRY HERE"` in PowerShell). \* Always ensure the chosen method correctly appends and does not truncate or replace the existing journal content. If unsure, or if the AI assistant lacks a direct append capability, it should inform the user and seek guidance on how to proceed with the journal update.

4.  **Perform Spot Grooming and Validate ACs:**

    - Before proceeding with the story's substantive ACs, and after the initial status/journal updates, the AI **MUST** perform "spot grooming" and facilitate an AI-assisted review of the story's Acceptance Criteria.
    - **Consult the [`stories-spot-grooming-guide.md`](stories-spot-grooming-guide.md) for the detailed methodology on performing this analysis.** This involves verifying links, checking for pre-existing artifacts, scanning for potential obsolescence/duplication, presenting findings and a proposed plan to the user, and then collaboratively reviewing and finalizing the ACs.
    - This step is typically guided by a process AC in the story's "Initial Story Setup" checkpoint (or "Combined Checkpoint" for lightweight stories) and is also performed when resuming a story for the first time in a new chat session.

5.  **Iterative AC Completion:** Work through the (now validated) ACs methodically.
6.  **Mark ACs as Complete:** As each AC is verifiably completed (typically as part of a Checkpoint Review Protocol), you **MUST** mark it as such in the `story.md` file by changing `- [ ]` to `- [x]`. This is a critical step.
7.  **Checkpoint Completion and Review (Mandatory):** Upon believing all ACs within a **Checkpoint** are complete, you **MUST** perform the **Checkpoint Review Protocol** with the user. Following this review and marking of ACs, you **MUST** ask the user for approval to proceed to the next Checkpoint. See details below.
8.  **Maintain the Journal:** Keep the `journal.md` file up-to-date with concise entries detailing progress, significant decisions, any issues encountered, their resolutions, and confirmations from Checkpoint Reviews. **All entries MUST follow the format specified in [`journal.template.md`](journal.template.md), starting with a `## YYYY-MM-DDTHH:MM:SSZ` timestamp heading followed by bulleted content.**
9.  **Final Status Update:** Once all ACs are complete and confirmed by the user, update the story's `status` to `"Done"` (or another appropriate terminal status like `"Closed"`) and set the `resolution` field accordingly in the `story.md` frontmatter.

## Acceptance Criteria (AC) Management

### Collaborative Drafting with `artifacts/`

When collaboratively developing content that might eventually be incorporated into main story files, AI-Guides, or other project documents (e.g., drafting new ACs, designing processes, outlining new guide sections), it is encouraged to use the story's `artifacts/` directory.

- **Create Draft Files:** Place draft documents (e.g., `my-new-process-draft.md`) within the `artifacts/` subdirectory of the current story.
- **Iterate and Review:** This allows for focused iteration and review of the draft content without cluttering the main files prematurely.
- **Final Integration:** Once the drafted content is approved, it can then be formally integrated into its target location (e.g., an AI-Guide, the `story.md` itself).

This practice keeps the primary documents cleaner during the drafting phase and provides a clear, version-controlled space for work-in-progress materials.

### In-line Reminder in `story.md`

Every `story.md` file, as per the **[Story Structuring Guide](stories-structuring-guide.md)** (which details the `story.template.md` content), contains an explicit instruction immediately before the AC list:

`**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]`to`- [x]`(or`- [X]`).`

You must adhere to this instruction diligently when performing the Checkpoint Review Protocol.

### Checkpoint Review Protocol

This protocol is mandatory and is performed when you, the AI assistant, believe all Acceptance Criteria (ACs) within a given **Checkpoint** have been fulfilled.

1.  **Initiate Review upon Checkpoint Completion:** Announce that you believe the current Checkpoint is complete. List all ACs within that Checkpoint, indicating which you believe are now fulfilled (they should all be fulfilled if the Checkpoint is considered complete).
    - **Example AI Dialogue:** "I believe Checkpoint '[Name of Checkpoint]' is now complete. The following ACs within this Checkpoint have been addressed:
      - `[AC 1 Description]`
      - `[AC 2 Description]`
        ...
        Do you agree these are all complete for this Checkpoint?"
    - For AI assistants with user query capability (like Cline's `ask_followup_question` tool, or Windsurf/Cascade's `suggested_responses` for simple choices and its general conversational flow for more complex confirmations), this is an ideal way to present this review and request confirmation.
2.  **Await User Confirmation:** The user will confirm if they agree with your assessment for all listed ACs for the Checkpoint.
3.  **Update `story.md` (Mark ACs):**
    - If the user confirms, ensure all ACs within the completed Checkpoint are marked with `[x]` in the `story.md` file. (This might have been done iteratively as you worked through them, but this is the final verification).
    - If the user disagrees or provides corrections for any ACs within the Checkpoint, address the feedback. Do not consider the Checkpoint complete until all its ACs are confirmed and marked.
4.  **Journal the Update:** Update the `journal.md` to reflect the completion of the Checkpoint. This entry should summarize what was accomplished in the checkpoint and note any significant decisions made or issues resolved. This fulfills the standard AC: "- [ ] **Process:** Journal updated to reflect completion of this '[Checkpoint Name]' Checkpoint and any significant decisions made within it."
5.  **Ask to Proceed (Mandatory Pause):** After successful completion of the Checkpoint Review Protocol (including marking ACs and updating the journal), you **MUST** explicitly ask the user for approval to proceed to the _next_ Checkpoint, fulfilling the standard AC: "- [ ] **Process:** User approval is obtained to proceed to the next Checkpoint."
    - **Example AI Dialogue:** "Checkpoint '[Name of Checkpoint]' is now complete, all its ACs are marked, and the journal has been updated. Shall I proceed to the next Checkpoint: '[Name of Next Checkpoint]'?"
    - Again, tools like `ask_followup_question` (or Windsurf/Cascade's `suggested_responses`/natural dialogue where appropriate) are ideal for this.

This protocol is reinforced by a standard "Process" AC in every story (related to applying this protocol). Fulfilling this is part of your core task.

### Handling Emergent or Related Tasks

During the course of working on a story, new related tasks or scope adjustments may become apparent. Here's a general approach, always in discussion with the user:

- **For Minor, Directly Related Tasks:**
  - If agreed, and the task is small and fits logically within an _existing_ Checkpoint's goals, it can be added as a new Acceptance Criterion (AC) to the current `story.md` under that Checkpoint.
  - Ensure this addition is noted in the `journal.md` for clarity.
- **For Medium-Sized, Related Tasks:**
  - If the emergent work is more substantial than a single AC but still closely related to the story's main objectives, consider adding it as a **new Checkpoint** within the current `story.md`.
  - This new Checkpoint would have its own set of ACs. Examples could include harmonizing a document with newly discovered related materials, or backfilling a new metadata field across existing related files.
  - This approach keeps the related work organized within the context of the original story while giving it proper structure. Document this decision and the new Checkpoint in the `journal.md`.
- **For More Significant or Tangential Tasks:**
  - It's often better to note these in the current story's `journal.md` as candidates for a _new, separate story_.
  - This keeps the current story focused and allows the new task to be planned and prioritized appropriately.
- **User Discretion:** Ultimately, the user will guide how to best incorporate or defer emergent work, choosing the method (new AC, new Checkpoint, or new story) that best fits the situation.
- **Utilizing the Inbox for Emergent Items (If Available or Explicitly Invoked):**
  - If the user explicitly initiates an inbox capture (e.g., using the "Inbox:" cue, case-insensitive), the AI **MUST** follow the [`inbox-capturing-guide.md`](../../contrib/inbox-capturing-guide.md). This may involve creating the `inbox/` directory if it's the first such capture in the project.
  - If an `inbox/` directory already exists (indicating the project or user has adopted this mechanism), for emergent thoughts that might become separate stories or require later focused attention, the AI can suggest using the inbox.
  - If no `inbox/` directory exists and the user has not explicitly cued its use with "Inbox:", the AI should rely on the other methods described above (new AC, new Checkpoint, or journaling for a new story) for handling emergent items. The AI should not unilaterally create the `inbox/` directory in this scenario.

## Guidance for Modal AI Assistants (e.g., Cline)

Some AI assistants, like Cline, operate with a concept of distinct "tasks" or work cycles, often involving Plan Mode and Act Mode. When working with such an assistant:

- **Treat Checkpoints as "Cline Tasks":** Each **Checkpoint** (a top-level bolded AC and all its nested ACs) should be treated as a single "Cline Task" (or the equivalent for other modal AIs).
- **Iterative Completion within Checkpoints:** Within a complex Checkpoint, you may work through its nested ACs iteratively. The formal **Checkpoint Review Protocol** and the mandatory "ask to proceed" occur once all ACs _within that Checkpoint_ are done.

## AI-Led Story Retrospective

After all substantive Acceptance Criteria for a story are completed and confirmed, and before the final story closure ACs (like updating status to "Done"), an AI-led retrospective **MUST** be performed. This process shifts the primary burden of reflection onto the AI assistant, ensuring valuable insights are captured and opportunities for improvement are identified with minimal overhead for the user.

The AI assistant **MUST** follow these steps:

1.  **AI Internal Reflection & Suggestion Generation:**

    - (Internal AI Step) The AI analyzes the completed story's execution. Aspects to consider include:
      - Tool usage efficacy and any difficulties encountered.
      - Patterns in user feedback, corrections, or clarifications during the story.
      - Clarity and completeness of the original story description and Acceptance Criteria.
      - Effectiveness of any consulted AI-Guides (identifying gaps, ambiguities, or needs for new guides).
      - Overall conversational flow and collaboration smoothness.
    - (Internal AI Step) Based on this analysis, the AI formulates 1-3 specific, actionable suggestions for process improvement. These suggestions can target:
      - Updates to existing AI-Guides.
      - Creation of new AI-Guides.
      - Modifications to `story.template.md` or other Vibe Tasking conventions.
      - Improvements to general collaboration patterns or tool usage.

2.  **AI Journals Its Suggestions:**

    - The AI **MUST** append its formulated suggestions to the `journal.md` of the completed story. Each suggestion should be clearly articulated.
      - _Journal Entry Example Snippet:_
        ```
        - AI Retrospective Suggestions:
          1.  Suggestion: Consider creating an AI-Guide for [specific task] due to [observation during story, e.g., "repeated clarifications needed"].
          2.  Suggestion: The story template for [type of story] could be enhanced by adding an AC for [missing check/step, e.g., "verifying X before Y"].
          3.  Suggestion: When using [tool_name], adopting [alternative approach, e.g., "providing parameter Z explicitly"] might improve efficiency because [reasoning, e.g., "it avoided an error we saw previously"].
        ```

3.  **AI Discusses Suggestions with User & Captures Actionable Items:**

    - The AI **MUST** then inform the user about the reflection and present a summary of the journaled suggestions.
    - **Example AI Dialogue (Presenting Suggestions):**
      "Okay, we've completed the main work for story `[Story ID] - [Story Title]`.
      I've taken a moment to reflect on how it went and have jotted down a few suggestions for potential process improvements in the story's `journal.md`.

      Here's a summary of what I noted:

      1.  `[AI Suggestion 1 (concise summary)]`
      2.  `[AI Suggestion 2 (concise summary)]`
      3.  `[AI Suggestion 3 (concise summary, if applicable)]`"

    - **AI Action: Check for `inbox/` directory.** The AI should determine if an `inbox/` directory exists at the project root.

    - **If `inbox/` directory exists:**

      - **Example AI Dialogue (Offering Inbox Capture):**
        "Which of these suggestions, if any, do you think are worth pursuing further? For any you'd like to track, I can capture them as new items in the `inbox/` directory, following the `inbox-capturing-guide.md`."
      - For each suggestion the user agrees is worth pursuing:
        - The AI **MUST** use the process detailed in [`inbox-capturing-guide.md`](../../contrib/inbox/inbox-capturing-guide.md) to create a new, individual item in the `inbox/` directory.
        - The AI should confirm with the user after each inbox item is created.

    - **If `inbox/` directory does NOT exist:**

      - **Example AI Dialogue (Inbox Not Available):**
        "These suggestions are recorded in this story's journal for your review. The `inbox/` mechanism for formally tracking such items doesn't seem to be set up in this project. We can discuss these further, or you can decide how to best proceed with them later."

    - **Invite General User Feedback (Applies in both cases):**
      - The AI also invites general user feedback: "Also, I'd be happy to hear any of your own reflections on this story – what went well from your perspective, or what could have been better?"

4.  **Capture General User Reflections (If Offered):**

    - If the user provides general retrospective thoughts (not related to specific AI suggestions already captured in the inbox), or feedback on the AI's suggestions that don't warrant a new inbox item, the AI **MUST** summarize these and append them to the `journal.md`.
      - _Journal Entry Example Snippet (User Feedback):_
        ```
        - User Retrospective Feedback (General):
          - User noted that [specific aspect of the story, e.g., "the use of the artifacts directory for drafting"] was particularly smooth.
          - User felt that [another aspect, e.g., "the initial ACs"] could be improved by [user's idea, e.g., "being more specific about X"].
        ```
    - Note: Specific AI suggestions agreed upon for action should already be in the inbox; this journal entry is for other feedback.

5.  **Conclude Retrospective:**
    - The AI confirms with the user if there's anything else to discuss for this retrospective (e.g., "I've captured [X] items in the inbox based on our discussion, and noted your other feedback in the journal.") before moving to final story closure steps.
    - **Example AI Dialogue Closer:** "Thanks for that discussion! I've captured the actionable items in the inbox and your other thoughts in the journal. Is there anything else for this retrospective, or are we ready to proceed with the final closure steps for the story?"

This AI-led retrospective process ensures that learning and improvement are continuous within the Vibe Tasking framework. The `story.template.md` will include ACs in its final checkpoint to ensure this retrospective is performed.

- **Communicate Checkpoint Completion:** When you complete a Checkpoint and have performed the Checkpoint Review Protocol (including getting user confirmation for all its ACs and marking them), you can consider that "Cline Task" complete. Use your AI's mechanism for indicating task completion (e.g., Cline's `attempt_completion` with a summary of the Checkpoint's completion, or by directly asking to proceed as per step 5 of the Checkpoint Review Protocol).
- **Story Remains "In Progress":** The overall Vibe Tasking story will remain `status: "In Progress"` until all its Checkpoints (and thus all ACs) are completed and confirmed.

This approach allows for focused work on a major phase (a Checkpoint), regular user validation at the end of each phase, and aligns with the natural cadence of modal AI assistants.

## Conclusion

By diligently following these guidelines, particularly the mandatory **Checkpoint Review Protocol** and the subsequent "ask to proceed" step, you will significantly contribute to the smooth and effective progression of Vibe Tasking stories, maintaining clarity and accuracy in project tracking.
