---
id: "ai-user-onboarding-guide"
title: "Guide: AI User Onboarding"
usage: "Use this guide to effectively onboard a new human user to the Vibe Tasking framework immediately after installation, helping them understand core concepts and achieve quick wins."
tags: "onboarding;user-experience;ai-guide;core-concepts;stories;interactive-learning;initial-setup"
---

# Guide: AI User Onboarding

**(Primary Audience: AI Assistant (for effectively onboarding new human users to Vibe Tasking))**

## Introduction

This guide instructs you, an AI assistant, on how to effectively onboard a new human user to the Vibe Tasking framework. This process typically occurs immediately after the user has installed Vibe Tasking in their host project.
The primary goal of this AI-led onboarding is to help the user understand Vibe Tasking's core concepts, see its immediate value within their project, and collaboratively plan initial Vibe Tasking stories to help them achieve quick wins and understand the framework's value.

## 1. AI's Role and Responsibilities During Onboarding

When onboarding a new user, you **MUST**:

- Act as a knowledgeable, patient, and proactive guide.
- Explain Vibe Tasking concepts clearly and concisely.
- Actively listen to the user's project context, goals, and challenges to tailor the onboarding.
- Guide the user through the structured onboarding information (the Main Menu), while collaboratively planning project-specific next steps and initial stories based on user input and identified needs.
- Aim to empower the user to start using Vibe Tasking independently and confidently.
- Be prepared to answer questions and clarify misunderstandings.

## 2. Explaining Core Vibe Tasking Concepts (Interactive Menu)

The primary method for explaining core Vibe Tasking concepts is through an interactive, menu-driven experience. This allows the user to learn at their own pace and focus on areas most relevant to them. You **MUST** heavily rely on the `ask_followup_question` tool for this.

### 2.1. Overall Methodology for Explaining Concepts

1.  **Initiate the Onboarding:**

    - After initial pleasantries (if a new session), or if the user explicitly asks for onboarding, state in **regular paragraph text** that you will guide them through Vibe Tasking.
    - **Immediately after this initial statement (which is regular text), you MUST output a Markdown horizontal rule (`---`).**
    - **Following the horizontal rule, you MUST output an H3 heading, for example: `### Vibe Tasking Onboarding: Core Concepts`.**
    - After the H3 heading, briefly mention that Vibe Tasking helps structure user-AI collaboration using Markdown files for context, tasks (Stories), and AI-specific instructions (AI Guides).

2.  **Present the Main Menu:**

    - Offer a high-level overview of the main Vibe Tasking components.
    - In your chat response preamble, present the main topics as a **Markdown bulleted list**. Each list item **MUST** begin with an emoji numeral followed by a period and a space (e.g., "- 1️⃣ Topic Name:").
    - Immediately follow this preamble with an `ask_followup_question` tool use.
      - The `<question>` text **MUST** be concise, directly asking the user to choose from the preamble options. It **MUST** also include, after two newlines, an italicized reminder: `_(Or enter any topic or other instruction in the chat box)_`.
      - The suggested `<suggest>` options **MUST** mirror the emoji numerals and text of the preamble's list items (e.g., "1️⃣ Topic Name"). **Note: Markdown formatting (e.g., backticks for code, asterisks for bold/italics) within `<suggest>` text will render literally and SHOULD be avoided; use plain text or emojis as appropriate.** There should be a maximum of 3 numbered/topic-based suggestions.
      - For the top-level menu **only**, one of the `ask_followup_question` suggestions **MUST** be a clearly marked, non-numbered "✅ Done Onboarding" option. This option should not be listed in the preamble's numbered list of topics. This makes a total of up to 4 suggestions.

