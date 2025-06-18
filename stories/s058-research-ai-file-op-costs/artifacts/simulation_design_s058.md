# Simulation Design for s058: Measure AI File Operation Costs

This document outlines the parameters and templates used for the simulation in story s058.

## Simulation Parameters

- **Preamble Length (simulated `story.md`):** Approximately 30 lines of realistic-looking preamble text (excluding frontmatter and AC section headers).
- **Number of Acceptance Criteria (simulated `story.md`):** 30 ACs.

## Simulated `story.md` Template

The following template will be used to initialize the `story.md` file for the simulation.

```markdown
---
id: "sim-s001-test-story"
title: "Simulated Test Story for Performance Measurement"
status: "In Progress"
---

# Story: sim-s001-test-story - Simulated Test Story

## Description

This is a simulated story file designed specifically for performance testing of AI file operations.
The primary goal is to measure the time taken for operations like marking Acceptance Criteria
as complete and appending entries to a corresponding journal file.

The structure of this file mimics a real Vibe Tasking story but uses placeholder content
to achieve the desired line counts for preamble and Acceptance Criteria.

This simulation focuses on the mechanical aspects of file manipulation rather than
the semantic content of a typical development story. The data gathered will help
in understanding the overhead associated with these common operations.

Preamble Line 1
Preamble Line 2
Preamble Line 3
Preamble Line 4
Preamble Line 5
Preamble Line 6
Preamble Line 7
Preamble Line 8
Preamble Line 9
Preamble Line 10
Preamble Line 11
Preamble Line 12
Preamble Line 13
Preamble Line 14
Preamble Line 15
Preamble Line 16
Preamble Line 17
Preamble Line 18
Preamble Line 19
Preamble Line 20

## Acceptance Criteria

**IMPORTANT:** As you complete each Acceptance Criterion below, you **MUST** mark it by changing `- [ ]` to `- [x]` (or `- [X]`).

- [ ] AC Item 1
- [ ] AC Item 2
- [ ] AC Item 3
- [ ] AC Item 4
- [ ] AC Item 5
- [ ] AC Item 6
- [ ] AC Item 7
- [ ] AC Item 8
- [ ] AC Item 9
- [ ] AC Item 10
- [ ] AC Item 11
- [ ] AC Item 12
- [ ] AC Item 13
- [ ] AC Item 14
- [ ] AC Item 15
- [ ] AC Item 16
- [ ] AC Item 17
- [ ] AC Item 18
- [ ] AC Item 19
- [ ] AC Item 20
- [ ] AC Item 21
- [ ] AC Item 22
- [ ] AC Item 23
- [ ] AC Item 24
- [ ] AC Item 25
- [ ] AC Item 26
- [ ] AC Item 27
- [ ] AC Item 28
- [ ] AC Item 29
- [ ] AC Item 30
```

**Line Count Analysis for `story.md` template:**

- Frontmatter: 4 lines
- Title Heading: 1 line
- Description Heading: 1 line
- Description Text: 10 lines
- Placeholder Preamble Lines: 20 lines
- Blank line before ACs: 1 line
- AC Heading: 1 line
- Blank line: 1 line
- "IMPORTANT" note: 1 line
- Blank line: 1 line
- AC Items: 30 lines
- **Total Lines:** 71 lines
- **Preamble Text Lines (Description + Placeholder Preamble):** 10 + 20 = 30 lines (Matches target)
- **AC Count:** 30 (Matches target)

## Simulated `journal.md` Template

The following template will be used to initialize the `journal.md` file for the simulation.

```markdown
# Journal: sim-s001-test-story - Simulated Test Story

## YYYY-MM-DDTHH:MM:SSZ

- Initial journal entry for simulated story.
- Simulation started.
```

This file will be appended to during the simulation. Each appended entry will consist of:

- A timestamp header (e.g., `## YYYY-MM-DDTHH:MM:SSZ`)
- A blank line
- 2-3 lines of placeholder text
- Totaling approximately 4-5 lines per new journal entry.

## Simulation Procedure and CSV Parsing

The following details the step-by-step procedure for an AI assistant (e.g., Cline) to execute the simulation, the data to be collected, and how it will be parsed.

### A. Simulation Execution Procedure

**Target Directory for Simulation Files:** `artifacts/temp_sim/` (This directory should be created before starting)

**I. Initialization:**

1.  **Create Simulated Story File:**
    - The AI assistant will use the `write_to_file` tool.
    - **Path:** `artifacts/temp_sim/simulated_story.md`
    - **Content:** The content of the "Simulated `story.md` Template" defined above in this document.
