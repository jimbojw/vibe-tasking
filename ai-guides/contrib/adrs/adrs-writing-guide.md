---
id: "adrs-writing-guide"
title: "Guide: Collaboratively Writing Architecture Decision Records (ADRs)"
usage: "Use this guide when assisting a user in collaboratively conceptualizing, drafting, and refining Architecture Decision Records (ADRs) according to project standards and best practices."
tags: "adrs;architecture;documentation;collaboration;authoring"
---

# Guide: Collaboratively Writing Architecture Decision Records (ADRs)

**(Primary Audience: AI Assistant (for assisting users in collaboratively conceptualizing, drafting, and refining ADRs using the standard template and Vibe Tasking best practices).)**

## Introduction

The purpose of this guide is to instruct you, an AI assistant, on how to effectively collaborate with a user to conceptualize, draft, and refine Architecture Decision Records (ADRs). ADRs are a crucial part of the Vibe Tasking methodology, serving as immutable records of significant architectural decisions. Your role is to facilitate a structured and efficient ADR authoring process, ensuring high-quality, compliant, and clear documentation.

This guide will walk you through the typical phases of ADR creation, highlighting how you can best support the user at each step.

## Phase 1: Understanding ADR Purpose & Initial Conceptualization

Before any writing begins, it's vital to help the user clarify the core purpose and scope of the ADR.

### Understanding User's Intent for the ADR

Initiate a discussion with the user to understand the decision they want to document. You might ask questions like:

- "What specific problem, architectural challenge, or opportunity is this ADR addressing?"
- "What is the core decision that needs to be recorded?"
- "What are the main goals, requirements, or constraints that influenced this decision?"
- "Who is the primary audience for this ADR (e.g., current development team, future maintainers, architects)?"
- "What do you hope someone reading this ADR in the future will understand or be able to do?"

### Conceptualizing the ADR Content

Based on the user's intent, guide them in outlining the key components of the ADR. Help them think through:

