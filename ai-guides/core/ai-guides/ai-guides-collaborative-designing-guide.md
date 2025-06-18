---
id: "ai-guides-collaborative-designing-guide"
title: "Guide: Collaboratively Designing and Authoring AI Guides"
usage: "Use this guide when assisting a user in designing and authoring new AI Guides, to ensure they meet project standards for structure, content, and collaborative design principles."
tags: "ai-guides;authoring;design;collaboration;standards;templates"
---

# Guide: Collaboratively Designing and Authoring AI Guides

**(Primary Audience: AI Assistant (for assisting users in designing and authoring new AI Guides according to project standards).)**

## Introduction

This guide, an exemplar of an AI-Guide itself, outlines the standards, best practices, and collaborative process for AI assistants when helping users design and author new AI-targeted guides. Your role is not just to transcribe or format, but to be an active partner in thinking through the guide's purpose, structure, and content to ensure it will be effective for future AI assistant use (like your own).

Adhering to these standards ensures that AI assistants (including you, when consuming other guides) receive clear, consistent, and actionable instructions, maximizing their effectiveness.

## Phase 1: Collaborative Guide Design & Conceptualization

When a user indicates a desire to create a new AI-Guide, your primary goal is to help them develop a clear vision for the guide.

### Understanding the User's Intent

Your first step is to help the user clarify the core purpose and intended impact of the new AI-Guide. Prompt the user with questions such as:

- "What specific problem, task, or scenario will this AI-Guide help a future AI assistant (like me) understand or execute?"
- "Who is the ultimate beneficiary of the AI's actions after it has consumed this guide? (e.g., a developer using Vibe Tasking, the Vibe Tasking project itself?)"
- "What should an AI assistant _be able to do differently_ or _understand more deeply_ after processing this guide?"
- "Are there any existing documents (other guides, articles, ADRs) that this new guide will relate to, build upon, or potentially supersede? If so, how?"
- "What are the 2-3 most critical pieces of information, instructions, or decision-making logic this guide _must_ convey to be successful?"
- "What is the intended title for this guide? Does it clearly reflect its purpose for an AI assistant?"

These questions are examples to stimulate discussion; you do not need to ask all of them verbatim. Adapt your questions based on the user's initial input and the evolving conversation.

Remember, the user may not be fully familiar with the nuances of AI-Guides or how they are best structured for AI consumption. Be prepared to explain the purpose of AI-Guides (referencing `docs/reference/glossary.md` if helpful) and offer more foundational guidance if needed. Your goal is to bridge any knowledge gaps and collaboratively arrive at a well-defined concept for the new guide.

### Leveraging AI Expertise in Guide Structuring

Based on the user's answers, you can propose an initial structure for the guide. Your understanding of how AI processes information and the existing Vibe Tasking documentation suite is valuable here.

- **Suggest Logical Flow:** Based on the problem or goal, propose a clear, step-by-step or conceptual flow for the guide's content.
- **Identify Potential Ambiguities:** Are there terms or concepts the user mentioned that might be ambiguous to an AI? Suggest clarifying them early in the guide or linking to the `docs/reference/glossary.md`.
- **Propose Sections:** Based on the core purpose, suggest a few key section headings. You can use `ai-guides/core/ai-guides/ai-guide.template.md` as a structural starting point for the new file.
- **Consider Edge Cases & Preconditions:** Are there any obvious edge cases, alternative scenarios, or necessary preconditions the guide should address? (e.g., "What if a required file doesn't exist?", "What if a command fails?", "What information must the AI have _before_ starting this process?").
- **OS-Specific Commands:** If the new guide will involve CLI tools with OS-specific commands (e.g., different commands for Linux/macOS vs. Windows), ensure the design includes how the AI assistant should determine the target OS. Consider adding an Acceptance Criterion to the _new guide being designed_ to verify this OS determination step is documented and tested.
- **Embed Collaborative Ethos:** When structuring the new guide, actively consider and discuss with the user how its content can promote effective user-AI collaboration when that future guide is used. For instance:
  - Does the new guide encourage the future AI assistant to ask clarifying questions at appropriate points?
  - Does it prompt the future AI to present options or seek user confirmation before taking significant actions?
  - Does it define clear points for user feedback or intervention if the process it describes is complex or iterative?
    Your goal is to help the user design a guide that makes the _next_ AI assistant a better collaborator.

## Phase 2: Collaborative Content Drafting and Refinement

As the user provides content, or as you collaboratively draft it, your role is to help refine it for clarity, actionability, and adherence to AI-Guide standards.

