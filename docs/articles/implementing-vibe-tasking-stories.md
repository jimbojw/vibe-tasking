# Vibe Tasking in Action: Implementing stories

**(Primary Audience: New users who have just learned about story structure.)**

## Introduction

This article is for new users of Vibe Tasking. It assumes you are already familiar with how stories are defined and organized, as detailed in '[Understanding Vibe Tasking story Structure](understanding-vibe-tasking-story-structure.md)', which itself builds upon the foundational concepts in '[Vibe Tasking: Core Mechanics and Usage Scenarios](vibe-tasking-core-mechanics.md)'.

After reading this article, you will understand:

1.  How to discover available Vibe Tasking stories with your AI assistant.
2.  How to initiate work on a chosen story.
3.  The AI's role in preparing for and starting story implementation.
4.  The collaborative process of working through acceptance criteria (ACs) and checkpoints.
5.  How changes and feedback are handled during story execution.
6.  The steps involved in formally completing and closing a story.

We will illustrate these concepts by walking through the implementation of an example story, `s042-user-profile-avatars`, from start to finish. Let's begin by looking at how you kick off work on a story.

## 1. Finding Your Next Story: Discovering Available Stories

Before you can kick off work on a specific story, you first need to know what stories are available. Vibe Tasking provides a straightforward way for you to query your AI assistant for stories that are ready to be started.

### Asking for Available stories

Typically, after your AI assistant has been initialized with the project's [`CONTEXT.md`](../../CONTEXT.md) (which often includes guidance on how to find stories), you can simply ask:

> **User:** "What stories are currently 'To Do'?"
>
> Or perhaps: "Can you list the available stories for me?"

### How the AI Finds stories

Your AI assistant, leveraging its understanding of the Vibe Tasking structure, will then:

1.  **Search for story Definitions:** It will look within the `stories/` directory for all `story.md` files.
2.  **Filter by Status:** For each `story.md` file found, it will parse the YAML frontmatter to check the `status` field. It will specifically look for stories where `status: "To Do"`.
3.  **Present the List:** The AI will then present you with a list of these available stories, often including their ID and title.

> **AI:** "Okay, I found the following stories with 'To Do' status:
>
> - `s035-refactor-workflow-documentation` - Refactor Workflow Documentation
> - `s042-user-profile-avatars` - Implement User Profile Avatars
> - `s048-document-git-workflow` - Document Git Workflow for AI Collaboration"

Once you have this list, you're ready to choose a story and initiate work on it.

## 2. Kicking Off: Starting Work on a Story

The journey of implementing a Vibe Tasking story begins when you decide it's time to work on it. In this section, we'll cover how you signal this intent to your AI assistant and the preparatory steps the AI takes to get started.

### Signaling Your Intent

You'll typically inform your AI assistant by referencing the story's unique identifier. Often, just providing the numeric ID (e.g., `s042`) is enough, as the AI can usually locate the full story directory. For instance:

> **User:** "Let's start working on `s042`."

The AI assistant can then find the full story path, such as `stories/s042-user-profile-avatars`, by searching for a directory starting with `s042-` within the `stories/` directory.

This clear instruction prompts the AI to prepare for this work.

### AI's Preparation Routine

Upon receiving your request, a well-versed Vibe Tasking AI assistant will perform several preparatory steps:

1.  **Consult Key Guidance:** The AI will often first refer to the [`story Working Guide`](../../ai-guides/core/stories/stories-working-guide.md). This guide provides the AI with the standard procedures for collaborating on story implementation, ensuring a consistent approach.
2.  **Read the `story.md` File:** The AI reads the core definition of the story, for example, [`stories/s042-user-profile-avatars/story.md`](../../stories/s042-user-profile-avatars/story.md). This allows it to understand:
    - The `title` (e.g., "Implement User Profile Avatars").
    - The current `status` (e.g., "To Do", "In Progress").
    - The detailed `description`.
    - The all-important `ACs`, noting which, if any, are already marked complete.
3.  **Review the `journal.md` File:** The AI will also check the corresponding [`stories/s042-user-profile-avatars/journal.md`](../../stories/s042-user-profile-avatars/journal.md). This helps it understand:
    - Any previous work sessions.
    - Decisions made or context gathered earlier.
    - The last point of progress if the story was previously "In Progress".

With this information, the AI is ready to begin active collaboration.

