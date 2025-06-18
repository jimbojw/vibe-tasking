---
id: "vibe-tasking-installing-guide"
title: "Guide: AI-Assisted Installation of Vibe Tasking (Git Submodule)"
usage: "Use this guide for AI-assisted installation of Vibe Tasking as a Git submodule. The AI will interactively guide the user, explain steps, seek consent, detect existing host project submodule conventions, and adapt the installation process accordingly."
tags: "installation;git;submodule;ai-assistant;setup;context-aware;interactive;user-coaching"
---

# Guide: AI-Assisted Installation of Vibe Tasking (Git Submodule)

**(Primary Audience: AI Assistant (to reliably and interactively install Vibe Tasking as a Git submodule, guiding the user through each step, explaining concepts, and adapting to the host project's conventions).)**

## Introduction for the AI Assistant

This guide is special. Your role is not just to execute commands, but to be a **collaborative partner and coach** for the user, especially if they are new to Git, submodules, or AI-assisted development tasks.

**Your Core Mandate:**

- **Explain Everything:** Clearly explain what you are about to do and why, before you do it.
- **Seek Explicit Consent:** Obtain user permission before running any commands or making changes. Use `ask_followup_question` or similar tools/phrasing to make this easy for the user.
- **Educate Gently:** Briefly explain technical terms (like Git, submodule, `git status`) as they arise. Assume the user may not be familiar with them.
- **Be Patient and Reassuring:** Let the user know they can ask questions at any point.
- **Adapt:** Be prepared to adapt based on user input and environment checks.

The goal is to successfully install Vibe Tasking _and_ ensure the user feels comfortable and informed throughout the process.

---

**(Instructions for the AI Assistant executing this guide begin here. Address the user directly as "you" meaning the human user you are interacting with.)**

## Phase 0: Setting the Stage – Let's Get Started!

**You (AI):** "Hello! It looks like you want to install Vibe Tasking into your current project. I can help with that! We'll do this by adding Vibe Tasking as a 'Git submodule', which is a way to include one Git project inside another."

**You (AI):** "The process will involve a few steps:

1.  **Check Prerequisites:** First, we'll do a quick check to make sure your project is set up for this (e.g., it's a Git project and the `git` command is available).
2.  **Get Repository URL:** Then, I'll ask you for the web address (URL) of the Vibe Tasking project.
3.  **Find Installation Path:** Next, we'll figure out the best place to put the Vibe Tasking files within your project.
4.  **Install Vibe Tasking:** Finally, I'll run the commands to install it."

**You (AI):** "At each step, I'll explain what I'm going to do and ask for your okay before proceeding. This is the 'Detailed Mode'."

**You (AI):** "Alternatively, if you're comfortable with common defaults and prefer a faster process, you can choose 'Express Mode'. In Express Mode, I'll:

- Assume consent for standard operational checks (like `git status`).
- Use default paths (e.g., `vendor/vibe-tasking`) if no other conventions are found in your project.
- Only pause to ask for essential information (like the Vibe Tasking repository URL) or if an unexpected issue or ambiguity arises that requires your input.
  I will still inform you of the actions I'm taking."

**You (AI):** "Which approach would you prefer for this installation?"

_(Use `ask_followup_question` to get user preference for the mode.)_

- Suggested options: "Detailed Mode: Guide me step-by-step.", "Express Mode: Faster installation with fewer questions.", "Can you briefly list the defaults first?"

## Phase 1: Checking Your Project's Setup

**You (AI):** "(If user selected Detailed Mode): Okay, we'll proceed in Detailed Mode. **Just so you know, if you change your mind later and prefer a faster process, you can simply type 'Express Mode' at any time to switch!**"
**You (AI):** "Great! Now, let's check your project's setup."

**You (AI):** "(If in Detailed Mode): First, I need to run a quick command, `git status`, to check a few things:

1.  That I (your AI assistant) can successfully execute commands in your terminal.
2.  That I can receive and understand the output from those commands.
3.  That the `git` command-line tool (which we need for this installation) is available on your system.
4.  And that your current project directory is indeed a Git repository.
    I will attempt to read its output directly.
    May I run the command `git status` to perform this check?"

_(Use `ask_followup_question` for permission if in Detailed Mode.)_

- Suggested options for Detailed Mode: "Yes, go ahead.", "What does `git status` do?", "No, not right now."

_(If in Detailed Mode and permission denied, explain that this check is important and ask if they have concerns. If they remain unwilling, explain you cannot proceed without this verification and STOP.)_

**You (AI):** "(If in Express Mode): I will now run `git status` to check your project's setup (availability of `git`, if this is a Git repository, and that I can execute commands and see output)."

**(Regardless of mode, proceed to execute and analyze):**

1.  **Execute Command:** Run `git status`.
2.  **Analyze Direct Output:**

    - Attempt to interpret the direct output from the `git status` command.
    - **If direct output is successfully read and understood:**
      - If the output indicates "not a git repository" (or similar error):
        **You (AI):** "It looks like the current project folder isn't a Git repository. Vibe Tasking needs to be installed into an existing Git project. You'll need to initialize this project as a Git repository first (e.g., by running `git init`). Would you like me to explain what that means or how to do it?"
        **(STOP, offer guidance if requested but do not proceed with Vibe Tasking install.)**
      - If the output indicates `git: command not found` (or similar):
        **You (AI):** "It seems the `git` command isn't available on your system. `git` is essential for this installation. Please make sure it's installed and accessible in your system's PATH. You can usually find instructions by searching for 'install git' for your operating system."
        **(STOP)**
      - If the output shows a valid `git status` (e.g., "On branch main", "nothing to commit", etc.):
        **You (AI):** "Excellent! The `git status` command worked, and I could read its output. This tells me your project is a Git repository and `git` is available. I've also analyzed this output to identify the paths of any existing Git submodules, which will help us in the next steps. We're good to go to Phase 2!"
        _(AI: Internally parse `git status` output and store a list of detected submodule paths as `[git_status_submodule_paths]`. If none, the list is empty. Proceed to Phase 2)_
      - **Else (if output is present but unclear, or indicates an unexpected Git state that isn't a clear error but isn't a clean status either):**
        **You (AI):** "I received some output from `git status`, but it's a bit unclear: `[Show a snippet of the unclear output if possible, or describe it]`. To be sure, I'd like to try saving the output to a temporary file. Is that okay?"
        _(Proceed to "Attempt Temporary File Method" below if user agrees)_
    - **If direct output is NOT successfully read/understood (e.g., you received no output, garbled text, an error from your `execute_command` tool about output capture, or a message like "command ran successfully, but couldn't capture output"):**
      **You (AI):** "Hmm, I tried running `git status` but I couldn't seem to get its output clearly. This can sometimes happen."
      _(Proceed to "Attempt Temporary File Method" below)_

3.  **Attempt Temporary File Method (Fallback):**
    **You (AI):** "(If in Detailed Mode): I'll try a different approach to check the `git status` (Detailed Mode): I'll save its output to a temporary file called `install_vt_git_check.tmp` in your project's main folder and then read that file. I'll delete it right after. May I try that?"

    _(Use `ask_followup_question` for permission to use temp file method if in Detailed Mode.)_

    - Suggested options for Detailed Mode: "Yes, try the temporary file.", "Why is the direct output not working?", "No, let's stop for now."

    _(If in Detailed Mode and permission for temp file method denied: **You (AI):** "Okay, without being able to reliably check the `git status`, I can't proceed with the installation. Please let me know if you'd like to try again or explore other options." **(STOP)**)_

    **You (AI):** "(If in Express Mode): I'll now try a different approach to check the `git status` (Express Mode): I'll save its output to a temporary file called `install_vt_git_check.tmp` in your project's main folder, read it, and then delete it."

    **(Regardless of mode, if Detailed Mode permission was granted or if in Express Mode, proceed):**

    1.  **Execute Command with Redirection:** Run `git status > ./install_vt_git_check.tmp 2>&1`.
    2.  **Attempt to Read Output File:** Try to read `./install_vt_git_check.tmp`.
    3.  **Analyze Temporary File Outcome:**
        - **If `./install_vt_git_check.tmp` cannot be read or is empty:**
          **You (AI):** "Unfortunately, even when trying to save the `git status` output to a temporary file, I couldn't access it. This might indicate a more persistent issue with running commands or reading files in this environment."
          **You (AI):** "Please see the 'Handling Command Output Issues' section in this guide for troubleshooting. For now, I'll have to stop here."
          **(STOP)**
        - **If `./install_vt_git_check.tmp` is read successfully:**
          - Examine the content:
            - If "not a git repository" (or similar): (Handle as above, then delete temp file)
              **You (AI):** "The output in the temporary file confirms this project isn't a Git repository. Vibe Tasking needs an existing Git project. You'll need to initialize it first (e.g., `git init`)."
              _(Execute `rm ./install_vt_git_check.tmp`)_
              **(STOP)**
            - If `git: command not found` (or similar): (Handle as above, then delete temp file)
              **You (AI):** "The output in the temporary file confirms `git` command isn't available. Please ensure `git` is installed."
              _(Execute `rm ./install_vt_git_check.tmp`)_
              **(STOP)**
            - If valid `git status` output:
              **You (AI):** "Great! Using the temporary file, I was able to confirm your `git status`. Your project is a Git repository, and `git` is available. I've also analyzed the output from the file to identify the paths of any existing Git submodules. We can proceed!"
              **You (AI):** "I'll now delete the temporary file `install_vt_git_check.tmp`."
              _(Execute `rm ./install_vt_git_check.tmp`)_
              _(AI: Internally parse `git status` output from the temp file and store a list of detected submodule paths as `[git_status_submodule_paths]`. If none, the list is empty. Proceed to Phase 2)_
            - **Else (output is still unclear even from file):**
              **You (AI):** "Even from the temporary file, the `git status` output is unclear: `[Show snippet or describe]`. I'm not sure how to proceed safely. It might be best to resolve this Git status issue manually before we continue."
              _(Execute `rm ./install_vt_git_check.tmp`)_
              **(STOP)**

## Phase 2: Getting/Confirming the Vibe Tasking Repository URL

**You (AI):** "(Attempt to extract URL from initial prompt. Let's call this `[EXTRACTED_URL_FROM_PROMPT]` if found, otherwise it's null/empty)."

**You (AI):** "(If `[EXTRACTED_URL_FROM_PROMPT]` was found): The initial instructions I received appear to include a Git repository URL for Vibe Tasking: `[EXTRACTED_URL_FROM_PROMPT]`."
**You (AI):** "(If `[EXTRACTED_URL_FROM_PROMPT]` was found AND in Detailed Mode): To ensure we're on the same page (Detailed Mode), is this the correct Git repository URL for the Vibe Tasking project you want to install?"

_(Use `ask_followup_question` for confirmation if `[EXTRACTED_URL_FROM_PROMPT]` was found AND in Detailed Mode.)_

- Suggested options for Detailed Mode (if URL found): "Yes, `[EXTRACTED_URL_FROM_PROMPT]` is correct.", "No, that's not the one, let me provide a different URL."

**You (AI):** "(If `[EXTRACTED_URL_FROM_PROMPT]` was found AND in Express Mode): I will proceed using this URL (Express Mode): `[EXTRACTED_URL_FROM_PROMPT]`."

**You (AI):** "(If `[EXTRACTED_URL_FROM_PROMPT]` was NOT found OR (if in Detailed Mode AND user said 'No' to the extracted one)): Could you please provide the Git repository URL for Vibe Tasking? This could be an HTTPS URL like `https://github.com/some-organization/vibe-tasking.git`, an SSH URL like `git@gitserver.com:path/repo.git`, or another scheme like `sso://internal-git/project/vibe-tasking`."

_(If user needs to provide it, wait for user input. Store the URL as `[USER_PROVIDED_URL]`.)_

**You (AI):** "(If user provided a URL now, i.e., `[USER_PROVIDED_URL]` is set): Thanks! I have the URL as: `[USER_PROVIDED_URL]`. Is that correct?"

_(Use `ask_followup_question` for confirmation if the user just provided it.)_

- Suggested options (if user provided URL): "Yes, that's the correct URL.", "No, let me correct it."

_(Logic: The AI should now have a `[FINAL_URL]`._

- _If `[EXTRACTED_URL_FROM_PROMPT]` was found and confirmed (Detailed) or accepted (Express), it's the `[FINAL_URL]`._
- _If `[EXTRACTED_URL_FROM_PROMPT]` was not found, or was rejected in Detailed mode, then the confirmed `[USER_PROVIDED_URL]` becomes the `[FINAL_URL]`._
  _This `[FINAL_URL]` will be used in Phase 5.)_

## Phase 3: Finding the Best Spot – Submodule Configuration

**You (AI):** "Now, let's figure out the best place to put the Vibe Tasking files. I'll use the submodule path information I gathered from the `git status` command in Phase 1."

**(AI: Recall the `[git_status_submodule_paths]` list from Phase 1. This list contains paths like 'libs/modA', 'vendor/modB', etc., or is empty.)**

1.  **If `[git_status_submodule_paths]` is NOT empty:**
    **You (AI):** "The `git status` output from earlier showed existing submodules in your project at paths like: `[display a few example paths from the list, e.g., '[git_status_submodule_paths[0]]', '[git_status_submodule_paths[1]]' or a summary if many]`. I'll analyze these to see if there's a common parent directory we can use."
    _(AI: Analyze `[git_status_submodule_paths]` to infer a common base directory. Let this be `[inferred_base_directory]` if found, otherwise null.)_

    - **If a clear `[inferred_base_directory]` is found (e.g., `vendor/`):**
      **You (AI):** "(If in Detailed Mode): Based on your existing submodules, it looks like they are often placed in a `[inferred_base_directory]/` folder. Would you like to install Vibe Tasking there too, for example, as `[inferred_base_directory]/vibe-tasking`?"
      **You (AI):** "(If in Express Mode): I see your existing submodules often use the `[inferred_base_directory]/` parent folder. I'll follow this convention and plan to install Vibe Tasking at `[inferred_base_directory]/vibe-tasking`. (Set `[chosen_parent_directory]` = `[inferred_base_directory]` and will proceed with this path)."
      _(If in Detailed Mode, wait for user input/confirmation. Goal: `[chosen_parent_directory]`.)_
    - **If no clear `[inferred_base_directory]` is found:**
      **You (AI):** "(If in Detailed Mode): I see existing submodules, but they are in different locations (e.g., `[list a few diverse paths from [git_status_submodule_paths]]`), so there isn't one single common parent directory. Could you tell me which parent folder you'd prefer for Vibe Tasking (e.g., `vendor/`, `external/`)? It will be placed in a subfolder named `vibe-tasking` inside the parent you choose."
      **You (AI):** "(If in Express Mode): Your existing submodules are in varied locations (e.g., `[list a few diverse paths]`). Since there's no single clear convention, I'll use the recommended default parent folder `vendor/`, making the path `vendor/vibe-tasking`. (Set `[chosen_parent_directory]` = `vendor` and will proceed with this path)."
      _(If in Detailed Mode, wait for user input/confirmation. Goal: `[chosen_parent_directory]`.)_

2.  **If `[git_status_submodule_paths]` IS empty:**
    **You (AI):** "The `git status` output from Phase 1 didn't show any existing Git submodules in your project. So, it looks like Vibe Tasking will be the first one!"
    **You (AI):** "(If in Detailed Mode): Where would you like to create the main folder for Vibe Tasking? The recommended and most common choice, which aligns with our documentation examples, is `vendor/`. This would mean Vibe Tasking will be installed in `vendor/vibe-tasking`. If you have a strong preference for a different parent folder (e.g., `libs/` or `external/`), please specify it. Otherwise, shall we proceed with `vendor/` as the parent directory?"
    **You (AI):** "(If in Express Mode): Since this will be the first Git submodule, I'll use the recommended default parent folder `vendor/`, making the path `vendor/vibe-tasking`. (Set `[chosen_parent_directory]` = `vendor` and will proceed with this path)."
    _(If in Detailed Mode, wait for user input. Goal: `[chosen_parent_directory]`.)_

## Phase 4: Confirming the Installation Path

_(Assume `[chosen_parent_directory]` was determined in Phase 3.)_
**You (AI):** "Alright, based on our discussion (or the defaults in Express Mode), the Vibe Tasking submodule will be installed at `[chosen_parent_directory]/vibe-tasking`. For example, if `[chosen_parent_directory]` is `vendor`, the path will be `vendor/vibe-tasking`."
**You (AI):** "(If in Detailed Mode): To be absolutely sure before we proceed with the installation commands (Detailed Mode): Is `[chosen_parent_directory]/vibe-tasking` the correct final path?"

_(Use `ask_followup_question` for final confirmation if in Detailed Mode.)_

- Suggested options (for Detailed Mode): "Yes, that path is correct.", "No, I need to change the parent directory."
  _(If "No" in Detailed Mode, loop back to the relevant part of Phase 3.)_
  **You (AI):** "(If in Express Mode): I will proceed with installing Vibe Tasking at `[chosen_parent_directory]/vibe-tasking` (Express Mode)."

## Phase 5: Installing Vibe Tasking!

**You (AI):** "Perfect! We have the URL and the installation path. I'm now ready to run the commands to add Vibe Tasking as a submodule."

**You (AI):** "(If in Detailed Mode): The first command is:
`git submodule add [URL_FROM_PHASE_2] [PATH_FROM_PHASE_4]`
This command tells Git to add the Vibe Tasking project (from the URL) as a submodule at the path we just confirmed. It will create the necessary directory and download the Vibe Tasking files.
May I run this command?"

_(Use `ask_followup_question` for permission if in Detailed Mode.)_

- Suggested options for Detailed Mode: "Yes, run the `git submodule add` command.", "Hold on, I have a question."

**You (AI):** "(If in Express Mode): I will now run the first command to add the submodule: `git submodule add [URL_FROM_PHASE_2] [PATH_FROM_PHASE_4]`."

**(Regardless of mode, if Detailed Mode permission was granted or if in Express Mode, proceed):**

1.  Execute `git submodule add [URL_FROM_PHASE_2] [PATH_FROM_PHASE_4]`.
    **You (AI):** "Okay, I've run the `git submodule add` command."

**You (AI):** "(If in Detailed Mode): The second command is:
`git submodule update --init --recursive`
This command makes sure the submodule is properly initialized and all its files are downloaded, especially if Vibe Tasking itself uses further submodules (which it might in the future).
May I run this command?"

_(Use `ask_followup_question` for permission if in Detailed Mode.)_

- Suggested options for Detailed Mode: "Yes, run the `git submodule update` command.", "What does `--init --recursive` mean?"

**You (AI):** "(If in Express Mode): I will now run the second command to ensure the submodule is fully initialized: `git submodule update --init --recursive`."

**(Regardless of mode, if Detailed Mode permission was granted or if in Express Mode, proceed):**

1.  Execute `git submodule update --init --recursive`.
    **You (AI):** "Okay, I've run the `git submodule update` command."

## Phase 6: All Done! Confirmation and Next Steps

**You (AI):** "Great news! I've executed both commands. Vibe Tasking should now be installed as a submodule in your project at `[PATH_FROM_PHASE_4]`."

**You (AI):** "When you add a submodule, a few things change in your main project:

1.  The Vibe Tasking files are now in the `[PATH_FROM_PHASE_4]` directory.
2.  A `.gitmodules` file was created or updated in your project's main folder. This file tells Git about your submodules.
3.  Git has noted the Vibe Tasking submodule as part of your project.
    These changes now need to be saved (committed) to your project's Git history."

**You (AI):** "So, the next important step for you is to commit these changes in your main project. You can typically do this with `git add .` followed by `git commit -m 'Added Vibe Tasking submodule'`."
**You (AI):** "Do you have any questions about this, or about Vibe Tasking now that it's installed?"

**You (AI):** "To help collaborators who clone your project, it's important they know how to initialize the Vibe Tasking submodule. The necessary commands are `git submodule init` and `git submodule update --recursive`."

**(AI: Check if `README.md` exists in the project root.)**

**You (AI):** "(If `README.md` exists and in Detailed Mode): I see you have a `README.md` file. Would you like me to try and add these submodule initialization instructions to it? I'll show you the proposed changes before applying them."
**You (AI):** "(If `README.md` exists and in Express Mode): I see you have a `README.md` file. I will now attempt to add the submodule initialization instructions to it. I'll aim for a relevant section like 'Installation' or 'Getting Started', or create a new 'Project Setup' section if needed."

**(AI: If user agrees in Detailed Mode, or if in Express Mode and `README.md` exists):**

1. Read `README.md`.
2. Formulate the instructions to add the submodule init and update commands. This may require creating a new section, or adding steps to an existing environment setup list. You'll have to be sensitive to the `README.md`'s formatting and blend in.
3. (Detailed Mode): Propose the change (e.g., using `apply_diff` with a clear SEARCH block or `insert_content` at a specific line/section). Ask for confirmation.
4. (Express Mode): Attempt to intelligently find a relevant section (e.g., "Installation", "Setup", "Getting Started") to append or prepend these instructions. If no obvious section, append to the end or create a new "Project Setup" or "Submodules" section. Use `insert_content` or `apply_diff`.
5. (After applying in either mode if successful): "I've added the submodule instructions to `README.md`." or "I've updated `README.md` with the submodule instructions at/near [describe location]."
6. (If AI cannot confidently modify `README.md` or user declines in Detailed Mode): Fall back to the general advice below.

**You (AI):** "(If `README.md` does not exist, or if AI couldn't modify it, or user declined in Detailed Mode): It's a good idea to add instructions for `git submodule init` and `git submodule update --recursive` to your project's main `README.md` or a contributor's guide (if you create one) so your collaborators know how to set up the project correctly."
**You (AI):** "Now that Vibe Tasking is installed, the very next step to make it usable is to create a `CONTEXT.md` file in the root of this project. This file is crucial as it tells me (and any AI assistant) what essential documents to read to understand your project. Without it, I won't know where to start!"
**You (AI):** "There's a specific guide within Vibe Tasking itself that details how I can help you create this `CONTEXT.md` file interactively. It's located at `[PATH_FROM_PHASE_4]/ai-guides/core/context/context-documents-authoring-guide.md`."
**You (AI):** "(If in Detailed Mode): Would you like me to read that guide now (it's at `[PATH_FROM_PHASE_4]/ai-guides/core/context/context-documents-authoring-guide.md`) and then help you create your project's `CONTEXT.md` file (Detailed Mode)?"

_(If in Detailed Mode, use `ask_followup_question` for permission.)_

- Suggested options (for Detailed Mode): "Yes, please help me create CONTEXT.md.", "What exactly is CONTEXT.md again?", "No, I'll do it later."\_
  _(If in Detailed Mode, offer to answer questions. The installation is complete from the AI's active involvement at this point if the user declines further help with CONTEXT.md.)_

**You (AI):** "(If in Express Mode): I recommend we create this `CONTEXT.md` file now, as it's crucial for our future interactions. I will proceed by reading the guide located at `[PATH_FROM_PHASE_4]/ai-guides/core/context/context-documents-authoring-guide.md` and then helping you create the `CONTEXT.md` file (Express Mode)."
_(In Express Mode, the AI will then move to assist with CONTEXT.md creation. The installation part of this guide is complete.)_

## Troubleshooting

- **Handling Command Output Issues (Especially during Phase 1 `git status` check):**

  - In Phase 1, I first attempt to read the output of `git status` directly. If that fails (e.g., I report no output, garbled output, or an error from my command execution tool), I will then suggest using a temporary file (`install_vt_git_check.tmp`) to capture the output.
  - **If Issues Persist Even with the Temporary File Method:**
    - If I still cannot read `install_vt_git_check.tmp` or it's empty after I've run the command to redirect output to it (e.g., `git status > ./install_vt_git_check.tmp 2>&1`):
      1.  **Did the command run?** I might ask you if you saw the command execute in your terminal. Sometimes I get confirmation before the command finishes writing its output.
      2.  **Can you see the file?** I might ask you to check if `install_vt_git_check.tmp` was created and what's inside it. You might need to open it in your editor.
      3.  **Permissions/Path:** If there are problems, we might need to check if I have permission to write files here, or if we're in the correct folder.
      4.  **Alternative Temp Location:** If writing to the main project folder is an issue, I might ask you to suggest another temporary spot for these output files (e.g., a `tmp/` directory you create). I would then adjust commands like `git status > [user_suggested_path]/install_vt_git_check.tmp 2>&1`.
  - **General Command Output Problems:** This strategy (try direct, then fallback to temp file) can be applied to other commands in this guide if output issues arise.
  - **Persistent Problems:** If reliable command output capture remains a problem even with these steps, it points to a more fundamental limitation of the AI assistant's environment for this kind of task. I will have to stop, as Vibe Tasking heavily relies on an AI's ability to execute commands and access their results.

- **"What is Git / Submodules?"**

  - **You (AI):** "Git is a version control system – it's like a 'save' button for your whole project that remembers all the changes you make over time. A 'submodule' is a way to include one Git project inside another Git project, keeping them separate but connected."
  - **You (AI):** "When we add Vibe Tasking as a submodule, Git creates or updates a special file in your main project called `.gitmodules`. This file keeps track of your submodules. It's important that you **commit this `.gitmodules` file** to your project's Git history, along with the record of the submodule itself. This ensures that when others clone your project, or when you clone it elsewhere, Git knows to also fetch Vibe Tasking."
  - **You (AI):** "Phase 6 of this guide will remind you about committing these changes. For a deeper understanding of how you, the user, manage Git changes (like staging, committing, and pushing) when working with AI assistants and Vibe Tasking, you can later refer to the article `docs/articles/implementing-vibe-tasking-stories.md`, particularly its section on 'Managing Change: Your Role in Version Control'. For now, just know that committing the `.gitmodules` file is a key step after the installation. If you'd like a more detailed explanation of Git or submodules now, just ask!"

- **Incorrect URL:** If `git submodule add` fails, I'll ask you to double-check the Vibe Tasking repository URL.
- **Permissions:** Ensure you (the user) have write permissions in your project directory and network access to the Git repository.
- **Path Conflicts:** If the chosen installation path already exists and isn't an empty folder, `git submodule add` might fail. We'll need to clarify this if it happens.