### Iterative Content Development

- **Ensure Imperative Voice:** For instructional parts of the guide, gently remind the user or offer to rephrase sentences into the imperative mood (e.g., "Execute the command" rather than "The AI should execute the command").
- **Check for Precision:** If the user provides a vague instruction (e.g., "The AI should look at the files"), prompt for specifics ("Which files specifically? What should the AI look _for_ in those files? What action should it take based on what it finds?").
- **Maintain AI Audience Focus:** Ensure the language remains targeted at an AI assistant, avoiding overly colloquial or human-centric phrasing where precision is key.
- **Suggest Examples:** If an instruction, concept, or data structure could benefit from a concrete example (e.g., a command, a file snippet, an API response structure), suggest adding one.
- **Cross-Referencing:** If the user mentions concepts detailed elsewhere in the Vibe Tasking documentation, suggest linking to the relevant document to avoid duplication and maintain a single source of truth.
- **Use of Formatting:** Encourage the use of Markdown for structure (headings, lists) and emphasis (bolding, backticks for code/literals) as per existing standards.

## Phase 3: Standard Structure and Formatting for AI-Guides

This section reiterates the established structural and formatting conventions that all AI-Guides must follow. The `ai-guides/core/ai-guides/ai-guide.template.md` provides a starting point.

### 1. YAML Frontmatter (Required)

All AI Guides **MUST** begin with a YAML frontmatter block. This metadata is crucial for discoverability and programmatic access to the guide's purpose. Refer to [`docs/adrs/adr-027-ai-guide-metadata-for-discoverability.md`](../../../docs/adrs/adr-027-ai-guide-metadata-for-discoverability.md) for the full specification.

The standard frontmatter fields are:

- `id`: (String, Required) A unique identifier for the guide, typically derived from its filename (e.g., for `ai-guides-collaborative-designing-guide.md`, the `id` would be `"ai-guides-collaborative-designing"`). Enclose in double quotes.
- `title`: (String, Required) The full H1 title of the guide as it appears in the document (e.g., `"Guide: Collaboratively Designing and Authoring AI Guides"`). This should match the H1 title following the frontmatter. Enclose in double quotes.
- `usage`: (String, Required) A concise (1-2 sentences) description of when this guide should be consulted or used. This field is **critical** for enabling AI assistants to quickly determine the guide's relevance to a user's task. Example: `"Use this guide when assisting a user in creating a new AI Guide to ensure it meets project standards for structure, content, and collaborative design."`. Enclose in double quotes.
- `tags`: (String, Optional) A semicolon-separated list of relevant keywords or concepts that can further aid in searching and categorization (e.g., `"authoring;collaboration;standards;template"`). All lowercase. Enclose in double quotes.

**Example (from `ai-guide.template.md`):**

```yaml
---
id: "your-guide-filename-without-extension"
title: "Guide: [Your Guide Title Here]"
usage: "A concise (1-2 sentences) description of when this guide should be consulted or used."
tags: "tag1;tag2;relevant-concept" # Optional
---
```

Ensure this frontmatter is at the very beginning of the file.

### 2. Title

- Use a clear, descriptive title prefixed with "Guide: ".
  - Example: `# Guide: Working on Vibe Tasking Stories`

### 3. Primary Audience Declaration

- Immediately after the title, explicitly state the primary audience.
- **Standard Format:** `**(Primary Audience: AI Assistant [optional additional context clarifying user benefit or specific AI role])**`
  - Example: `**(Primary Audience: AI Assistant (to understand and implement best practices when actively working on a Vibe Tasking story). The User benefits from the AI's adherence to these practices.)**`
  - Example for this guide: `**(Primary Audience: AI Assistant (for assisting users in designing and authoring new AI Guides according to project standards).)**`

### 4. Introduction/Purpose (of the guide being written)

- Briefly explain the purpose of the guide and what the AI assistant (or human reader, if applicable as a secondary audience) will learn or be able to do after reading it.

### 5. Sections and Headings

- Use Markdown headings (`##`, `###`, etc.) to structure content logically.
- Keep headings concise and descriptive.

### 6. Imperative Voice

- **Always use the imperative mood** when providing instructions to an AI assistant. This means starting sentences with a verb, as if giving a direct command.
  - **Do:** "Update the `story.md` file."
  - **Don't:** "You should update the `story.md` file."

### 7. Key Instructions and Requirements

- Use **bold text** for emphasis on critical instructions, keywords, or file names.
- Use `backticks` for inline code, file paths, commands, or specific literal strings.
- Use lists (bulleted or numbered) for sequences of steps or related items.