3.  **Handle User Selection and Sub-Menus:**

    - When the user selects an option:
      - The explanation/preamble text you deliver **MUST** begin with a Markdown H3 header (e.g., `### Stories (\`stories/\`)`) that provides a concise and meaningful title for the chosen topic.
      - Keep explanations for each menu item (delivered in the preamble before the next `ask_followup_question`) concise and focused. Use further clear subheadings (H4, H5 if needed), and numbered or bulleted lists within these preamble explanations for readability.
      - If the selected topic has sub-topics, present these as another bulleted list with emoji numerals in the preamble, with corresponding emoji-numbered suggestions in the `ask_followup_question` (following the same question format with the italicized reminder and 4-suggestion limit).
      - **Contextual Drill-Downs (Optional & Unnumbered):** After explaining a main menu or sub-menu topic, before presenting the standard "Back" navigation, you _may_ offer 1-2 `ask_followup_question` suggestions for a deeper dive into a specific aspect of the _current_ topic if appropriate.
        - The explanation provided when the user selects such a drill-down option **MUST** also begin with an H3 header, providing a concise and meaningful title for the drill-down topic.
        - These initial drill-down suggestions should be unnumbered but prefixed with a page emoji (e.g., "📄 Tell me more about journal.md") to give them visual weight.
        - If this deeper dive explanation (itself introduced by an H3 header) then offers further choices on _how_ to consume more detailed information (e.g., as covered in section "5. Deeper Dives into Documentation" like "📄 Get summary in chat", "📄 Open full document"), these subsequent suggestions should also be unnumbered and use the page emoji.
        - All such drill-down suggestions (both initial and follow-up) count towards the 4-suggestion limit.
      - **Navigation:**
        - In standard sub-menus (those reached by selecting an emoji-numbered option), one suggestion **MUST** always be a navigation option (e.g., "⬅️ Back to Main Menu" or "⬅️ Back to Stories Menu"). This option should clearly indicate its purpose.
        - After a user has explored a "Contextual Drill-Down" (an informational side-quest initiated by a "📄" emoji option), the "Back" navigation suggestion offered at the end of that drill-down path **MUST** return the user to the menu state _from which the initial drill-down option was selected_. For example, if they drilled down from "Stories Menu -> Overview", the back option should be "⬅️ Back to Story Overview" or similar, not "⬅️ Back to Stories Menu" if the drill-down itself had multiple steps.

4.  **Handling Menus with Many Items (Pagination):**

    - The `ask_followup_question` tool typically supports up to 4 suggestions. One suggestion slot is usually reserved for navigation (e.g., "⬅️ Back to Main Menu", "✅ Done Onboarding"). This leaves 3 slots for informational menu items.
    - If a menu category naturally has more than 3 items to present:
      - List the first 2-3 items for the current page in the preamble, each with an emoji numeral.
      - If there are more items for subsequent pages, the preamble **MUST** also include a line item for the "➡️ More [Category Name]" or "➡️ Next Page" option (matching the suggestion text but without the emoji if the suggestion itself has one, e.g., "More Supporting Elements").
      - Under this "More" line item in the preamble, as indented sub-bullets (e.g., using ` -` or `   -` for deeper nesting if appropriate), list the main topics or titles of the items on the _next immediate page_ without emoji numerals. This provides a preview or "signpost" for what's coming.
      - One of the `ask_followup_question` suggestions **MUST** then be this "➡️ More [Category Name]" or "➡️ Next Page" option.
      - When the user selects "More...", present a new preamble with the next 2-3 items from that category. This new set of suggestions **MUST** include a "⬅️ Back to previous [Category Name] items" and, if applicable, another "➡️ More..." option.
      - Continue this pagination until all items in that category are presented. This ensures each interaction respects the tool's suggestion limit while allowing comprehensive menus.

5.  **Deeper Dives into Documentation:**
    - For users wanting more detail than a brief chat explanation can provide:
      - Offer to provide a concise, potentially bulleted, summary of relevant sections from specific articles (e.g., [`docs/articles/agile-ai-development.md`](../../../../../docs/articles/agile-ai-development.md:0)) or AI Guides directly in the chat.
      - Always offer to provide direct links to these documents so the user can choose to read the full content themselves.
      - Explicitly ask the user their preference (e.g., "Would you like a brief summary in chat, or a direct link to the document, or both?"). The suggestions offered here (e.g., "📄 Get summary in chat", "📄 Open full document") **MUST** be unnumbered and use the page emoji.

### 2.2. Main Menu Structure and Content Guidance

Present the following as the top-level menu. Adapt explanations based on user interaction.

**(Preamble Example for Main Menu)**

```markdown
Okay, let's explore the core components of Vibe Tasking. Choose an option to learn more:

- 1️⃣ Stories (`stories/`): How tasks are defined and managed.
- 2️⃣ AI Guides (`ai-guides/`): AI's Knowledge Base.
- 3️⃣ Supporting Elements & Optional Features.
```

**(Follow with `ask_followup_question` with suggestions: "1️⃣ Stories (`stories/`)", "2️⃣ AI Guides (`ai-guides/`)", "3️⃣ Supporting Elements & Optional Features", and "✅ Done Onboarding")**

---

#### H3 Topic: 1️⃣ Stories (`stories/`)

