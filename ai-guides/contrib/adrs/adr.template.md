---
id: "adr-XXX" # e.g., "adr-001" - MUST BE UNIQUE
title: "A Concise and Descriptive Title for the Decision"
status: "Proposed" # Proposed | Accepted | Deprecated | Superseded
date: "{{YYYY-MM-DD}}" # Date of last status change, e.g., "2025-05-23"
tags: "tag1;tag2;relevant-area" # Semicolon-separated list. All lowercase.
# deciders: "" # Optional: Uncomment and provide value if used, otherwise remove this line.
# consulted: "" # Optional: Uncomment and provide value if used, otherwise remove this line.
# informed: "" # Optional: Uncomment and provide value if used, otherwise remove this line.
---

<!--
Guidance for Optional Frontmatter Fields (deciders, consulted, informed):
- The 'deciders', 'consulted', and 'informed' fields are optional.
- To include an optional field in your ADR:
  1. Uncomment the line (remove the leading '# ').
  2. Replace the empty double quotes "" with the actual string value (e.g., deciders: "User, Roo").
- If an optional field is not being used, it is recommended to remove the entire line for that field from the final ADR.
-->

# ADR-{{ADR_NUMBER_PLACEHOLDER}}: {{ADR_TITLE_PLACEHOLDER}}

<!-- The H1 title should match the 'id' (number part) and 'title' from the frontmatter. -->
<!-- Example: # ADR-021: Formalize ADR Authoring Process -->

<!-- Optional: If status is "Deprecated" or "Superseded", uncomment and fill this section: -->
<!-- ## Status -->
<!-- This ADR is {{STATUS}}. It was superseded by [ADR-YYY](adr-YYY-link-to-superseding-adr.md) on {{YYYY-MM-DD}}. -->
<!-- OR -->
<!-- This ADR is {{STATUS}}. It was deprecated on {{YYYY-MM-DD}} because [reason for deprecation]. -->

## Context

<!--
This section describes the forces at play, including technological, political, social, and project local. These are the "why" of the decision.
- What is the issue that we're seeing that this ADR is addressing?
- What is the problem statement or the driving force that leads us to make this decision?
- What are the constraints and assumptions?
-->

## Alternatives Considered (Optional)

<!--
This section describes other options considered for addressing the context.
If no significant alternatives were considered, this section can be omitted or briefly state that.
For each alternative:
- Briefly describe the alternative.
- Pros: Advantages of this alternative.
- Cons: Disadvantages of this alternative.
-->

### Alternative 1: [Name of Alternative]

- **Description:** (Brief description)
- **Pros:**
  - (Pro 1)
  - (Pro 2)
- **Cons:**
  - (Con 1)
  - (Con 2)

### Alternative 2: [Name of Alternative]

- **Description:** (Brief description)
- **Pros:**
  - (Pro 1)
- **Cons:**
  - (Con 1)

## Decision

<!--
This section describes our response to the context and the chosen solution. It's the "what we decided."
- Clearly state the decision.
- Justify the decision, referencing the context and why this option was chosen over alternatives.
- Include any diagrams or code snippets if helpful.
-->

## Consequences

<!--
This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones.
Consider various aspects like:
- Impact on developers, users, maintainability, performance, security, etc.
- Positive outcomes.
- Negative outcomes or trade-offs.
- Any follow-up work or new decisions that might be needed.
-->

### Positive

- (Benefit 1)
- (Benefit 2)

### Negative

- (Drawback 1 or Trade-off 1)
- (Potential Risk 1)

<!-- Optional:
## Links / References
- (Link to related ADRs, issues, documentation, etc.)
-->
