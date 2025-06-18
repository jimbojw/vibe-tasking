---
id: "context-documents-authoring-guide"
title: "Guide: Interactively Assisting Users in Authoring Their First CONTEXT.md Document"
usage: "Use this guide when a user, especially one new to Vibe Tasking, needs to create their initial CONTEXT.md file. This guide outlines an interactive, coaching-focused process for the AI assistant to help the user understand, create, and learn how to use their CONTEXT.md."
tags: "context;onboarding;ai-assistant;initialization;workflow;authoring;interactive-tutorial;user-coaching;new-user"
---

# Guide: Interactively Assisting Users in Authoring Their First `CONTEXT.md` Document

**(Primary Audience: AI Assistant (to understand and execute an interactive, coaching-focused process for helping users, especially those new to Vibe Tasking, create their first `CONTEXT.md` file).)**

## Introduction: The Importance of a Guided First Step

Creating a `CONTEXT.md` file is often a new user's first significant interaction with the Vibe Tasking framework. They may not understand its purpose or how to best construct it. This guide provides **you, the AI assistant**, with a step-by-step interactive process to not only help the user create this crucial file but also to educate them on its importance and usage. Your role is that of a collaborative partner and coach.

This process emphasizes understanding the user's project, making informed suggestions, and ensuring the user is comfortable with both the `CONTEXT.md` file and how to use it effectively.

## The Interactive `CONTEXT.md` Authoring Workflow

When a user indicates they need to create a `CONTEXT.md` file (e.g., after initializing Vibe Tasking as a submodule, or when starting a new project with Vibe Tasking), **you MUST follow these steps**:

### Step 1: Initiation and Setting Expectations

