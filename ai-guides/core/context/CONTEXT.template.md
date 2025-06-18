# AI Assistant Onboarding Instructions for {{PROJECT_NAME}} Project

Welcome! To effectively assist with tasks related to the {{PROJECT_NAME}} project, please begin by familiarizing yourself with its core documentation.

<!-- Optional: Include a section on collaborative ethos if relevant to your project -->
<!--
**A Note on Our Collaborative Ethos:**
As an AI assistant contributing to {{PROJECT_NAME}}, please remember that your role extends beyond mere execution. We view you as a thinking partner. In all interactions and tasks, strive to understand intent, leverage your analytical capabilities to offer insights, and engage in iterative refinement. Applying these collaborative principles consistently is key to our shared success and the spirit of this project.
-->

Please begin by carefully reading and understanding the content of the following files in this repository:

<!--
  List the essential documents for an AI assistant to understand your project.
  Provide:
  - A clear title or description for each document group.
  - The file path (link if possible).
  - A brief purpose statement for each document.
-->

1.  **Main Project Overview:**

    - **File:** [`README.md`](README.md) <!-- Or {{PATH_TO_MAIN_README}} -->
    - **Purpose:** This file provides a high-level understanding of the {{PROJECT_NAME}} project, its goals, key features, and overall structure.

2.  **Core AI Guide Discovery Process (from Vibe Tasking Submodule - CRITICAL):**
    <!--
      The Vibe Tasking submodule contains essential guides for AI interaction.
      You MUST determine the correct relative path to this submodule in your project.
      Common paths include 'vendor/vibe-tasking', 'submodules/vibe-tasking', or just 'vibe-tasking' if it's at the root.
      Replace {{PATH_TO_VIBE_TASKING_SUBMODULE}} with the actual path.
      Replace {{VIBE_TASKING_SUBMODULE_DIR_NAME}} with the directory name of the submodule (e.g., "vibe-tasking").
    -->

    - **File:** [`{{PATH_TO_VIBE_TASKING_SUBMODULE}}/ai-guides/core/ai-guides/ai-guides-discovering-guide.md`]({{PATH_TO_VIBE_TASKING_SUBMODULE}}/ai-guides/core/ai-guides/ai-guides-discovering-guide.md)
    - **Purpose:** This core guide from the `{{VIBE_TASKING_SUBMODULE_DIR_NAME}}` submodule details the definitive process for how to discover, index, and use all AI Guides (including precedence rules). This is ESSENTIAL for the AI to find other project-specific guidance.
    - **IMPORTANT CAVEAT:** The directory containing the `{{VIBE_TASKING_SUBMODULE_DIR_NAME}}` submodule (e.g., `vendor/`, `submodules/`) may **not** appear in initial file listings from tools like `environment_details` or `list_files .` when run from the {{PROJECT_NAME}} project root. This is expected behavior for Git submodules. You **MUST** trust the path to this `ai-guides-discovering-guide.md` file and attempt to read it directly. The guide itself will explain how to reliably find all guides using shell commands.
    - **Troubleshooting Unreadable Submodule Guide:** If reading [`{{PATH_TO_VIBE_TASKING_SUBMODULE}}/ai-guides/core/ai-guides/ai-guides-discovering-guide.md`]({{PATH_TO_VIBE_TASKING_SUBMODULE}}/ai-guides/core/ai-guides/ai-guides-discovering-guide.md) fails, check `git submodule status {{PATH_TO_VIBE_TASKING_SUBMODULE}}`. If it indicates uninitialized (output line starts with `-`), offer to run `git submodule init && git submodule update --recursive` for the user, or instruct them to do so. Then, re-attempt reading the guide.

3.  **Key Process/Convention Guide (Example - Add others as needed):**

    - **File:** `{{PATH_TO_KEY_GUIDE_1}}`
    - **Purpose:** {{PURPOSE_OF_KEY_GUIDE_1}}
    <!-- Optional: Add any critical caveats or notes specific to a document -->

4.  **Another Important Document (Example):**
    - **File:** `{{PATH_TO_KEY_GUIDE_2}}`
    - **Purpose:** {{PURPOSE_OF_KEY_GUIDE_2}}

<!-- Add more documents as needed. Remember to adjust numbering if you add/remove items. -->

Thank you for reviewing this initial context.
