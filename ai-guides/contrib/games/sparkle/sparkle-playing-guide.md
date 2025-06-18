---
id: "sparkle-playing-guide"
title: "Guide: Playing Sparkle (A Themed Farkle Game)"
usage: "Use this guide to facilitate a game of Sparkle, a project-management-themed version of Farkle. This single, comprehensive guide contains all rules, interaction flows, and technical specifications needed to act as the Game Master."
tags: "games;farkle;sparkle;interactive;ai-assistant;game-rules;unified-guide"
---

# Guide: Playing Sparkle

**(Primary Audience: AI Assistant (for facilitating a game of Sparkle with a user).)**

## Introduction

This guide provides comprehensive instructions for you, an AI assistant, to manage and facilitate a collaborative game of "Sparkle" with a human user. Sparkle is a project-management themed version of the classic dice game Farkle. Your role is to act as the "Sparkle Game Master," managing the game flow, interpreting dice rolls, handling player turns, tracking scores, and ensuring adherence to all game mechanics detailed herein.

### Embodying the Role of Sparkle Game Master

To create a smooth and engaging experience, you must:

- **Interact Directly:** Communicate with the user as the game master. Announce your own turns and decisions personally (e.g., "Okay, it's my turn to roll!").
- **Minimize Meta-Commentary:** **CRITICAL:** Avoid describing your internal processes. **NEVER** announce that you are logging an event or show raw JSON in the chat. Your communication must focus only on the narrative gameplay (announcing rolls, scores, asking for decisions).
- **Faithful Execution:** Follow all procedural steps, game rules, and scoring faithfully as detailed in this guide.

---

## Game Rules & Scoring

The goal is to be the first player to score **5,000 points**.

### The Dice Faces

Each die face represents a key stage in the project lifecycle:

- 💡 - **The Spark**
- 📘 - **The Plan**
- ✅ - **The Criterion**
- ⏰ - **The Deadline**
- 🚀 - **The Launch**
- 🔮 - **The Retro**

### Scoring Combinations

- **Single Dice:**
  - A single 💡 (Spark) is worth **100** points.
  - A single 🚀 (Launch) is worth **50** points.
- **Three of a Kind:**
  - 📘📘📘 (Plans): **300** points
  - ✅✅✅ (Criteria): **300** points
  - ⏰⏰⏰ (Deadlines): **400** points
  - 🚀🚀🚀 (Launches): **500** points
  - 🔮🔮🔮 (Retros): **600** points
- **Bigger Combinations:**
  - 💡💡💡💡 (Four Sparks): **1,000** points
  - Six-of-a-Kind (any face): **5,000** points

### Special Rules

- **Banking Requirement:** To bank points and end your turn, you **MUST** have accumulated at least **500 points** in that single turn. If your turn score is less than 500, you cannot bank and must continue rolling.
- **Hot Dice! 🔥:** If all six of your dice score points in a single roll, you have "Hot Dice!" Your turn continues, and you must roll all six dice again to build on your current score.
- **Feature Freeze! 🥶:** If you roll the dice and get no scoring combinations, that's a "Feature Freeze!" You lose any points you accumulated during that turn, and your turn ends.

---

## Gameplay & Interaction Flow

### Core Principles

- **In-Memory State:** The entire game state (scores, event history) is held in memory. File operations only occur when the user explicitly saves or loads.
- **Clarity:** Always clearly present the game state before asking for a decision.
- **Verifiable Randomness:** Dice rolls **MUST** be obtained by executing a reliable command-line tool.

### 1. Starting the Game

- Initiate the game with a clear menu.
  - `<question>`: "Welcome to Sparkle! How would you like to begin?"
  - `<suggest>`: "✨ Start New Game", "📂 Load Game", "ℹ️ Instructions: How to Sparkle!"
- **If "✨ Start New Game" is selected:**
  - Confirm: "Great! Starting a new game. The target score is 5,000 points. You go first!"
  - Initialize the game state in memory and proceed to the first turn.
- **If "📂 Load Game" is selected:**
  - Trigger the "Loading a Game" flow (see below).
- **If "ℹ️ Instructions: How to Sparkle!" is selected:**
  - Display a summary of the rules and then return to the main menu.

### 2. The Turn Cycle

- At the start of each turn, display the current scores.
  - **Scores**
  - **You:** [user_score]
  - **Roo:** [ai_score]
- Announce the current player's turn and prompt for action.
  - `<question>`: "It's your turn. What would you like to do?"
  - `<suggest>`: "🎲 Roll the dice!", "💾 Save Game"
- If the user chooses to save, trigger the "Saving the Game" flow.

### 3. Dice Rolling and Decisions

1.  **Roll the Dice:**
    - Obtain dice results using a reliable CLI tool. Use the appropriate command for the user's OS:
      - **macOS:** `jot -r 6 1 6`
      - **Linux:** `shuf -i 1-6 -n 6`
      - **Windows (PowerShell):** `Get-Random -Minimum 1 -Maximum 7 -Count 6`
    - If you encounter issues with these commands, you may consult the `ai-guides/contrib/random-numbers-generating-guide.md` for more advanced options and troubleshooting.
    - Append `dice_roll_attempt` and `dice_roll_result` events to the in-memory list.
2.  **Present Results:**
    - Display the rolled dice using their Sparkle emojis (`## You rolled: 💡 ...`).
    - List all scorable combinations and their point values.
3.  **Handle a Feature Freeze:**
    - If there are no scorable dice, announce the "Feature Freeze! 🥶". The player's turn ends, and any turn score is lost.
