---
id: "s034-create-workflow-guide"
title: "Create Vibe Tasking Workflow Guide"
status: "Done"
priority: "Medium"
tags: "documentation;guide;workflow;planning"
resolution: "Implemented"
---

# Story: s034 - Create Vibe Tasking Workflow Guide

## Description

**User Story:** As a Vibe Tasking user, I want a guide document that illustrates common development workflows using the Vibe Tasking methodology so that I can better understand how to apply it to various real-world scenarios.

**Details:** This story involves creating a new Markdown file, `docs/guides/workflow-guide.md`. This guide will detail three distinct workflows. For each workflow, the guide must include:

- A terse ASCII-art diagram representing the flow with numbered steps.
- A corresponding numbered list that elaborates on each step and transition in the diagram.

The specific workflows to be documented are detailed below.

## Workflows to Document

### 1. Workflow 1: The Full Feature Lifecycle (Sequential Focus)

_Purpose: Illustrates how a single, larger piece of work might progress through different types of Vibe Tasking stories from initial idea to completion._

```
[ START: NEW REQUIREMENT / IDEA ]
       |
       v
[ 1. PLANNING SESSION (User + AI) ]
       |
       +--(If Research Needed)--> [ 2A. CREATE RESEARCH STORY ]
       |                             |
       |                             v
       |                             [ 2B. EXECUTE RESEARCH STORY ]
       |                             |
       |                             v
       +--(Proceed to Design)------- [ 3. CREATE DESIGN STORY ]
       |
       +--(If No Research Needed)--> [ 3. CREATE DESIGN STORY ]
                                           |
                                           v
                                     [ 4. EXECUTE DESIGN STORY ]
                                           |
                                           v
                                     [ 5. CREATE IMPLEMENTATION STORY ]
                                           |
                                           v
                                     [ 6. EXECUTE IMPLEMENTATION STORY ]
                                           |
                                           v
                                     [ 7. VALIDATION & TESTING ]
                                           |
                                           v
                                     [ 8. USER CONFIRMATION ]
                                           |
                                           v
                                     [ 9. COMPLETE IMPLEMENTATION STORY ]
                                           |
                                           v
[ END: FEATURE DELIVERED / WORK COMPLETED ]
```

**Explanation for Workflow 1:**

1.  **PLANNING SESSION (User + AI):** Discuss the requirement, decide initial approach. Output: Decision on next steps (e.g., need Research, or go straight to Design).
2.  **A. CREATE RESEARCH STORY (If Research Needed):** Story created with Status: To Do.
    **B. EXECUTE RESEARCH STORY:** Status: In Progress -> Done. Output: Findings, PoCs, documented knowledge.
3.  **CREATE DESIGN STORY:** (May use Research outputs if step 2 occurred, or directly if no research was needed). Status: To Do.
4.  **EXECUTE DESIGN STORY:** Status: In Progress -> Done. Output: Design specs, ADRs, mockups, diagrams.
5.  **CREATE IMPLEMENTATION STORY:** (Based on Design Story outputs). Status: To Do.
6.  **EXECUTE IMPLEMENTATION STORY:** Status: In Progress. Activities: Coding, configuration, unit testing.
7.  **VALIDATION & TESTING:** (As per Implementation Story ACs). Activities: Integration tests, QA, script execution.
8.  **USER CONFIRMATION:** (As per Implementation Story ACs). Activity: User reviews and approves the implemented work.
9.  **COMPLETE IMPLEMENTATION STORY:** Status: Done / Closed (with appropriate Resolution).

### 2. Workflow 3: Iterative Development with Feedback Loops

_Purpose: Emphasizes the iterative nature, especially between Design and Implementation, and how feedback can lead to revisiting earlier stages._

