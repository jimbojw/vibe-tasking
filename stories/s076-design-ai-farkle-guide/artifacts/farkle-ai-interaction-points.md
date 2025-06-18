**Note: This document is superseded by [`artifacts/sparkle-ai-interaction-points.md`](./sparkle-ai-interaction-points.md:0) which details the AI interaction flow for the "Sparkle" themed version of the game.**

---

## AI Interaction Points

This document outlines key points of interaction for an AI assistant when participating in or facilitating a game of Farkle.

- **Game State Tracking:** A line-delimited JSON log will be essential for maintaining a persistent and auditable record of the game's progress. The AI will be responsible for appending new events to this log.
- **Dice Rolling:** The AI needs a reliable mechanism to obtain Pseudo-Random Number Generator (PRNG) based dice rolls. It should not "invent" or "choose" dice values. This will likely involve executing a shell command that calls a simple script or one-liner.
- **User Choices:** The AI will use its `ask_followup_question` tool (or equivalent) to learn the human user's decisions during their turn. This includes:
  - Which dice to set aside for scoring after a roll.
  - Whether to roll again with remaining dice or bank the current turn's score.
- **AI Choices:** The AI will need its own decision-making logic for its turns. This includes:
  - Evaluating its roll for scoring combinations.
  - Deciding which dice to hold.
  - Deciding whether to roll again or bank its score, based on risk/reward assessment (which could be simple or complex).
- **Display:** The AI will be responsible for presenting the game state clearly to the user. This includes:
  - Displaying current dice rolls using Unicode dice characters.
  - Showing which dice are held.
  - Indicating current turn scores and total banked scores for all players.