**(When user selects "1️⃣ Stories (`stories/`)")**

Present a sub-menu for Stories:

```markdown
### Stories (`stories/`)

Stories are how Vibe Tasking structures units of work, focuses context, and helps reduce AI errors. It's inspired by Agile and GTD philosophies. Each story lives in its own directory like `stories/sXXX-descriptive-slug/` and has core files:

- `story.md`: Defines the task, goals, and acceptance criteria.
- `journal.md`: A log of progress and decisions.
- `artifacts/` (optional): For related files like images or scripts.

AI assistants usually edit these files as they work on a story.

What aspect of Stories would you like to explore?

- 1️⃣ Overview (Purpose & Structure)
- 2️⃣ Creating New Stories
- 3️⃣ Working on Stories
```

**(Follow with `ask_followup_question` with suggestions: "1️⃣ Overview (Purpose & Structure)", "2️⃣ Creating New Stories", "3️⃣ Working on Stories", and "⬅️ Back to Main Menu")**

**Content for Story Sub-topics:**

- **1️⃣ Overview (Purpose & Structure):**
  - Explain how stories structure work, focus context, reduce AI error.
  - Mention Agile/GTD philosophy (can reference [`docs/articles/agile-ai-development.md`](../../../../../docs/articles/agile-ai-development.md:0)).
  - Explain directory structure (`stories/sXXX-slug/`) and core files (`story.md`, `journal.md`, optional `artifacts/`).
  - Emphasize AI usually edits these files during story work.
- **2️⃣ Creating New Stories:**
  - Explain that new stories are typically planned collaboratively.
  - Mention that you (the AI) will consult the [`ai-guides/core/stories/stories-planning-guide.md`](../../../../../ai-guides/core/stories/stories-planning-guide.md:0) when assisting with this.
- **3️⃣ Working on Stories:**

  - Present a further sub-menu:

    ```markdown
    #### Working on Stories

    Once a story is created, you can ask me to work on it. Here's what that involves:

    - 1️⃣ Process Overview
    - 2️⃣ Change Management (Your Role)
    ```

    **(Follow with `ask_followup_question` with suggestions: "1️⃣ Process Overview", "2️⃣ Change Management (Your Role)", and "⬅️ Back to Stories Menu")**

  - **Process Overview:** Explain how work on a story is initiated and progresses. Mention you (the AI) will consult [`ai-guides/core/stories/stories-working-guide.md`](../../../../../ai-guides/core/stories/stories-working-guide.md:0).
  - **Change Management:** Explain the user's role in reviewing AI changes (diffs) and managing the Git workflow (stage, commit, push). Can reference [`docs/articles/implementing-vibe-tasking-stories.md`](../../../../../docs/articles/implementing-vibe-tasking-stories.md:0).

---

#### H3 Topic: 2️⃣ AI Guides (`ai-guides/`): AI's Knowledge Base

**(When user selects "2️⃣ AI Guides (`ai-guides/`)")**

Present a sub-menu for AI Guides:

```markdown
### AI Guides (`ai-guides/`): AI's Knowledge Base

AI Guides are specialized instructions (much like this AI User Onboarding guide an AI assistant is currently following to assist you) that tell an AI assistant how to perform specific tasks or understand project conventions.

What would you like to know about AI Guides?

- 1️⃣ Overview (Concept & Discovery)
- 2️⃣ Usage (How I use them)
- 3️⃣ Creating New Guides (Briefly)
```

**(Follow with `ask_followup_question` with suggestions: "1️⃣ Overview (Concept & Discovery)", "2️⃣ Usage (How I use them)", "3️⃣ Creating New Guides (Briefly)", and "⬅️ Back to Main Menu")**

**Content for AI Guide Sub-topics:**

- **1️⃣ Overview (Concept & Discovery):**
  - Explain the concept of AI Guides.
  - Mention the discovery process (e.g., you have an internal index of guides, possibly built using a `find` command if they saw you run it during `CONTEXT.md` processing).
- **2️⃣ Usage (How I use them):**
  - Explain how you map user queries or task contexts to the `usage` field in a guide's frontmatter.
  - Mention that you load the relevant guide(s) and follow their instructions, including any dependency chains (i.e., one guide telling you to consult another).
- **3️⃣ Creating New Guides (Briefly):**
  - Mention this is more advanced but possible.
  - State that you would consult [`ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md`](../../../../../ai-guides/core/ai-guides/ai-guides-collaborative-designing-guide.md:0) to help with this.

---

