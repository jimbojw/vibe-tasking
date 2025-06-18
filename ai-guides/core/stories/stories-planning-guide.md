---
id: "stories-planning-guide"
title: "Guide: Collaboratively Planning Vibe Tasking Stories"
usage: "Use this guide when assisting users in the 'Planning' phase of the Vibe Tasking workflow to collaboratively translate their intentions into well-structured story files (story.md and journal.md)."
tags: "stories;planning;workflow;collaboration;templates;acceptance-criteria;lightweight-stories"
---

# Guide: Collaboratively Planning Vibe Tasking Stories

**(Primary Audience: AI Assistant (for collaboratively assisting users in planning and creating new Vibe Tasking stories).)**

## Introduction: AI as a Planning Partner

This guide outlines a collaborative approach for assisting users in the "Planning" phase of the Vibe Tasking workflow. Your role is not merely to fill a template, but to act as a **thinking partner**. The goal is to help users explore their ideas, clarify their objectives, and then collaboratively structure these into well-defined Vibe Tasking stories—be they standard or lightweight. This approach is inspired by principles similar to David Allen's Natural Planning Method, focusing on starting with purpose, envisioning outcomes, brainstorming, and then organizing to define actionable steps.

This process emphasizes a conversational start, allowing the user to "braindump" context. You will then use your understanding of Vibe Tasking structures and common patterns to:

1. Synthesize this information and suggest appropriate story types (Research, Design, Implementation) and formats (Standard or Lightweight).
2. Collaboratively determine and verify the core YAML frontmatter for the story.
3. Draft the full story content (description, artifacts, Acceptance Criteria) based on the preceding discussions.
4. Write the initial story files to disk.
5. Iteratively refine the written story files with the user in their editor.

## Core Principle: Adherence to Story Structure and Templates

**Before proceeding with planning, you MUST thoroughly familiarize yourself with:**

1.  The **[`Story Structuring Guide`](stories-structuring-guide.md)**: This document explains the conventions, purpose of fields, and overall methodology for stories.
2.  The **Core Story Templates** (co-located in this directory):
    - [`story.template.md`](story.template.md): The definitive starting point for new standard `story.md` files.
    - [`lightweight-story.template.md`](lightweight-story.template.md): The definitive starting point for new lightweight `story.md` files.
    - [`journal.template.md`](journal.template.md): The definitive starting point for all new `journal.md` files.

These resources are the canonical sources for all story file structure, directory naming conventions, YAML frontmatter fields, `story.md` content requirements, and `journal.md` formatting. All stories created **MUST** ultimately be formalized using these templates and adhere to the conventions described in the [`Story Structuring Guide`](stories-structuring-guide.md).

## The Collaborative Planning Flow

The planning process is envisioned in distinct, yet fluid, phases:

### Phase 1: Collaborative Story Conceptualization

This phase is about understanding the user's raw intent and initial thoughts.

**Step 1.1: Open-Ended Context Gathering**

Initiate the conversation by inviting the user to freely share their ideas for the new story. Avoid premature structuring or direct questions about story "type" at this very initial stage.

- **Example AI Prompt:** "I understand you'd like to create a new story. I can certainly help with that! To start, why don't you tell me a bit about what you have in mind? You can share as much or as little detail as you feel is necessary, and we can refine it together."
- Listen actively to the user's "braindump." Encourage them to elaborate on key points if needed.

**Step 1.2: AI Synthesis and Initial Proposal**

Once the user has provided their initial thoughts, synthesize the information and offer a preliminary interpretation. This is where you start to gently guide towards structure.

- **Analyze User Input:** Based on the user's description, try to infer:
  - The primary goal or problem to be solved.
  - The likely nature of the work (e.g., is it about finding information, designing something, or building/fixing something?).
  - The potential complexity or scope.
- **Formulate a Concise Summary and Proposal:**
  - **Example AI Dialogue:** "Thanks for sharing that. From what you've described, it sounds like the main goal is to [concisely restate the core objective]. Does that sound right as a starting point?"
  - If the initial input is clear enough, you might also tentatively suggest a type and format: "Based on that, it seems like this might be a [Lightweight/Standard] [Research/Design/Implementation] story focused on [brief summary]. What are your thoughts on that initial direction?"

**Step 1.3: Discussing Story Type (Research, Design, Implementation) and Format (Standard vs. Lightweight)**

Engage in a discussion to collaboratively determine the most appropriate story type and format.

