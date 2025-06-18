---
id: "inbox-processing-guide"
title: "Guide: AI-Assisted Inbox Processing"
usage: "Use this guide to systematically process items from the `inbox/` directory with AI assistance, following GTD principles."
tags: "inbox;processing;gtd;workflow;ai-assistant;automation;task-management"
---

# Guide: AI-Assisted Inbox Processing

**(Primary Audience: AI Assistant (for guiding users through inbox processing), User (for understanding the workflow).)**

## Introduction

This guide details the AI-assisted workflow for processing items captured in the project's `inbox/` directory. The goal is to systematically review each item, decide on its nature and next action (if any), and ensure the inbox remains clear and manageable. This process emphasizes AI as an intelligent partner, recommending actions based on its understanding of the inbox item and Vibe Tasking principles.

**Prerequisite Knowledge:** Before proceeding with this guide, it is **essential** that you, the AI assistant, have thoroughly read and understood the [`stories-planning-guide.md`](../../core/stories/stories-planning-guide.md). Many inbox items will result in the creation of new Vibe Tasking stories, and a strong understanding of the collaborative story planning process detailed in that guide is crucial for effectively triaging inbox items and initiating new stories correctly.
**Core Principle:** Once an inbox item is selected for processing, it is dealt with to a conclusion in that session (actioned, converted to a story, filed as reference, or trashed). It does not go back into the inbox.

## Workflow Steps

### 1. Initiation

Inbox processing is user-initiated.

- **User-Initiated:** The user might say:
  - "Let's process the inbox."
  - "What's in the inbox?"
- Upon initiation, you (the AI assistant) **MUST** perform an initial scan of the `inbox/` directory using `list_files` (excluding `README.md`) to build an internal list of all current inbox items. This list will be processed sequentially.

### 2. Item Retrieval and Presentation (Loop Start for each item)

1.  If your internal list of inbox items is empty:
    - **You:** "The inbox is currently empty." (Workflow concludes for this session).
    - Proceed to Step 5.
2.  Take the next item from your internal list. Initially, this should be the oldest item based on the `YYYY-MM-DD` date in its filename. If multiple items share the oldest date, process them alphabetically by filename.
    - **You:** "Processing next item: `[filename]`."
3.  Use the `read_file` tool to read the content of the selected inbox item and prepare a brief summary.
    - **You:** "Here's a summary of `[filename]`: `[one-line summary or a few bullet points of the inbox item content]`"

### 3. AI-Assisted Triage & Recommendation

After presenting the summary of the inbox item:

1.  **You (AI):** "Based on this summary: `[summary provided earlier]`..."
2.  **Internal Analysis by AI:**
    - Evaluate the item's clarity and apparent intent.
    - Consider if it aligns with creating a new Vibe Tasking story (standard or lightweight).
    - Determine if it suggests a "single-step" quick action (e.g., minor file edit, renaming).
    - Assess if it might be obsolete or unclear.
    - Check if it could be pure reference material for `docs/reference/`. If so, assess if its current raw state needs cleanup/reformatting to be suitable as a formal reference document. Also, check if similar reference materials already exist in `docs/reference/` that could serve as formatting templates.
    - Consult your AI Guide Index: Are there any host-project specific AI Guides or general documentation formatting guides that might define a particular way to handle this type of item or its content?
