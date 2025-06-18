# Journal: s085-research-chat-markdown-rendering - Research and Document AI Chat Markdown Rendering Capabilities

## 2025-06-10T10:46:28Z

- Story `s085-research-chat-markdown-rendering` created.
- Purpose: To systematically research, document, and codify the Markdown rendering capabilities and limitations of typical AI assistant chat UIs. This includes a focus on Unicode character behavior and common formatting elements.
- The primary output will be a new reference document: `docs/reference/ai-chat-markdown-rendering-capabilities.md`.
- This research will build upon and consolidate findings from previous explorations, notably story `s076-design-ai-farkle-guide`.
- The goal is to enable better design of AI-generated chat responses and AI Guides for optimal and predictable display.
- Story created using `ai-guides/core/stories/story.template.md`.

## 2025-06-11T15:20:03Z

- Incorporated findings from deleted inbox item `inbox/2025-06-11-document-markdown-support-in-ask-followup-question-and-research-windsurf.md` into the 'Research Area: Markdown in `ask_followup_question` Tool Strings' section of the Acceptance Criteria.
- The findings note that for the `ask_followup_question` tool (observed in Roo Code during `s073`):
  - Markdown IS supported in the main `<question>` text.
  - Markdown IS NOT supported in the `<suggest>` option texts (it renders literally).
