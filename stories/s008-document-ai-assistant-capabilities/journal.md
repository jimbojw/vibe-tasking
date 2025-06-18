# Journal: s008 - Research and Document AI Coding Assistant Capabilities

## 2025-05-16

- Story created.
- Status updated to "In Progress".
- Created artifact `docs/reference/ai-assistant-capabilities.md`.
- Outlined document structure within the artifact and populated the "Cline" section.
- Updated artifact link in `story.md`.
- Updated relevant acceptance criteria in `story.md`.
- Received user feedback on Cline:
  - Noted Cline's modal nature (Plan vs. Act mode) as a unique feature. User observed that the interaction model takes getting used to, especially regarding mode transitions during an active question flow.
    - Noted Cline's ability for direct backend connections (e.g., to Google's Gemini models via API key) as distinct from assistants that intermediate connections.
- Updated `docs/reference/ai-assistant-capabilities.md` to include these points under the "Cline" heading and in "Other Notable Features".
- Added user's note about Cursor AI's intermediated backend connections to `docs/reference/ai-assistant-capabilities.md` under the "Cursor AI" heading.
- Researched Cursor AI modes using the browser tool by visiting `https://docs.cursor.com/chat/agent` and `https://docs.cursor.com/chat/`.
- Documented Cursor AI's modes (Agent, Ask, Manual, Custom) in `docs/reference/ai-assistant-capabilities.md`.
- User requested to continue research on Windsurf.
- Cleared `./.tmp_ai_output/` directory.
- Fetched `https://docs.windsurf.com/windsurf/cascade/cascade` to `./.tmp_ai_output/windsurf_cascade_docs_main.html`.
- Read `windsurf_cascade_docs_main.html` and identified 5 additional links.
- Attempted to fetch the 5 additional links. Noted that these links appeared to redirect to a general "Getting Started" page.
- Synthesized information from `windsurf_cascade_docs_main.html` and the "Getting Started" page content.
- Updated the Windsurf (Codeium Cascade) section in `docs/reference/ai-assistant-capabilities.md` with the gathered information.
- Attempted to fetch specific Windsurf feature pages using corrected URLs. Confirmed `image-upload` and `web-search` pages, but others still led to general content. Decided to rely on the information gathered from the overview and "Getting Started" pages for Windsurf for now.
- With Cline, Cursor AI, and Windsurf now having initial details, the criterion for documenting at least two assistants is met, and research has been conducted for Windsurf.
- Updated acceptance criteria in `story.md`.
- Per user request, concluding this phase of research for s008. Story status updated to "Done".
