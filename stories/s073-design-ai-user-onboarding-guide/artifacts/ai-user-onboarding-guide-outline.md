# Outline: AI User Onboarding Guide

## 1. Introduction and Purpose

- **Purpose of this AI Guide:** To instruct an AI assistant on how to effectively onboard a new human user to the Vibe Tasking framework immediately after the user has installed it in their host project.
- **Goal of AI-Led Onboarding:** Help the user understand Vibe Tasking's core concepts, see its immediate value in their project, and collaboratively plan initial stories to achieve quick wins.
- **Primary Audience (of this AI Guide):** AI Assistant.
- **Beneficiary (of the onboarding process):** New Vibe Tasking human user.

## 2. AI's Role and Responsibilities During Onboarding

- Act as a knowledgeable and proactive guide.
- Explain concepts clearly and concisely.
- Listen actively to user's project context, goals, and challenges.
- Collaboratively plan, rather than prescribe.
- Aim to empower the user to start using Vibe Tasking independently.

## 3. Explaining Core Vibe Tasking Concepts

- **Overall Methodology for Explaining Concepts (Interactive & User-Driven):**

  - **Primary Interaction Model:** Structure the explanation of core concepts as an interactive, menu-driven experience, heavily relying on the `ask_followup_question` tool. This emulates a "choose-your-own-adventure" or CLI `--help` style, allowing users to navigate and learn at their own pace.
  - **Initial Offer:** Proactively offer a high-level overview of the main Vibe Tasking components (e.g., `CONTEXT.md`, AI Guides, Stories).
  - **Menu-Based Navigation:**
    - After an initial overview, present main topics or components as a **Markdown bulleted list** in the AI's chat response preamble. Each list item should **begin with an emoji numeral followed by a period and a space (e.g., "- 1️⃣ Topic Name:")**.
    - Immediately follow this preamble with an `ask_followup_question`.
      - The `<question>` text should be concise, directly asking the user to choose from the preamble options. It **MUST** also include, after two newlines, an italicized reminder like: `_(Or enter any topic or other instruction in the chat box)_`.
      - The suggested `<suggest>` options **MUST mirror the emoji numerals and text of the preamble's list items (e.g., "1️⃣ Topic Name")**. This provides clear visual mapping for the user. Numbered suggestions should _only_ correspond to items listed in the immediately preceding preamble.
    - Each selected topic may lead to further sub-menus, also presented as bulleted lists with emoji numerals in the preamble, with corresponding emoji-numbered suggestions in the `ask_followup_question` (following the same question format with the italicized reminder).
    - **Contextual Drill-Downs (Optional & Unnumbered):** After explaining a topic, before presenting the standard "Back" navigation, the AI _may_ offer 1-2 `ask_followup_question` suggestions for a deeper dive into a specific aspect of the _current_ topic if appropriate. These suggestions should be unnumbered but prefixed with a page emoji (e.g., "📄 Tell me more about Dependency Chains") to give them visual weight consistent with other options. These should be distinct from the numbered menu options.
    - **Crucially, always include a navigation option (e.g., "⬅️ Back to [Previous Menu Level]" or "⬅️ Back to main topics") as one of the suggestions in sub-menus.** This option should clearly indicate its purpose. The italicized reminder in the question text covers the "type freely" aspect.
    - **For the top-level menu only, one of the `ask_followup_question` suggestions should be a clearly marked, non-numbered "Done Onboarding" option (e.g., "✅ Done Onboarding").** This option should not be listed in the preamble's numbered list of topics.
  - **Content Delivery:**
    - **Start with an H3 Header:** The explanation/preamble text delivered after a user selects a menu option **MUST** begin with a Markdown H3 header (e.g., `### AI Guides`) that provides a concise and meaningful title for the chosen topic. This provides clear signposting.
    - Keep explanations for each menu item (delivered in the preamble before the `ask_followup_question`) concise and focused.
    - Use further clear subheadings (H4, H5 if needed), and numbered or bulleted lists within these preamble explanations for readability.
    - Be mindful of cognitive overload; prioritize brevity for initial explanations.
  - **Deeper Dives:** For users wanting more detail than a brief chat explanation can provide:
    - Offer to provide a concise, potentially bulleted, summary of relevant sections from specific articles (e.g., [`docs/articles/agile-ai-development.md`](../../../../../docs/articles/agile-ai-development.md)) or AI Guides directly in the chat.
    - Always offer to provide direct links to these documents so the user can choose to read the full content themselves.
    - Explicitly ask the user their preference (e.g., "Would you like a brief summary in chat, or a direct link to the document, or both?").
  - **AI's Role:** The AI acts as a facilitator, guiding the user through the available information based on their choices and preferred learning style, rather than delivering a monolithic explanation.