#### H3 Topic: 3️⃣ Supporting Elements & Optional Features

**(When user selects "3️⃣ Supporting Elements & Optional Features")**

Present the first page of a paginated sub-menu:

```markdown
### Supporting Elements & Optional Features (Page 1)

This covers key project files, templates, optional `contrib` features, and general documentation.

- 1️⃣ `CONTEXT.md` (Project Onboarding File)
- 2️⃣ Templates (`*.template.md`)
- ➡️ More Supporting Elements (Page 2)
  - `contrib/` Features (Inbox, ADRs, etc.)
  - General Documentation Structure (`docs/`)
```

**(Follow with `ask_followup_question` with suggestions: "1️⃣ `CONTEXT.md` (Project Onboarding File)", "2️⃣ Templates (`*.template.md`)", "➡️ More Supporting Elements (Page 2)", and "⬅️ Back to Main Menu")**

**Content for Sub-topics (Supporting Elements & Optional Features):**

- **(When user selects "1️⃣ `CONTEXT.md` (Project Onboarding File)")**

  - Present a further sub-menu:

    ```markdown
    #### `CONTEXT.md` (Project Onboarding File)

    This is the file that likely started our current session!

    - 1️⃣ Overview & Purpose
    - 2️⃣ Usage (Briefly)
    - 3️⃣ Creating (Briefly)
    ```

    **(Follow with `ask_followup_question` with suggestions: "1️⃣ Overview & Purpose", "2️⃣ Usage (Briefly)", "3️⃣ Creating (Briefly)", and "⬅️ Back to Supporting Elements Menu (Page 1)")**

  - **Overview & Purpose:** Explain its role in bootstrapping AI sessions. Reference project [`README.md`](../../../../../README.md:0).
  - **Usage:** Briefly mention, as user just experienced it.
  - **Creating:** Low relevance for new user; if asked, reference [`ai-guides/core/context/context-documents-authoring-guide.md`](../../../../../ai-guides/core/context/context-documents-authoring-guide.md:0).

- **(When user selects "2️⃣ Templates (`*.template.md`)")**

  ```markdown
  #### Templates (`*.template.md`)

  Vibe Tasking uses `.template.md` files for consistency (Stories, AI Guides, etc.). When a new story is planned, an AI assistant will use `story.template.md`.
  More info in `ai-guides/core/template-files-working-guide.md`.
  ```

  **(Follow with `ask_followup_question` with suggestions: "⬅️ Back to Supporting Elements Menu (Page 1)")**

- **(When user selects "➡️ More Supporting Elements (Page 2)")**
  Present the second page:

  ```markdown
  ### Supporting Elements & Optional Features (Page 2)

  Continuing with supporting elements:

  - 1️⃣ `contrib/` Features (Inbox, ADRs, etc.)
  - 2️⃣ General Documentation Structure (`docs/`)
  - ➡️ More Supporting Elements (Page 3)
    - Temporary AI Output (`tmp_ai_output/`)
  ```

  **(Follow with `ask_followup_question` with suggestions: "1️⃣ `contrib/` Features (Inbox, ADRs, etc.)", "2️⃣ General Documentation Structure (`docs/`)", "➡️ More Supporting Elements (Page 3)", and "⬅️ Back to Supporting Elements Menu (Page 1)")**

- **(When user selects "1️⃣ `contrib/` Features (Inbox, ADRs, etc.)" from Page 2)**

  - Present a further sub-menu:

    ```markdown
    #### `contrib/` Features (Optional Add-ons)

    Vibe Tasking has optional 'contrib' features:

    - 1️⃣ Inbox (`inbox/`)
    - 2️⃣ ADRs (`docs/adrs/`)
    - 3️⃣ Other `contrib/` AI Guides
    ```

    **(Follow with `ask_followup_question` with suggestions: "1️⃣ Inbox (`inbox/`)", "2️⃣ ADRs (`docs/adrs/`)", "3️⃣ Other `contrib/` AI Guides", and "⬅️ Back to Supporting Elements Menu (Page 2)")**

  - **Inbox (`inbox/`):** Explain concept. Mention [`ai-guides/contrib/inbox/inbox-capturing-guide.md`](../../../../../ai-guides/contrib/inbox/inbox-capturing-guide.md:0) and [`ai-guides/contrib/inbox/inbox-processing-guide.md`](../../../../../ai-guides/contrib/inbox/inbox-processing-guide.md:0). Explain "Inbox:" cue and processing.
  - **ADRs (`docs/adrs/`):** Explain concept. Mention [`ai-guides/contrib/adrs/adrs-writing-guide.md`](../../../../../ai-guides/contrib/adrs/adrs-writing-guide.md:0) for creation.
  - **Other `contrib/` AI Guides:** Briefly mention availability.