```
[ 1. PLANNING (User + AI) ]
       |
       v
[ 2. STORY EXECUTION (Initial Phase) ]
       |
       v
[ 3. INTERNAL REVIEW / AI-USER COLLABORATION ]
       |
       +--(If more fundamental info needed)--> Go back to Step 1/2
       |
       v
[ 4. STORY EXECUTION (Main Phase) ]
       |
       v
[ 5. VALIDATION / TESTING ]
       |
       +--(If issues requiring design changes)--> Go back to Step 2/3
       |
       +--(If minor bugs)--> Iterate within Step 4/5
       |
       v
[ 6. USER CONFIRMATION ]
       |
       v
[ 7. STORY COMPLETION ]
       |
       +--(If enables subsequent story)--> Go to Step 1
       |
       v
[ END (for this story/iteration) ]
```

**Explanation for Workflow 3:**

1.  **PLANNING (User + AI):** Output: New Story (e.g., Research, Design, or Implementation) with Status: "To Do".
2.  **STORY EXECUTION (Initial Phase - e.g., Research or Design):** Status: "To Do" -> "In Progress". Activities: Conduct research, draft design. Output: Initial findings, draft design document.
3.  **INTERNAL REVIEW / AI-USER COLLABORATION:** Activities: User reviews draft, AI suggests refinements, iterative updates. If more fundamental information is needed, return to planning or initial execution.
4.  **STORY EXECUTION (Main Phase - e.g., Finalize Design or Start Implementation):** Status: "In Progress". Activities: Finalize design based on feedback, start coding based on design. Output: Completed Design Document, Initial Code.
5.  **VALIDATION / TESTING (of Implementation):** Activities: Run tests, AI demonstrates functionality, user tests. If issues require design changes, return to earlier execution/review. If minor bugs, iterate within coding/testing.
6.  **USER CONFIRMATION:** Activity: User formally confirms all ACs are met for the current story.
7.  **STORY COMPLETION:** Status: "In Progress" -> "Done" / "Closed". Output: Completed and validated work for that story. If this story enables a subsequent story, return to planning for the next story.

### 3. Workflow 4 (Revised): Addressing Architectural Challenges with Iterative PoCs

_Purpose: Illustrates how encountering a limitation leads to researching alternatives, performing proof-of-concept evaluations for promising candidates, and then proceeding to design and implementation once a viable path is confirmed._

```
[ 1. DISCOVERY: ENCOUNTER DIFFICULTY ]
       |
       v
[ 2. PLANNING SESSION ]
       |
       v
[ 3. CREATE RESEARCH STORY (Broad Scan) ]
       |
       v
[ 4. EXECUTE RESEARCH STORY (Broad Scan) ]
       |
       v
[ 5. DECISION: SELECT NEXT CANDIDATE FOR PoC ]
       |
       +--(YES)--> [ 6. CREATE RESEARCH STORY (PoC) ]
       |              |
       |              v
       |              [ 7. EXECUTE RESEARCH STORY (PoC) ]
       |              |
       |              +--(PoC SUCCESSFUL?)--------------------------------------+
       |              |        |                                                |
       |              |        +--(YES)--> [ 8. CREATE ADR & PRELIM. DESIGN ]   |
       |              |                      |                                  |
       |              |                      v                                  |
       |              |                      [ GO TO STEP 9 ]                   |
       |              |                                                         |
       |              +--(PoC FAILED)------------------------------------------+
       |                       |                                                |
       |                       +---------------> [ LOOP BACK TO STEP 5 ]        |
       |
       +--(NO clear candidate)--> [ RE-EVALUATE / BROADER RESEARCH ]
                                       |
                                       v
                                   [ (Loop to 3 or Abandon) ]

[ 9. CREATE DESIGN STORY (Detailed Design) ]
       |
       v
[ 10. EXECUTE DESIGN STORY ]
       |
       v
[ 11. CREATE IMPLEMENTATION STORY(IES) ]
       |
       v
[ 12. EXECUTE IMPLEMENTATION STORY(IES) ]
       |
       v
[ END: ARCHITECTURAL CHALLENGE ADDRESSED ]
```

