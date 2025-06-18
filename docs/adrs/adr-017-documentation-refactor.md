---
id: "adr-017"
title: "Refactor Documentation Structure and Standardize Terminology"
status: "Proposed"
date: "2025-05-21"
tags: "documentation;structure;refactor;terminology;information-architecture"
deciders: "Vibe Tasking Maintainers"
consulted: "AI Assistant (Cline)"
informed: "All Vibe Tasking Users and Contributors"
---

# ADR-017: Refactor Documentation Structure and Standardize Terminology

## Context

The existing Vibe Tasking documentation, primarily located within the `docs/` directory, has grown organically. While functional, the structure lacks clear distinctions between different types of documentation (e.g., user-facing articles, AI-specific guides, executable playbooks for AI). This ambiguity can lead to:

- Difficulty for users in finding relevant information quickly.
- Confusion for AI assistants in understanding the intended purpose and audience of specific documents.
- Challenges in maintaining consistency as the documentation scales.
- A less intuitive onboarding experience for new users and contributors.
- Inconsistent terminology for document types.

A more deliberate information architecture is needed to improve organization, discoverability, maintainability, and clarity for all consumers of the documentation.

**Decision Drivers:**

- **Improved User Experience:** Users should be able to easily navigate and find the information they need.
- **Enhanced AI Comprehension:** AI assistants need clear signals about document purpose to provide accurate and context-aware assistance (e.g., distinguishing between a conceptual guide it should learn from vs. a playbook it should execute).
- **Maintainability and Scalability:** A well-defined structure makes it easier to add new documentation and manage existing content consistently.
- **Clarity of Purpose:** Standardized terminology and distinct locations for different document types will make the role of each document unambiguous.
- **Streamlined Onboarding:** A logical structure supports a more effective learning path for new users.

## Alternatives Considered

### Alternative 1: Minor Reorganization

- **Description:** Make small adjustments to existing directories, perhaps adding a few subdirectories but largely keeping the current top-level structure.
- **Pros:** Less disruptive in the short term.
- **Cons:** Does not fully address the core issues of ambiguity and lack of clear distinction between document types. Unlikely to scale well.

### Alternative 2: Introduce Audience-Primary Directories (e.g., `docs/user/`, `docs/ai/`)

- **Description:** Structure based on the primary audience.
- **Pros:** Clear audience separation.
- **Cons:** Some documents serve both audiences (e.g., reference material). Might lead to duplication or awkward placement for mixed-audience content.

### Alternative 3: Introduce Purpose-Primary Directories

- **Description:** Structure based on the primary purpose/type of the document (e.g., articles for learning, playbooks for execution, guides for AI conceptual understanding, reference for lookup).
- **Pros:** Clearly defines the intent of each document. Allows for nuanced categorization (e.g., AI conceptual guides vs. AI executable playbooks). Provides logical homes for different kinds of content.
- **Cons:** Requires careful definition of categories. Involves a more significant one-time refactoring effort.

## Decision

It was decided to **Introduce Purpose-Primary Directories (Option 3)**.

The `docs/` directory will be restructured as follows:

```
docs/
├── README.md              # Overview of all documentation
├── adrs/                  # Architecture Decision Records
│   ├── README.md
│   └── ...
├── reference/             # Factual, descriptive information (e.g., glossary, capability lists)
│   ├── README.md
│   └── glossary.md
│   └── ...
│
├── articles/              # User-focused documentation for learning and understanding
│   ├── README.md
│   ├── onboarding/        # Sequential learning path for users
│   │   ├── README.md
│   │   └── ...
│   └── ...                # Other general user articles
│
├── ai-playbooks/          # AI-focused, step-by-step executable instructions
│   ├── README.md
│   └── INSTALLING.md
│   └── ...
│
└── ai-guides/             # AI-focused, conceptual/scenario guidance
    ├── README.md
    ├── ...                # VT-Core project maintenance guides for AI
    └── vibe-tasking/      # General Vibe Tasking framework usage guides for AI
        ├── README.md
        └── ...
```

> **Note:** The `ai-playbooks/` directory and the "AI-Playbook" terminology described in this ADR have been superseded by [`docs/adrs/adr-022-retire-ai-playbooks-concept.md`](docs/adrs/adr-022-retire-ai-playbooks-concept.md:0).

**Key Terminology (defined in `docs/reference/glossary.md`):**

- **Article:** User-focused documentation for readers.
- **AI-Playbook:** AI-focused, step-by-step executable instructions. (Formerly "Playbook")
  > **Note:** This term is now retired per [`adr-022-retire-ai-playbooks-concept.md`](docs/adrs/adr-022-retire-ai-playbooks-concept.md:0).
- **AI-Guide (AI Conceptual):** AI-focused documentation for conceptual understanding and decision-making. (Formerly "Guide (AI Conceptual)")
  - **VT-Core Maintenance AI-Guides:** For maintaining the Vibe Tasking Core project.
  - **General Vibe Tasking Framework AI-Guides:** For assisting users with the general VT framework.
- **Onboarding:** A specialized series of Articles for sequential user learning.
- **Reference:** Factual, descriptive information.

This structure provides clear distinctions based on document purpose and primary audience, enhancing usability for both users and AI assistants.

The new structure will be validated by:

- Successfully migrating all existing documentation.
- Updating all internal links and verifying their correctness.
- Ensuring `README.md` files in each new/restructured directory clearly explain its purpose.
- User feedback post-implementation.

## Consequences

### Positive

- Improved clarity and organization of documentation.
- Easier navigation for users.
- Better contextual understanding for AI assistants.
- Enhanced maintainability and scalability.
- Standardized terminology for document types.

### Negative

- Requires a one-time effort to migrate existing files and update all internal links.
- Users and contributors will need to familiarize themselves with the new structure.

## Links / References

- This ADR documents the decisions made as part of story `s045-refactor-documentation-structure`.
- The "Next Steps" outlined in the original version of this ADR (implement structure, create READMEs, migrate files, update links, update ADR status) are considered part of the work for story `s045`.
