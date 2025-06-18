---
id: "inbox-capturing-guide"
title: "Guide: Capturing Emergent Thoughts to the Inbox"
usage: "If a top-level `inbox/` directory exists, this guide **MUST** be consulted by an AI assistant when the user explicitly signals intent to capture an emergent thought using the primary cue 'Inbox:' (case-insensitive). It should also be consulted if the AI identifies a need to capture an item and the user agrees. It details the mandatory process for creating inbox items."
tags: "inbox;capture;gtd;workflow;ai-assistant;process"
---

# Guide: Capturing Emergent Thoughts to the Inbox

**(Primary Audience: AI Assistant (for reliably capturing emergent items into the `inbox/` directory).)**

## Introduction

If a top-level `inbox/` directory exists in the Vibe Tasking project, this guide **MUST** be followed by AI assistants when capturing emergent thoughts, ideas, or ancillary tasks. This is primarily triggered when a user explicitly signals intent to capture by starting their input with "Inbox:" (case-insensitive). The guide should also be followed if the AI, in discussion with the user, identifies an item suitable for the inbox and the user agrees to capture it.

This guide details the mandatory, low-friction process for creating these inbox items, ensuring they are recorded reliably and consistently as per the mechanism defined in [`adr-028-inbox-capture-mechanism.md`](../../../docs/adrs/adr-028-inbox-capture-mechanism.md).

**Core Principle: Capture, Don't Execute Immediately**
It is crucial for the AI assistant to understand that the primary intent of the "Inbox:" cue and the inbox capture process is to _record_ an emergent thought or task for later, systematic processing (as detailed in the `inbox-processing-guide.md`). The AI **MUST NOT** interpret an "Inbox:" request as an instruction to immediately execute the described task. The focus is solely on capturing the item accurately and efficiently.

## 1. Recognizing Cues and Prompting for Capture

AI assistants should be aware of situations where capturing a thought to the inbox is appropriate:

- **Primary User Cue:** The user explicitly signals intent to capture by starting their input with "Inbox:" (case-insensitive). This guide **MUST** be consulted by the AI when this cue is detected.
  - **Example:** `Inbox: We should define how AI assistants write README.md files for directories.`
- **Other User Phrasing:** The user might also use phrases like "Capture this thought: [thought content]", "Add to inbox: [thought content]", or "Idea: [thought content]". While these don't mandate consulting this guide with the same force as "Inbox:", they are strong indicators. The AI should confirm if the user wishes to use the formal inbox capture process detailed here.
  - **Example AI Dialogue (for "Idea:"):** "That's an interesting idea. Would you like me to formally capture it in the project inbox using the standard procedure?"
- **AI Identifies an "Open Loop":** During a discussion or while working on a task, the AI might identify a related but out-of-scope item.
  - **Example AI Dialogue:** "That's a good point about [related item]. It seems outside the immediate scope of story `sXXX`. Would you like me to capture it in the inbox for later review using the standard process?"
- **User Expresses a Fleeting Idea (without explicit cue):** The user mentions something in passing that seems valuable but isn't immediately actionable in the current context.
  - **Example AI Dialogue:** "You mentioned [fleeting idea]. That sounds interesting. Shall I add it to the inbox so we don't lose it?"

**Key Principle:** When a user begins their input with "Inbox:" (case-insensitive), the AI **MUST** follow this guide. For other indications of a desire to capture a thought, the AI should offer to use this formal process. In all cases, be proactive but not intrusive in offering to capture items to maintain focus on the primary task.

## 2. Process for Creating an Inbox Item

Once a thought is identified for capture:

1.  **Determine Content to Capture:**
    - If the user initiated with the "Inbox:" cue (e.g., "Inbox: [thought content]"), the content following the cue forms the basis of the text to be captured. **No further confirmation of this initial text is needed before proceeding to enrich it.**
    - If capture was initiated through other means (e.g., AI suggestion, less direct user phrasing), briefly confirm with the user the exact core text to be captured:
      - **AI:** "Okay, I'll capture: '[confirmed thought content]'. Is that correct?"
2.  **Generate Filename:**
    - **Date Stamp:** Obtain the current UTC date in `YYYY-MM-DD` format.
      - **Priority Method:** If the AI has access to the current UTC date via `SYSTEM INFORMATION` or has reliably fetched and cached it earlier in the current session, use this information directly.
      - **Fallback Method (if date not readily available or needs refresh):** Execute a system command.
        - **Linux/macOS:** `date -u +%Y-%m-%d`
        - **Windows (PowerShell):** `Get-Date -UFormat %Y-%m-%d`
      - The AI **MUST** ensure it uses the correct command for the user's operating system if resorting to the fallback method.
    - **Descriptive Slug:** Create a highly descriptive, kebab-case slug from the core captured content (before AI enrichment). The slug **SHOULD** start with a verb indicating the primary action or intent of the inbox item.
      - Remove punctuation, convert to lowercase, replace spaces with hyphens.
      - Prioritize maximum descriptiveness, including an action verb (e.g., `create-`, `update-`, `research-`, `fix-`), over brevity to aid later identification. Don't be afraid of longer slugs if they add clarity.
      - **Example:** If user input was "Inbox: ADR for guide discovery", a good slug might be `create-adr-for-ai-guide-shell-command-discovery-mechanism`. If the thought was "Update the existing s068 journal with more detail", a slug could be `update-s068-journal-with-retrospective-notes`.
    - **Combine:** Form the filename: `inbox/YYYY-MM-DD-descriptive-slug.md`.