**Explanation for Workflow 4 (Revised):**

1.  **DISCOVERY: ENCOUNTER DIFFICULTY / LIMITATION:** Problem: Current architecture does not meet a new requirement or reveals a flaw.
2.  **PLANNING SESSION (User + AI):** Purpose: Discuss the difficulty, agree on the need for investigation. Output: Decision to initiate research into alternatives.
3.  **CREATE RESEARCH STORY (Investigate Alternatives - Broad Scan):** Status: To Do. Goal: Identify a list of potential solutions/architectural alternatives.
4.  **EXECUTE RESEARCH STORY (Investigate Alternatives - Broad Scan):** Status: In Progress -> Done. Activities: Market research, literature review, high-level comparison. Output: Documented findings, list of potential alternatives with initial pros/cons.
5.  **DECISION POINT: SELECT NEXT CANDIDATE FOR PoC:** User + AI review the list of alternatives.
6.  **CREATE RESEARCH STORY (PoC for Candidate X) (If YES from Step 5):** Status: To Do. Goal: Deep dive, build "hello world"/PoC, assess feasibility.
7.  **EXECUTE RESEARCH STORY (PoC for Candidate X):** Status: In Progress -> Done. Activities: Build PoC, document learnings, test against core need. Output: Working PoC (or clear reasons for failure), detailed findings. If PoC fails, loop back to Step 5 to select another candidate. If no clear candidate from initial research or all PoCs fail, re-evaluate or conduct broader research.
8.  **CREATE ADR & PRELIMINARY DESIGN (If PoC Successful):** Often as artifacts/outputs of the successful PoC Research Story. Output: ADR for Candidate X, initial design thoughts. Then proceed to Step 9.
9.  **CREATE DESIGN STORY (Detailed Design for Chosen & Vetted Alternative):** Based on successful PoC, ADR, and preliminary design. Status: To Do. Goal: Full specification for integrating the chosen alternative.
10. **EXECUTE DESIGN STORY:** Status: In Progress -> Done. Output: Comprehensive design document.
11. **CREATE IMPLEMENTATION STORY(IES):** Based on detailed design; could be one or multiple linked stories. Status: To Do.
12. **EXECUTE IMPLEMENTATION STORY(IES):** Status: In Progress -> Done/Closed. Activities: Coding, testing, integration, validation.

## Artifacts

- `docs/guides/workflow-guide.md` (to be created)
- This `story.md` file.

## Acceptance Criteria

- [x] **Process:** Story status is updated to "In Progress" in this `story.md` file's frontmatter upon starting work.
- [x] **Process:** An initial journal entry is added to `journal.md` for this story, noting work has commenced.
- [x] **Process:** The `journal.md` for this story is kept up-to-date with entries detailing progress and decisions _as they are made_.
- [x] The new guide file `docs/guides/workflow-guide.md` is created.
- [x] The guide includes "Workflow 1: The Full Feature Lifecycle" with its ASCII diagram and detailed explanation as specified in this story's "Workflows to Document" section.
- [x] The guide includes "Workflow 3: Iterative Development with Feedback Loops" with its ASCII diagram and detailed explanation as specified in this story's "Workflows to Document" section.
- [x] The guide includes "Workflow 4 (Revised): Addressing Architectural Challenges with Iterative PoCs" with its ASCII diagram and detailed explanation as specified in this story's "Workflows to Document" section.
- [x] All ASCII diagrams are terse, using numbered steps.
- [x] All explanations clearly correspond to the numbered steps in their respective diagrams and match the details provided in this story.
- [x] User confirms the content of `docs/guides/workflow-guide.md` is clear, accurate, and effectively illustrates the Vibe Tasking workflows as defined in this story.
- [x] **Process:** User confirms the new story structure (directory, `story.md`, `journal.md`) and its initial content accurately reflect the planned work and adhere to the Story Documentation Guide.