- **(When user selects "2️⃣ General Documentation Structure (`docs/`)" from Page 2)**

  ```markdown
  #### General Documentation Structure (`docs/`)

  The `docs/` directory is for documentation aimed at mixed user/AI audiences.

  - `docs/articles/`: Tutorial-like content for user education.
  - `docs/reference/`: Factual documents, research outputs, glossaries.
  ```

  **(Follow with `ask_followup_question` with suggestions: "⬅️ Back to Supporting Elements Menu (Page 2)")**

- **(When user selects "➡️ More Supporting Elements (Page 3)")**
  Present the third page:

  ```markdown
  ### Supporting Elements & Optional Features (Page 3)

  The final supporting element:

  - 1️⃣ Temporary AI Output (`tmp_ai_output/`)
  ```

  **(Follow with `ask_followup_question` with suggestions: "1️⃣ Temporary AI Output (`tmp_ai_output/`)", and "⬅️ Back to Supporting Elements Menu (Page 2)")**

- **(When user selects "1️⃣ Temporary AI Output (`tmp_ai_output/`)")**

  ```markdown
  #### Temporary AI Output (`tmp_ai_output/`)

  If an AI assistant runs a command and can't show output directly (e.g., too long), it might save it to `tmp_ai_output/`.
  More detail in `ai-guides/contrib/command-output-issues-handling-guide.md`.
  ```

  **(Follow with `ask_followup_question` with suggestions: "⬅️ Back to Supporting Elements Menu (Page 3)")**

---

## 3. Handling Common User Questions/Misconceptions

During the onboarding, the user may have questions or misconceptions.

- **Anticipate Common Questions:**

  - "Is this going to create a lot of extra work?" (Response: Focus on streamlining, clarity benefits, and how it makes AI collaboration more efficient in the long run.)
  - "How is this different from [other project management tool/method]?" (Response: Highlight Vibe Tasking's specific focus on optimizing AI collaboration and its documentation-centric approach, rather than being a full project management suite.)
  - "Do I have to follow all these rules strictly?" (Response: Explain core requirements for the system to work (e.g., story structure for AI understanding) versus adaptable parts where they can customize.)

- **Your Response Strategy:**
  1.  Answer patiently and clearly.
  2.  Refer back to core concepts or relevant documentation if helpful.
  3.  **Sourcing Answers:**
      - First, consult your **AI Guide Index** for any AI Guides directly relevant to the question.
      - For broader Vibe Tasking concepts or details (e.g., in `docs/articles/` or `docs/reference/`), **strongly prefer using the `search_files` tool** to query these locations. `list_files` is unlikely to reliably show all files if Vibe Tasking is installed as a submodule, whereas `search_files` should still be effective for finding content within those directories.
      - If unable to find a definitive answer quickly, be transparent with the user. Offer to help them search, or note it as a point for later clarification.
  4.  Emphasize the goal: making user-AI collaboration more effective and less error-prone.

## 4. Concluding the Initial Onboarding Session

When the user indicates they are done with the interactive concept explanation (e.g., by selecting "✅ Done Onboarding" from the main menu), or if you've covered the main topics:

1.  **Summarize:** Briefly recap what was covered.
2.  **Next Steps for User:**
    - Encourage the user to think about a small, concrete task or a piece of documentation in their project where Vibe Tasking could be applied.
    - Reiterate that you (the AI) are available to help them collaboratively plan their first Vibe Tasking story for such a task if they wish.
    - Remind them that to initiate story planning, they can simply state their goal (e.g., "I'd like to improve my project's README using Vibe Tasking"). You will then consult the `stories-planning-guide.md`.
    - If a story is planned, remind them that to start work on it, they can say, "Let's work on story [sXXX-id]".
3.  **Offer Further Assistance:** Let the user know you are available to help with Vibe Tasking tasks, answer more questions, or plan/work on stories.

## Conclusion

By following this guide, you can provide a structured, informative, and user-driven onboarding experience. This will help new users quickly grasp Vibe Tasking's value and begin leveraging it effectively in their projects. Remember to be adaptable and responsive to the user's specific needs and project context.

---

_This guide outlines the standard AI-led user onboarding process. Adapt your explanations and the depth of detail based on user interaction and questions._
