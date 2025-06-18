# Onboarding Documentation Harmonization Plan (s042)

This document outlines the plan to harmonize the Vibe Tasking onboarding documents located in `docs/onboarding/`. The goal is to ensure a consistent structure, voice, flow, and navigation experience for the user.

**Files to Harmonize:**

- `docs/onboarding/README.md`
- `docs/onboarding/01-introduction.md`
- `docs/onboarding/02-prerequisites.md`
- `docs/onboarding/03-installation.md`
- `docs/onboarding/04-planning-stories.md`
- `docs/onboarding/05-working-with-stories.md`
- `docs/onboarding/06-example-walkthrough.md`
- `docs/onboarding/07-workflow-feature-lifecycle.md`
- `docs/onboarding/08-workflow-architectural-challenges.md`

## Harmonization Guidelines

### 1. Consistent Introductory Signposting (Per File)

**A. For `docs/onboarding/README.md` (The Main Index):**

- **Current:** Starts directly with "Welcome to Vibe Tasking! This onboarding guide provides a structured path..."
- **Plan:** Enhance the initial welcome.
  - Add a more engaging introductory paragraph before listing the documents, setting the stage for the entire onboarding journey and its benefits.
  - Briefly reiterate the primary goal of Vibe Tasking.

**B. For Numbered Files (`01-introduction.md` to `08-workflow-architectural-challenges.md`):**

- **Current:** Varies. Some have good introductions, others are more direct.
- **Plan:** Each numbered file should begin with a consistent introductory block immediately after the H1 title. This block should contain:
  - A sentence identifying the document: "This is document `0X - [Document Title]` in the Vibe Tasking onboarding sequence."
  - A concise one-sentence summary of what the reader will learn or achieve in this specific document.
  - For documents `02` through `08`: A brief mention of what the _previous_ document covered (e.g., "Previously, in [0X-1 - Previous Title](./0X-1-previous.md), we discussed...").
  - A brief mention of what the _next_ document will cover (e.g., "In this document, we will explore... Next, in [0X+1 - Next Title](./0X+1-next.md), you will learn about...").
- **Optional additions (if contextually valuable):**
  - "Key Takeaways:" (bullet list for complex docs).
  - "Who is this for?" (if not implicitly clear from the overall onboarding context).

### 2. Prominent and Consistent Navigation Links

**A. For `docs/onboarding/README.md`:**

- **Top:** No navigation links needed (it's the root).
- **Bottom:** Add a clear "Start Onboarding" link:

  ```markdown
  ---

  [Start Onboarding: 01 - Introduction to Vibe Tasking](./01-introduction.md)
  ```

**B. For Numbered Files (`01-introduction.md` to `08-workflow-architectural-challenges.md`):**

- **Current:** Mostly "Next Steps" at the bottom. No consistent "Previous" or "Up" links. No top navigation.
- **Plan:** Add identical navigation blocks at the **top** (immediately below the H1 title and introductory signposting block) and at the **bottom** (as the very last content) of each file.
  - **Template for Top/Bottom Navigation Block:**
    ```markdown
    ---
    [<< Previous: 0X-1 - PreviousTitle](./0X-1-previous.md) | [Up: Onboarding Home](./README.md) | [Next: 0X+1 - NextTitle >>](./0X+1-next.md)
    ---
    ```
  - **Adjustments:**
    - For `01-introduction.md`, there is no "Previous" link.
    - For `08-workflow-architectural-challenges.md`, the "Next" link might point back to the `README.md` or a concluding remark. (To be decided: for now, assume it might say "End of Onboarding Sequence" or similar if no explicit next).
    - Ensure all link paths and titles are accurate. The `---` provides visual separation.

### 3. Consistent Internal Section Signposting

- **Current:** Generally good use of headings.
- **Plan:**
  - Maintain consistent heading hierarchy (H1 for main title, H2 for major sections, H3 for sub-sections).
  - Use **bold text** for emphasis consistently and appropriately.
  - When a section refers to a concept detailed in another _onboarding_ document, provide an explicit link, e.g., "(as discussed in [02 - Prerequisites](./02-prerequisites.md))."
  - Ensure diagrams, code blocks, or important lists are briefly introduced with a sentence or two explaining their purpose or context.

### 4. Guidelines for Section Endings

- **Current:** Mostly okay, but some sections end abruptly with lists or code.
- **Plan:**
  - Review sections that end with lists, bullet points, or code blocks. If they feel abrupt, add a brief concluding sentence or a transition to the next section to improve flow.
  - The final content section of each numbered file (before the "Next Steps" section or bottom navigation links) should aim to provide a sense of closure for that document's topic and naturally lead the reader to expect the next step in their learning journey.

### 5. Approach for Subtly Indicating Target Audience

- **Current:** `01-introduction.md` has an explicit "Target Audience" section. Others imply it.
- **Plan:**
  - The introductory signposting paragraph (Guideline #1B) for each document should subtly reinforce who the document is for or what prior knowledge/context is assumed (e.g., "Building on your understanding of X from the previous guide...").
  - Avoid adding explicit "Target Audience:" sections to every document unless a particular document deviates significantly in its intended audience from the general onboarding flow.
  - Maintain a consistent instructional voice suitable for users who are new to Vibe Tasking but are technically proficient (e.g., developers, technically-minded PMs, or other AI assistants).

## Implementation Notes

- Changes will be applied file by file.
- The implementation within story `s042` will be structured into distinct, sequential Checkpoints, each focusing on a specific set of guidelines from this plan:
  - Checkpoint 1: Guidelines #1 (Introductory Signposting) & #2 (Navigation Links). (Completed)
  - Checkpoint 2: Guideline #3 (Consistent Internal Section Signposting).
  - Checkpoint 3: Guideline #4 (Guidelines for Section Endings).
  - Checkpoint 4: Guideline #5 (Audience/Voice Consistency).
- After all files are updated according to all guidelines, a final review will ensure cross-file consistency in links and tone.
