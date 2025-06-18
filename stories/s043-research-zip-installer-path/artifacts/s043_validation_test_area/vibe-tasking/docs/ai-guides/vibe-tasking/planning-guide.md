# Vibe Tasking: AI-Assisted Planning Guide

## Purpose / Introduction

This guide provides instructions and best practices for assisting users in the "Planning" phase of the Vibe Tasking workflow. Your role is to help users translate their intentions into well-structured Vibe Tasking story files (`story.md` and `journal.md`).

## Target Audience

AI Assistant

## Core Principle: Adherence to Story Structure

**Before proceeding, you MUST thoroughly familiarize yourself with the [Vibe Tasking - Story Documentation Guide](../../stories/README.md).** This document is the canonical source for all story file structure, directory naming conventions, YAML frontmatter fields, `story.md` content requirements, and `journal.md` formatting. All stories created during a planning session must meticulously adhere to these established conventions. Failure to do so will result in inconsistencies and hinder project management.

## Assisting with Story Creation: Overview

The "Planning" activity itself is best understood as a **meta-task**, similar to backlog grooming in Agile methodologies. It's the collaborative process between a user and an AI assistant (you) where future work is discussed, and new stories (for Research, Design, or Implementation) are identified, defined, and documented.

Your primary goal during a planning session is to help the user create well-defined `story.md` and `journal.md` files for the _actual work_ being planned. These files become the tangible output of the planning session.

**Typical Outputs of a Planning Session:**

- A new story directory (e.g., `docs/stories/sXXX-descriptive-slug/`).
- Inside this directory: `story.md`, `journal.md`, and an optional `artifacts/` directory.
- **All created files and directory structures MUST adhere to the [Vibe Tasking - Story Documentation Guide](../../stories/README.md).**

