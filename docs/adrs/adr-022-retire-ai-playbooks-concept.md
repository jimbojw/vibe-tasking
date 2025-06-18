---
id: "adr-022"
title: "Retire AI-Playbooks Concept and AI-Assisted Installation"
status: "Accepted"
date: "2025-05-28"
tags: "ai-playbook;installation;refactor;documentation;onboarding"
---

# ADR-022: Retire AI-Playbooks Concept and AI-Assisted Installation

## Context

The Vibe Tasking project initially adopted an AI-assisted installation process guided by an "AI-Playbook" (`INSTALLING.md`), as documented in [`adr-008-ai-assisted-setup.md`](adr-008-ai-assisted-setup.md:1). The broader concept of "AI-Playbooks" was also introduced for AI-focused, step-by-step executable instructions (see [`adr-017-documentation-refactor.md`](adr-017-documentation-refactor.md:1)).

Over time, and with evolving understanding of AI assistant capabilities and user needs, the `ai-playbooks` concept, particularly for installation, is now being reconsidered:

- **Untested and Necessity Unclear:** The `INSTALLING.md` playbook, designed for AI-driven setup, was never fully tested. It's unknown if this approach is necessary or would have been effective.
- **Potential Redundancy with AI-Guides:** It's not clear that "AI-Playbooks" needed to be a distinct document type. Existing "AI-Guides" might be suitable for detailing procedural instructions for AI assistants (e.g., for installation or updates), potentially making a separate "playbook" category redundant and adding unnecessary complexity.
- **Alternative Approaches:** Simpler, more direct instructions for users, or more conventional scripted setups, might offer better clarity and reliability for initial project setup.
- **Streamlining Focus:** There's a desire to streamline the core Vibe Tasking framework and its documentation, focusing on the story management and AI collaboration aspects rather than prescriptive, AI-driven setup mechanisms.

This ADR addresses the need to formally retire this concept and adjust the project's installation and onboarding strategy accordingly.

## Alternatives Considered (Optional)

- **Refine AI-Playbooks:** Invest more effort in making `INSTALLING.md` and the general AI-Playbook concept more robust and universally compatible.
  - **Pros:** Could still leverage AI for setup if successful.
  - **Cons:** Significant effort with uncertain outcomes; doesn't address the core desire for simplification.
- **Maintain Status Quo:** Keep the existing `INSTALLING.md` and AI-Playbook concept.
  - **Pros:** No immediate work required.
  - **Cons:** Continues with a potentially problematic/outmoded concept; documentation for `s046` (creating a guide for playbooks) becomes irrelevant.

## Decision

1.  The **`ai-playbooks` concept is officially retired** from the Vibe Tasking project.
2.  The primary AI-Playbook, [`docs/ai-playbooks/INSTALLING.md`](docs/ai-playbooks/INSTALLING.md:1) (formerly at the root, then moved), will be **deleted**.
3.  The associated guide, [`docs/ai-guides/updating-installing-md-guide.md`](docs/ai-guides/updating-installing-md-guide.md:1), will be **deleted**.
4.  The directory [`docs/ai-playbooks/`](docs/ai-playbooks/) will be **deleted**.
5.  All textual references to "ai-playbook(s)", `INSTALLING.md` (in the context of AI-driven setup), and the `docs/ai-playbooks/` directory will be removed or updated throughout the project documentation.
6.  Story [`s046-create-writing-ai-playbooks-guide`](docs/stories/s046-create-writing-ai-playbooks-guide/story.md:2) will be marked as "Closed" with resolution "Obsolete".
7.  The Vibe Tasking installation process will shift away from AI-assisted setup via `INSTALLING.md`. The [`docs/articles/onboarding/03-installation.md`](docs/articles/onboarding/03-installation.md:1) guide will be updated to reflect this, initially with placeholder content stating new installation instructions are forthcoming. A subsequent effort (new story) will be required to define and document the new installation mechanism.
8.  This ADR **supersedes [`adr-008-ai-assisted-setup.md`](adr-008-ai-assisted-setup.md:1)**.

## Consequences

### Positive

- **Streamlined Documentation:** Project documentation will be simpler and more focused.
- **Reduced Maintenance:** No need to maintain `INSTALLING.md` or the `ai-playbooks` directory and associated guides.
- **Clarity on Installation:** Moves towards a clearer, albeit initially less defined, installation strategy.
- **Focus on Core:** Allows development effort to focus on the core Vibe Tasking story management and AI collaboration features.

### Negative

- **Temporary Gap in Installation Instructions:** The onboarding guide for installation will temporarily lack detailed steps until a new mechanism is designed and documented.
- **Manual Setup (Interim):** Users will need to rely on more manual setup steps or await new instructions.
- **Impact on Existing ADRs:** Several ADRs reference the `INSTALLING.md` or `ai-playbooks` concept and will need to be understood in this new context (see Links/References).

## Links / References

- **Supersedes:**
  - [`adr-008-ai-assisted-setup.md`](adr-008-ai-assisted-setup.md:1)
- **Affected ADRs (sections referencing `INSTALLING.md` or `ai-playbooks` are now historical or contextually altered):**
  - [`docs/adrs/adr-005-core-directory-structure.md`](docs/adrs/adr-005-core-directory-structure.md:1)
  - [`docs/adrs/adr-010-root-context-md.md`](docs/adrs/adr-010-root-context-md.md:1)
  - [`docs/adrs/adr-011-story-readme-sot.md`](docs/adrs/adr-011-story-readme-sot.md:1)
  - [`docs/adrs/adr-013-structured-onboarding.md`](docs/adrs/adr-013-structured-onboarding.md:1)
  - [`docs/adrs/adr-015-enhancing-ac-update-compliance.md`](docs/adrs/adr-015-enhancing-ac-update-compliance.md:1)
  - [`docs/adrs/adr-017-documentation-refactor.md`](docs/adrs/adr-017-documentation-refactor.md:1)
- **Related Story:**
  - [`docs/stories/s060-retire-ai-playbooks-concept/story.md`](docs/stories/s060-retire-ai-playbooks-concept/story.md:1) (This ADR is an outcome of this story)
  - [`docs/stories/s046-create-writing-ai-playbooks-guide/story.md`](docs/stories/s046-create-writing-ai-playbooks-guide/story.md:2) (To be closed as Obsolete)
