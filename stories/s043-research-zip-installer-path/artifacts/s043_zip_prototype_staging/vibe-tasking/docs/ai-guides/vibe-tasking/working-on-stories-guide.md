# Guide: Working on Vibe Tasking Stories

**Primary Audience:** AI Assistant (to understand and implement best practices when actively working on a Vibe Tasking story). The Human User benefits from the AI's adherence to these practices.

This guide details best practices and required protocols for AI assistants when actively engaged in "working on" or "progressing" a Vibe Tasking story. Adherence to these guidelines ensures clear communication, accurate progress tracking, and effective collaboration.

## Core Responsibilities During Story Work

When a user instructs you to begin work on a Vibe Tasking story (e.g., "Let's work on s042-implement-new-feature"), you **MUST** adhere to the following:

1.  **Understand the Story:** Thoroughly read the `story.md` file, paying close attention to its `Description` and all `Acceptance Criteria (ACs)`.
2.  **Update Story Status:** Immediately update the story's `status` in its `story.md` frontmatter from `"To Do"` to `"In Progress"`.
3.  **Journal Entry for Commencing Work:** Append a new entry to the story's `journal.md` (or create the file with this entry if it doesn't already exist) noting that work has commenced, the current timestamp, and any initial thoughts or clarifications.
4.  **Iterative AC Completion:** Work through the ACs methodically.
5.  **Mark ACs as Complete:** As each AC is verifiably completed (typically as part of a Checkpoint Review Protocol), you **MUST** mark it as such in the `story.md` file by changing `- [ ]` to `- [x]`. This is a critical step.
6.  **Checkpoint Completion and Review (Mandatory):** Upon believing all ACs within a **Checkpoint** are complete, you **MUST** perform the **Checkpoint Review Protocol** with the user. Following this review and marking of ACs, you **MUST** ask the user for approval to proceed to the next Checkpoint. See details below.
7.  **Maintain the Journal:** Keep the `journal.md` file up-to-date with concise entries detailing progress, significant decisions, any issues encountered, their resolutions, and confirmations from Checkpoint Reviews. Entries should be timestamped.
8.  **Final Status Update:** Once all ACs are complete and confirmed by the user, update the story's `status` to `"Done"` (or another appropriate terminal status like `"Closed"`) and set the `resolution` field accordingly in the `story.md` frontmatter.

## Acceptance Criteria (AC) Management

### In-line Reminder in `story.md`

Every `story.md` file, as per the `docs/stories/README.md` template, contains an explicit instruction immediately before the AC list:

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

-   **For Minor, Directly Related Tasks:**
    -   If agreed, and the task is small and fits logically within an *existing* Checkpoint's goals, it can be added as a new Acceptance Criterion (AC) to the current `story.md` under that Checkpoint.
    -   Ensure this addition is noted in the `journal.md` for clarity.
-   **For Medium-Sized, Related Tasks:**
    -   If the emergent work is more substantial than a single AC but still closely related to the story's main objectives, consider adding it as a **new Checkpoint** within the current `story.md`.
    -   This new Checkpoint would have its own set of ACs. Examples could include harmonizing a document with newly discovered related materials, or backfilling a new metadata field across existing related files.
    -   This approach keeps the related work organized within the context of the original story while giving it proper structure. Document this decision and the new Checkpoint in the `journal.md`.
-   **For More Significant or Tangential Tasks:**
    -   It's often better to note these in the current story's `journal.md` as candidates for a *new, separate story*.
    -   This keeps the current story focused and allows the new task to be planned and prioritized appropriately.
-   **User Discretion:** Ultimately, the user will guide how to best incorporate or defer emergent work, choosing the method (new AC, new Checkpoint, or new story) that best fits the situation.

## Guidance for Modal AI Assistants (e.g., Cline)

Some AI assistants, like Cline, operate with a concept of distinct "tasks" or work cycles, often involving Plan Mode and Act Mode. When working with such an assistant:

- **Treat Checkpoints as "Cline Tasks":** Each **Checkpoint** (a top-level bolded AC and all its nested ACs) should be treated as a single "Cline Task" (or the equivalent for other modal AIs).
- **Iterative Completion within Checkpoints:** Within a complex Checkpoint, you may work through its nested ACs iteratively. The formal **Checkpoint Review Protocol** and the mandatory "ask to proceed" occur once all ACs _within that Checkpoint_ are done.
- **Communicate Checkpoint Completion:** When you complete a Checkpoint and have performed the Checkpoint Review Protocol (including getting user confirmation for all its ACs and marking them), you can consider that "Cline Task" complete. Use your AI's mechanism for indicating task completion (e.g., Cline's `attempt_completion` with a summary of the Checkpoint's completion, or by directly asking to proceed as per step 5 of the Checkpoint Review Protocol).
- **Story Remains "In Progress":** The overall Vibe Tasking story will remain `status: "In Progress"` until all its Checkpoints (and thus all ACs) are completed and confirmed.

This approach allows for focused work on a major phase (a Checkpoint), regular user validation at the end of each phase, and aligns with the natural cadence of modal AI assistants.

## Conclusion

By diligently following these guidelines, particularly the mandatory **Checkpoint Review Protocol** and the subsequent "ask to proceed" step, you will significantly contribute to the smooth and effective progression of Vibe Tasking stories, maintaining clarity and accuracy in project tracking.
