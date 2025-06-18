---
id: "s041-research-ai-web-fetching-filtering"
title: "Research AI Assistant Capabilities for Web Page Fetching and Content Filtering"
status: "To Do"
priority: "Medium"
tags: "research;ai-capabilities;web-fetching;content-filtering;documentation"
resolution: "Unresolved"
---

# Story: s041 - Research AI Assistant Capabilities for Web Page Fetching and Content Filtering

As a Vibe Tasking user, I want to understand the capabilities and best practices for AI assistants to fetch web page content, filter it down to essential information, and make it available for analysis, so that AI-assisted web research can be more efficient and effective within a no-code project context.

**Details:**
This research story aims to produce a comprehensive report on available options for AI assistants to fetch and read web pages. The focus is on minimizing extraneous content (scripts, ads, navigation) and preserving structural elements, ideally outputting Markdown or minimalistic HTML. Since Vibe Tasking is a no-code project, all findings should be documented, even if code samples are developed for testing.

**Scope of Research:**

- **AI Assistants with Native Web Search/Browse:**
  - Cursor: Investigate its search capability (backend mechanisms if discernible, effectiveness).
  - Cline: Document observations of its browser-based actions (screenshots, OCR, scrolling).
  - Windsurf: Investigate and document its web-related capabilities (if any).
  - Other assistants (Copilot, Gemini Code Assist) are likely out of scope if they lack direct query/browse features, but this should be briefly confirmed.
- **Command-Line Tools via `execute_command`:**
  - `curl`: As a baseline for fetching raw HTML.
    - **Note on MediaWiki sites (e.g., Wikipedia):** Using `curl` with the `action=raw` URL parameter (e.g., `curl -L "https://en.wikipedia.org/w/index.php?title=PAGETITLE&action=raw"`) has proven effective for fetching clean, structured wikitext, bypassing much of the HTML chrome. This was successfully used in the context of story `s049`.
  - `lynx`: If available/installable without complex dependencies, for text-based rendering.
  - `pandoc`: For converting HTML to Markdown (GitHub Flavored Markdown preferred).
    - **Note on `curl | pandoc` for dynamic/complex pages:** During investigation of Cline's `execute_command` (ref: `docs/reference/cline-execute-command-behavior.md`), an attempt was made to fetch a GitHub issue page using `curl -sL [URL] | pandoc -f html -t markdown`. While this converted the initially served HTML, the result had two major issues:
      1. It failed to capture dynamically loaded content (like user comments).
      2. It included a significant amount of irrelevant structural elements (e.g., navigation bars, sidebars, UI components) from the GitHub page, making the actual issue content hard to discern.
         This highlights that this simple pipe is often insufficient for complex, JavaScript-heavy web pages or when a clean extraction of main content is needed. Alternatives like manual content provision (e.g., copy-pasting `document.body.textContent`) or browser automation tools (if available to the AI) would be necessary for more complete and cleaner capture.
  - Mozilla's `readability.js`: Explore how this JavaScript library could be used (e.g., potentially via a simple Node.js script executed by the AI, or if there are CLI wrappers) to extract main content. This should also consider its use in conjunction with browser automation.
- **Browser Automation for Dynamic Content & Readability Tools:**
  - Investigate the feasibility of AI assistants using `execute_command` to:
    - Launch and control headless browsers (e.g., Puppeteer with Node.js, Playwright, or direct browser CLI flags if available for Chrome/Firefox).
    - Navigate to a URL, allow JavaScript to render the page.
    - Execute a script (like a wrapper for `readability.js`) within the browser's context to extract the main content from the rendered DOM.
    - Output the cleaned content (e.g., to a file for the AI to read).
  - Key research questions:
    - Time taken for headless browser launch/page load.
    - Potential for reusing existing headless browser instances.
    - Complexity of scripting this flow for an AI assistant.
    - Dependencies required (e.g., Node.js, browser binaries).
- **Content Reduction/Filtering Techniques:**
  - Focus on methods to strip scripts, CSS, data URIs, ads, navigation, etc., both from raw HTML and from browser-rendered content.
  - Aim for outputs that preserve semantic structure (Markdown, minimal HTML).
- **Workflow for AI:** How can an AI assistant best leverage these tools? (e.g., fetching to `.tmp_ai_output/`, then processing, then reading the processed file). Reference `docs/guides/handling-command-output-issues.md`.
- **Output:** The primary output will be one or more research documents (e.g., a main report, potentially separate PoC notes) stored in this story's `artifacts/` directory. A dedicated guide is not expected from this story initially, but the research should lay the groundwork.