- **If the user agrees with your initial proposal (from Step 1.2):** Proceed to Phase 2.
- **If the user is unsure, or your initial proposal needs adjustment:**
  - Briefly explain the primary Vibe Tasking story types if clarification is needed:
    - **Research:** Gathering information, exploring solutions, investigating issues. Outputs are typically documented knowledge or proofs-of-concept.
    - **Design:** Synthesizing findings into specifications or plans (e.g., ADRs, technical designs, UI mockups).
    - **Implementation:** Building or modifying software/systems based on a design or clear requirement.
  - Introduce the concept of **Standard vs. Lightweight Stories**:
    - **Standard Stories:** Best for more complex tasks with multiple phases or numerous distinct ACs. They use the full multi-checkpoint structure defined in [`story.template.md`](story.template.md).
    - **Lightweight Stories:** Ideal for simple, single-focus tasks with one primary deliverable or AC (e.g., "fix a typo," "update a version number"). They use the streamlined "Combined Checkpoint" structure from [`lightweight-story.template.md`](lightweight-story.template.md). Refer to [`docs/adrs/adr-029-lightweight-story-type.md`](../../../docs/adrs/adr-029-lightweight-story-type.md) for the full ADR.
  - **Guiding Questions for Format Choice:**
    - "What distinct steps or deliverables do you envision for this?"
    - "Is this a straightforward task with one main outcome, or does it involve several stages?"
  - **Handling Lightweight Story Intent (as per ADR-029):**
    - The _request_ or _intent_ to create a "lightweight" story during this planning phase signals to you to consider the [`lightweight-story.template.md`](lightweight-story.template.md).
    - Assess if the task's scope is genuinely suitable. If it seems too broad for a single checkpoint, advise the user: "It sounds like there are a few distinct parts to this. A full story structure with separate checkpoints might be better to track this clearly. Shall we use the standard story template instead?"
    - The optional `lightweight` tag in the `tags:` field is for later categorization/discovery and is applied _after_ planning if a lightweight structure is chosen.

### Phase 2: Collaborative Frontmatter Definition & Verification

After Phase 1, you have a shared understanding of the story's intent, type, and format. This phase focuses _exclusively_ on defining and verifying the YAML frontmatter for the new story in chat.

**Step 2.1: AI Proposes Frontmatter Fields**

Based on the collaborative understanding from Phase 1:

- Determine the next sequential story `id` (e.g., `sXXX`) and a descriptive `slug`.
- Propose a `title`.
- Propose initial `tags` (including `lightweight` if a lightweight story was decided upon in Phase 1).
- Propose an initial `priority`.
- The `status` will default to `"To Do"`, and `resolution` to `"Unresolved"`.

**Step 2.2: AI Presents Frontmatter for User Verification**

Present **only the drafted YAML frontmatter fields** to the user in the chat:

- **Example AI Dialogue:** "Okay, based on our discussion for the new [Standard/Lightweight] [Research/Design/Implementation] story, here's the proposed frontmatter:
  - ID: `sXXX-slug`
  - Title: `Proposed Title`
  - Status: `To Do`
  - Priority: `Medium` (or as discussed)
  - Tags: `tag1;tag2` (as discussed, potentially including 'lightweight')
  - Resolution: `Unresolved`
    Please review these core metadata details. Do they accurately capture the story's identity?"

**Step 2.3: User Verification and Refinement of Frontmatter (in Chat)**

- The user reviews your proposed frontmatter.
- The user provides feedback _only on the frontmatter fields_. This might involve:
  - Confirming the frontmatter looks good.
  - Requesting changes to the slug, title, tags, or priority.
- Incorporate this feedback, potentially re-presenting the frontmatter in chat until the user is satisfied with these metadata fields.
- If major misunderstandings about the story's core identity surface here, the conversation might loop back to Phase 1.

### Phase 3: AI-Drafted Story Body, File Creation, & Iterative Refinement

Once the user approves the frontmatter (Step 2.3), proceed to draft the story body, create the files, and then iterate on their content with the user in their editor.

**Step 3.1: AI Drafts Story Body Content (Description, Artifacts, ACs)**

Based on the **approved frontmatter** from Phase 2 and the **full context from Phase 1**:

- Draft the `Description` section, incorporating the user's input from Phase 1.
- Draft the `Artifacts` list (or a placeholder).
- **Crucially, draft a set of initial Acceptance Criteria (ACs):**
  - For **Standard Stories**: Propose logical **Checkpoints** and populate them with common/suggested ACs based on the story type (Research, Design, Implementation), using [`story.template.md`](story.template.md) as a guide for process ACs and typical substantive AC patterns.
    - _Example AC Patterns for AI to draw upon when drafting:_
      - **Research:** `- [ ] Research findings documented in [link].`, `- [ ] [Question 1] answered.`, `- [ ] User confirms findings are comprehensive.`
      - **Design:** `- [ ] Design document [link] created.`, `- [ ] Design addresses [requirement].`, `- [ ] User confirms design is clear and complete.`
      - **Implementation:** `- [ ] [Feature X] implemented per [spec].`, `- [ ] Tests pass.`, `- [ ] User confirms functionality.`
      - **Testing New Methodologies/Features (Especially AI Guides):** If the story introduces a new methodology, workflow, user-facing feature, or particularly a new **AI Guide**, it is crucial to add ACs to test its usability and effectiveness in practice. For example:
        - `- [ ] The new [methodology/feature/AI Guide] is tested with a practical scenario (e.g., for an AI Guide, this might involve the AI attempting to follow the guide in a separate, simulated session).`
        - `- [ ] User confirms the new [methodology/feature/AI Guide] works as intended, is understandable, and achieves its purpose.`
  - For **Lightweight Stories**: Populate the "Core Task" AC and other process ACs within the "Combined Checkpoint" structure of [`lightweight-story.template.md`](lightweight-story.template.md).
  - The goal is a complete first draft of ACs, not just placeholders.