- **Context:** What is the relevant background, current system state, or problem statement that necessitates this decision?
- **Decision Drivers:** What are the key technical or business requirements, constraints, principles, or forces leading to this specific decision?
- **Considered Options:** What alternative solutions or approaches were evaluated? Briefly describe them and why they were not chosen. (It's important to capture this to prevent re-litigation of past decisions).
- **The Decision:** Clearly and concisely state the architectural decision that was made.
- **Consequences:** What are the expected positive and negative impacts of this decision? Consider technical debt, operational impact, developer experience, future flexibility, etc.

### Linking to Existing Knowledge

Ask the user if this new ADR relates to, builds upon, or potentially supersedes any existing ADRs, articles, or other project documentation. If so, plan to reference these connections within the new ADR.

## Phase 2: Utilizing the ADR Template & Drafting Content

Once the conceptual foundation is laid, you can begin drafting the ADR content, leveraging the standard Vibe Tasking ADR template.

### Introducing `ai-guides/contrib/adrs/adr.template.md`

Inform the user that you will use the standard ADR template located at `ai-guides/contrib/adrs/adr.template.md`. Explain that this template provides the necessary YAML frontmatter and standard section headings.

### Populating Frontmatter

Collaborate with the user to populate the YAML frontmatter fields. You should:

- **`id`**: Before suggesting an ADR number, you **MUST** first list the files in the `docs/adrs/` directory to determine the highest existing ADR number. Then, suggest the next sequential number (e.g., if the highest existing ADR is `adr-020-some-topic.md`, suggest `adr-021-`). The user will provide the descriptive slug. If the user provides a full ID, use that.
- **`title`**: Craft a concise title that clearly reflects the core decision.
- **`status`**: This will typically be `"Proposed"` or `"Accepted"` for new ADRs. Confirm with the user. Other statuses like `"Deprecated"` or `"Superseded"` might be used if updating an existing ADR's lifecycle.
- **`date`**: Use the current date in YYYY-MM-DD format.
- **`tags`**: Elicit a semicolon-separated list of relevant keywords from the user (e.g., `"api;security;database"`).

Ensure all frontmatter string values are enclosed in double quotes as per `adr-003-yaml-frontmatter.md`.

### Drafting Core ADR Sections

Using the information gathered in Phase 1, begin drafting the content for each standard ADR section:

- **Context:** Describe the problem, existing state, and why a decision is needed.
- **Decision Drivers:** (This can be a subsection of Context or its own section). Detail the specific factors influencing the decision.
- **Considered Options:** List and briefly describe the alternatives that were evaluated. For each, explain why it was not chosen.
- **Decision:** Clearly articulate the chosen solution. Be specific and unambiguous.
- **Consequences:** Detail the expected outcomes, both positive and negative. Include any trade-offs, risks, or future work implied by this decision.

Throughout this drafting process, your role is to:

- Translate the user's thoughts and discussions into clear, written statements.
- Suggest phrasing for clarity and precision.
- Ensure all aspects discussed in Phase 1 are adequately covered.
- Maintain a logical flow within and between sections.

### Adherence to Standards

Continuously ensure the ADR adheres to project standards, particularly:

- `adr-003-yaml-frontmatter.md` for frontmatter requirements.
- The general structure and spirit of existing ADRs in `docs/adrs/`.

## Phase 3: Refining Content for Clarity and Completeness

Once the initial draft is complete, work with the user to refine the ADR.

### Reviewing for Clarity

- Is the problem statement clear?
- Is the decision unambiguous?
- Is the rationale easy for someone unfamiliar with the immediate context to understand?
- Are there any jargon or acronyms that need explanation?

### Reviewing for Completeness

- Have all critical aspects of the decision been captured?
- Are the "Considered Options" and their rejection reasons adequately explained?
- Are the "Consequences" thorough, covering both pros and cons, and potential future implications?
- Is the "Context" sufficient?

### Maintaining Neutral and Objective Tone

ADRs should be factual and objective. Guide the user to ensure the language used is neutral and avoids overly strong opinions where a balanced perspective is needed, especially when describing alternatives or consequences.

### Formatting and Readability

Ensure the ADR uses Markdown effectively for structure and readability:

- Proper use of headings (`##`, `###`) for sections.
- Bulleted or numbered lists for options, consequences, or steps.
- `Backticks` for code snippets, commands, or specific technical terms.
- Ensure consistency in style with other ADRs in the project.

## Phase 4: User Review, Finalization, and Storage

The final steps involve user approval and correctly storing the ADR.

### Presenting the Draft ADR for User Review

Clearly present the complete draft of the ADR to the user for their final review and approval.

### Incorporating User Feedback

Diligently incorporate any final changes or corrections requested by the user.

### Confirming Final `status`

Confirm the final `status` of the ADR with the user (e.g., if it moves from `"Proposed"` to `"Accepted"`). Update the frontmatter accordingly.

### Guidance on Naming and Saving the ADR

- Remind the user of the standard ADR naming convention: `adr-XXX-descriptive-slug.md` (e.g., `adr-021-standardize-api-authentication.md`).
- Ensure the file is saved in the `docs/adrs/` directory.

## Best Practices for AI Collaboration in ADR Authoring

- **Be Proactive:** Don't just wait for explicit instructions. If you see an opportunity to improve clarity, suggest it. If a standard section seems to be missing, point it out.
- **Offer to Summarize or Rephrase:** If the user is thinking aloud or providing complex information, offer to summarize or rephrase it for inclusion in the ADR.
- **Cross-Reference:** Proactively suggest adding links to other relevant ADRs or project documents. This is especially important when:
  - Discussing the 'Cons' of an alternative if they relate to a decision in another ADR.
  - Explaining the 'Rationale' for the current decision if it builds upon or is constrained by other ADRs.
    Explicitly linking these connections improves the robustness and interconnectedness of your ADRs.
- **Reinforce ADR Principles:** Gently remind the user of ADR best practices, such as "one decision per ADR," or the importance of documenting "why not" for alternatives.

## Conclusion

By following this guide, you can significantly enhance the ADR authoring process. Your ability to structure discussions, draft content based on user input, ensure adherence to standards, and refine the document for clarity makes you an invaluable partner in creating high-quality Architecture Decision Records. This collaborative effort strengthens the Vibe Tasking project by ensuring that critical decisions are well-documented and easily accessible.
