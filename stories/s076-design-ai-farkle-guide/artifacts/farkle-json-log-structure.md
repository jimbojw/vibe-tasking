## Line-Delimited JSON Game State Log Structure

Each line in the game log (`.jsonl` file) will be a self-contained JSON object representing a distinct game event or state change.

**Common Fields (present in most events):**

- `timestamp`: (String) ISO 8601 timestamp (e.g., `"2025-06-09T20:55:00Z"`).
- `event_type`: (String) The type of event (see specific event types below).
- `player_id`: (String, optional) Identifier for the player associated with the event (e.g., `"user"`, `"ai"`).
- `current_total_scores`: (Object, optional) Contains current total scores for all players (e.g., `{"user": 1200, "ai": 850}`).

**Specific Event Types and Their Fields:**

1.  **`game_start`**:

    - `event_type`: `"game_start"`
    - `target_score`: (Integer) The score needed to win (e.g., `10000`).
    - `players`: (Array of Strings) List of player IDs (e.g., `["user", "ai"]`).
    - `starting_player_id`: (String) The ID of the player who starts the game.
    - `initial_total_scores`: (Object) Scores at the beginning, typically all zero (e.g., `{"user": 0, "ai": 0}`).

2.  **`turn_start`**:

    - `event_type`: `"turn_start"`
    - `player_id`: (String) Player whose turn is starting.
    - `turn_number`: (Integer) The sequential number of the turn in the game.
    - `current_total_scores`: (Object) Scores before this turn begins.
    - `dice_available_count`: (Integer) Number of dice available at turn start (usually 6).

3.  **`dice_roll_attempt`**: (Logged when the AI is about to request/simulate a dice roll)

    - `event_type`: `"dice_roll_attempt"`
    - `player_id`: (String) Player attempting the roll.
    - `dice_to_roll_count`: (Integer) Number of dice being rolled.
    - `current_turn_score_accumulated`: (Integer) Score accumulated so far in _this specific turn_.

4.  **`dice_roll_result`**: (Logged after dice are rolled)

    - `event_type`: `"dice_roll_result"`
    - `player_id`: (String) Player who rolled.
    - `rolled_dice`: (Array of Integers) The faces of the dice that were rolled (e.g., `[1, 5, 5, 2, 4, 3]`).
    - `scorable_combinations_found`: (Array of Objects, optional) Details of scorable dice/combinations from this roll. Each object might contain:
      - `combo_name`: (String) e.g., `"triplet_5s"`, `"single_1"`.
      - `dice_values`: (Array of Integers) e.g., `[5,5,5]`.
      - `points`: (Integer) e.g., `500`.
    - `is_farkle_from_roll`: (Boolean) True if this specific roll resulted in no scorable dice.

5.  **`player_decision_prompt`**: (Logged when AI needs input from user, or AI logs its decision point)

    - `event_type`: `"player_decision_prompt"`
    - `player_id`: (String) Player who needs to make a decision.
    - `rolled_dice_context`: (Array of Integers) The dice roll leading to this decision.
    - `current_turn_score_accumulated`: (Integer) Score accumulated so far this turn.
    - `available_options`: (Array of Strings) e.g., `["hold_dice_and_roll_again", "bank_score"]`, or `["acknowledge_farkle"]`.

6.  **`player_holds_dice`**:

    - `event_type`: `"player_holds_dice"`
    - `player_id`: (String) Player making the decision.
    - `dice_selected_to_hold`: (Array of Integers) Dice chosen from the last roll.
    - `points_from_selected_dice`: (Integer) Points gained from these held dice.
    - `new_turn_score_accumulated`: (Integer) Updated score for the current turn.
    - `dice_remaining_to_roll_count`: (Integer) Number of dice left to roll.
    - `is_hot_dice_achieved`: (Boolean) True if all 6 dice scored and player can roll all 6 again.
    - `player_choice`: (String) e.g., `"roll_again"`, `"bank_after_hot_dice"`.

7.  **`player_banks_score`**:

    - `event_type`: `"player_banks_score"`
    - `player_id`: (String) Player banking the score.
    - `score_banked_this_turn`: (Integer) Amount of points added to total.
    - `previous_total_score`: (Integer) Player's total score before banking.
    - `new_total_score`: (Integer) Player's total score after banking.
    - `updated_total_scores`: (Object) All players' scores after this banking event.

