**Note: This document, detailing Unicode pip dice display, is superseded by the emoji dice definitions in [`artifacts/sparkle-game-rules.md`](./sparkle-game-rules.md:0) for the "Sparkle" themed version of the game.**

---

## Using Unicode Dice Characters for Game State Display

To provide a user-friendly and visually clear representation of the game, Unicode dice characters will be used. The selected standard for displaying held and remaining/rolled dice utilizes H1 Markdown headings with inline code blocks, and link styling for held dice to enhance visibility.

**Standard Unicode Dice Characters:**

- Die Face 1: `⚀` (U+2680)
- Die Face 2: `⚁` (U+2681)
- Die Face 3: `⚂` (U+2682)
- Die Face 4: `⚃` (U+2683)
- Die Face 5: `⚄` (U+2684)
- Die Face 6: `⚅` (U+2685)

**Standard Display Format for Held and Rolled/Remaining Dice:**

The game state, particularly the distinction between dice held for scoring and dice remaining to be rolled (or just rolled), will be presented using a two-line H1 format:

**Line 1: Held Dice (Styled as a Link)**

```markdown
# [`[ HELD_DICE_UNICODE ]`](./)
```

_Example: Held ⚄ ⚄ ⚄ ⚀_

```markdown
# [`[ ⚄ ⚄ ⚄ ⚀ ]`](./)
```

**Line 2: Rolled/Remaining Dice (Prefixed with an Arrow)**

```markdown
# `➢ ROLLED_OR_REMAINING_DICE_UNICODE`
```

_Example: Remaining ⚁ ⚂ to be rolled_

```markdown
# `➢ ⚁ ⚂`
```

_Example: Just rolled ⚀ ⚃ ⚅ (if it's an initial roll display before selection)_

```markdown
# `➢ ⚀ ⚃ ⚅`
```

This format aims to use the H1 for large, legible dice pips and the link styling (often a different color and/or underline) on the first line to visually distinguish the "held" dice. The second line clearly indicates the dice that were just rolled or are available for the next roll.

**Outline for Displaying Game State Elements (Revised):**

1.  **Displaying an Initial Dice Roll:**

    - When dice are first rolled in a turn, before any are selected, they can be displayed on the second line of the standard format, perhaps with a contextual label if needed, or simply as the "current roll."
    - **Example:** A roll of `[1, 5, 5, 2, 4, 3]` might initially be shown as:
      _(Contextual text from AI: "Your roll is:")_
      ```markdown
      # `➢ ⚀ ⚄ ⚄ ⚁ ⚃ ⚂`
      ```

2.  **Indicating Held Dice and Showing Remaining Dice:**

    - Once the player selects dice to hold, the display will update to the full two-line format.
    - **Example:** If the player holds `1, 5, 5` (⚀ ⚄ ⚄) from the roll above, and `2, 4, 3` (⚁ ⚃ ⚂) remain:

      ```markdown
      # [`[ ⚀ ⚄ ⚄ ]`](./)

      # `➢ ⚁ ⚃ ⚂`
      ```

      _(Contextual text from AI: "You held [dice] (XXX points). Remaining dice to roll:")_

3.  **Hot Dice:**

    - If "Hot Dice" are achieved (all six dice scored), the display for remaining dice would show all six dice again.
      _(Contextual text from AI: "Hot Dice! You scored with all dice. You can roll all 6 again.")_

      ```markdown
      # [`[ ALL_SIX_SCORED_DICE ]`](./)

      # `➢ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅`
      ```

4.  **Contextual Game Information:**
    - The dice display should always be presented alongside other critical game state information, such as:
      - Whose turn it is (e.g., "User's Turn" or "AI's Turn").
      - The score accumulated _within the current turn_ before banking.
      - The total banked scores for all players.

**Conceptual Example of AI Output During a User's Turn (Revised):**

```
--- User's Turn ---
Current Turn Score: 0
Your Total Score: 1200 | AI's Total Score: 850

Rolling 6 dice...
Result: [1, 5, 2, 4, 5, 3]

(AI presents the roll)
# `➢ ⚀ ⚄ ⚁ ⚃ ⚄ ⚂`

Available scoring dice from this roll:
- ⚀ (100 pts)
- ⚄ (50 pts)
- ⚄ (50 pts)
(AI would list valid combinations if applicable)

What dice would you like to hold? (e.g., "hold 1 5 5", "hold 1", "hold 5s")
You can also choose to 'bank' if you have a valid score, or declare 'farkle' if no score.
```

If the user chooses to hold `1, 5, 5` (⚀ ⚄ ⚄), accumulating 200 points for the turn:

```
--- User's Turn ---
Current Turn Score: 200
Your Total Score: 1200 | AI's Total Score: 850

(AI presents held and remaining dice)
# [`[ ⚀ ⚄ ⚄ ]`](./)
# `➢ ⚁ ⚃ ⚂`

You held ⚀ ⚄ ⚄ for 200 points. 3 dice remaining.
What next?
1. Roll again (3 dice)
2. Bank 200 points
```

This revised method aims to provide maximum legibility and a clear distinction between held and active dice using standard Markdown features. The AI Guide will instruct the AI assistant on how to format these displays.
