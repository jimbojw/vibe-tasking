# Vibe Tasking: Core Mechanics and Usage Scenarios

**(Primary Audience: Software engineers familiar with the concepts in "The Vibe Coding Journey" and "Agile Reimagined: Applying Timeless Principles to AI-Centric Development", being brought up to speed on Vibe Tasking.)**

## Introduction

To get the most out of this article, you should already have a grasp of modern "vibe coding"; for background, please see [The Vibe Coding Journey](vibe-coding-journey.md). You should also have a reasonably firm understanding of Agile development principles and their applicability to AI-centric development, as described in [Agile Reimagined: Applying Timeless Principles to AI-Centric Development](agile-ai-development.md).

Now, we'll walk through the core mechanics of the Vibe Tasking approach. You'll learn how Vibe Tasking prescribes methods for context initialization, providing AI guidance, and managing work in the form of structured user stories. This leads naturally into the next article, '[Understanding Vibe Tasking Story Structure](understanding-vibe-tasking-story-structure.md)'.

## The Three Pillars of Vibe Tasking

This section delves into the three fundamental components—the core—of the Vibe Tasking framework:

1.  **Context Initialization:** Using a primary `CONTEXT.MD` file.
2.  **AI-Guides:** A collection of instructional documents for the AI.
3.  **Stories:** Structured units of work, akin to agile user stories.

Understanding these pillars is key to appreciating how they interoperate to create a structured and effective environment for AI-assisted development, which we will see in action in the subsequent scenarios.

### Context Initialization: The `CONTEXT.md` File

The `CONTEXT.md` file (or a similarly purposed document, as the name is a convention) serves as the primary bootstrapping mechanism for AI assistant chat sessions. At the highest level of your project, the `CONTEXT.md` file sits alongside other key files:

```text
your-project-root/
├── CONTEXT.md
├── README.md
└── ... (other project files and directories like ai-guides/, stories/, src/, docs/, etc.)
```

The core role of `CONTEXT.md` is to provide immediate, essential orientation to the AI. This typically includes:

- **Links to Crucial Documents:** Pointers to foundational project information, such as the main `README.md`, key architectural diagrams, or critical AI-Guides.
- **Meta-Guidance:** Instructions on how the AI can discover more specific guidance for various scenarios, often by directing it to the `ai-guides/` directory and explaining how to use guide frontmatter (like `title` and `usage`) for discovery.
- **Project Ethos or High-Level Directives:** Any overarching principles or operational notes the AI should always keep in mind while assisting on the project.

The following sequence diagram shows the beginning of a new chat session.

_Note: In most such sequence diagrams you'll see a single lifeline for the AI assistant, labeled "AI". Here we separate out the AI's client extension ("AI UX") from the back-end large language model ("LLM") providing tokens._

```text
┌──────┐                  ┌───────┐              ┌─────────┐         ┌─────┐
│ User │                  │ AI UX │              │ FS/Repo │         │ LLM │
└──────┘                  └───────┘              └─────────┘         └─────┘
   │                          │                       │                 │
   ├─1. "@CONTEXT.md"────────►│                       │                 │
   │                          │                       │                 │
   │                          ├─2. Read CONTEXT.md───►│                 │
   │                          │                       │                 │
   │                          ├─3. Prompt & Context Content────────────►│
   │                          │                       │                 │
   │                          │◄---4. Initial Response------------------│
   │                          │                       │                 │
   │◄---5. Rendered Response--│                       │                 │
   │                          │                       │                 │
   │                          ├─6. Read README.md────►│                 │
   │                          │                       │                 │
   │                          ├─7. README.md Content───────────────────►│
   │                          │                       │                 │
   │                          │◄---8. Query Response--------------------│
   │                          │                       │                 │
   │◄---9. Query Choices------│                       │                 │
   │                          │                       │                 │
```

1.  **"@CONTEXT.md":** User begins a chat session with the AI UX—the VSCode extension. The User's message consists of just the literal string `@CONTEXT.md`.
2.  **Read CONTEXT.md:** The high-functionality AI assistant plugin interprets the `@` as a signal to read the named file and include it in the LLM prompt.
3.  **Prompt & Context Content:** In addition to a system propmt, the model receives the literal string `**CONTEXT.md**` as the text prompt (double-asterisk, bolded Markdown), along with the attached file content.
4.  **Initial Response:** The model interprets the User's request as a prompt to read the `CONTEXT.md` file and does so. Its response includes:

