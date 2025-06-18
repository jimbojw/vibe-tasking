---
id: "stories-spot-grooming"
title: "Guide: AI Spot Grooming for Vibe Tasking Stories"
usage: "Use this guide when an AI assistant needs to perform 'spot grooming' (initial due diligence and analysis) on a Vibe Tasking story, typically at story start-up or resumption in a new chat session, to verify its viability and currency."
tags: "stories;spot-grooming;due-diligence;validation;workflow;ai-assistant"
---

# Guide: AI Spot Grooming for Vibe Tasking Stories

**(Primary Audience: AI Assistant (to understand and execute the standard process for performing 'spot grooming' on Vibe Tasking stories).)**

## 1. Introduction

This guide details the standard methodology an AI assistant **MUST** follow when performing "spot grooming" on a Vibe Tasking story. Spot grooming is an initial due diligence and analysis process undertaken at story start-up or when resuming a story for the first time in a new chat session. Its purpose is to proactively verify the story's viability, currency, and the integrity of its linked resources before significant work commences.

This process is typically invoked by an Acceptance Criterion in the "Initial Story Setup" checkpoint of a story or by the AI's internal logic when resuming a story in a new session, as outlined in the `ai-ac-validation-process-design.md` artifact for story `s081`.

## 2. Core Principles of Spot Grooming

- **Proactive Analysis:** The AI takes the initiative to investigate the story's context and dependencies.
- **Due Diligence:** Ensure the story is based on up-to-date information and valid links.
- **Efficiency:** Identify potential issues (obsolescence, duplication, broken dependencies) early to save effort.
- **Collaborative Partnership:** Present findings and a proposed plan to the user for validation before making significant changes or proceeding with the story if major issues are found.

## 3. Spot Grooming Process Steps

The AI assistant **MUST** perform the following steps:

**Step 3.1: Understand Story Context**

1.  **Thoroughly Read `story.md`:**
    - Pay close attention to the `Description`, all `Acceptance Criteria (ACs)`, and any files/documents listed in the `Artifacts` section or linked elsewhere in the story.
2.  **Review `journal.md`:**
    - Scan the journal for historical context, previous decisions, reported issues, or open questions that might impact the story's current state or ACs.

**Step 3.2: Verify Linked Resources**

1.  **Identify All Links:** Systematically identify all explicit links within the `story.md` file. These may include links to:
    - Other Vibe Tasking stories (`stories/sXXX-slug/story.md`)
    - AI-Guides (`ai-guides/...`)
    - ADRs (`docs/adrs/...`)
    - Reference documents (`docs/reference/...`)
    - Story-specific artifacts (`artifacts/...` within the current story or other stories)
    - Source code files or directories within the project.
    - External URLs (less common in core story definitions but possible).
2.  **Check Link Validity:** For each internal project link:
    - Verify if the linked file or directory exists at the specified path using file system checking capabilities.
    - **Note:** If there are numerous links (e.g., more than 5), consider using a batch shell command (via `execute_command`) to check for the existence of all linked files/directories at once for efficiency, rather than checking them individually.
3.  **Handle Broken Links:**
    - If a link is broken (file/directory not found):
      - **Attempt to Find:** Perform a targeted search for the intended file in likely alternative locations. For example, if `docs/old-spec.md` is broken, look for `docs/specs/current-spec.md` or similar plausible variations based on common project structures.
      - **Note Findings:** Record the broken link and any potential correct path found.
4.  **Assess Link Context (Light Check):**
    - If a linked file exists, briefly assess if its nature aligns with the link's descriptive text or context. For example, if a link says "[Design Mockup]" but points to a `.txt` file, this might be worth noting. This is a superficial check, not a deep content analysis.

**Step 3.3: Quick Check for Obvious Story Overlap**

1.  **Review Current Story's Goal:** Briefly re-confirm the core objective of the current story from its `title` and `description`.
2.  **Consider Obvious Overlaps (Light Check):**
    - Based on your immediate awareness (e.g., stories worked on very recently, or highly memorable, similar titles you've encountered), quickly consider if the current story's core objective might:
      - Directly duplicate another _active_ story you are aware of.
      - Have already been clearly addressed by a _very recently completed_ story you are aware of.
    - **This is intended as a brief sanity check, not an exhaustive search across all stories.** The goal is to catch immediately apparent conflicts with minimal overhead. Do not perform a full scan unless specifically requested by the user or if a very strong, immediate suspicion arises.
3.  **Note Concerns (If Any):**
    - If a clear and obvious overlap is immediately apparent, note this concern (e.g., "This story's goal to 'X' seems very similar to active story sYYY," or "The objective to 'Y' might have been covered by recently completed story sZZZ.").
    - If no such obvious overlap comes to mind quickly, it's okay to proceed.

**Step 3.4: Formulate Findings and Proposed Plan of Action**

1.  **Synthesize Information:** Consolidate all findings from the previous steps (link verification, obvious overlap check).
2.  **Develop a Proposed Plan:** For each issue identified, propose a specific, actionable step. Examples:
    - Broken link: "Propose updating link X to Y."
    - Potential duplicate/superseded story: "Reviewed story S123 (Done). It appears to [cover/not cover] the goals of the current story S456. Propose [closing S456 as duplicate / proceeding with S456 as distinct]."
3.  **Overall Assessment:** Provide a brief, high-level summary of the story's apparent health (e.g., "Overall, the story seems current, but with a few broken links to update." or "There are indications this story might be superseded by sZZZ.").

**Step 3.5: Present Analysis, Plan, and Seek User Validation**

1.  **Clearly Present Findings and Plan:** Communicate the summary of findings and the proposed plan of action to the user. Keep descriptions concise, as the user can refer to source files for full details.

    - **AI Dialogue Example (Illustrative - adapt to actual findings):**
      "Before we proceed with story `sXYZ - [Story Title]`, I've performed a spot grooming check and have a few findings and a proposed plan:

      - The link to `[old_document.md]` in AC 1.2 appears broken. I found `[new_document_path.md]` which seems to be the correct file. **I propose we update this link in `story.md`.**
      - I also reviewed story `sUVW - [Similar Story Title]`, which is 'Done'. Based on its description (summary of sUVW's scope), it seems to substantially cover the goals of this current story. **Therefore, I recommend we consider closing this story `sXYZ` as a duplicate.**
      - Overall, the remaining ACs seem [brief, high-level assessment].

      Do you agree with this plan: update the link and adopt my recommendation regarding closing this story as a duplicate? Or would you like to discuss any of these points further?"

2.  **Use `ask_followup_question` (or similar):** The AI **SHOULD** use an appropriate tool to get structured feedback on its proposed plan, offering clear options for the user to agree, disagree, or request modifications.
3.  **Execute Agreed-Upon Actions:** Based on user validation, perform the agreed-upon initial corrective actions (e.g., update links, mark story as closed if confirmed duplicate).
4.  **Proceed to AC Review (If Story Continues):** If the story is deemed active and initial fixes are made, then proceed to the detailed review of the (now potentially updated) ACs with the user, as outlined in the broader AI-Assisted AC Validation process.

## 4. Conclusion

By diligently following this spot grooming process, the AI assistant acts as a crucial first line of defense against working on outdated, incorrect, or redundant story information. This proactive due diligence enhances workflow efficiency and the overall quality of story execution within the Vibe Tasking framework.
