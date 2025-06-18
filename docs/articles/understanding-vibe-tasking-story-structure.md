# Understanding Vibe Tasking Story Structure

**(Primary Audience: New users who have read the preceding articles in the Vibe Tasking series, particularly [`vibe-tasking-core-mechanics.md`](vibe-tasking-core-mechanics.md:1).)**

## Introduction

This article takes a deeper dive into the structure and components of Vibe Tasking Stories, building upon the concepts introduced in [Vibe Tasking: Core Mechanics and Usage Scenarios](vibe-tasking-core-mechanics.md). Stories are the fundamental units of work in Vibe Tasking, and understanding their structure is key to effectively collaborating with AI assistants to manage and execute project tasks.

Here, we'll explore the standard organization of story directories, the key files within them (`story.md` and `journal.md`), their typical content and formatting, and the role of associated templates. A recurring theme will be that while users guide the process, AI assistants are typically responsible for the mechanics of creating and maintaining these structured files.

Knowing how stories are structured then prepare you for the next article, '[Vibe Tasking in Action: Implementing Stories](implementing-vibe-tasking-stories.md)', which details how these stories are brought to life.

## Story Directory Structure: `sXXX-descriptive-slug`

Each Vibe Tasking story resides in its own dedicated directory within the main `stories/` folder. These directories follow a consistent naming convention:

`sXXX-descriptive-slug`

- **`sXXX`**: A prefix consisting of a literal 's' followed by a three-digit number (e.g., `s001`, `s042`).
  - The 's' prefix aids in discoverability, especially in AI assistant user interfaces that support `@` mentions for file/directory autocompletion (e.g., `@s001...`).
  - The numeric part provides easy identification and a natural ordering for stories.
  - Users can often simply type `sXXX` in a chat with an AI assistant to signal that they are referring to a specific story, prompting the AI to look up its details.
- **`descriptive-slug`**: A short, lowercase, hyphenated string that briefly conveys the story's primary purpose (e.g., `initial-project-setup`, `refactor-user-authentication`).

For example, a story focused on adding user profile avatars might reside in a directory named `stories/s042-user-profile-avatars/`.

A typical story directory might look like this:

```
stories/
└── s042-user-profile-avatars/
    ├── story.md
    ├── journal.md
    └── artifacts/  (optional)
        └── avatar-design-spec.png
```

This consistent structure ensures that stories are easy to find, reference, and manage.

## The `story.md` File: Defining the Work

The `story.md` file is the heart of every Vibe Tasking story. It contains all the essential information defining the task, its scope, and how to determine its completion. It adheres to a predictable format, typically based on the [`story.template.md`](../../ai-guides/core/stories/story.template.md) found in the `ai-guides/core/stories/` directory.

Key components of a `story.md` file include:

### 1. YAML Frontmatter

The file **must** begin with a YAML frontmatter block providing structured metadata. This allows for easy parsing, querying, and potential automation. Common fields include:

```yaml
id: "s042-user-profile-avatars"
title: "Implement User Profile Avatars"
status: "To Do" # Other values: "In Progress", "Done", "Closed", "Blocked"
priority: "High" # Other values: "Medium", "Low"
tags: "feature;ui;user-profile"
resolution: "Unresolved" # Becomes e.g., "Implemented" when status is "Done"
```

- `id`: A unique identifier, usually matching the story directory slug.
- `title`: A human-readable title for the story.
- `status`: The current workflow state of the story.
- `priority`: The story's priority level.
- `tags`: Semicolon-separated keywords for categorization and filtering.
- `resolution`: The outcome when a story reaches a terminal state (like "Done" or "Closed"). For active stories, it's "Unresolved".

### 2. Story Title (Markdown)

Following the frontmatter, a Markdown H1 heading displays the story ID and title, e.g., `# Story: s042-user-profile-avatars - Implement User Profile Avatars`.

### 3. Description

This section provides a clear narrative of the story, often in the "As a [user type], I want [action], so that [benefit]" format. It elaborates on the story's purpose and scope.

Example:

