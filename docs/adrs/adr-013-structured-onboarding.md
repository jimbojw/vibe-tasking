---
id: "adr-013"
title: "Provision of Structured Onboarding Guide for Vibe Tasking Framework"
status: "Accepted"
date: "2025-05-19"
tags: "documentation;onboarding;user-experience;education;framework-adoption"
---

# ADR-013: Provision of Structured Onboarding Guide for Vibe Tasking Framework

## Context

For users to effectively adopt and utilize the Vibe Tasking framework, they need a clear and structured introduction to its core concepts, setup process, and fundamental workflows. Simply providing the framework files and the `docs/ai-guides/core/stories/stories-structuring-guide.md` might not be sufficient for a smooth learning curve, potentially leading to misuse or underutilization.

## Alternatives Considered

1.  **No Dedicated Onboarding Guide:** Expect users to learn Vibe Tasking by reading the `docs/ai-guides/core/stories/stories-structuring-guide.md`, `CONTEXT.md` examples, and inferring usage from the framework's own stories.

    - _Pros:_ Minimizes documentation overhead for the framework maintainers.
    - _Cons:_ High barrier to entry for new users. Steep learning curve. Increased likelihood of inconsistent or incorrect adoption of Vibe Tasking principles.

2.  **Single, Large "Getting Started" Document:** Combine all introductory, installation, and usage information into one extensive document.

    - _Pros:_ All information in one place.
    - _Cons:_ Can be overwhelming for new users. Difficult to navigate and find specific pieces of information. Less digestible than a step-by-step approach.

3.  **Rely on Community/External Guides:** Do not provide official onboarding and hope that community members or third parties create tutorials.
    - _Pros:_ No official maintenance burden.
    - _Cons:_ Unreliable. Quality and accuracy of external guides can vary. Lack of an official path can deter potential adopters.

## Decision

The Vibe Tasking framework project itself will provide a **structured, multi-part onboarding guide**, located within its own `docs/onboarding/` directory.

This guide will consist of several focused Markdown files, presented in a recommended reading order, covering:

- Introduction to Vibe Tasking concepts.
- Installation process (referencing `INSTALLING.md`).
  > **Note:** The reference to `INSTALLING.md` for the installation process is now outdated due to adr-022-retire-ai-playbooks-concept.md. The onboarding guide will need to reflect the new installation mechanism once defined.
- Planning first stories.
- Working with stories (exploring, querying, updating).
- An example walkthrough of a typical Vibe Tasking session.

The `docs/onboarding/README.md` will serve as the entry point and table of contents for this structured onboarding experience.

## Consequences

### Positive

- **Improved User Experience:** Provides a clear, step-by-step path for new users to learn Vibe Tasking.
- **Faster Adoption:** Lowers the barrier to entry and helps users become productive more quickly.
- **Consistent Understanding:** Ensures users are introduced to core concepts and recommended practices in a standardized way.
- **Reduced Support Burden:** A comprehensive onboarding guide can preemptively answer many common new user questions.
- **Foundation for Deeper Learning:** Once onboarded, users are better equipped to understand more advanced guides and reference materials.
- **Showcases Best Practices:** The onboarding guide itself can serve as an example of good documentation within the Vibe Tasking philosophy.

### Negative

- **Maintenance Overhead:** The onboarding guide requires initial creation effort and ongoing maintenance to keep it synchronized with any evolution of the Vibe Tasking framework.
- **Potential for Information Overlap:** Care must be taken to ensure that the onboarding guide appropriately references other key documents (like `docs/ai-guides/core/stories/stories-structuring-guide.md`) rather than duplicating their detailed content extensively, to avoid SOT violations.
- **Initial Scope Definition:** Defining the right level of detail and the number of steps for the onboarding process requires careful consideration.

This decision prioritizes user success and effective adoption of the Vibe Tasking framework by providing dedicated, structured learning materials.
