# Sparkle: AI Interaction Points

This document outlines the key interaction points and communication flow for an AI assistant facilitating a game of "Sparkle" with a user. The game rules, dice faces (emojis), and scoring are defined in `sparkle-game-rules.md`. The AI should leverage the `ask_followup_question` tool for managing user choices effectively.

## Core Principles:

1.  **Clarity:** Always clearly present the game state to the user before asking for a decision.
2.  **Guidance:** Briefly explain options or consequences where helpful (e.g., "Banking now will add X to your total score.").
3.  **Theme Consistency:** Use "Sparkle" terminology and emojis throughout the interaction.
4.  **PRNG for Rolls:** AI MUST obtain dice rolls by consulting the [`ai-guides/contrib/random-numbers-generating-guide.md`](../../../../ai-guides/contrib/random-numbers-generating-guide.md). It does not "choose" dice outcomes.
5.  **JSON Logging:** All significant game events are logged to a line-delimited JSON file as per `farkle-json-log-structure.md`.

## Interaction Flow:

### 1. Game Start

- AI confirms game start, target score, and who is starting (user or AI).
- Logs `game_start` event.

### 2. Turn Start

- AI announces whose turn it is.
- AI states the player's current total score and that they have 6 dice.
- Logs `turn_start` event.

### 3. Dice Rolling (User or AI)

- **Action:** Player (user or AI) decides to roll.
- AI logs `dice_roll_attempt` (including dice_to_roll_count, current_turn_score_accumulated).
- AI obtains dice roll results (e.g., 6 dice: 💡, 📘, ✅, ⏰, 🚀, 🔮) using the PRNG guide.
- AI logs `dice_roll_result` (including rolled_dice, scorable_combinations_found, is_farkle_from_roll).
- **AI Presents Roll & Scores:**
  - Displays the rolled dice using Sparkle emojis.
  - Lists scorable dice/combinations and their point values from that specific roll.
  - States the current accumulated score for the turn _if these scorable dice were selected_.

### 4. Handling a "Feature Freeze!" (No Scoring Dice on a Roll)

- **AI Announces:** "Oh no, that's a Feature Freeze! 🥶 Your current turn's points are lost." (Or similar thematic phrase).
- AI states that the turn score is lost and the turn ends.
- Logs `feature_freeze_event` (details to be updated in JSON log structure doc).
- Logs `turn_end`.
- Proceeds to next player's turn.

### 5. Player Decision: Holding Dice (User's Turn)

- **Context:** AI has presented a roll with scorable dice.
- **AI Preamble (Example):**
  "You rolled: 💡 💡 🚀 📘 ✅ 🔮
  Scorable from this roll:
  - Two Sparks (💡💡) = 200 points
  - One Rocket (🚀) = 50 points
    Your current turn score is 0. If you hold 💡💡 and 🚀, your turn score will be 250."
- **AI uses `ask_followup_question`:**
  - `<question>`: "Which scorable dice would you like to hold? (Or bank current turn score if applicable)"
  - `<suggest>` options:
    - Valid combinations of scorable dice (e.g., "Hold 💡💡 (200 pts)", "Hold 🚀 (50 pts)", "Hold 💡💡 and 🚀 (250 pts)").
    - If `current_turn_score_accumulated` > 0 from previous holds in this turn: "Bank [current_turn_score_accumulated] points".
    - If no valid dice selected by user from suggestions: (AI may need to re-prompt or clarify rules if user tries an invalid hold).
- **User Selects Dice to Hold:**
  - AI confirms the held dice and the points added to the turn score.
  - AI states how many dice are remaining.
  - Logs `player_holds_dice` event.

### 6. Player Decision: Roll Again or Bank Score (User's Turn)

- **Context:** User has successfully held dice.
- **AI Preamble (Example):**
  "You held 💡💡 and 🚀. Your turn score is now 250. You have 3 dice remaining."
- **AI uses `ask_followup_question`:**
  - `<question>`: "What would you like to do next?"
  - `<suggest>` options:
    - "Roll remaining 3 dice"
    - "Bank 250 points"
- **If User Chooses to Roll Again:**
  - Return to Step 3 (Dice Rolling).
- **If User Chooses to Bank Score:**
  - AI confirms score banked.
  - AI updates and states the player's new total score.
  - Logs `player_banks_score` event.
  - Logs `turn_end` event.
  - Proceeds to next player's turn.

### 7. Handling "Hot Dice"

- **Context:** All dice rolled by a player contribute to their score in a single roll sequence (either the initial 6 dice, or subsequent rolls if all remaining dice scored).
- **AI Announces:** "Hot Dice! 🔥 You scored with all your dice! You get to roll all 6 dice again to continue your turn. Your current turn score of [X points] is safe for now."
- The `player_holds_dice` event should have `is_hot_dice_achieved: true`.
- Player _must_ roll all 6 dice again. Proceed to Step 3 (Dice Rolling) with 6 dice.

### 8. AI's Turn

- The AI follows the same general flow (Roll -> Evaluate -> Hold/Bank).
- The `sparkle-playing-guide.md` will define the AI's decision-making logic (e.g., risk assessment for re-rolling vs. banking).
- AI should announce its actions and reasoning concisely:
  - "AI rolls: 🚀 🚀 🚀 💡 📘 ✅"
  - "AI scores Three Rockets (🚀🚀🚀) for 500 points and one Spark (💡) for 100 points. Turn score: 600."
  - "AI will hold 🚀🚀🚀 and 💡, and roll the remaining 2 dice."
  - (or) "AI will bank 600 points."
- All AI actions (rolls, holds, banks, farkles) are logged just like user actions.

### 9. Game End

- **Context:** A player reaches the target score (e.g., 10,000 points) and all other players have had one final turn.
- AI announces the winner and final scores.
- Logs `game_over` event.

This flow provides a structured way for the AI to manage the game, present choices clearly, and keep the user informed, leveraging `ask_followup_question` for interactive decision-making.