## 3. The First Steps: Initial Engagement with Acceptance Criteria

Once prepared, the AI will typically focus on the first incomplete AC listed in the `story.md` file.

### Scenario: Starting a Brand New story

Let's assume `s042-user-profile-avatars` currently has a status of "To Do".

1.  **Updating Status:** The AI will propose updating the story's status.

    > **AI:** "Okay, I've reviewed `s042-user-profile-avatars`. The current status is 'To Do'. I'll update this to 'In Progress' in the `story.md` file."
    > The AI then modifies the `status: "To Do"` line to `status: "In Progress"` in the frontmatter of [`story.md`](../../stories/s042-user-profile-avatars/story.md). Then, it appends an entry to the [`journal.md`](../../stories/s042-user-profile-avatars/journal.md) file, noting the status update and that work is beginning on the story.

2.  **Confirming acceptance criteria:** Before diving into implementation, the AI will usually confirm the existing ACs with you.

    > **AI:** "As part of the 'Initial Story Setup' checkpoint for `s042-user-profile-avatars`, the next step is to ensure all ACs for the entire story are accurate and complete. The relevant process AC is:
    > `- [ ] **Process:** User confirms the overall ACs list for this story is accurate and complete before proceeding with substantive work checkpoints.`
    >
    > Could you please review all the currently defined ACs for `s042` in its `story.md` file? Let me know if they fully capture the requirements, or if we need to make any adjustments before we move on to the first substantive work checkpoint, which is 'Backend API Development'."

3.  **Incorporating User Feedback on ACs:** This is a crucial step. Perhaps since the story was planned, new considerations have emerged.

    > **User:** "Actually, let's add an AC for image validation to the backend checkpoint: `[ ] Uploaded images are validated for size and type.`"
    > The AI will then edit the [`story.md`](../../stories/s042-user-profile-avatars/story.md) file to include this new AC under the "Backend API Development" checkpoint.

4.  **Journaling AC Confirmations:** The AI will also record the confirmation of ACs (and any modifications made based on your feedback) in the [`journal.md`](../../stories/s042-user-profile-avatars/journal.md) file, creating a timestamped entry.

### Scenario: Resuming an "In Progress" story

If the story was already "In Progress", the AI would skip the status change and use the `journal.md` to pick up from the last point of activity, then proceed to confirm the next incomplete AC.

## 4. Making Progress: Iterating Through Checkpoints and Acceptance Criteria

With the initial setup complete, the process of implementing a story involves systematically working through its defined checkpoints. As detailed in the [`Story Working Guide`](../../ai-guides/core/stories/stories-working-guide.md), your AI assistant will typically address one checkpoint at a time, seeking your approval before starting each new one.

Within each active checkpoint, the AI will work to complete the specific ACs, pausing for your input or confirmation primarily when an AC explicitly requires user interaction, or upon completion of all ACs within that checkpoint.

### Addressing Individual ACs

For each AC, the AI will assist in its completion. This might involve writing code, drafting documentation, running tests, or performing other tasks as defined by the AC.

Once an AC is verifiably met:

1.  **Marking AC Complete:** The AI will update the [`story.md`](../../stories/s042-user-profile-avatars/story.md) file by changing the AC's checkbox from `- [ ]` to `- [x]`.

    > **AI:** "The API endpoint for avatar upload is now created and tested. I've marked the AC '- [x] API endpoint for avatar upload is created.' as complete in `story.md`."

2.  **Journaling Progress:** A corresponding entry is made in [`journal.md`](../../stories/s042-user-profile-avatars/journal.md), detailing what was done to complete the AC.

### Advancing Through checkpoints

As defined in the [`story Structuring Guide`](../../ai-guides/core/stories/stories-structuring-guide.md), ACs are often grouped into **checkpoints**. When all ACs within a checkpoint are completed:

> **AI:** "checkpoint 1: 'Backend API Development' is now complete. All its ACs have been addressed. Shall I proceed to the next checkpoint, 'Frontend Implementation'?"

This pause is vital. It gives you a chance to review the completed work for a logical phase before moving on, ensuring alignment and quality.

## 5. Handling Changes and Feedback Mid-story

Software development is dynamic. Requirements can evolve, or new insights might emerge even after a story has started.

If you realize an AC needs to be changed, added, or removed:

> **User:** "For the frontend, we also need an AC to ensure the avatar component is responsive on mobile devices."