- Thoughts (if it's a thinking model),
- Answer text for the User, and
- A `read_file` tool invocation for required additional reading, such as for the `README.md` file.

5.  **Rendered Response:** The User sees, first, the model's thoughts (if provided and supported by the AI UX) and then the rendered inital response text (Markdown).
6.  **Read README.md:** The AI UX honors the LLM's `read_file` tool invocation and loads the `README.md` file content from the file system.
7.  **README Content:** The LLM receives the output of the `read_file` tool call, which includes the `README.md` file content.
8.  **Query Response:** Having read the `CONTEXT.md` document and required additional linked documents (`README.md`), the LLM respons with a query to the User about next steps.
9.  **Query Choices:** The AI UX presents the query to the User, either as rendered Markdown, or perhaps as a multiple-choice question.

Note that in this example, the hypothetical `CONTEXT.md` file only links out to a single required document, the `README.md`. In actual use, the `CONTEXT.md` may link out to multiple required documents, which would lead to more round-trips of reading files and loading them, perhaps even transitively.

By consistently loading this context at the start of a session, you prime the AI assistant with the necessary foundational knowledge and navigational Cues to operate effectively within the Vibe Tasking framework.

### AI-Guides: Empowering the Assistant

AI-Guides are specialized documents designed to provide AI assistants with explicit, task-specific operational instructions. They reside within the `ai-guides/` directory and are a cornerstone of enabling effective AI participation in complex project workflows.

Key characteristics of AI-Guides include:
A typical `ai-guides/` directory structure might look like this:

```text
your-project-root/
└── ai-guides/
    ├── README.md
    ├── core/
    │   ├── README.md
    │   ├── stories/
    │   │   ├── stories-planning-guide.md
    │   │   ├── stories-structuring-guide.md
    │   │   └── story.template.md
    │   └── template-files-working-guide.md
    └── contrib/
        ├── README.md
        ├── articles/
        │   ├── articles-writing-guide.md
        │   └── article.template.md
        ├── adrs/
        │   └── adrs-writing-guide.md
        └── command-output-issues-handling-guide.md
```

- **Location and Organization:** Found in `ai-guides/`, often with subdirectories for organizing specialized guidance.
- **Purpose:** To equip the AI with the knowledge to perform specific tasks, handle particular scenarios, or adhere to project conventions. This could range from how to format a commit message to steps for troubleshooting a common issue, or even how to author new AI-Guides.
- **Authorship:** Primarily written by and for AI assistants, though human users create and maintain them. The language and structure are optimized for AI comprehension.
- **Discoverability:** Each guide **must** include standardized YAML frontmatter containing at least `id`, `title`, and `usage` fields. The `usage` field is critical, as it describes when the guide should be consulted, enabling the AI to dynamically find relevant help. `tags` can further aid discovery.
- **Evolutionary Nature:** The collection of AI-Guides is a living system. As new tasks are identified, new challenges arise, or processes evolve, new guides are authored and integrated, ensuring the AI's knowledge base grows with the project.

By consulting these guides, the AI can perform tasks more autonomously, consistently, and accurately, reducing the need for repeated, detailed human instruction for common operations.

### Stories: Structuring the Work

Stories are the Vibe Tasking equivalent of user stories or tasks in Agile/Scrum methodologies, specifically adapted for collaborative completion by users and AI assistants. They represent discrete units of work within the project.

A typical `stories/` directory might look like this:

```text
your-project-root/
└── stories/
    ├── README.md
    ├── s001-initial-project-setup/
    │   ├── story.md
    │   └── journal.md
    ├── s002-design-new-api/
    │   ├── story.md
    │   ├── journal.md
    │   └── artifacts/
    │       └── api-design-v1.json
    └── s003-implement-feature-x/
        ├── story.md
        └── journal.md
```

Key aspects of Vibe Tasking Stories include:

- **Organizational Structure:** Each story resides in its own subdirectory within the main `stories/` directory. These subdirectories follow a consistent naming convention: `sXXX-descriptive-slug` (e.g., `s001-initial-project-setup`), where `XXX` is a sequential number. This ensures clear identification and ordering.
- **Core Files:**
  - `story.md`: This is the central document defining the story. It includes YAML frontmatter for metadata (like `id`, `title`, `status`, `priority`, `tags`, `resolution`), a detailed description of the task, and a checklist of acceptance criteria (ACs) structured into checkpoints.
  - `journal.md`: A chronological log of all activities, discussions, decisions, and progress related to the story. It provides a traceable history of the story's lifecycle.
- **Optional Artifacts:** An `artifacts/` subdirectory can be created within a story's directory to hold any relevant files produced or consumed by the story, such as scripts, data files, images, or small documents.
- **AI-Guided Processes:** The creation, structuring, planning, and execution of stories are themselves guided by specific AI-Guides (e.g., [`Story Structuring Guide`](@/ai-guides/core/stories/stories-structuring-guide.md), [`Story Planning Guide`](@/ai-guides/core/stories/stories-planning-guide.md), and [`Story Working Guide`](@/ai-guides/core/stories/stories-working-guide.md)). These ensure consistency and adherence to best practices.

Stories provide a structured and version-controlled way to define, manage, and track work, making them ideal for the iterative and collaborative nature of AI-assisted development.

## Vibe Tasking in Action: Illustrative Scenarios

To illustrate how these core components work in concert, let's consider a few common scenarios:

### Scenario 1: The AI Encounters a Novel Task

Consider the AI assistant is asked to perform a task for which it doesn't have an immediate, pre-programmed procedure, or a task that requires adherence to a specific project convention. For example, the user says, "We need to draft a new Architecture Decision Record (ADR) for the recent database change."

1.  **Task Analysis:** The AI identifies the core task: "draft a new ADR."
2.  **Guide Discovery (Triggered by `CONTEXT.MD` meta-guidance):** Recalling instructions from `CONTEXT.MD` about how to find help, the AI searches within the `ai-guides/` directory for guides related to "ADR," "architecture decision record," or "authoring."
3.  **Guide Selection:** It finds a guide, perhaps `ai-guides/contrib/adrs/adrs-writing-guide.md`, by examining its `title` ("Guide: Authoring Architecture Decision Records") and `usage` ("Use this guide for structuring and writing ADRs...").
4.  **Guided Execution:** The AI reads the selected guide and follows its instructions to collaborate with the user on drafting the ADR, using the specified template (e.g., `adr.template.md`) and adhering to the conventions outlined in the guide.

This scenario demonstrates how AI-Guides provide extensible, just-in-time knowledge, allowing the AI to handle new or specialized tasks effectively.

### Scenario 2: Planning and Executing a Development Story

This scenario illustrates the end-to-end lifecycle of a typical development task managed through Vibe Tasking.

1.  **Planning Phase (New Story Creation):**
    - The user decides a new feature is needed. They tell the AI, "Let's plan a new story for adding user profile avatars."
    - The AI, guided by `CONTEXT.MD` and potentially the [`Story Planning Guide`](@/ai-guides/core/stories/stories-planning-guide.md), collaborates with the user to:
      - Define the story's `id`, `title`, `status` (initially "To Do"), `priority`, and `tags`.
      - Write a clear description and acceptance criteria in a new `story.md` file (e.g., `stories/s042-user-profile-avatars/story.md`), using the standard template.
      - Create an initial `journal.md` entry.
2.  **Working Phase (Story Execution):**
    - Later, the user instructs the AI: "Let's start working on story `s042-user-profile-avatars`."
    - The AI reads `stories/s042-user-profile-avatars/story.md` and `journal.md` to understand the task and its current state.
    - It consults relevant AI-Guides (e.g., for coding standards, API usage, or even the [`Story Working Guide`](@/ai-guides/core/stories/stories-working-guide.md) itself) as needed to complete the acceptance criteria.
    - As work progresses (e.g., code is written, designs are drafted), the AI updates the `journal.md` with progress notes and marks off completed ACs in `story.md`. If artifacts are produced, they are saved in the `artifacts/` subdirectory.
3.  **Completion and Review:**
    - Once all ACs are met, the AI updates the story `status` to "Done" (or "In Review" if applicable) and records the `resolution` in `story.md`.
    - The `journal.md` reflects the completion.

This scenario highlights how `CONTEXT.MD` sets the stage, AI-Guides provide procedural knowledge, and Stories provide the structured framework for defining, executing, and tracking work.

## Conclusion

With a foundational understanding of Vibe Tasking's core mechanics—Context Initialization, AI-Guides, and the high-level concept of Stories—you are now equipped to see how these pieces fit together.

The true workhorse of the Vibe Tasking framework is its **Stories** system. To delve deeper into how stories are planned, structured, and executed, including a look at the common archetypes of Research, Design, and Implementation stories, please proceed to our next article: [Understanding Vibe Tasking Story Structure](understanding-vibe-tasking-story-structure.md).

## Related Links

- [The Vibe Coding Journey](@/docs/articles/vibe-coding-journey.md)
- [Agile Reimagined: Applying Timeless Principles to AI-Centric Development](@/docs/articles/agile-ai-development.md)
