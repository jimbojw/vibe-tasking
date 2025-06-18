---
id: "ascii-art-diagrams-authoring-guide"
title: "Guide: Effective ASCII-Art Diagrams"
usage: "Use this guide for principles and best practices when creating clear, consistent, and maintainable ASCII-art diagrams within the project, especially for version-control friendliness and Markdown integration."
tags: "ascii-art;diagrams;documentation;style-guide;markdown"
---

# Guide: Effective ASCII-Art Diagrams

**(Primary Audience: Project Contributors (and AI Assistants aiding them) seeking to create clear, consistent, and maintainable ASCII-art diagrams.)**

## Introduction

This guide provides principles and best practices for creating effective ASCII-art diagrams within this project. Clear, consistent, and maintainable diagrams are crucial for effective communication and documentation. Adhering to these guidelines will help ensure that our diagrams serve their purpose well.

The use of ASCII-art for diagrams is a deliberate choice, as outlined in [ADR-016: ASCII-Art Diagrams](../../../docs/adrs/adr-016-ascii-art-diagrams.md), primarily for its version-control friendliness, accessibility, and ease of integration into Markdown documentation.

This guide synthesizes lessons learned from previous diagramming efforts and aims to establish a common standard.

## Core Principles

### 1. Use Clear Connecting Characters

**Rationale:** Clear and appropriate connectors are essential for showing flow and relationships accurately. Prefer dedicated box-drawing characters over simple ASCII `|`, `-`, and `+` for more visually appealing and unambiguous diagrams.

**DO (Clear Connector Usage):**

- Vertical lines: Use `│` (box drawings light vertical).
- Horizontal lines: Use `─` (box drawings light horizontal).
- Junctions:
  - For T-junctions from a vertical line: `├` (tee right), `┤` (tee left).
  - For T-junctions from a horizontal line: `┬` (tee down), `┴` (tee up).
  - For crossing lines: `┼` (cross).
- Corners: Use `└` (up and right), `┘` (up and left), `┌` (down and right), `┐` (down and left).