3.  **AI Recommends Action (Present one primary suggestion):**
    - **Example (Suggest New Story):**
      - **You:** "...this looks like it could be a new [standard/lightweight] story titled '[Proposed Story Title]'. The goal would be `[briefly state goal]`. To create this, I will initiate the story planning process, following the `stories-planning-guide.md`. Given we have context from this inbox item, we can likely streamline the initial conceptualization and move quickly to defining frontmatter (Phase 2 of the planning guide) after confirming the story type and format. Shall I proceed?"
    - **Example (Suggest Quick Simple Change - Single-Step Action):**
      - **You:** "...this seems to be a straightforward, single-step update to the file `[path/to/file.md]`. The change would be `[describe the change]`. Shall I attempt this using `apply_diff` (or `insert_content` / `search_and_replace`)?"
    - **Example (Suggest Item is Obsolete/Unclear):**
      - **You:** "...the intent of this item isn't immediately clear to me, or it might be outdated. My best interpretation is `[AI's interpretation]`. Do you agree this should be deleted, or would you like to clarify, or perhaps create a research story for it?"
    - **Example (Suggest Filing as Reference):**
      - **You:** "...this item seems to be reference material. Its current content is: `[briefly show/describe raw content if very short, otherwise refer to summary]`. I can clean this up, reformat it (potentially using existing documents in `docs/reference/` as a style guide, and consulting any relevant documentation guides), and save it to `docs/reference/[proposed_filename.md]`. Shall I proceed with that?"
      - **You (if it's a simple, single-step creation of a new reference doc):** "...this suggests creating a small reference document at `docs/reference/[proposed_filename.md]`. I can take the essence of the inbox item, format it appropriately (checking for similar existing documents as style guides), and write it there. This seems like a single-step action. Shall I proceed using `write_to_file`?"
    - **Example (Host-Project Specific Action):**
      - **You:** "...according to the host project's AI Guide `[host_guide.md]`, items like this are typically handled by `[host-specific process]`. Shall I proceed with that?"
4.  **User Confirmation:**
    - The user reviews your recommendation. They can:
      - **Accept:** "Yes, proceed."
      - **Reject/Refine:** "No, instead let's..." or "That's close, but let's adjust the story title to..."
      - **Pause/Stop:** "Let's stop processing for now."
    - If the user refines or rejects, engage in a brief clarification to arrive at one of the primary outcomes:
      - Create a new story (standard or lightweight).
      - Perform a quick, single-step action (AI executes).
      - File as reference material (AI cleans up, reformats, and moves/copies content).
      - Delete as obsolete.
      - Perform a host-project specific action (AI executes if capable).
    - If the user wishes to stop processing, proceed to Step 5.
    - _(Once a course of action is agreed for the current item, proceed to Step 4: AI Actions & Original Item Handling.)_

### 4. AI Actions & Original Item Handling

Based on the user's decision from Step 3 for the current item:

- **Trash it:**
  - Use `execute_command` with `rm inbox/[filename]` (or `del inbox\[filename]` on Windows).
  - **You:** "Okay, I've deleted `inbox/[filename]`."
- **Filed as Reference:**
  - _(AI performs necessary cleanup/reformatting of the inbox item's content, consulting relevant guides and using similar existing documents as style templates if available.)_
  - After using `write_to_file` or `insert_content` to save the refined information:
  - **You:** "The information has been cleaned up and saved to `[new_location]`. I will now delete the original `inbox/[filename]`."
  * _(AI proceeds to delete the original inbox item.)_
- **Actioned (Single-Step Quick Change):**
  - After the user confirms the single-step action is complete:
  - **You:** "That action is complete. I will now delete the original `inbox/[filename]`."
  * _(AI proceeds to delete the original inbox item.)_
- **Converted to New Story:**
  - After the story planning process has been successfully initiated:
  - **You:** "Okay, I've initiated the new story planning process. I will now delete the original `inbox/[filename]`."
  * _(AI proceeds to delete the original inbox item.)_
- After the action, remove the processed item from your internal list.

### 5. Workflow Loop and Conclusion

1.  **You:** "That item (`[filename]`) is processed."
2.  If your internal list of inbox items is not empty AND the user has not indicated they wish to stop:
    - Loop back to Step 2 (Item Retrieval and Presentation) for the next item.
3.  Else (internal list is empty or user stopped processing):
    - If your internal list is empty: **You:** "The inbox is now empty."
    - Else (user stopped with items remaining): **You:** "Okay, we'll pause inbox processing for now. There are still items remaining."
    - _(The workflow concludes for this session.)_

## Strategies and Considerations

- **Batch vs. One-by-One:** This workflow is designed for one-by-one processing to ensure each item gets appropriate attention.
- **Minimizing User Cognitive Load:** Your role as AI is to analyze the item, propose a clear course of action, and then reliably execute the agreed-upon steps. This includes handling necessary content cleanup for reference materials.
- **Configuration:**
  - The primary configuration is the existence of the `inbox/` directory itself.

## Example Interaction Snippet

**User:** "Let's process the inbox."

**AI:** "Okay, let's process the inbox. (Scanning `inbox/` with `list_files`...) I found these items: `inbox/2025-06-10-idea-for-new-logo.md`, `inbox/2025-06-11-fix-typo-in-readme.md`, `inbox/2025-06-12-raw-notes-on-api-auth.md`."
**AI:** "Processing next item: `inbox/2025-06-10-idea-for-new-logo.md`."
**AI:** "(Reading file and summarizing...) Here's a summary of `inbox/2025-06-10-idea-for-new-logo.md`: 'Suggests sketching out ideas for a new project logo, possibly with a Vibe theme.' "
**AI:** "Based on this summary: 'Suggests sketching out ideas for a new project logo, possibly with a Vibe theme.' ... this looks like it could be a new standard story titled 'Design New Project Logo Concepts'. The goal would be to brainstorm and sketch initial concepts for a new project logo, considering themes of collaboration and AI. To create this, I will initiate the story planning process, following the `stories-planning-guide.md`. Given we have context from this inbox item, we can likely streamline the initial conceptualization and move quickly to defining frontmatter. Shall I proceed?"
**User:** "Yes, that sounds good."
**AI:** "(Initiating story planning process...) Okay, I've initiated the new story planning process. I will now delete the original `inbox/2025-06-10-idea-for-new-logo.md`."
**User:** "Okay."
**AI:** "(Deleting file...) Okay, I've deleted `inbox/2025-06-10-idea-for-new-logo.md`."
**AI:** "That item (`inbox/2025-06-10-idea-for-new-logo.md`) is processed."

**AI:** "Processing next item: `inbox/2025-06-11-fix-typo-in-readme.md`."
**AI:** "(Reading file and summarizing...) Here's a summary of `inbox/2025-06-11-fix-typo-in-readme.md`: 'Pointed out a typo on line 42 of README.md, 'teh' should be 'the'.' "
**AI:** "Based on this summary: 'Pointed out a typo on line 42 of README.md, 'teh' should be 'the'.' ... this seems to be a straightforward, single-step update to the file `README.md`. The change would be to replace 'teh' with 'the' on line 42. Shall I attempt this using `apply_diff`?"
**User:** "Yes, please."
**AI:** "(Preparing and executing `apply_diff`...) The typo in `README.md` has been corrected. I will now delete the original `inbox/2025-06-11-fix-typo-in-readme.md`."
**User:** "Great."
**AI:** "(Deleting file...) Okay, I've deleted `inbox/2025-06-11-fix-typo-in-readme.md`."
**AI:** "That item (`inbox/2025-06-11-fix-typo-in-readme.md`) is processed."

**AI:** "Processing next item: `inbox/2025-06-12-raw-notes-on-api-auth.md`."
**AI:** "(Reading file and summarizing...) Here's a summary of `inbox/2025-06-12-raw-notes-on-api-auth.md`: 'Contains raw, unformatted notes about API authentication methods, including token types and refresh strategies.' "
**AI:** "Based on this summary: ...this item seems to be reference material. Its current content is raw notes. I can clean this up, structure it with appropriate Markdown headings and code blocks (consulting any relevant documentation guides and checking for similar existing reference files for style), and save it to `docs/reference/api-authentication-notes.md`. Shall I proceed with that?"
**User:** "Yes, that would be very helpful."
**AI:** "(Cleaning up content, formatting with Markdown, and using `write_to_file`...) The information has been cleaned up and saved to `docs/reference/api-authentication-notes.md`. I will now delete the original `inbox/2025-06-12-raw-notes-on-api-auth.md`."
**User:** "Excellent."
**AI:** "(Deleting file...) Okay, I've deleted `inbox/2025-06-12-raw-notes-on-api-auth.md`."
**AI:** "That item (`inbox/2025-06-12-raw-notes-on-api-auth.md`) is processed."
**AI:** "The inbox is now empty."
