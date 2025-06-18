# Design: AI-Assisted Acceptance Criteria (AC) Validation Process

## 1. Introduction

This document outlines the proposed process for an AI assistant to proactively analyze and help a user validate and refine a Vibe Tasking story's Acceptance Criteria (ACs) when starting work on that story. The primary goal is for the AI to act as an intelligent partner, performing initial "spot grooming" to ensure ACs are current, relevant, complete, and that the story itself is still viable, especially for stories planned previously.

## 2. Trigger for AI-Assisted AC Validation

The AI-Assisted AC Validation process, including "spot grooming," is triggered in two main scenarios:

1.  **Initial Story Start-up (Primary Trigger):**

    - A **standard Acceptance Criterion (AC)** included within the "Initial Story Setup" checkpoint of standard story templates (or the "Combined Checkpoint" for lightweight stories) will explicitly direct the AI to perform this validation and spot grooming analysis when a story is first started (i.e., moving from "To Do" to "In Progress").

2.  **Story Resumption in a New Chat Session (Secondary Trigger):**
    - When a user requests to resume work on a story that is already `status: "In Progress"`, AND this is the _first time that specific story is being addressed within the current AI chat session_.
    - This ensures that if context has been lost due to a new session, the AI performs due diligence before continuing. If a story is paused and resumed multiple times _within the same chat session_, this secondary trigger would not repeatedly fire after the first resumption in that session.

The detailed methodology for _how_ the AI performs this analysis (the "spot grooming" steps) will be documented within a new, dedicated AI Guide, named `stories-spot-grooming-guide.md` (to be located in `ai-guides/core/stories/`). The [`stories-working-guide.md`](../../../../ai-guides/core/stories/stories-working-guide.md) will be updated to instruct the AI to consult this new guide at the appropriate trigger points. This current design document focuses on the _what_ and _why_ of the validation process itself and its intended flow.

This validation, prompted by either trigger, is **most critical** for stories:

- Created in a previous chat session.
- Where a significant amount of time may have passed since their creation or last review.
- Where the project context might have evolved since the story was planned.

For stories planned and started within the _same continuous chat session_, this explicit validation step, while still triggered by the AC, might be lighter, but the AI should still perform a brief check as guided by the `stories-working-guide.md`.

## 3. Proposed AI-Assisted AC Validation Steps

When triggered, the AI assistant will guide the user through the following steps:

**Step 3.1: AI Proactive Analysis ("Spot Grooming")**

The AI performs an initial analysis of the story and its context:

1.  **Understand Story:** Thoroughly re-reads the `story.md` (description, ACs, linked artifacts) and `journal.md` (for historical context).
2.  **Verify Linked Resources:**
    - For each link in `story.md` (to documents, code, other stories, artifacts):
      - Check if the linked file/resource exists at the specified path.
      - If a link is broken:
        - Attempt a quick search for the intended file in likely alternative locations (e.g., nearby directories, common doc/artifact locations).
        - Note the broken link and any potential new path found.
      - If a file exists, briefly assess if its nature aligns with the link's context (e.g., a link to "design spec" points to a Markdown file, not an image). (This is a light check, not a deep content review).
3.  **Check for Pre-existing Artifacts:**
    - If the story ACs mention creating specific artifacts (e.g., `artifacts/new-diagram.png`), check if files with those names or very similar names already exist in the story's `artifacts/` directory or other relevant locations.
4.  **Scan for Potential Obsolescence/Duplication:**
    - Briefly scan titles and statuses of other stories (especially those created more recently or with similar keywords) to identify:
      - Potential duplicate stories.
      - Stories that might have superseded the current one.
5.  **Formulate Initial Findings & Questions:** Based on the above, the AI prepares a summary of:
    - Any broken links found (and potential corrections).
    - Any artifacts to be created that seem to already exist.
    - Any potentially duplicate or superseding stories.
    - Any other immediate questions or observations about the ACs' clarity or apparent completeness based on this initial scan.

**Step 3.2: AI Presents Analysis, Proposes Plan, and Seeks Validation**