1.  **Acknowledge User's Intent or AI's Proactive Guidance:**
    _(AI: Determine if this guide was invoked by explicit user request for `CONTEXT.md` creation, or as an automatic next step from another guide, e.g., `INSTALL_VIBE_TASKING.md`. Let's call this `[is_ai_initiated_flow]` which is true if AI is proactively guiding, false if user explicitly asked.)_

    - (If `[is_ai_initiated_flow]` is false) User: "I need to create a CONTEXT.md file." or "How do I set up my project for Vibe Tasking?"
    - **You (AI):** "(If `[is_ai_initiated_flow]` is true): Now that the previous step (e.g., Vibe Tasking installation) is complete, the next crucial step is creating a `CONTEXT.md` file. This file helps me understand your project better right from the start. I can guide you through that process."
    - **You (AI):** "(If `[is_ai_initiated_flow]` is false): Great! Creating a `CONTEXT.md` file is an excellent first step to ensure we can work together effectively on your project. I can guide you through that process."

2.  **Explain the Purpose of `CONTEXT.md`:**
    - You: "The `CONTEXT.md` file serves as an initial briefing for me (and any AI assistant you work with). It points me to the most important documents I need to read to understand your project's basics. This helps me provide more relevant and accurate assistance right from the start."
    - **You (AI):** "(If `[current_mode]` is 'Detailed' or `[is_ai_initiated_flow]` is false): We'll want to keep it brief, mainly linking to a few key files. The standard name for this file is `CONTEXT.md` and it's usually placed in the root of your project. Does that sound good?"
    - **You (AI):** "(If `[current_mode]` is 'Express' and `[is_ai_initiated_flow]` is true): We'll want to keep it brief, mainly linking to a few key files. The standard name for this file is `CONTEXT.md` and it's usually placed in the root of your project. I'll proceed with this understanding."

### Step 1.5: Determine Interaction Mode

**(AI: Check if an interaction mode - Detailed or Express - has been inherited from a previous guide, like the Vibe Tasking installation guide. Let's call this `[inherited_mode]` which could be "Detailed", "Express", or null.)**

**You (AI):** "(If `[inherited_mode]` is 'Detailed'): We were previously in Detailed Mode, so I'll continue to guide you step-by-step."
**You (AI):** "(If `[inherited_mode]` is 'Express'): We were previously in Express Mode, so I'll continue with a faster process and fewer questions, using sensible defaults where possible."
**You (AI):** "(If `[inherited_mode]` is null, meaning no mode was passed from a previous context): To help you create the `CONTEXT.md` file, I can operate in one of two modes:"
**You (AI):** "(If `[inherited_mode]` is null):

1.  **Detailed Mode:** I'll explain each step, what I'm doing, and why, and ask for your okay before taking actions like scanning files or writing the `CONTEXT.md` file. This is great if you're new or want to understand the process thoroughly.
2.  **Express Mode:** I'll use common defaults and my best judgment to create the `CONTEXT.md` file more quickly, only pausing if I absolutely need specific input from you (like a project name if I can't find one). I'll still inform you of the actions I'm taking."

**You (AI):** "(If `[inherited_mode]` is null): Which approach would you prefer for creating your `CONTEXT.md` file?"

_(If `[inherited_mode]` is null, use `ask_followup_question` to get user preference for the mode.)_

- Suggested options (if `[inherited_mode]` is null): "Detailed Mode: Guide me step-by-step.", "Express Mode: Faster creation with fewer questions."
- _(AI: If user selects Detailed Mode here, add: **You (AI):** "Okay, we'll proceed in Detailed Mode. **Just so you know, if you change your mind later and prefer a faster process, you can simply type 'Express Mode' at any time to switch!**")_

**(AI: Set the `[current_mode]` to `[inherited_mode]` if not null, otherwise set it to the user's selection. This `[current_mode]` will determine behavior in subsequent steps.)**

### Step 2: Propose Collaborative Discovery

1.  **Offer to Analyze Project Files:**

    - You: "To help create a useful `CONTEXT.md`, I can look at your project's file structure. This will help me suggest which documents are most important to include, like a main project README and the Vibe Tasking initialization guides."

2.  **Seek User Permission (Detailed Mode) or State Intent (Express Mode):**
    - **You (AI):** "(If `[current_mode]` is 'Detailed'): To best assist you, I can scan your project's top-level files and identify the Vibe Tasking submodule. This will help us identify key documents for your `CONTEXT.md`. May I proceed with listing the files in your project root and checking for common submodule paths? Here are some options:"
      - _(Use `ask_followup_question` if in Detailed Mode)_
      - Suggested options: "Yes, please proceed with scanning the project files.", "No, I'll tell you which files to include.", "Can you explain more about what you'll be looking for?"
    - **You (AI):** "(If `[current_mode]` is 'Express'): To best assist you (Express Mode), I will now scan your project's top-level files and identify the Vibe Tasking submodule. This will help us identify key documents for your `CONTEXT.md`."
    - _(AI: If in Detailed Mode and user selects "No, I'll tell you which files to include.", then skip Step 3 and proceed to Step 4, prompting the user for the main README path and Vibe Tasking submodule path directly.)_
    - _(AI: If in Detailed Mode and user selects "Can you explain more...", provide a brief explanation of looking for READMEs and the Vibe Tasking submodule path, then re-present the options.)_

### Step 3: Project Investigation (If Approved in Detailed Mode, or Proceeding in Express Mode)

1.  **Initial Project Files Reconnaissance:**

    - You: "Okay, I'll start by looking at the files in your project root to identify a main README file."
    - **Tool Usage & Awareness:**
      - Use [`list_files`](#) with `path: "."` and `recursive: false` to get a top-level view.
      - **Important Note on Tool Limitations:** Be aware that tools like `list_files` (and information from `environment_details`) often omit git submodules from listings of parent directories and may not recurse into them as expected. They also typically exclude files and directories specified in `.gitignore` (e.g., `node_modules`) and git-internal directories (e.g., `.git`). These omissions are by design to focus on primary project files but can affect reconnaissance.
    - You: "I've listed the top-level files. Next, I'll identify your main project README and then determine the Vibe Tasking submodule path."

2.  **Identify Potential Main README:**

    - From the file list, look for `README.md`, `README.txt`, `README`, `docs/README.md`, `docs/index.md`, or similar common overview files.
    - Note its existence and path.
    - Read the README to determine project details such as the project name.

3.  **Determine Vibe Tasking Submodule Path:**

    - **Attempt Self-Awareness & Validation:**

      - You: "First, I'll try to determine the Vibe Tasking submodule path based on how I'm currently running this guide."
      - _(AI: Attempt to extract `[self_aware_vt_path]` from the execution context of this guide. Immediately validate this path by checking for the existence of `[self_aware_vt_path]/ai-guides/core/ai-guides/ai-guides-discovering-guide.md`. If validation is successful, set `[confirmed_vt_path] = [self_aware_vt_path]` and skip to the AI comment at the end of this sub-step.)_

    - **Attempt `git status` (Inherited or New) & Validation (If Self-Awareness Failed or Was Invalid):**

      - _(AI: If `[confirmed_vt_path]` is not yet set):_
        - You: "(If `[current_mode]` is 'Detailed'): My initial attempt to locate the Vibe Tasking submodule using its own path was inconclusive."
        - _(AI: Check if `[git_status_submodule_paths]` (from a previous guide like INSTALL_VIBE_TASKING) is available. If so, try to identify the Vibe Tasking path from this list, let it be `[git_status_candidate_path]`. Validate `[git_status_candidate_path]` by checking for `.../ai-guides-discovering-guide.md`. If valid, set `[confirmed_vt_path] = [git_status_candidate_path]` and skip to the AI comment at the end of this sub-step.)_
        - _(AI: If `[confirmed_vt_path]` is still not set):_
          - **You (AI):** "(If `[current_mode]` is 'Detailed'): To find its registered path, may I run `git status`? This command lists project status including submodules."
            - _(Use `ask_followup_question` if in Detailed Mode. If permission denied, proceed to User Fallback / Placeholder below.)_
          - **You (AI):** "(If `[current_mode]` is 'Express'): I'll now run `git status` (Express Mode) to try and find the Vibe Tasking submodule's registered path."
          - _(AI: If proceeding, execute `git status`. Parse its output to find the Vibe Tasking submodule path. Let this be `[new_git_status_candidate_path]`. Validate `[new_git_status_candidate_path]` by checking for `.../ai-guides-discovering-guide.md`. If valid, set `[confirmed_vt_path] = [new_git_status_candidate_path]`.)_

    - **User Fallback / Placeholder (If All Automated Methods Failed or Were Invalid):**
      - _(AI: If `[confirmed_vt_path]` is still not set):_
        - **You (AI):** "(If `[current_mode]` is 'Detailed'): I'm having trouble automatically determining and validating the location of the Vibe Tasking submodule. Could you please tell me the path to the `vibe-tasking` directory from your project root (e.g., `vendor/vibe-tasking`, `libs/vibe-tasking`) so I can link its core guides?"
          - _(AI: If user provides path, set `[confirmed_vt_path]` to user's input. It's still a good idea to inform the user if a subsequent check for `.../ai-guides-discovering-guide.md` at this user-provided path fails, though you might proceed with the user's path for `CONTEXT.md` creation regardless, noting the potential issue.)_
        - **You (AI):** "(If `[current_mode]` is 'Express'): I couldn't automatically determine and validate the exact Vibe Tasking submodule path (Express Mode). I'll proceed with drafting `CONTEXT.md`, but the links to Vibe Tasking's internal guides might use a placeholder like `[PATH_TO_VIBE_TASKING_SUBMODULE_HERE]` which you may need to update later."
          - _(AI: Set `[confirmed_vt_path]` to a clear placeholder like `[UNKNOWN_VIBE_TASKING_PATH]`.)_

    _(AI: The `[confirmed_vt_path]` (which could be from self-awareness, git status, user input, or a placeholder) is now considered the `[path/to/vibe-tasking_submodule]` for subsequent steps.)_

4.  **Present Findings Concisely:**
    - You: "Okay, here's what I found that might be relevant for your `CONTEXT.md`:"
      - **You (AI):** "(If `[current_mode]` is 'Detailed'): A main project overview document at: `[path/to/README.md]` (If found, otherwise: 'I didn't immediately spot a main README. Is there a specific overview document you'd like me to reference?')"
      - **You (AI):** "(If `[current_mode]` is 'Express'): A main project overview document at: `[path/to/README.md]` (If found, otherwise: 'I didn't immediately spot a main README; I'll proceed without it for now in `CONTEXT.md` unless you specify one later.')"
      - "The Vibe Tasking submodule appears to be at: `[path/to/vibe-tasking_submodule]` (or 'The Vibe Tasking submodule path could not be automatically determined and will use a placeholder.')."
    - **You (AI):** "(If `[current_mode]` is 'Detailed'): Based on this, I can draft a `CONTEXT.md` that points to your project overview and the essential Vibe Tasking AI Guide discovery document. How does that sound?"
    - **You (AI):** "(If `[current_mode]` is 'Express'): Based on this (Express Mode), I will now draft a `CONTEXT.md` that points to your project overview (if found) and the essential Vibe Tasking AI Guide discovery document."

### Step 4: Draft and Write `CONTEXT.md`

1.  **Confirm Details with User (Detailed Mode Only):**

    - **(If `[current_mode]` is 'Detailed'):**
      - Ensure the user agrees with the identified README (or provides an alternative) and the Vibe Tasking submodule path. If these were not confirmed in Step 3 (e.g., user opted to provide them directly), ask now.
      - **You (AI):** "Before I draft the `CONTEXT.md`, could you confirm the main project README path is `[path/to/README.md]` and the Vibe Tasking submodule is at `[path/to/vibe-tasking_submodule]`? Also, what is your project's name?"

2.  **Locate and Use the Template:**

    - Mentally (or by internal reference) use the [`CONTEXT.template.md`](./CONTEXT.template.md) (located in the same directory as this guide).

3.  **Populate the Template:**

    - **Project Name:**
      - If `[current_mode]` is 'Detailed' and project name is unknown from README, ask the user.
      - If `[current_mode]` is 'Express' and project name is unknown, use a placeholder like "My Project" or the current directory name, and inform the user.
      - Replace `{{PROJECT_NAME}}` accordingly.
    - Set `{{PATH_TO_MAIN_README}}` (or equivalent) based on user confirmation (Detailed) or AI's findings/placeholders (Express).
    - Set `{{PATH_TO_VIBE_TASKING_SUBMODULE}}` and `{{VIBE_TASKING_SUBMODULE_DIR_NAME}}` based on findings/placeholders.
    - **Collaborative Ethos Note:**
      - **You (AI):** "(If `[current_mode]` is 'Detailed'): The template includes an optional 'Note on Our Collaborative Ethos'. This section emphasizes my role as a thinking partner. Here's the standard text: [Present text from template]. Would you like to include this standard note in your `CONTEXT.md`, or would you prefer to omit it for now?"
        - _(AI: Based on user's response, either keep or remove the ethos section from the template content.)_
      - **You (AI):** "(If `[current_mode]` is 'Express'): I've included the standard 'Note on Our Collaborative Ethos' in `CONTEXT.md` by default (Express Mode), as it emphasizes my role as a thinking partner. You can review or remove it later if you wish."
        - _(AI: In Express mode, include the ethos note uncommented by default.)_
    - Remove any other unused optional sections and all instructional comments from the template.

4.  **Write the File:**
    - Use [`write_to_file`](#) to create `CONTEXT.md` in the project root (`path: "CONTEXT.md"`).
    - **You (AI):** "(If `[current_mode]` is 'Detailed'): I've drafted the `CONTEXT.md` file and placed it in your project root. Here's the content:"
    - **You (AI):** "(If `[current_mode]` is 'Express'): I've created the `CONTEXT.md` file in your project root with the information gathered (Express Mode). Here's the content:"
    - Present the full content of the newly written `CONTEXT.md` for the user to see.

### Step 5: User Review and Iteration

1.  **Request Feedback (Detailed Mode) / Notify (Express Mode):**

    - **You (AI):** "(If `[current_mode]` is 'Detailed'): Please take a look at the `CONTEXT.md` content I provided. Does this accurately reflect the key starting documents for your project? Are there any other essential documents you think I should be aware of from the start?"
    - **You (AI):** "(If `[current_mode]` is 'Express'): I've created the `CONTEXT.md` (Express Mode) with the information gathered (or placeholders if some details were unavailable). Please review it when you can. If you need any changes or want to add more documents later, just let me know!"
      - _(AI: In Express Mode, if critical placeholders like `[UNKNOWN_VIBE_TASKING_PATH]` were used, add: "You'll particularly want to update the placeholder(s) for any missing information.")_

2.  **Make Adjustments (Primarily Detailed Mode):**
    - **(If `[current_mode]` is 'Detailed'):**
      - If the user suggests changes (e.g., adding another document, correcting a path), use [`apply_diff`](#) or [`write_to_file`](#) (for larger changes) to update `CONTEXT.md`.
      - Repeat the review process (showing the updated content and asking for feedback) until the user is satisfied.
    - **(If `[current_mode]` is 'Express' and user volunteers immediate changes):**
      - Accommodate reasonable immediate changes if the user offers them, but the primary goal was to create the initial file quickly.

### Step 6: Confirming Understanding of `CONTEXT.md` Usage

1.  **Ask About Usage Familiarity (Detailed Mode) / Offer Choices (Express Mode):**
    - **You (AI):** "(If `[current_mode]` is 'Detailed'): Now that we have the `CONTEXT.md` file, are you familiar with how you'll typically use it when starting a new chat session with an AI assistant like me?"
      - _(AI: If user is familiar, skip to Step 8. If unsure, proceed to Step 7.)_
    - **You (AI):** "(If `[current_mode]` is 'Express'): Now that `CONTEXT.md` is created (Express Mode), please let me know how you'd like to proceed. Here are the options:"
      - _(Use `ask_followup_question` if in Express Mode)_
      - Suggested options: "I know how to use CONTEXT.md.", "I'd like to practice using it."
      - _(AI: If user selects "I know how to use CONTEXT.md.", proceed to Step 8, Express Mode conclusion. If user selects "I'd like to practice using it.", proceed to Step 7.)_

### Step 7: Explaining and Practicing Usage (If User is Unsure or Opts to Practice)

1.  **Explain the `@` Convention:**

    - **You (AI):** "(If `[current_mode]` is 'Detailed' and user was unsure, OR if `[current_mode]` is 'Express' and user opted to practice): It's quite simple! When you start a new chat session, the most common way to provide this context is to type the literal string "`@CONTEXT.md`" as your very first message. The `@...` symbol usually opens an autocompleter which will find available files, featuring TAB-complete. This tells the chat interface to include the content of that file in your message to me. I'll then read it to get up to speed on your project."
    - You: "This ensures I have the necessary background before we dive into specific tasks."

2.  **Suggest a Practice Run:**

    - You: "Would you like to try it out now? To do this, please send a new, separate message in the chat that consists _only_ of the text `@"CONTEXT.md"` (without the surrounding quotes). I'll then check if I received its content in your next message to me."
    - _(AI: IMPORTANT - Do NOT use `ask_followup_question` here. The user needs to *type* `@"CONTEXT.md"` themselves as a new chat message to properly trigger the file attachment/linking behavior of the chat interface. Using a suggested reply would bypass this. End your turn and wait for the user's next chat message. You will verify their input in the subsequent turn as per Step 7.3.)_

3.  **Verify Practice Run:**
    - After the user sends their next message:
    - Check if the input you received includes markers indicating the `CONTEXT.md` file was embedded (e.g., the literal text `**CONTEXT.md**` or the actual file content if the interface expands it).
    - You: "Excellent! I see the `CONTEXT.md` content (or 'I see the reference to `CONTEXT.md`'). That's exactly how it works. I've now 'read' it for this session."
    - If it didn't work as expected: "Hmm, it seems the content wasn't included as expected. The exact way to include file content can sometimes vary slightly between AI assistant interfaces. Usually, typing `@` followed by the filename and selecting it from a suggestion list is the way. For now, just know that providing its content at the start of a session is the goal."
    - _(AI: After practice, proceed to Step 8.)_

### Step 8: Concluding the Authoring Process

1.  **Reconfirm User Readiness (Detailed Mode) / Conclude (Express Mode):**

    - **You (AI):** "(If `[current_mode]` is 'Detailed'): So, to recap, you now have a `CONTEXT.md` file in your project root. When you start new sessions with an AI assistant for this project, providing the content of this file first (often by typing `@"CONTEXT.md"`) will help the AI get oriented quickly. Do you feel ready to use this `CONTEXT.md` and the Vibe Tasking system?"
    - **You (AI):** "(If `[current_mode]` is 'Express' and user chose 'I know how to use CONTEXT.md.' or has just completed practice): Great! Your `CONTEXT.md` is set up (Express Mode), and you should be ready to use it effectively. This completes the `CONTEXT.md` authoring process."

2.  **Offer Next Steps (Optional):**
    - You: "Now that this is set up, we could move on to [suggest a common next step, e.g., 'creating your first story' or 'exploring other AI guides']."

## Information to Convey to the User (Key Elements & Best Practices)

Throughout the interactive process, subtly weave in these points about `CONTEXT.md` files:

- **Brevity is Key:** Emphasize that `CONTEXT.md` itself should be short; its main role is to point to a few _other_ comprehensive documents.
- **Accurate File Paths:** Stress the importance of correct relative paths from the project root.
- **Foundational Knowledge Only:** Guide the user to select documents that provide essential, high-level context, not highly specific or transient details.
- **Periodic Review:** Mention that as the project evolves, they should occasionally review and update their `CONTEXT.md`.

By following this interactive guide, you will empower users to create effective `CONTEXT.md` files and understand their vital role in the Vibe Tasking ecosystem, setting them up for successful collaboration.