2.  **Create Simulated Journal File:**
    - The AI assistant will use the `write_to_file` tool.
    - **Path:** `artifacts/temp_sim/simulated_journal.md`
    - **Content:** The content of the "Simulated `journal.md` Template" defined above, with `YYYY-MM-DDTHH:MM:SSZ` replaced by the current UTC timestamp.

**II. Iterative Steps (Loop 1 to 30):**

For each step `N` from 1 to 30:

1.  **Mark Acceptance Criterion in `simulated_story.md`:**

    - The AI assistant will use the `apply_diff` tool.
    - **Path:** `artifacts/temp_sim/simulated_story.md`
    - **Diff Block:**
      ```diff
      <<<<<<< SEARCH
      :start_line:M
      -------
      - [ ] AC Item N
      =======
      - [x] AC Item N
      >>>>>>> REPLACE
      ```
      Where `N` is the current step number (1-30).
      The `start_line` `M` for `AC Item N` is `41 + N`. (e.g., for AC Item 1, line is 42; for AC Item 30, line is 71).
    - **Data to Record:** Start time, end time, and/or duration of the `apply_diff` operation from the AI assistant's tool execution report.

2.  **Append Entry to `simulated_journal.md`:**

    - **Read:** The AI assistant will use `read_file` to get the current content of `artifacts/temp_sim/simulated_journal.md`.
    - **Construct New Entry:**

      ```markdown
      ## YYYY-MM-DDTHH:MM:SSZ (Current UTC Timestamp)

      - Step N completed.
      - Marked AC Item N in simulated_story.md.
      - Placeholder journal text for step N, ensuring entry is ~5 lines total.
      ```

      (Replace `N` with the current step number and `YYYY-MM-DDTHH:MM:SSZ` with the actual current UTC timestamp).

    - **Append:** The AI will append the new entry (including a preceding newline if necessary to separate from the last entry) to the content read in memory.
    - **Write:** The AI assistant will use `write_to_file` to write the entire modified content back to `artifacts/temp_sim/simulated_journal.md`.
    - **Data to Record:** Start time, end time, and/or duration of the `write_to_file` operation from the AI assistant's tool execution report. (Note: This duration effectively covers the "append" operation, as the read operation is typically much faster and preparatory).

**III. Data Logging:**

- Throughout the simulation, the AI assistant's complete interaction log (including all tool calls, parameters, and reported results/timings) must be saved. This log is the primary source for parsing data.

### B. CSV Data Structure for Output

The collected data will be parsed into a CSV file named `artifacts/simulation_data_s058.csv`.

**Columns:**

1.  `step_number`: (Integer) The simulation step number (1 to 30).
2.  `operation_type`: (String) Describes the action performed. Values:
    - `mark_ac` (for updating `simulated_story.md`)
    - `append_journal` (for updating `simulated_journal.md`)
3.  `file_type`: (String) The type of file operated on. Values:
    - `story_md`
    - `journal_md`
4.  `tool_used`: (String) The specific AI tool invoked. Values:
    - `apply_diff`
    - `write_to_file` (representing the append operation which includes a read)
5.  `start_time_iso`: (String) The ISO 8601 timestamp (e.g., `YYYY-MM-DDTHH:MM:SS.sssZ`) when the tool operation started, if available from the AI's log.
6.  `end_time_iso`: (String) The ISO 8601 timestamp when the tool operation ended, if available from the AI's log.
7.  `duration_ms`: (Integer) The duration of the tool operation in milliseconds, as reported by the AI or calculated from start/end times.

Each simulation step (1-30) will result in two rows in the CSV: one for the `mark_ac` operation and one for the `append_journal` operation.

### C. Data Parsing Method

**Initial Method: Manual Parsing from AI Log**

1.  After the AI assistant (Cline) completes the 30-step simulation, save the entire chat/interaction log.
2.  Manually review the log for each of the 30 steps.
3.  For each step `N`:
    - **Locate `apply_diff` for `simulated_story.md`:**
      - Extract the reported start time, end time, or duration for this `apply_diff` call.
      - Create a CSV row with `step_number=N`, `operation_type="mark_ac"`, `file_type="story_md"`, `tool_used="apply_diff"`, and the timing data.
    - **Locate `write_to_file` for `simulated_journal.md`:**
      - Extract the reported start time, end time, or duration for this `write_to_file` call.
      - Create a CSV row with `step_number=N`, `operation_type="append_journal"`, `file_type="journal_md"`, `tool_used="write_to_file"`, and the timing data.
4.  Compile all 60 rows into `artifacts/simulation_data_s058.csv`.

This manual method is suitable for the single planned simulation run. If more extensive testing is done later, scripting this parsing process would be beneficial.