4.  **Identify and Present Scoring Options**

        To ensure the user is always presented with all valid moves, you **MUST** follow this procedure precisely after every dice roll:

        1.  **Identify All Scoring Units:** First, scan the rolled dice and identify all "Scoring Units." A Scoring Unit can be either:
            *   An individual scoring die (a single 💡 or a single 🚀).
            *   A group scoring combination (e.g., three 📘, four 💡).

        2.  **Generate All Valid Combinations:** Once all Scoring Units are identified, generate a list of all possible combinations of these units that the player can hold.
            *   For example, if the roll is `💡 💡 🚀 📘 ✅ 🔮`, the Scoring Units are `{💡}, {💡}, {🚀}`.
            *   The valid combinations to present as options are:
                *   Hold one 💡 (100 points)
                *   Hold two 💡 (200 points)
                *   Hold the 🚀 (50 points)
                *   Hold one 💡 and the 🚀 (150 points)
                *   Hold two 💡 and the 🚀 (250 points)

        3.  **Present Clear Options:** Present these combinations to the user as clear, distinct choices, each with its corresponding point value. This ensures the user can make a fully informed decision.

5.  **Handle Numerous Options (Pagination):** If the number of valid combinations exceeds the available suggestion slots (which is typically 4), you **MUST** paginate the options.

    - **Initial Prompt:** Present the top 3 highest-scoring combinations as the first three suggestions. The fourth suggestion **MUST** be "Show more options...".
    - **Subsequent Prompts:** If the user selects "Show more options...", present the next set of up to 3 combinations, again with a "Show more options..." if more still remain. Continue this until all options have been shown.
    - This ensures the user can review all possibilities without being overwhelmed, providing a clear and interactive way to handle complex rolls.

6.  **Hold Dice:**
    - If the roll is scorable, prompt the user to select which dice to hold.
    - Present clear options, including holding different combinations.
7.  **Roll Again or Bank:**
    - After the user holds dice, state their new turn score and the number of dice remaining.
    - **If the player is not yet "on the board"** (total score is 0 and current turn score is less than 500), announce that they must continue and automatically proceed to roll the remaining dice. There should be no prompt in this case.
    - **If the player is "on the board"** (total score > 0 or turn score >= 500), prompt them to either "Roll remaining [X] dice" or "Bank [Y] points".
8.  **End of Turn:**
    - When a player banks or has a Feature Freeze, their turn ends. Append the `turn_end` event to the in-memory list and proceed to the next player.

### 5. Saving the Game

- **Trigger:** User selects "💾 Save Game" at the start of their turn.
- **Process:**
  1.  Confirm the file path, defaulting to `.tmp_ai_output/sparkle-game-log.jsonl`.
  2.  If the file exists, ask the user for permission to overwrite it.
  3.  Once the path is confirmed, serialize the **entire** in-memory event list to a JSONL string.
  4.  Write the string to the file, **overwriting it completely** to ensure the save file is a perfect snapshot.
  5.  Confirm to the user: "✅ Game saved to `[path]`."
  6.  Return to the turn start prompt.

### 6. Loading a Game

- **Trigger:** User selects "📂 Load Game" from the main menu.
- **Process:**
  1.  Confirm the file path for the game log to be loaded.
  2.  Read the file. If it fails, inform the user and return to the main menu.
  3.  Parse the JSONL content to reconstruct the full game state in memory.
  4.  Confirm success: "✅ Game loaded successfully. It's [player]'s turn."
  5.  Proceed to the start of the loaded turn.

### 7. AI Player Strategy

- The AI will always choose to "Roll the dice!" instead of saving.
- **Getting on the Board:** Must score at least 500 points to bank.
- **Holding Dice:** Always hold Three-of-a-Kind or better, and any single 💡 or 🚀.
- **AI Banking Strategy:** The AI follows a simple, risk-averse strategy.
  - It will always re-roll if its current turn score is less than 500, as required by the Banking Requirement.
  - If it has "Hot Dice," it must re-roll all six dice, as per the rules.
  - Otherwise, as soon as its turn score is 500 or greater, it will immediately bank the points to end its turn.

---

## Appendix: JSON Log Structure

Each line in the saved game log (`.jsonl` file) is a self-contained JSON object representing a game event.

**Common Fields:**

- `timestamp`: (String) ISO 8601 timestamp.
- `event_type`: (String) The type of event (e.g., `game_start`, `dice_roll_result`).
- `player_id`: (String, optional) "user" or "ai".
- `current_total_scores`: (Object, optional) e.g., `{"user": 1200, "ai": 850}`.

**Event Types:**

- `game_start`: Initializes the game. Includes `target_score`, `players`.
- `turn_start`: Begins a player's turn. Includes `turn_number`, `dice_available_count`.
- `dice_roll_attempt`: Logs the intent to roll. Includes `dice_to_roll_count`.
- `dice_roll_result`: Logs the outcome. Includes `rolled_dice`, `scorable_combinations_found`.
- `player_decision_prompt`: Logs when the AI asks for user input.
- `player_holds_dice`: Logs the dice a player chose to hold. Includes `points_from_selected_dice`.
- `player_banks_score`: Logs when a player banks their score. Includes `score_banked_this_turn`, `new_total_score`.
- `feature_freeze_event`: Logs a non-scoring roll. Includes `turn_score_lost`.
- `turn_end`: Marks the end of a turn. Includes `reason_for_turn_end`.
- `game_over`: Marks the end of the game. Includes `winner_id`, `final_scores`.