**Step 3.2: Formalizing the Story - Template Population and File Creation**

- Explicitly state which template will be used (`story.template.md` or `lightweight-story.template.md`).
- Populate the chosen template with:
  - The **approved frontmatter** from Phase 2.
  - The **AI's drafted `Description`** from Step 3.1.
  - The **AI's drafted `Artifacts` list** from Step 3.1.
  - The **AI's drafted `Acceptance Criteria` (including Checkpoints)** from Step 3.1.
- Populate [`journal.template.md`](journal.template.md) with an initial entry (ID, title, and you **MUST** inject the current date/time for the timestamp, plus a note about collaborative planning and template used).
- Determine the story directory name (using the approved `id`/`slug`).
- **Important for Submodule Users:** Ensure this new story directory is created in your host project's primary `stories/` directory, **not** within a Vibe Tasking submodule's own `stories/` directory (e.g., avoid `vendor/vibe-tasking/stories/`).
- Use tools to create the directory, `story.md` (with full drafted content), `journal.md`.

**Step 3.3: User Review of Written Files & Iterative Refinement**

- Inform the user: "Okay, I've created the initial story files using the approved frontmatter and my draft for the description and acceptance criteria: `stories/sXXX-slug/story.md` and `journal.md`. They should be open in your editor. Please take a look at the full content."
- **This is the primary loop for detailed refinement of the description, ACs, and any other part of `story.md`.** The user reviews the actual files in their editor.
- The user provides specific feedback on the content of `story.md` or `journal.md`.
  - **Example User Feedback:** "In `story.md`, let's rephrase the third AC under 'Core Work' to..." or "The description needs to mention Y."
- Use tools (`apply_diff`, `insert_content`, etc.) to make the requested changes directly to the files.
- This cycle of (user reviews file -> user provides feedback -> AI modifies file) continues until the user is satisfied with the written story files.

### Phase 4: Concluding the Planning Session

This phase remains crucial for clear hand-off.

- **Planning for _this specific new story_ is now complete.**
- **DO NOT proceed to execute or work on the newly created story unless the user explicitly instructs you to do so.**
- **Clearly inform the user:** "The new story `sXXX-descriptive-slug` has been created and refined with its `story.md` and `journal.md` files, structured as a [Standard/Lightweight] story. What would you like to do next?"

This ensures user control over when work commences.

## General Principles for Collaborative Planning

- **Iterative Refinement:** Planning is rarely linear. Be prepared to revisit earlier points as new information emerges or understanding evolves, both during chat-based drafting and file-based refinement.
- **AI as a Knowledgeable Partner:** You understand Vibe Tasking structure, common story patterns, and potential ACs. Offer this knowledge proactively to help the user.
- **User is the Authority:** While you guide and suggest, the user's goals and decisions are paramount. Your role is to help them articulate and structure those decisions effectively within the Vibe Tasking framework.
- **Focus on Clarity:** Strive for clarity in the story's title, description, and ACs so that anyone (including a future AI or a different team member) can understand the work to be done.

## Further Reading / Related Links

- **[`Story Structuring Guide`](stories-structuring-guide.md):** (Essential Reading) Explains conventions, fields, and methodology.
- **Core Story Templates:**
  - [`story.template.md`](story.template.md)
  - [`lightweight-story.template.md`](lightweight-story.template.md)
  - [`journal.template.md`](journal.template.md)
- **[`docs/adrs/adr-029-lightweight-story-type.md`](../../../docs/adrs/adr-029-lightweight-story-type.md):** ADR defining Lightweight Stories.
- **[`Template Files Working Guide`](../template-files-working-guide.md):** Details on using templates.
- [`README.md`](../../../../README.md) (Project Overview)

## Conclusion

By embracing this collaborative, conversational approach to story planning, you can significantly enhance the process. Helping users to first explore their ideas, then collaboratively defining core metadata, followed by AI-drafting of the story body and iterative refinement of the written files, ensures that new Vibe Tasking stories are well-understood, clearly defined, and ready for effective execution.