The AI will:

1.  Update the AC list in [`story.md`](../../stories/s042-user-profile-avatars/story.md).
2.  Log this change and the reason in [`journal.md`](../../stories/s042-user-profile-avatars/journal.md).

The `journal.md` becomes an invaluable record for understanding why changes were made during the story's lifecycle.

## 6. Reaching the Finish Line: Completing a Story

Eventually, all ACs for all checkpoints will be marked as complete.

1.  **Final Review:** The AI will typically prompt for a final confirmation.

    > **AI:** "All ACs for `s042-user-profile-avatars` are now complete. Please review the implemented features. Are you satisfied that the story's goals have been met?"

2.  **Updating story Status:** Once you confirm, the AI updates the [`story.md`](../../stories/s042-user-profile-avatars/story.md) frontmatter:

    - `status` changes to `"Done"` (or perhaps `"In Review"` if your workflow includes a separate review step).
    - `resolution` is set appropriately (e.g., `"Implemented"`).

3.  **Final Journal Entry:** A concluding entry is made in [`journal.md`](../../stories/s042-user-profile-avatars/journal.md), noting the story's completion and final status.

The story `s042-user-profile-avatars` is now successfully implemented!

## 7. Managing Change: Your Role in Version Control

A notable aspect of the Vibe Tasking workflow is that version control (using tools like Git) remains entirely the user's responsibility. The AI assistant does not stage files, commit changes, or interact with your version control system. This is an intentional design choice.

### The Change Progression: From Suggestion to Merge

By managing commits and branches yourself, you maintain full control over the project's history and retain the crucial ability to revert to known good states if any AI-driven changes prove undesirable. The progression typically looks like this:

- **AI-Suggested Edit:** An ephemeral change proposed by the AI within the chat or a diff view, not yet applied to any file.
- **Filesystem Change:** The AI (or you, based on the AI's suggestion) modifies a file directly on your local filesystem.
- **Staged Change (Git):** You use `git add` to stage specific modifications from the filesystem, preparing them for a commit. While staging often immediately precedes a commit, these actions are decoupled. Maintaining in-progress work in the staging area provides a safety net, as you can revert changes in your working directory back to this staged state if needed. As AI makes further modifications to files, you can incrementally add validated changes to the staging area. This also allows you to diff the latest edits in your working directory against what you've already staged, providing a clear comparison of iterative AI contributions within the same story implementation.
- **Local Commit (Git):** You use `git commit` to save a snapshot of the staged changes to your local repository's history, often with a descriptive message. As long as this commit has not yet been pushed to a remote repository, it can also be amended (e.g., using `git commit --amend`) to incorporate further refinements before sharing.
- **Pushed to Feature Branch (Git):** You use `git push` to send your local commits from a feature branch to a remote repository (e.g., on GitHub, GitLab). This allows for collaboration, backup, and potentially automated checks or code reviews.
- **Merged to Main/Trunk (Git):** After review and approval (e.g., via a Pull Request or Merge Request), the changes from the feature branch are integrated into the main development line of the project.

Effectively managing this change progression is key to leveraging AI assistance while maintaining control and quality. Consider your own workflow and how you can best use tools like the Git staging area as an intermediary space to collect, review, and refine AI-generated modifications before committing them as a cohesive, validated set of changes.

### Auto-Approval: Dialing in AI Assistance

The ability to configure auto-approval for AI actions provides a valuable dial: you can allow more AI autonomy for speed on simpler modifications, or require explicit approval for each change when working on complex or critical sections, ensuring meticulous oversight.

## Conclusion

Working on Vibe Tasking stories is a collaborative dance between you and your AI assistant. You provide the direction, domain knowledge, and critical review, while the AI diligently manages the structural mechanics of the story files (`story.md`, `journal.md`), follows procedural guidance from AI-Guides, and assists with the implementation work. This structured approach ensures clarity, traceability, and allows both you and the AI to work together effectively to bring project features to life.

## Related Links

- [Understanding Vibe Tasking story Structure](understanding-vibe-tasking-story-structure.md)
- [`story Working Guide`](../../ai-guides/core/stories/stories-working-guide.md)
- [`story Structuring Guide`](../../ai-guides/core/stories/stories-structuring-guide.md)
- [`story Planning Guide`](../../ai-guides/core/stories/stories-planning-guide.md)