**Example:**
(Note how vertical lines connect to the center of box frames, main vertical stems are aligned, and horizontal arrows point to the middle of the target box's side. This example uses the recommended full ASCII box style.)

```
   ┌───────┐
   │ Start │
   └───────┘
       │
       │↓
   ┌────────────────┐
   │ Decision Point │
   └────────────────┘
       │
       │      ┌───────────┐
       ├────► │ Process X │
       │      └───────────┘
       │            │
       │            │↓
       │         ┌──────────┐
       │         │ Result X │
       │         └──────────┘
       │
       │      ┌───────────┐
       └────► │ Process Y │
              └───────────┘
                    │
                    │↓
                 ┌──────────┐
                 │ Result Y │
                 └──────────┘
```

**(Optional) DON'T (Confusing or Ambiguous Connectors):**
(This example uses simple brackets for brevity, as the focus is on bad connectors)

```
[Start]
  | // Using simple pipe which might look like 'l' or 'I'
  +-- [Branch A] // '+' can be visually jarring
  |   || // Unclear double lines
[Main Flow] -- [Branch B] // Simple dashes lack connection
```

### 2. Prefer Arrowheads for Clarity

**Rationale:** While flow can sometimes be inferred from context, explicitly using arrowheads removes ambiguity and makes diagrams significantly easier to follow. A mixed approach can offer the best clarity:

- Use standard arrow characters (`→`, `←`, `↑`, `↓`) for arrows directly connected to boxes or on very short line segments (standalone arrows).
- Use triangle arrowheads (`►`, `◄`) for arrows at the end of longer **horizontal** connecting lines, as they provide a more distinct termination. (Vertical arrows are handled with standard arrowheads, as detailed below).

**DO (Use Arrowheads - Style Guide):**
Apply arrowhead styles consistently based on orientation and space:

- **Vertical Arrows:** Always use standard arrow characters inline with the vertical bar. This applies regardless of the length of the vertical segment.
  - Examples: `│↓` (downward), `│↑` (upward)
- **Horizontal Arrows:**
  - **Preferred:** Use triangle arrowheads at the end of a horizontal line for a clear termination.
    - Examples: `──►` (rightward), `◄──` (leftward)
  - **Space-Saving Alternative:** If horizontal space is very constrained, a single standard arrow character may be used.
    - Examples: `→` (rightward), `←` (leftward)

**Preview of Arrowhead Styles (using full boxes):**

```
┌─────────┐
│  Box 1  │
└─────────┘
    │↓
┌─────────┐        ┌─────────┐
│  Box 2  │ ◄────► │  Box 3  │
└─────────┘        └─────────┘
    │↑                 │↓
┌─────────┐        ┌─────────┐
│  Box 4  │ ◄───── │  Box 5  │
└─────────┘        └─────────┘
    │↓
┌─────────┐
│  Box 6  │
└─────────┘
```

_Comments on preview:_
_// Box 1 to Box 2: Vertical arrow (standard, inline)_
_// Box 2 to Box 3: Horizontal arrow (triangle preferred)_
_// Box 4 to Box 2: Vertical arrow (standard, inline)_
_// Box 5 to Box 4: Horizontal arrow (triangle preferred - assuming space)_
_// Box 5 to Box 6: Vertical arrow (standard, inline)_

**Consideration:**
Clarity and consistency are paramount. Choose the appropriate style based on these guidelines and apply it uniformly within your diagram.

### 3. Minimize Horizontal Width & Indentation

**Rationale:** Wide diagrams or those with excessive indentation can easily wrap in different viewing environments. Wrapping breaks the visual flow. Prefer "un-indented" or minimally indented styles. Full ASCII boxes (see Section 6) naturally require more width than simple brackets; balance this with concise labels.

**DON'T (Overly Wide/Indented with Full Boxes):**

```
                        ┌───────────┐
                        │ StartHere │  // Too much indent
                        └───────────┘
                              │
                              │↓
┌───────────────────────────────────────────────────────────────────────────┐
│ Process A (Details that make it very wide and hard to read in a full box) │
└───────────────────────────────────────────────────────────────────────────┘
                              │
                              │↓
                        ┌───────────┐
                        │ Process B │ // Still too wide due to content
                        └───────────┘
                              │
                              │↓
                        ┌──────────┐
                        │ End Here │
                        └──────────┘
```

**DO INSTEAD (Narrower/Less Indented with Full Boxes):**

```
┌────────────┐
│ Start Here │
└────────────┘
      │↓
┌────────────┐
│ Process A  │
└────────────┘
(Details below)
      │↓
┌────────────┐
│ Process B  │
└────────────┘
(More details)
      │↓
┌────────────┐
│ End Here   │
└────────────┘
```

_1. Details for Process A can be elaborated here._
_2. Further information about Process B follows here._

### 4. Keep Diagram Labels Concise ("Text-Light")

**Rationale:** Overly verbose labels within boxes create clutter and wide boxes. The diagram should provide clear visual structure; elaborate details in accompanying text.

**DON'T (Overly Verbose Labels in Full Boxes):**

```
┌───────────────────────────────────────────────────────────────┐
│ This is the Very First Step in Our Extremely Complex Workflow │
└───────────────────────────────────────────────────────────────┘
                                 │↓
┌───────────────────────────────────────────────────────────────────────────────────┐
│ Next, We Diligently Perform Exhaustive Data Validation and Preprocessing Which    │
│ Involves Several Critical Sub-steps That Must Be Documented Verboseley Inside Box │
└───────────────────────────────────────────────────────────────────────────────────┘
                                 │↓
┌──────────────────────────────────────────────────────────────────────────────┐
│ Finally, the Results Are Aggregated and Presented to the End User for Review │
└──────────────────────────────────────────────────────────────────────────────┘
```

**DO INSTEAD (Concise Labels with Numbering in Full Boxes):**

```
┌────────────────────┐
│ 1. Workflow Start  │
└────────────────────┘
          │↓
┌────────────────────┐
│ 2. Data Validation │
└────────────────────┘
          │↓
┌────────────────────┐
│ 3. Present Results │
└────────────────────┘
```

1. **Workflow Start:** Initiates the overall process.
2. **Data Validation:** Includes sub-steps for data cleaning and transformation.
3. **Present Results:** Aggregated data is shown to the user.

### 5. Use Supplementary Explanations Below Diagrams

**Rationale:** Keeping diagrams clean is key. Use numbered lists or paragraphs below the diagram for details.

- **Direct Mapping:** Number elements in the diagram (e.g., `│ 1. First Step │`) to link to numbered explanations.
- **Grouped Mapping:** Use a suffix for multiple elements mapping to one explanation (e.g., `│ Box A (1) │`, `│ Box B (1) │`).

**DON'T (Explanatory Text Crammed into Full Boxes):**

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ Step 1: User submits request. This must be a POST request to /api/submit with a  │
│ JSON payload containing 'id' (UUID) and 'data' (string).                         │
└──────────────────────────────────────────────────────────────────────────────────┘
                                       │↓
┌──────────────────────────────────────────────────────────────────────────────────┐
│ Step 2: System validates input. Checks for required fields: 'id', 'data'. 'id'   │
│ must be a valid UUID format. 'data' must not be empty.                           │
└──────────────────────────────────────────────────────────────────────────────────┘
                                       │↓
                                      ...
```

**DO INSTEAD (Clean Diagram with Numbered Supplementary Text - Full Boxes):**

```
   ┌─────────────────┐
   │ 1. User Request │
   └─────────────────┘
           │↓
   ┌───────────────────┐
   │ 2. Validate Input │
   └───────────────────┘
           │
           │   ┌─────────────────┐
           ├─► │ 3. Return Error │
           │   └─────────────────┘
           │
           │↓ (Valid)
   ┌─────────────────┐
   │ 4. Process Data │
   └─────────────────┘
```

_1. **User Request:** User submits a POST request to `/api/submit` with a JSON payload._
_2. **Validate Input:** The system checks for required fields (`id`, `data`). The `id` field must be a UUID._
_3. **Return Error:** If validation fails, a 400 error with details is returned._
_4. **Process Data:** If validation succeeds, the data is processed._

**DO INSTEAD (Grouped Mapping with Suffix - Full Boxes):**

```
┌────────────────┐
│ Action A (1)   │
└────────────────┘
        │↓
┌────────────────┐
│ Action B (1)   │
└────────────────┘
        │↓
┌────────────────┐
│ Action C (2)   │
└────────────────┘
```

_1. **Initial Phase:** Action A and Action B together constitute the initial phase of the process, where X and Y occur._
_2. **Concluding Step:** Action C represents the final step._

### 6. Consistent Box Styles and Label Casing

**Rationale:** Consistency in visual elements aids readability and professionalism.

**DO (Recommended Style - Full ASCII Boxes):**

- Use full ASCII boxes:
  ```
  ┌─────────┐
  │  Label  │
  └─────────┘
  ```
- Ensure the label text is padded with at least one space on each side within the box (e.g., `│  Label  │` not `│Label│`).
- Use Title Case for labels within boxes (e.g., `│ My Label │`). Numbered labels (e.g., `│ 1. My Label │`) are also fine.
- Strive to make boxes of similar conceptual weight or hierarchy level roughly the same width for visual balance, if content allows.

**Example:**

```
┌────────────────────┐
│ Standard Full Box  │
└────────────────────┘
          │↓
┌────────────────────┐
│ Another Full Box   │
└────────────────────┘
```

**(Optional) DON'T (Inconsistent Styling):**
(This example uses mixed styles for illustration of what to avoid)

```
[ Bracket Box ]
        │
        V
  *****************
  * Asterisk Box  *
  *****************
        │↓
┌────────────────────┐
│ Full Box Correctly │
└────────────────────┘
```

### 7. Consider "Taller" Diagram Style for Clarity

**Rationale:** Sometimes, giving elements more vertical space (longer connecting lines `│`) can prevent cramping and improve clarity, especially when horizontal space is constrained by full boxes.

**DON'T (Too Cramped Vertically with Full Boxes):**
(Assumes A, B, C are related sequentially, then D, E, F are related sequentially below them)

```
┌───┐  ┌───┐  ┌───┐
│ A │─►│ B │─►│ C │
└───┘  └───┘  └───┘
  │↓     │↓     │↓
┌───┐  ┌───┐  ┌───┐
│ D │─►│ E │─►│ F │
└───┘  └───┘  └───┘
```

**DO INSTEAD (Effective Use of Vertical Space with Full Boxes):**

```
┌───────┐         ┌───────┐         ┌───────┐
│   A   │  ────►  │   B   │  ────►  │   C   │
└───────┘         └───────┘         └───────┘
    │                 │                 │
    │↓                │↓                │↓
    │                 │                 │
┌───────┐         ┌───────┐         ┌───────┐
│   D   │  ────►  │   E   │  ────►  │   F   │
└───────┘         └───────┘         └───────┘
```

Alternatively, for purely vertical flows that are complex:

```
      ┌──────────────┐
      │ Top Element  │
      └──────────────┘
            │
            │↓ (long connector)
            │
      ┌────────────────┐
      │ Middle Element │
      └────────────────┘
            │
            │↓
            │
      ┌────────────────┐
      │ Bottom Element │
      └────────────────┘
```

## Comprehensive Example

Here is an example of a moderately complex flow, a "Documentation Review Process," illustrating several of the principles discussed, using full ASCII boxes:

```
      ┌───────────────────┐
      │ 1. Draft Document │
      └───────────────────┘
              │↓
      ┌──────────────────────┐
      │ 2. Submit for Review │
      └──────────────────────┘
              │↓
      ┌──────────────────────┐
      │ 3. Reviewer Assesses │  ◄─────────┐
      └──────────────────────┘            │
              │                           │
              │   ┌───────────────────┐   │
              ├─► │ 4. Author Revises │   │
              │   └───────────────────┘   │
              │         │                 │
              │         └─► (Re-submit) ──┘
              │
              │   ┌───────────────────┐
              └─► │ 5. Final Approval │
                  └───────────────────┘
                          │↓
                 ┌─────────────────────┐
                 │ 6. Publish Document │
                 └─────────────────────┘
```

**Explanation of Diagram Elements:**

1.  **Draft Document:** The author creates the initial version of the document.
2.  **Submit for Review:** The draft is submitted to designated reviewers.
3.  **Reviewer Assesses:** The reviewer examines the document.
    - If feedback is provided, the process moves to step 4.
    - If no feedback is given (or minor points are addressed and it's approved), it moves to step 5.
4.  **Author Revises:** The author incorporates the feedback into the document. After revision, the document is re-submitted for review (looping back to the line above "3. Reviewer Assesses").
5.  **Final Approval:** Once all feedback is addressed and reviewers are satisfied, the document receives final approval.
6.  **Publish Document:** The approved document is published to its intended location.

This diagram uses:

- Full ASCII boxes with centered text.
- Clear connecting characters (`│`, `─`, `├`, `└`, `┌`, `┐`).
- Arrowheads (inline `↓`/`↑` for vertical; `►`/`◄` for horizontal line ends) for unambiguous flow.
- Concise labels with numbering.
- An explicit loop.
- Supplementary numbered explanations below for clarity.
- Minimized horizontal width where possible, balanced with full box style.

---

_This guide is a living document and may be updated as new best practices emerge._