## Artifacts (Links)

- [Web Fetching Research Report](artifacts/web_fetching_research_report.md) (To be created)
- (Potentially other documents like PoC notes, TBD by research findings)
- [Handling Command Output Issues Guide](../../guides/handling-command-output-issues.md) (Reference)

## Acceptance Criteria

- [ ] **Checkpoint: Initial Story Setup**

  - [ ] **Process:** Story status is updated to "In Progress" in this story.md file's frontmatter upon starting work.
  - [ ] **Process:** A new journal entry is _appended_ to `journal.md` for this story, noting work has commenced.
  - [ ] **Process:** User confirms the overall Acceptance Criteria list (including all Checkpoints and nested ACs) for this story is accurate and complete before substantive work begins on later Checkpoints.
  - [ ] **Process:** All ACs within this 'Initial Story Setup' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Initial Story Setup' Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Investigate Native AI Capabilities' Checkpoint.

- [ ] **Checkpoint: Investigate Native AI Capabilities**

  - [ ] Document observed web search/browsing capabilities of Cursor.
  - [ ] Document observed web interaction capabilities of Cline.
  - [ ] Research and document web-related capabilities of Windsurf (if any).
  - [ ] Briefly confirm and document the lack of direct web query/browse for Copilot and Gemini Code Assist (unless new information suggests otherwise).
  - [ ] Summarize findings for native capabilities in `artifacts/web_fetching_research_report.md`.
  - [ ] **Process:** All ACs within this 'Investigate Native AI Capabilities' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Investigate Command-Line Tools & Filtering Techniques' Checkpoint.

- [ ] **Checkpoint: Investigate Command-Line Tools & Filtering Techniques**

  - [ ] Research and document the use of `curl` for raw HTML fetching by an AI.
  - [ ] Research and document the use of `lynx` (if feasible as a low-dependency tool) for text conversion.
  - [ ] Research and document the use of `pandoc` for HTML to Markdown conversion (focus on GFM).
    - [ ] Test with a sample complex webpage.
  - [ ] Research and document methods to use Mozilla's `readability.js` (e.g., via Node.js script or CLI wrapper if simple enough) for main content extraction.
    - [ ] Test with a sample complex webpage.
  - [ ] For each tool/technique, document:
    - [ ] How an AI assistant could invoke it (e.g., `execute_command` syntax).
    - [ ] Effectiveness in filtering "junk" and preserving structure.
    - [ ] Quality of output (e.g., readability of Markdown, completeness of extracted content).
    - [ ] Any significant dependencies or setup complexities from a no-code perspective.
  - [ ] Summarize findings for CLI tools and filtering in `artifacts/web_fetching_research_report.md`.
  - [ ] (Optional) Create small proof-of-concept scripts or command sequences for promising tool combinations, storing them in `artifacts/poc_scripts/`.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Synthesize Findings and Document Workflow' Checkpoint.

- [ ] **Checkpoint: Synthesize Findings and Document Workflow**

  - [ ] Consolidate all research into `artifacts/web_fetching_research_report.md`.
  - [ ] The report should include a comparison of the different approaches (native AI vs. CLI tools).
  - [ ] The report should recommend preferred workflows for AI assistants to fetch, filter, and read web content, considering efficiency and output quality.
  - [ ] Document how these workflows align with `docs/guides/handling-command-output-issues.md` (e.g., using `.tmp_ai_output/`).
  - [ ] Ensure the report is structured clearly and provides actionable insights.
  - [ ] User reviews the `artifacts/web_fetching_research_report.md`.
  - [ ] **Process:** All ACs within this Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this Checkpoint.
  - [ ] **Process:** User approval is obtained to proceed to the 'Final Review and Closure' Checkpoint.

- [ ] **Checkpoint: Final Review and Closure**
  - [ ] **Process:** User confirms all Checkpoints and their ACs are satisfactorily completed, and the research report is comprehensive.
  - [ ] **Process:** Story status is updated to "Done" and `resolution` field is set to `"Research Complete"`.
  - [ ] **Process:** All ACs within this 'Final Review and Closure' Checkpoint are reviewed with the user and marked as complete (`- [x]`).
  - [ ] **Process:** Journal updated to reflect completion of this 'Final Review and Closure' Checkpoint and the story's overall completion.