- **Main Menu for Explaining Core Concepts (Top Level):**
  1.  **Stories (`stories/`)**
      1.  Overview (Purpose & Structure) - Explain how stories structure work, focus context, reduce AI error. Mention Agile/GTD philosophy (ref: [`docs/articles/agile-ai-development.md`](../../../../../docs/articles/agile-ai-development.md)). Explain directory structure (`stories/sXXX-slug/`) and core files (`story.md`, `journal.md`, optional `artifacts/`). Emphasize AI usually edits these files during story work.
      2.  Creating - How new stories are planned (AI will consult [`stories-planning-guide.md`](../../../../../ai-guides/core/stories/stories-planning-guide.md)).
      3.  Working on Stories
          1.  Process Overview - How work on a story is initiated and progresses (AI will consult [`stories-working-guide.md`](../../../../../ai-guides/core/stories/stories-working-guide.md)).
          2.  Change Management - User's role in reviewing AI changes (diffs) and managing Git workflow (stage, commit, push). (ref: [`docs/articles/implementing-vibe-tasking-stories.md`](../../../../../docs/articles/implementing-vibe-tasking-stories.md)).
      4.  Other Story Aspects (e.g., `journal.md` details, `artifacts/` usage - if user wants more detail after overview).
  2.  **AI Guides (`ai-guides/`)**
      1.  Overview - The concept, discovery process (mention `find` command they saw AI run if applicable, or that AI has an index).
      2.  Usage - How AI maps user queries to "usage" field in guide frontmatter, loads guides, and follows dependency chains.
      3.  Creating (moderate relevance, for later, AI consults `ai-guides-collaborative-designing-guide.md`)
  3.  **Other Key Vibe Tasking Elements**
      1.  `CONTEXT.md`
          1.  Overview - Purpose (ref: project [`README.md`](../../../../../README.md) for general description).
          2.  Usage (briefly, as user just did it).
          3.  Creating (low relevance for new user, but AI can ref `context-documents-authoring-guide.md` if asked).
      2.  `contrib/` Features (Optional)
          1.  Inbox (`inbox/`)
              1.  Overview - Concept of capturing emergent thoughts. (AI ready to review `inbox-capturing-guide.md` and `inbox-processing-guide.md`).
              2.  Creating - The "Inbox: " cue, its effect, and saving to Git.
              3.  Processing - Overview of "Let's process the inbox" and the guided workflow.
          2.  ADRs (`docs/adrs/`)
              1.  Overview - Concept of Architecture Decision Records.
              2.  Creating (AI will consult `adrs-writing-guide.md`).
          3.  Other `contrib/` guides (brief mention of availability if user explores).
      3.  General Documentation Structure (`docs/`)
          1.  Overview - Documentation for mixed user/AI audiences.
          2.  `docs/articles/` - Tutorial-like content for user education.
          3.  `docs/reference/` - Factual documents, research outputs.
  4.  Templates (`*.template.md`)
      1.  Purpose and usage of template files for stories, guides, etc. (ref: `template-files-working-guide.md`).
  5.  Temporary AI Output (`tmp_ai_output/`)
      1.  Briefly explain its use for capturing command outputs when direct streaming fails (ref: `command-output-issues-handling-guide.md`).
  - Offer to give a brief overview of the story planning process if the user is interested.
  - **Working on Stories (Highly Relevant):**
    - Explain that once a story is created, the user can instruct the AI to work on it.
    - The AI will consult the [`stories-working-guide.md`](../../../../../ai-guides/core/stories/stories-working-guide.md) for this process.
    - Offer to give a brief overview of how working on a story proceeds.

## 4. Handling Common User Questions/Misconceptions

- **Anticipate Common Questions (Examples):**
  - "Is this going to create a lot of extra work?" (Address by focusing on streamlining and clarity benefits).
  - "How is this different from [other project management tool/method]?" (Highlight Vibe Tasking's focus on AI collaboration and documentation-centric approach).
  - "Do I have to follow all these rules strictly?" (Explain core requirements vs. adaptable parts).
- **Response Strategy:**
  - Answer patiently and clearly.
  - Refer back to core concepts or relevant documentation if helpful.
  - **Sourcing Answers:**
    - Consult your **AI Guide Index** for relevant AI Guides.
    - For broader Vibe Tasking concepts or details (e.g., in `docs/articles/` or `docs/reference/`), **strongly prefer using `search_files`** to query these locations. `list_files` is unlikely to reliably show all files if Vibe Tasking is installed as a submodule, whereas `search_files` should still be effective for finding content within those directories.
    - If unable to find a definitive answer, be transparent with the user and offer to help them search or note it as a point for later clarification.
  - Emphasize the goal of making user-AI collaboration more effective.

## 5. Concluding the Initial Onboarding Session

- **Summarize:** Briefly recap what was covered and the initial stories planned.
- **Next Steps for User:** Suggest how the user can start working on the planned stories (potentially with AI assistance, referencing the `stories-working-guide.md`).
- **Offer Further Assistance:** Let the user know the AI is available to help with Vibe Tasking tasks.