> As a registered user, I want to be able to upload and display a profile avatar, so that I can personalize my account and be more easily recognizable to other users.
>
> This involves adding an image upload component to the profile settings page and displaying the uploaded avatar in the site header and on my profile page.

### 4. Artifacts (Links)

A dedicated section lists and links to any relevant artifacts, such as design documents, technical specifications, or related code. This centralizes all associated information. Links can point to files within the story's `artifacts/` directory, other project files, or external URLs.

### 5. Acceptance Criteria (ACs) & Checkpoints

This is a critical section outlining the specific, verifiable conditions that must be met for the story to be considered complete. ACs are often grouped into **Checkpoints**, which represent major phases or logical groupings of work.

- **Checkpoints**: Bolded, top-level list items. A checkpoint is complete when all its nested ACs are done.
- **Acceptance Criteria (ACs)**: Detailed, verifiable tasks, marked with `- [ ]` (incomplete) or `- [x]` (complete).

Example:

> **Checkpoint 1: Backend API Development**
>
> - [ ] API endpoint for avatar upload is created.
> - [ ] API endpoint for avatar retrieval is created.
> - [ ] User authentication is enforced on both endpoints.
> - [ ] Unit tests for API endpoints pass.
>
> **Checkpoint 2: Frontend Implementation**
>
> - [ ] Image upload component is added to the profile settings page.
> - [ ] Uploaded avatar is displayed in the site header.
> - [ ] User confirms the avatar displays correctly.

Special process steps, like requiring user sign-off or validation, are often included as explicit ACs.

## The `journal.md` File: Logging Progress

The `journal.md` file serves as a chronological log for the story. It captures progress updates, decisions made, discussions, important notes, and any other relevant information accumulated throughout the story's lifecycle. This provides a traceable history.

Like `story.md`, the `journal.md` file typically starts from a template, [`journal.template.md`](../../ai-guides/core/stories/journal.template.md). Entries are usually timestamped and appended over time.

## The `artifacts/` Directory: Storing Related Files

Optionally, each story directory can contain an `artifacts/` subdirectory. This is a designated place to store any actual files related to the story, such as:

- Design mockups or sketches (e.g., `avatar-design-spec.png`)
- Small data files or test data
- Scripts used or produced during the story
- Text snippets or configuration examples

This keeps all story-specific assets organized and co-located with the story definition and journal.

## The AI-Driven Process: Your Role as Guide

It's important to reiterate that while understanding this structure is beneficial for users, you are generally **not expected to manually create or meticulously format these files**. This is a primary role of your AI assistant.

When you decide to create a new story, you'll typically engage your AI assistant in a conversation. Guided by your inputs and its knowledge of Vibe Tasking conventions (often from guides like the [`Story Planning Guide`](../../ai-guides/core/stories/stories-planning-guide.md)), the AI will:

1.  Prompt you for necessary details (title, description, ACs, etc.).
2.  Generate the story directory with the correct naming convention.
3.  Create the `story.md` and `journal.md` files, populating them based on your discussion and the standard templates.
4.  Manage updates to these files (e.g., marking ACs complete, adding journal entries) as you work through the story together.

Your role is to provide the vision, requirements, and clarifications, while the AI handles the structural mechanics.

## Conclusion

Vibe Tasking stories provide a robust and consistent framework for defining, tracking, and collaborating on project tasks with AI assistants. By understanding the standard directory structure, the purpose and format of `story.md` and `journal.md`, and the optional `artifacts/` directory, you can more effectively guide your AI partner. Remember that this structured approach is designed to empower the AI to manage the details, allowing you to focus on the substance of the work.

To learn how these structured stories are then brought to life, proceed to our next article: [Vibe Tasking in Action: Implementing Stories](implementing-vibe-tasking-stories.md).

## Related Links

- [Vibe Tasking: Core Mechanics and Usage Scenarios](vibe-tasking-core-mechanics.md)
- [`Story Structuring Guide`](../../ai-guides/core/stories/stories-structuring-guide.md) (for more detailed specifications)
- [`Story Planning Guide`](../../ai-guides/core/stories/stories-planning-guide.md)