**Guidance for AI during Planning (Defining the _New_ Story's Acceptance Criteria):**
A key part of your role is to help the user define clear acceptance criteria for the _new_ story being planned. This involves structuring ACs using **Checkpoints** for major phases, with detailed individual ACs nested under them, as defined in the [Vibe Tasking - Story Documentation Guide](../../stories/README.md).

For _any_ newly planned story, ensure its creation process and initial setup are captured, perhaps as the first Checkpoint. For example:

- `- [ ] **Checkpoint: Initial Story Setup and Confirmation**`
  - `- [ ] User confirms the new story structure (directory, `story.md`, `journal.md`) and its initial content (title, description, proposed Checkpoints and ACs) accurately reflect the planned work and adhere to the Story Documentation Guide.`

_(Detailed example AC patterns for Research, Design, and Implementation stories are covered in Step 1 below. Your goal in Planning is to help populate these using the Checkpoint model, always following the canonical Story Documentation Guide.)_

## Step-by-Step Planning Assistance

### 1. Initiating the Planning Discussion & Identifying Story Type

When a user indicates they want to create a new story (or stories), start by clarifying the nature of the work. This will help tailor the story effectively.

- **Example First Question:** "Okay, I can help with that! To start, what kind of story or stories are you looking to write? Are we focusing on Research, Design, or Implementation? Understanding the main goal will help us define the story."

Be prepared to briefly explain these story types if the user is unsure:

- **Research (A Story Type):**

  - **Purpose:** To gather information, explore solutions, investigate issues, or understand existing systems. The outcome is knowledge, codified as documentation or proof-of-concept artifacts.
  - **Typical Outputs:** Documentation (e.g., in `docs/reference/` or `docs/guides/`), findings reports, root cause analyses, small test programs, API exploration scripts, "hello world" examples.
  - **Example Acceptance Criteria Pattern (for the new Research story's `story.md`):**
    - `- [ ] Research findings documented in [link to document/artifact].`
    - `- [ ] [Specific research question 1] answered and documented.`
    - `- [ ] [Specific research question 2] explored and findings recorded.`
    - `- [ ] (If applicable) Proof-of-concept code [link to code/artifact] created and demonstrates [specific capability].`
    - `- [ ] User confirms the research findings are comprehensive and clearly presented.`

- **Design (A Story Type):**

  - **Purpose:** To synthesize research findings, current state, and user goals into a specification or a plan for how something should be built or changed.
  - **Typical Outputs:** Architecture documents, design specifications, API designs, UI mockups, database schemas, Architecture Decision Records (ADRs). These are often stored in dedicated subdirectories within `docs/` or as artifacts within a story.
  - **Example Acceptance Criteria Pattern (for the new Design story's `story.md`):**
    - `- [ ] Design document [link to document/artifact] created, detailing [specific aspects of the design].`
    - `- [ ] The design addresses [key requirement 1] and [key requirement 2].`
    - `- [ ] (Optional, but recommended) Alternative approaches, potential unforeseen benefits---focusing on positives and value---and potential risks/pitfalls---focusing on caution and critical judgment---of the proposed design have been explored and documented.`
    - `- [ ] (If applicable) ADR created for [significant design decision].`
    - `- [ ] Diagrams/mockups illustrating the design are included.`
    - `- [ ] User confirms the design specification is clear, complete, addresses explored alternatives (if any), and meets the objectives.`

- **Implementation (A Story Type):**
  - **Purpose:** To carry out a design intent, bringing a specification into being. This usually involves writing, testing, and deploying code, or configuring systems.
  - **Typical Outputs:** Working software, deployed features, configured infrastructure, passing tests, updated application code.
  - **Example Acceptance Criteria Pattern (for the new Implementation story's `story.md`):**
    - `- [ ] [Feature X] implemented according to [link to design specification].`
    - `- [ ] All unit and integration tests for [Feature X] pass.`
    - `- [ ] Code reviewed and merged into the main branch.`
    - `- [ ] (If applicable) [Feature X] deployed to [environment].`
    - `- [ ] User confirms [Feature X] functions as expected and meets the requirements.`

### 2. Gathering Story Details & Suggesting Metadata

Once the type of work for the new story is generally understood, guide the user in populating its `story.md` file. **All structural and formatting details for `story.md` (including YAML frontmatter, Markdown title, sections like Description, Artifacts, and Acceptance Criteria) MUST follow the [Vibe Tasking - Story Documentation Guide](../../stories/README.md).**

- **Suggest Defaults & Conventions (in accordance with the Story Documentation Guide):**
  - `id`: Propose based on the directory naming convention (e.g., `s016-new-user-dashboard`).
  - `title`: Suggest a concise, human-readable title.
  - `status`: Default to `"To Do"`. (The AI should be aware of all statuses, including `"Closed"`, as defined in `docs/stories/README.md`, but new stories typically start as `"To Do"`).
  - `priority`: **Default to `"Medium"**. Explain that this can be changed if needed.
  - `tags`: Suggest relevant, semicolon-separated tags (e.g., `"feature;ui;backend"`).
  - `resolution`: Default to `"Unresolved"`. Explain that this field is always present and will track the story's outcome or reason for its terminal state.
  - Ensure the user is aware that all frontmatter string values must be in double quotes and each field on its own line, as per the `docs/stories/README.md`.
  - Remind the user that the full list of recommended `status` and `resolution` values and their interactions are detailed in `docs/stories/README.md`.
- **Confirm with User:** After outlining the proposed `story.md` structure (referencing the Story Documentation Guide for specifics) and suggesting frontmatter: "We will structure the `story.md` for this new [Research/Design/Implementation] story according to the project's Story Documentation Guide. For the metadata, I suggest: [list key suggestions like ID, title, default status/priority, and default resolution]. Does this sound like a good starting point, or would you like to adjust these initial values?"

### 3. Defining Acceptance Criteria for the New Story (Using Checkpoints)

This is a crucial step. Based on the identified story type (Research, Design, or Implementation), guide the user in formulating clear, actionable, and testable acceptance criteria for the _new story_, structured using **Checkpoints**.

- **Structure with Checkpoints:** Help the user break down the story into major phases or logical groupings of work. Each of these will become a **Checkpoint** (a bolded, top-level AC item).
- **Detail with Nested ACs:** Under each Checkpoint, list the specific, verifiable Acceptance Criteria (ACs) required to complete that phase. These are the items that will be individually checked off.
- **Use Example Patterns:** Adapt the example AC patterns provided in Step 1 to fit this Checkpoint model. For instance, a "Design" story might have Checkpoints like "**Checkpoint: Define Core Requirements**", "**Checkpoint: Draft Initial Design Document**", "**Checkpoint: Review and Refine Design**", each with their own nested ACs.
- **Standard Process Checkpoints:** Incorporate standard process steps as Checkpoints or ACs within Checkpoints, as recommended in `docs/stories/README.md`. This includes an initial Checkpoint for story setup confirmation and a final one for overall review and closure.
  Example of an initial Checkpoint:
  ```markdown
  - [ ] **Checkpoint: Initial Story Setup and Confirmation**
    - [ ] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work (once work actually begins on this story, not during planning).
    - [ ] **Process:** An initial journal entry is added to journal.md for this story, noting work has commenced (similarly, when work begins).
    - [ ] **Process:** User confirms the overall Acceptance Criteria list (including all Checkpoints and nested ACs) for this story is accurate and complete before substantive work begins on later Checkpoints.
  ```
- Ensure nested ACs include user confirmation for substantive deliverables and, where applicable, validation/testing steps.

### 4. Crafting the Story Description

Help the user write a concise description for the new `story.md` file. This should clearly state the goal of the story, often using the "As a [user type], I want [action] so that [benefit]" format, followed by any necessary details.

### 5. Creating the Initial Journal Entry for the New Story

For the new `journal.md` file, the first entry should include:

- The current date.
- A brief note about this planning session that led to the story's creation, and any key points not captured in the `story.md` itself.

### 6. Asking Context-Enhancing Questions

To avoid overwhelming the user, ask clarifying questions **one at a time** and keep them **limited in number (2-4 questions are often sufficient)** to gather the core information needed for the new story. Focus on questions that will directly help in populating its `story.md` (especially the description and acceptance criteria).

Examples of good follow-up questions (after the initial type-of-work question):

- "Could you describe the main goal or outcome you're hoping for with this [Research/Design/Implementation] story?"
- "What are the key things that need to be true for you to consider this story 'Done'?"
- "Are there any specific artifacts (documents, code, etc.) that will be produced or modified by this story?"

### 7. Concluding the Planning Session & Awaiting Next Steps

**Crucial Final Step for AI Assistant:**

Once the new story directory, `story.md`, and `journal.md` files have been successfully created according to the user's direction and Vibe Tasking conventions:

- **Your role in planning _this specific new story_ is now complete.**
- **DO NOT proceed to execute or work on the newly created story unless the user explicitly instructs you to do so.**
- **Clearly inform the user that the story has been created and you are awaiting their next instruction.** For example: "The new story `sXXX-descriptive-slug` has been created with its `story.md` and `journal.md` files. What would you like to do next?"

This step is critical to ensure that the user retains control over when work on a new story actually commences. The planning phase concludes with the _definition_ of the story, not its immediate execution, unless otherwise specified by the user.

## General Principles

- **Iterative Refinement:** Be prepared to go back and forth. The user might refine their thoughts as you ask questions.
- **User is the Authority (with a Caveat):** While the user's stated goals are primary, your broad training might offer valuable alternative perspectives or solutions they haven't considered. After understanding their initial request for a new story, you can offer to explore these. For example: "I understand your goal for this new story is [restate goal]. Based on that, we can proceed with creating a story for [proposed task]. Alternatively, if you're open to it, we could briefly discuss other approaches like [mention a high-level alternative, e.g., 'using an existing library for X' or 'a different architectural pattern for Y'] that might also meet your needs. Would you like to explore that, or shall we focus on the current plan for this story?" This empowers the user to leverage your knowledge without derailing their initial intent.
- **User is the Authority:** The user's input is paramount. Your role is to guide and structure, not to dictate.

## Further Reading / Related Links

- **[Vibe Tasking - Story Documentation Guide](../../stories/README.md):** (Essential Reading) This is the canonical source for all story file structure, naming conventions, YAML frontmatter fields, and `story.md` content requirements. You **must** be familiar with and adhere to this guide.
- `README.md` (Project Overview)

## Conclusion

By following this guide, and meticulously adhering to the [Vibe Tasking - Story Documentation Guide](../../stories/README.md), you can effectively assist users in the planning phase, ensuring that new Vibe Tasking stories are well-defined, correctly structured, and ready for action.