3.  **Prepare Content (Enriched Raw Text):**
    - The content of the file should be the captured thought, enriched by the AI to be self-contained and understandable later.
    - **If the user provided an "Inbox:" cue (e.g., "Inbox: [shorthand idea]"):**
      - Take the user's [shorthand idea] as the core.
      - Leverage your understanding of the current conversation and context to expand on this shorthand, ensuring the captured note clearly articulates the underlying idea, task, or point. Include any immediately relevant context that a future reader (human or AI) would need.
      - The goal is to capture the _meaning and intent_, not just the literal words of the cue. The user will have an immediate opportunity to review and correct the AI's interpretation as the new file will typically open in their editor.
    - **If capture was AI-initiated or from less direct user phrasing:**
      - Use the confirmed text (from step 1) as the basis.
      - Similarly, add any necessary context from the current discussion to make the note comprehensive.
    - **General Principles for Content:**
      - The content should be natural language prose (plain text or simple Markdown).
      - No specific internal structure (like YAML frontmatter) is required or prescribed.
      - Aim for clarity and completeness so the item can be understood on its own during later processing.
      - Example: If user says "Inbox: ADR for guide discovery", the AI might write: "Create an ADR to document the decision and rationale for the shell-command-based AI Guide indexing and discovery mechanism, as discussed during story s068. This ADR should cover why this method was chosen over alternatives and its consequences."
4.  **Write to File:** Use the `write_to_file` tool to create the new Markdown file in the `inbox/` directory with the prepared content.
    - The `write_to_file` tool will create the `inbox/` directory if it doesn't already exist (though it should, along with its `README.md`, as per `adr-028`).
5.  **Confirm Capture (Post-Write):** Inform the user that the item has been captured.
    - **Example AI Dialogue:** "Okay, I've captured that as `inbox/[filename]`." (If user used "Inbox:" cue).
    - **Example AI Dialogue:** "Okay, I've captured '[thought content with enrichment]' as `inbox/[filename]`." (If content was confirmed and enriched).

### 2.1. Handling Immediate User Follow-up

After an inbox item has been written and confirmed (e.g., "Okay, I've captured that as `inbox/[filename]`."), the AI assistant should be sensitive to the user's next utterance.

- **If the user's immediate follow-up appears to be a clarification, addition, or refinement of the thought just captured:** The AI should offer to update the _newly created_ inbox file.
  - **Example AI Dialogue:** "I see. Would you like me to add that detail to the `inbox/[filename]` we just created?"
  - If the user confirms, the AI should use appropriate file modification tools (e.g., `apply_diff` or `insert_content`) to update the existing inbox item.
- **If the user's follow-up is clearly a new, unrelated request or a direct instruction to act on something else:** The AI should proceed as it normally would for a new interaction.

This allows the user to iteratively refine a captured thought with the AI's help, ensuring the inbox item is as complete as needed before moving on. The AI should avoid prematurely interpreting a follow-up as an instruction to execute the captured task or as an entirely new, unrelated command.

### 2.2. Handling Tool Use Interruptions

If a user initiates an "Inbox:" capture request (as per Section 1) while you (the AI assistant) have a tool use pending (e.g., an `execute_command` or `apply_diff` that has been sent but not yet confirmed by the user), you should be aware of the following:

- **Potential UI Artifacts:** The user's action of sending a new "Inbox:" message might cause the user interface to report the pending tool use as "rejected" or "cancelled." This may be a UI artifact due to the interruption and not necessarily a deliberate rejection of the tool use itself by the user.
- **Prioritize Inbox Capture:** Your immediate priority is to process the user's "Inbox:" request according to this guide (Sections 2 and 2.1). Complete the capture of the inbox item as described.
- **Resume Interrupted Task:** Once the inbox item has been successfully captured and confirmed (e.g., "Okay, I've captured that as `inbox/[filename]`."), you **MUST** then address the interrupted tool use.
  - **Clarify and Re-propose:** Inform the user that you are now returning to the previously pending task.
    - **Example AI Dialogue:** "Now that I've captured your inbox item, I'll return to the previous task. Before you sent the 'Inbox:' message, I was about to [describe the pending tool use, e.g., 'execute the command to list files']. Shall I proceed with that now?"
  - **Retry if Appropriate:** If the user confirms, re-issue the original tool use. If the original tool use involved complex parameters or context that might have been lost, briefly re-confirm those before re-issuing.

This approach ensures that user-initiated inbox captures are handled promptly while preventing prior pending actions from being silently dropped due to UI interruptions. This behavior was noted as important during story s087.

## Example Interaction Flow

**User:** "Inbox: ADR for guide discovery"

**AI (Roo):** _(Internally determines current UTC date, e.g., `2025-06-08`)_
_(Internally generates a highly descriptive slug including a verb, e.g., `create-adr-for-ai-guide-shell-command-discovery-mechanism`)_
_(Prepares enriched content based on current context, e.g.: "Create an ADR to document the decision and rationale for the shell-command-based AI Guide indexing and discovery mechanism, as discussed during story s068. This ADR should cover why this method was chosen over alternatives and its consequences. This was captured during our discussion about s068 and the need to formalize the guide discovery process.")_
_(Uses `write_to_file` with path `inbox/2025-06-08-create-adr-for-ai-guide-shell-command-discovery-mechanism.md` and the enriched content)_
_(The file `inbox/2025-06-08-create-adr-for-ai-guide-shell-command-discovery-mechanism.md` opens in the user's editor, showing the enriched content.)_
"Okay, I've captured that as `inbox/2025-06-08-create-adr-for-ai-guide-shell-command-discovery-mechanism.md`."

## Conclusion

Following this guide will ensure that emergent thoughts are captured reliably and consistently into the Vibe Tasking `inbox/`, ready for later processing. The key is low-friction capture of a contextually complete thought, clear communication with the user, and adherence to the defined file naming convention (prioritizing descriptive slugs that include an action verb).