8.  **`feature_freeze_event`**:

    - `event_type`: `"feature_freeze_event"`
    - `player_id`: (String) Player who experienced a Feature Freeze.
    - `rolled_dice_that_caused_freeze`: (Array of Integers) The dice roll that resulted in the Feature Freeze.
    - `turn_score_lost`: (Integer) The score accumulated in the current turn, which is now lost.

9.  **`turn_end`**:

    - `event_type`: `"turn_end"`
    - `player_id`: (String) Player whose turn ended.
    - `reason_for_turn_end`: (String) e.g., `"banked_score"`, `"feature_freeze"`.
    - `final_total_scores_after_turn`: (Object) Scores of all players at the end of this turn.

10. **`game_over`**:
    - `event_type`: `"game_over"`
    - `winner_id`: (String, nullable) ID of the winning player, or `null` if a draw (though Farkle usually has a winner).
    - `final_scores`: (Object) Final scores for all players (e.g., `{"user": 10500, "ai": 9850}`).
    - `reason_for_game_over`: (String) e.g., `"target_score_reached_and_final_turns_completed"`.

**Example Log Line (Dice Roll Result):**

```json
{
  "timestamp": "2025-06-09T21:00:05Z",
  "event_type": "dice_roll_result",
  "player_id": "user",
  "rolled_dice": [1, 5, 2, 2, 6, 3],
  "scorable_combinations_found": [
    { "combo_name": "single_1", "dice_values": [1], "points": 100 },
    { "combo_name": "single_5", "dice_values": [5], "points": 50 }
  ],
  "is_farkle_from_roll": false,
  "current_total_scores": { "user": 500, "ai": 300 }
}
```

**Further Examples:**

**1. Dice Roll Result (Later in a Turn):**
This example shows a `dice_roll_result` after a player has already held some dice and is rolling the remaining ones.
_Narrative Context:_ Assume the player ("user") on their turn initially rolled 6 dice. Let's say that first roll was `[1, 5, 2, 4, 6, 3]` (in "Sparkle" terms, this could be 💡, 🚀, 📘, ⏰, 🔮, 📌). From this initial roll, they held the `[1]` (a Spark 💡, 100 points) and the `[5]` (a Rocket 🚀, 50 points). These two dice, `[1, 5]`, are set aside. Their `current_turn_score_accumulated` is now 150 points. They chose to roll the remaining 4 dice. The `dice_roll_attempt` event (not shown here for this specific re-roll) would have indicated `dice_to_roll_count: 4` and `current_turn_score_accumulated: 150`. The example JSON below shows the result of these 4 dice being rolled.

```json
{
  "timestamp": "2025-06-09T21:02:15Z",
  "event_type": "dice_roll_result",
  "player_id": "user",
  "rolled_dice": [1, 3, 3, 6],
  "scorable_combinations_found": [
    { "combo_name": "single_1", "dice_values": [1], "points": 100 }
  ],
  "is_farkle_from_roll": false,
  "current_total_scores": { "user": 500, "ai": 300 }
}
```

_Interpretation:_ The user rolled their 4 remaining dice and got a 1 (worth 100 points). The other three dice ([3,3,6]) from this specific roll did not form any scorable combination on their own. The AI, following the game guide, would then prompt the user for their next decision (e.g., hold the new 1 and roll again, or bank the total turn score of 150 + 100 = 250).

**2. Feature Freeze Event:**
This example shows a `feature_freeze_event`.
_Narrative Context:_ Continuing from the previous example, the user held the new 1 (a Spark 💡, 100 points), bringing their current turn's accumulated score to 250 points. They chose to roll the remaining 3 dice. The `dice_roll_attempt` (not shown) would indicate `dice_to_roll_count: 3` and `current_turn_score_accumulated: 250`. The subsequent `dice_roll_result` (not shown here for brevity) for these 3 dice was, for example, `[2, 4, 6]` (e.g., 📘, ⏰, 🔮), which has no scorable dice, so `is_farkle_from_roll: true` in that `dice_roll_result` event. This triggers the `feature_freeze_event`.

```json
{
  "timestamp": "2025-06-09T21:03:00Z",
  "event_type": "feature_freeze_event",
  "player_id": "user",
  "rolled_dice_that_caused_freeze": [2, 4, 6],
  "turn_score_lost": 250,
  "current_total_scores": { "user": 500, "ai": 300 }
}
```

_Interpretation:_ The user's roll of `[2, 4, 6]` resulted in a Feature Freeze! 🥶 They lose the 250 points accumulated during this turn. Their total score remains unchanged from the start of the turn. The turn then ends.