1.  **Present Analysis Summary & Proposed Plan:** The AI shares its findings from Step 3.1 and immediately proposes a plan to address them.

    - **AI Dialogue Example:** "Before we confirm the ACs for story `sXYZ - [Story Title]`, I've done a quick review and have a few findings and suggestions:

      - The link to `[old_document.md]` in the description appears broken. I found a similar file at `[new_document_path.md]`. **I propose we update this link in `story.md`.**
      - An AC mentions creating `[artifact_name.ext]`. A file with this name already exists in `artifacts/`. **I suggest we review this existing artifact to see if it fulfills the AC, potentially marking that AC as complete or adjusting it.**
      - I reviewed story `sUVW - [Similar Story Title]`, which is marked 'Done'. Based on its description (AI to provide a concise summary of sUVW's outcome/scope here), it appears [AI's assessment: e.g., 'to substantially cover the goals of this current story sXYZ.' OR 'to address a related but distinct issue.']. **Therefore, I recommend [AI's proposed action: e.g., 'we consider closing sXYZ as a duplicate.' OR 'we proceed with sXYZ as it seems distinct.'].**
      - Overall, the remaining ACs seem [AI to provide a brief, high-level assessment, e.g., 'clear', 'a bit vague on X', full details are in `story.md`].

      Do you agree with this plan: update the link, review the existing artifact, and adopt my recommendation regarding story `sXYZ` based on the review of `sUVW`? Or would you like to discuss any of these points further before we proceed to a detailed AC review?"

    - The AI **SHOULD** use a tool like `ask_followup_question` here, providing suggested responses like:
      - "Yes, that plan sounds good."
      - "Let's modify the plan regarding [specific point]."
      - "No, let's discuss [specific point] further before acting."

2.  **Execute Agreed-Upon Initial Actions:** Based on user validation of the plan (or a refined plan):
    - The AI performs the agreed-upon actions (e.g., updates links in `story.md` using `apply_diff`, reads the potentially duplicate story `sUVW` and presents a summary).
    - If these actions lead to the conclusion that the current story `sXYZ` is obsolete or fully duplicated, the AI will suggest updating its status (e.g., to "Closed", with an appropriate `resolution`) and, upon user confirmation, will do so. Work on the story might then conclude.
3.  **Present Current ACs (If Story Proceeds):** If the story is still deemed active after the initial actions and discussion, the AI then presents the (potentially revised by link updates, etc.) ACs.
    - **AI Dialogue Example:** "Okay, I've updated the link as we discussed, and it seems story `sUVW` covers a different aspect. Now, let's look at the current Acceptance Criteria for this story. I'll keep the descriptions brief, as the full details are in `story.md`:"
      ```
      * **Checkpoint: [Checkpoint 1 Name]**
          * [Concise summary of AC 1.1]
          * [Concise summary of AC 1.2]
          * **Process:** [Concise summary of Process AC for Checkpoint 1]
      * **Checkpoint: [Checkpoint 2 Name]**
          * [Concise summary of AC 2.1]
          * **Process:** [Concise summary of Process AC for Checkpoint 2]
      ...
      ```
4.  **General Prompt for Validity (Post-AI Analysis):**
    - **AI Dialogue Example:** "Considering our discussion and the AI's initial review, do these ACs now accurately reflect the remaining work needed? Are there any other adjustments, additions, or removals we should make?"

**Step 3.3: AI Facilitates Further Discussion on Specific ACs (Iterative)**

Based on the user's feedback, or if further clarification is needed:

1.  **Relevance & Obsolescence (Deeper Dive):**
    - **AI Prompt Example:** "For AC `[Specific AC]`, given [context from earlier discussion or AI finding], is it still fully relevant, or does it need modification?"
2.  **Clarity & Completeness:**
    - **AI Prompt Example:** "You mentioned AC `[Another Specific AC]` might be unclear. How can we rephrase it for better clarity, or what sub-steps might be missing?"
3.  **Potential New ACs:**
    - **AI Prompt Example:** "Based on our discussion about [topic], should we add a new AC to cover [new aspect]?"

**Step 3.4: AI Assists in Modifying ACs**

If the user identifies further changes:

1.  The AI helps the user articulate new or modified ACs.
2.  The AI updates the `story.md` file with the agreed-upon changes to the ACs.
3.  Each significant change to ACs is noted in the `journal.md`.

**Step 3.5: Confirmation of Finalized ACs**

1.  Once the review and all modifications are complete, the AI presents the finalized list of ACs.
2.  **AI Dialogue Example:** "Okay, here are the fully revised ACs (I'll present concise summaries). Please give them a final confirmation before we proceed with the first active checkpoint."
3.  User confirms.

## 4. Integration with Story Workflow

- This AI-assisted AC validation process becomes a standard part of the "Initial Story Setup" phase, as defined in the `stories-working-guide.md`.
- A new process AC will be added to the story templates (both standard and lightweight) under the initial setup checkpoint to ensure this validation occurs. E.g., "- [ ] **Process:** AI has performed an initial analysis of this story (links, artifacts, potential obsolescence) and assisted in reviewing and confirming the validity and completeness of all ACs."

## 5. Benefits

- Reduces the risk of working on outdated, irrelevant, or duplicate tasks.
- Ensures a shared understanding of "done" before work begins.
- Reinforces the AI's role as an active thinking partner and "spot groomer".
- Improves the quality and efficiency of story planning and execution.
- Proactively identifies potential issues with story dependencies or context.
