---
id: "s040-create-ascii-art-diagram-guide"
title: "Create Guide for Effective ASCII-Art Diagrams"
status: "Done"
priority: "Medium"
tags: "documentation;guide;ascii-art;diagrams;design-principles"
resolution: "Implemented"
---

# Story: s040 - Create Guide for Effective ASCII-Art Diagrams

As a project contributor, I want a dedicated guide on creating effective ASCII-art diagrams, so that diagrams across the project are clear, consistent, and maintainable.

**Details:**
This story involves creating a new guide document: `docs/ai-guides/ascii-art-diagrams-authoring-guide.md`.
The guide should synthesize lessons learned from previous diagramming efforts (notably from story `s034-create-workflow-guide` and its journal) into a set of affirmative directives and best practices.
Key principles to document include:

- Preferring "un-indented" or minimally indented styles to prevent wide diagrams from wrapping and breaking the visual flow.
- Keeping diagrams "text-light" by using concise labels within the diagram itself.
- Supplementing diagrams with numbered lists or detailed explanations below the diagram for more comprehensive descriptions.
- Using consistent elements like bracket boxes (`[ Label ]`) and Title Case for labels.
- Employing vertical bars (`|`) and other characters (`─`, `└`, `├`) to show flow and relationships clearly.
- Considering a "taller" diagram style where appropriate for clarity.
- The guide should include examples of good and, perhaps, "less effective" diagram snippets to illustrate the principles.
- Reference `adr-016-ascii-art-diagrams.md` for the rationale behind using ASCII-art.

## Artifacts (Links)

- [ASCII-Art Diagram Guide](../../ai-guides/ascii-art-diagrams-authoring-guide.md)
- [Journal for s034 (for lessons learned)](../s034-create-workflow-guide/journal.md)
- [ADR for ASCII-Art Diagrams](../adrs/adr-016-ascii-art-diagrams.md)
- [Workflow 1 Example (Story Lifecycle in Introduction)](../../onboarding/01-introduction.md#how-vibe-tasking-works-for-you-the-story-lifecycle)
- [Workflow 2 Example (Full Feature Lifecycle)](../../onboarding/06-workflow-feature-lifecycle.md)
- [Workflow 3 Example (Architectural Challenges)](../../onboarding/07-workflow-architectural-challenges.md)

## Acceptance Criteria

- [x] **Checkpoint: Initial Story Setup**

  - [x] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.
  - [x] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [x] **Process:** User confirms the overall Acceptance Criteria list (including all Checkpoints and nested ACs) for this story is accurate and complete before substantive work begins on later Checkpoints.
  - [x] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Draft ASCII-Art Diagram Guide' Checkpoint.

- [x] **Checkpoint: Draft ASCII-Art Diagram Guide**

  - [x] A new file `docs/ai-guides/ascii-art-diagrams-authoring-guide.md` is created.
  - [x] The guide's introduction explains its purpose and references `adr-016-ascii-art-diagrams.md`.
  - [x] For the principle of minimizing horizontal width/indentation:
    - [x] Clearly explains the rationale (preventing wrapping, improving readability).
    - [x] Includes a "DON'T" example illustrating overly wide/indented art.
    - [x] Includes a "DO INSTEAD" example showing a narrower/less indented alternative.
  - [x] For the principle of keeping diagram labels concise ("text-light"):
    - [x] Clearly explains the rationale (improving diagram clarity, reducing clutter).
    - [x] Includes a "DON'T" example with overly verbose labels within the diagram.
    - [x] Includes a "DO INSTEAD" example with concise labels.
  - [x] For the practice of using numbered lists/detailed text below diagrams for explanations:
    - [x] Clearly explains the rationale (keeping diagrams clean, providing space for detail).
    - [x] Includes a "DON'T" example where too much explanatory text is crammed into the diagram.
    - [x] Includes a "DO INSTEAD" example showing a clean diagram with supplementary numbered explanations below.
  - [x] For conventions on box styles (e.g., `[ Label ]`) and label casing (e.g., Title Case):
    - [x] Clearly documents the recommended style.
    - [x] Includes a "DO" example of the correct styling.
    - [x] (Optional) May include a "DON'T" example of inconsistent or unclear styling.
  - [x] For conventions on using connecting characters (`|`, `─`, `└`, `├`, etc.) effectively:
    - [x] Clearly documents recommended usage for clarity and flow.
    - [x] Includes a "DO" example of clear connector usage.
    - [x] (Optional) May include a "DON'T" example of confusing or messy connector usage.
  - [x] For the "taller" diagram style:
    - [x] Explains when and why to use more vertical space for clarity.
    - [x] Includes a "DON'T" example of a diagram that is too cramped vertically.
    - [x] Includes a "DO INSTEAD" example demonstrating effective use of vertical space.
  - [x] The guide includes at least one comprehensive, well-structured ASCII-art diagram that synthesizes multiple of these "DO" principles.
  - [x] User reviews the initial draft of `docs/ai-guides/ascii-art-diagrams-authoring-guide.md`.
  - [x] **Process:** All ACs within this 'Draft ASCII-Art Diagram Guide' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Draft ASCII-Art Diagram Guide' Checkpoint, including any feedback on the draft.
  - [x] **Process:** User approval is obtained to proceed to the 'Refine and Finalize Guide' Checkpoint.

- [x] **Checkpoint: Refine and Finalize Guide**

  - [x] Incorporate user feedback from the draft review into `docs/ai-guides/ascii-art-diagrams-authoring-guide.md`.
  - [x] Ensure the guide is clearly written, well-organized, and easy to understand.
  - [x] Verify all examples are accurate and effectively illustrate the principles.
  - [x] Perform a final proofread of the guide.
  - [x] User confirms the final version of `docs/ai-guides/ascii-art-diagrams-authoring-guide.md` is complete and meets all requirements.
  - [x] **Process:** All ACs within this 'Refine and Finalize Guide' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Refine and Finalize Guide' Checkpoint.
  - [x] **Process:** User approval is obtained to proceed to the 'Final Review and Closure' Checkpoint.

- [x] **Checkpoint: Final Review and Closure**
  - [x] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed.
  - [x] **Process:** Story status is updated to "Done" and `resolution` field is set to `"Implemented"`.
  - [x] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [x] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
