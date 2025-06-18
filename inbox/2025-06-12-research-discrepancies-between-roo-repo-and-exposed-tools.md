# Research Story: Discover Discrepancies Between Roo's Repo and Exposed Tools

This is a new standard research story to discover discrepancies between the Roo codebase and the tools exposed to the AI agent.

## Procedure:

1.  **Setup:** Create a temporary git submodule from the Roo codebase (`git@github.com:RooCodeInc/Roo-Code.git`), then initialize and update it.

2.  **Discovery:** Have the AI assistant investigate the `core/prompts` directory within the new submodule.

    - The AI must be aware of the limitations of the `list_files` tool when interacting with git submodules, as documented in `docs/reference/roo-code-capabilities.md`.
    - The AI should use the `find` command for reliable file discovery within the submodule.

3.  **Analysis & Artifact Creation:**

    - Create a new document in the `artifacts/` directory for this story.
    - In this document, list all discovered tool prompt files from the Roo codebase.
    - Note any discrepancies between this discovered list and the list of tools known to the AI from its initial system instructions.
    - Further note any discrepancies between the _features_ described in the discovered tool files (e.g., the availability of multi-file reads in `read_file`) and the AI's a priori knowledge.

4.  **Documentation Update:**
    - Update the primary `docs/reference/roo-code-capabilities.md` document with details about any newly discovered tools or features (like the `browser_action` tool).
