# Journal: s036 - ADR: Document Decision to Use ASCII-Art for Diagrams

## 2025-05-20T11:43:37Z

- Story `s036` created to document an Architecture Decision Record (ADR) for using ASCII-art diagrams.
- **Type:** Documentation (ADR Creation).
- **Goal:** Create `docs/adrs/adr-015-ascii-art-diagrams.md` detailing the decision and rationale.
- **Key Rationale Points from User for ADR Context/Alternatives:**
  - Current Git hosting platforms for the project do not natively render Mermaid charts.
  - Using Mermaid would require taking on rendering/build/deployment burdens, challenging `adr-001-code-free-framework.md`.
  - ASCII-art ensures diagrams are viewable directly in text environments and version control.
  - The decision can be revisited if Mermaid support becomes more widespread on the hosting platform.
  - Regarding "Embedded Images" as an alternative:
    - Binary images (like PNGs) have less widespread AI assistant support for interpretation.
    - SVGs, while textual, are still complex and hard to diff meaningfully.
- Initial scope and Acceptance Criteria (including these points for the ADR content) discussed and finalized with the user.

## 2025-05-20T19:45:57Z

- Work commenced on story s036.
- Story status was updated to "In Progress".
- ADR number confirmed as adr-016. Story file `story.md` was updated to reflect this.
- User confirmed overall Acceptance Criteria list for s036 is accurate and complete.

## 2025-05-20T20:02:42Z

- Pausing active work on s036 to prioritize the creation of story s038 (Clarify Journal Entry Process).
- Story s036 status updated to "Blocked" and resolution set to "Blocked pending s038 completion".

## 2025-05-20T21:40:10Z

- Resuming work on story s036 as s038 is now complete.
- Story status updated to "In Progress" and resolution to "Unresolved" in `story.md`.
- Confirmed ADR number `adr-016` is still available.
- All ACs in the "Initial Story Setup" checkpoint are now marked as complete in `story.md`.
- This checkpoint is now considered complete.

## 2025-05-20T21:42:19Z

- Checkpoint "Create ADR for ASCII-Art Diagrams" completed.
- New ADR file `docs/adrs/adr-016-ascii-art-diagrams.md` created.
- User confirmed ADR content is accurate, complete, and captures the decision rationale effectively.
- All ACs for this checkpoint, including user confirmation and process steps, have been marked as complete in `story.md`.

## 2025-05-20T21:43:01Z

- Checkpoint "Final Review and Closure" completed.
- User confirmed all previous Checkpoints and their ACs were satisfactorily completed.
- Story `s036` status updated to "Done" and resolution to "Implemented" in `story.md`.
- All ACs for the "Final Review and Closure" checkpoint marked as complete.
- Story `s036` is now complete.