### 8. Examples and Templates

- Provide concrete examples whenever possible.
- Use Markdown code blocks for multi-line examples.
- For a starter template for new AI Guides, refer to `ai-guide.template.md` located in this same directory (`ai-guides/core/`).

### 9. Referencing Other Documents

- When referencing other documents, provide the full path from the project root or a clear relative path.
  - Example: "Consult `ai-guides/core/stories/stories-structuring-guide.md` for details on story structure."

### 10. AI-Guide Filename Convention

To ensure consistency and discoverability, all AI-Guide documents should adhere to a standardized naming convention. This convention is also documented in `docs/adrs/adr023-standardize-ai-guides-naming.md`.

**Convention:** `[object-noun]-[verb-form-action]-guide.md`

- **`[object-noun]`**: The primary subject or entity the guide is about.
  - It is **recommended** that this noun be in **plural form** (e.g., `stories`, `adrs`, `articles`) when the guide addresses multiple instances or a general category.
  - However, a **singular form** should be used if it enhances clarity, the concept is inherently singular (e.g., `onboarding`), or the plural form sounds awkward.
- **`[verb-form-action]`**: The primary activity, process, or aspect the guide addresses, typically represented by a verb.

  - It is **recommended** to use the **gerund form** (`-ing`) of a verb (e.g., `planning`, `writing`, `designing`) where it naturally fits.
  - However, other verb forms (e.g., base verb) can be used if the gerund sounds awkward or if another form improves legibility. The goal is to clearly convey the action.

  The core structure to enforce is `[noun]-[verb]-guide.md`, ensuring the guide's filename clearly indicates the **object** of the task and the general **activity** involved. Prioritize overall legibility and clarity of the filename over strict adherence to plural nouns or gerund verb forms if they lead to awkward or unclear names.

- The filename always ends with `-guide.md`.

**Examples:**

- `stories-planning-guide.md`
- `adrs-writing-guide.md`
- `onboarding-updating-guide.md`
- `ai-guides-collaborative-designing-guide.md` (This very guide)

**Exception for Template Files:**
Template files within `ai-guides/` (or its subdirectories) will continue to use the simpler `[object].template.md` convention (e.g., `adr.template.md`, `article.template.md`, `ai-guide.template.md`), as this clearly identifies them as templates for a specific object.

When assisting a user in creating a new AI-Guide, ensure the proposed filename conforms to this convention.

### 11. AI-Guide File Location

- **Default Location:** New AI Guides are typically created within an `ai-guides/` directory at the root of the **host project**. For example, a new guide would be placed at a path like `ai-guides/your-new-guide-filename.md` relative to the project root.
- **AI Assistant Responsibility:**
  - When assisting in the creation of a new AI-Guide, the AI assistant should propose this default location within the host project.
  - The AI assistant **MUST** explicitly confirm the final file path with the user before writing the new guide file. This ensures the location aligns with any project-specific organizational preferences or if the guide is intended for a different scope (e.g., a submodule, though less common for host-initiated guides).
  - **Example Confirmation:** "I'll create this new guide at `ai-guides/your-new-guide-filename.md` in the current project. Is this correct?"

## Phase 4: User Review and Finalization

- Once a draft of the new AI-Guide is complete, encourage the user to review it thoroughly.
- Incorporate any feedback from the user.
- Ensure all ACs for the story tasking the creation of this guide are met.
- **Consider Meta-Execution for Validation:** For process-oriented AI-Guides, recommend 'meta-execution' as a best practice for testing and validation. This involves having an AI assistant attempt to follow the newly drafted guide to perform a real task. For example, this approach was successfully used during story s069 (Design and Implement AI-Assisted Inbox Processing Workflow) where the inbox processing guide was tested by processing actual inbox items, providing robust, practical validation.

## Conclusion

By actively collaborating with users in the design and authoring process, as detailed in this guide, AI assistants can help create highly effective, clear, and precise AI-Guides. This collaborative approach, combined with adherence to structural and formatting standards, is key to enhancing the overall Vibe Tasking user-AI partnership.

**A Note on Ethos for Guide Design:** The collaborative principles detailed in this guide—actively understanding user intent, offering your unique AI insights during structuring, and iteratively refining content—are paramount when you are assisting a user in _designing and authoring a new AI-Guide_. Your role in this specific context is to be an effective, thinking partner to help the user create the best possible guide. This guide itself aims to be an example of such a collaboratively developed document.
