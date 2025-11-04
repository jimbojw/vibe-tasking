# Vibe Tasking

Vibe Tasking is a lightweight, **documentation-centric framework** using simple Markdown files to optimize user/AI assistant collaboration in software development. It provides a structured methodology for managing development tasks, project context, and AI-specific guidance, enhancing AI accuracy and streamlining workflows.

## How it Works

Vibe Tasking operates on three core pillars to create a structured and effective environment for AI-assisted development:

1.  **Context Initialization (`CONTEXT.md`):** A primary file at the project root (e.g., [`CONTEXT.md`](CONTEXT.md)) that bootstraps AI assistant chat sessions. It provides essential orientation, links to crucial documents, and meta-guidance on how the AI can discover more specific instructions.
2.  **AI-Guides (`ai-guides/`):** A collection of specialized instructional documents (e.g., [`ai-guides/core/stories/stories-structuring-guide.md`](ai-guides/core/stories/stories-structuring-guide.md)) designed to provide AI assistants with explicit, task-specific operational procedures and project conventions. These are discoverable via their YAML frontmatter. The guides within Vibe Tasking apply to any project using the framework; host projects can add their own `ai-guides/` directory to create custom guides or override the default ones.
3.  **Stories (`stories/`):** Structured units of work, akin to agile user stories (e.g., `stories/s001-initial-project-setup/story.md`). Each story is defined in its own directory and includes a `story.md` file (with metadata, description, and acceptance criteria) and a `journal.md` for logging progress. When you use Vibe Tasking in your project, a `stories/` directory will be created to house your project-specific work. _(Note: The [`stories/`](./stories) directory within the Vibe Tasking repository itself document its own development.)_

These components interoperate to enhance AI accuracy, streamline workflows, and foster a more effective user-AI partnership.

For a deeper dive into these concepts and their practical application, explore the articles in our **[docs/articles/](docs/articles/)** directory.

## Prerequisites & Installation

This section outlines the key prerequisites for your AI assistant's user interface (UX) and backend model, followed by installation notes.

### AI Assistant (User Experience - UX) Prerequisites

To effectively use Vibe Tasking, your AI assistant's UX (e.g., IDE plugin, chat interface) should ideally support:

- **Reading Arbitrary Project Files:** Essential for accessing `CONTEXT.md`, AI-Guides, and story files.
- **Executing Shell Commands:** Necessary for tasks that involve running scripts or build processes as part of story completion.
- **Backend Model Selection:** Allows choosing an LLM with appropriate capabilities (see below).

Known AI assistant systems that generally meet these core criteria include [Cursor AI](docs/reference/cursor-ai-capabilities.md), [Windsurf](docs/reference/windsurf-capabilities.md), [Cline](docs/reference/cline-capabilities.md), and [Roo Code](docs/reference/roo-code-capabilities.md). Refer to our [AI Assistant Capabilities Overview](docs/reference/ai-assistant-capabilities.md) for more details.

### AI Model (Backend) Prerequisites

Vibe Tasking relies heavily on providing comprehensive textual context and guidance to the AI. Therefore, the backend Large Language Model (LLM) should have a **Large Context Window**.

Ideally, it should support **hundreds of thousands of tokens** (e.g., 200k+). Models with smaller context windows may struggle to process the full context provided by Vibe Tasking documents, potentially leading to degraded performance or incomplete understanding.

### Installation

To integrate Vibe Tasking into your project using its dedicated AI-Assisted Installation Guide:

1. **Open Host Project:** Open your host project directory in your IDE.
2. **Start a New Chat:** Begin a new chat session with your configured AI assistant.
3. **Paste Installation Command:** Copy the entire text block below and paste it exactly as is into the chat input box, then press Enter:

```
Your immediate task is to act as an AI installation assistant. To begin, you must retrieve the operational guide from the following URL using an available tool or operating system specific command, such as `curl`:  
https://raw.githubusercontent.com/PAIR-code/vibe-tasking/refs/heads/main/INSTALL_VIBE_TASKING.md

If, for any reason, you cannot fetch the operational guide, you MUST inform me (the user) of the specific cause of the failure and then STOP. Do not attempt to proceed further or retry the command unless I explicitly instruct you to do so.

If the the operational guide was successfully retrieved, follow these critical instructions when processing it:

1.  **Embody the Role:** You ARE the AI assistant described in the guide.
2.  **Direct Speech:** When the guide contains lines like 'You (AI): "Hello there!"', you must say "Hello there!" directly to me (the user). **Crucially, you must OMIT the 'You (AI):' prefix itself from your spoken output.**
3.  **Execute Actions:** Follow all procedural steps, decision logic, and tool usage instructions outlined in the guide as if you are performing them.
4.  **Immediate Start:** Once the guide content is retrieved, begin your performance as the AI assistant immediately.

Proceed now. Execute the command and enact the guide.
```

Your AI assistant will then read and follow the instructions within `INSTALL_VIBE_TASKING.md`. This interactive process will:

1.  Verify necessary prerequisites (like `git` availability and project setup).
2.  Guide you in determining the correct installation path for the Vibe Tasking submodule, respecting any existing submodule conventions in your project.
3.  Execute the commands to initialize the Vibe Tasking submodule.
4.  Offer to help you create an initial `CONTEXT.md` file for your project, which is essential for using Vibe Tasking effectively. This step itself uses guidance from a document within the newly installed Vibe Tasking submodule.

Further steps, such as creating your first Vibe Tasking story, will typically occur in a new chat session after your `CONTEXT.md` file is in place and you invoke it. To begin an interactive onboarding session, you can ask your assistant a question like, "How do I get started with Vibe Tasking?"

## Why Vibe Tasking? (The Motivation)

In an era of "Vibe Coding"—heavy reliance on AI assistants—managing context effectively becomes crucial, especially as projects scale. Vibe Tasking addresses this by:

- **Enhancing AI Accuracy:** Provides explicit, relevant context to reduce incorrect AI "hallucinations."
- **Streamlining Workflow:** Minimizes AI guesswork and rework by clearly defining expectations.
- **Meticulous Context Management:** Establishes an infrastructure of stories, guides, and reference materials that act as "guardrails" for AI contributions.
- **Facilitating Context Recovery:** Structured journaling within stories helps quickly bring new AI chat sessions up to speed.

The core philosophy is that **"the AI knows everything, but not all at once."** Vibe Tasking uses version-controlled text files to direct the AI's focus, fostering a more effective user-AI partnership.

## Key Features

- **Flexible & Adaptable:** Provides a default story structure that can be easily adapted to your specific workflow and project needs, including a lightweight variant for simpler tasks.
- **Broadly Agnostic:** Works across various Operating Systems, IDEs, Version Control Systems, AI Assistant UIs (e.g., Cline, Cursor AI, Copilot), and AI Models (e.g., Claude, Gemini, ChatGPT).
- **Repository-Integrated:** Keeps all documentation directly within your project, version-controlled and accessible.
- **Markdown-Based:** Leverages the simplicity and readability of Markdown.
- **Extensible:** Lightweight core allows for easy extensions and custom tooling.

## Optional Contributed Features

Beyond the core pillars, Vibe Tasking offers several **contrib** features that host projects can adopt to further enhance their workflow and documentation practices. The `contrib` nomenclature signifies that these features contribute to the base Vibe Tasking approach but are not strictly necessary for its core functionality. These are typically found within the `ai-guides/contrib/` and `docs/` directories of the Vibe Tasking framework.

The best way to learn more about these `contrib` features is to install Vibe Tasking and ask your AI assistant about them.

- **Architecture Decision Records (ADRs):**

  - **Location:** `docs/adrs/`
  - **Purpose:** A formal way to document significant architectural decisions, their context, and consequences. Vibe Tasking provides templates and AI-Guides to assist in creating ADRs.
  - **Benefit:** Ensures key decisions are recorded, preventing re-litigation and providing historical context.

- **Reference Documentation:**

  - **Location:** `docs/reference/`
  - **Purpose:** A place to store detailed technical specifications, glossaries, or documentation on specific tools, capabilities, or project-specific information that doesn't fit neatly into an article or AI-Guide.
  - **Benefit:** Centralizes important reference material for both humans and AI assistants.

- **Articles:**

  - **Location:** `docs/articles/`
  - **Purpose:** User-focused documentation explaining concepts, providing guidance on using Vibe Tasking, or discussing best practices. Vibe Tasking includes templates and AI-Guides to assist in producing these.
  - **Benefit:** Offers in-depth explanations and tutorials for users to understand and leverage the framework effectively.

- **Inbox Mechanism:**
  - **Location:** `inbox/` (at the host project root, if adopted)
  - **Purpose:** A lightweight system for capturing emergent thoughts, ideas, or tasks that arise during development or conversation with an AI. Items in the inbox can then be processed systematically (e.g., converted to stories, filed as reference, or discarded). AI-Guides are available to instruct AI assistants on how to use this mechanism.
  - **Benefit:** Prevents good ideas from being lost and provides a structured way to handle ad-hoc inputs.

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project's documentation is licensed under the Creative Commons Attribution License 4.0. See the [LICENSE-CC-BY-4.0.txt](LICENSE-CC-BY-4.0.txt) file for details.

This project's source code is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards
Program](https://bughunters.google.com/open-source-security).
