# CLI Random Number Generation Tool Testing Log

## `shuf` (Linux)

- **Date:** 2025-06-11
- **Source:** Based on documentation in `draft-cli-random-number-generation.md`. Direct testing not performed as current environment is macOS.
- **Syntax Verification (N dice, range 1-6):**
  - The syntax `shuf -i 1-6 -n X` (where X is the number of dice) is documented for generating X random numbers in the range 1-6.
  - Example for 6 dice: `shuf -i 1-6 -n 6`
  - Example for 3 dice: `shuf -i 1-6 -n 3`
- **Output Format Confirmation:**
  - The documented output format is one number per line.
- **Notes:**
  - `shuf` is part of GNU Coreutils, expected on most Linux systems.
  - Uses `-i` or `--input-range` for the range and `-n` or `--head-count` for the number of items.

## `jot` (macOS)

- **Date:** 2025-06-11
- **Source:** Tested on macOS. Confirmed against documentation in `draft-cli-random-number-generation.md`.
- **Syntax Verification (N dice, range 1-6):**
  - The syntax `jot -r X 1 6` (where X is the number of dice) is documented for generating X random numbers in the range 1-6.
  - Example for 6 dice: `jot -r 6 1 6`
  - Example for 1 die: `jot -r 1 1 6`
- **Output Format Confirmation:**
  - Confirmed: Output is one number per line.
  - Example output for `jot -r 6 1 6`:
    ```
    1
    4
    6
    2
    5
    3
    ```
- **Notes:**
  - `jot` is a standard utility on macOS.
  - The `-r` flag signifies random generation. The arguments are count, lower bound, and upper bound.

## `bash $RANDOM` (Universal \*nix)

- **Date:** 2025-06-11
- **Source:** Tested on macOS (zsh, compatible with bash). Confirmed against documentation in `draft-cli-random-number-generation.md`.
- **Syntax Verification (N dice, range 1-6):**
  - The syntax `for i in {1..X}; do echo $((RANDOM % 6 + 1)); done` (where X is the number of dice) is confirmed for generating X random numbers in the range 1-6.
  - Example for 6 dice: `for i in {1..6}; do echo $((RANDOM % 6 + 1)); done`
  - Example for variable number of dice (e.g., 4): `num_dice=4; for ((i=0; i&lt;$num_dice; i++)); do echo $((RANDOM % 6 + 1)); done`
- **Output Format Confirmation:**
  - Confirmed: Output is one number per line.
  - Example output for `for i in {1..6}; do echo $((RANDOM % 6 + 1)); done`:
    ```
    6
    2
    5
    3
    2
    3
    ```
- **Notes:**
  - `$RANDOM` returns a pseudo-random integer between 0 and 32767.
  - The modulo operator (`%`) is used to scale the number to the desired range (1-6).
  - This method has a negligible, but technically present, modulo bias. Generally acceptable for non-cryptographic purposes.
  - Portable across Linux and macOS environments with bash-compatible shells.

## `/dev/urandom` pipeline (Advanced Universal \*nix)

- **Date:** 2025-06-11
- **Source:** Tested on macOS. Confirmed against documentation in `draft-cli-random-number-generation.md`.
- **Syntax Verification (N dice, range 1-6):**
  - Single string output: `xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c X`
  - Output each number on a new line: `xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c X | grep -o .`
  - Example for 6 dice (new lines): `xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c 6 | grep -o .`
- **Output Format Confirmation (for new-line separated version):**
  - Confirmed: Output is one number per line.
  - Example output for `xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c 6 | grep -o .`:
    ```
    2
    3
    5
    3
    5
    3
    ```
- **Notes:**
  - This method uses `xxd` to get a hex dump of random bytes from `/dev/urandom`.
  - `sed` filters out any characters not in the range 1-6.
  - `head -c X` takes the first X characters (dice rolls).
  - `grep -o .` (optional) formats the output to one character (digit) per line.
  - Considered a statistically pure, bias-free method due to oversampling and filtering.
  - Robust and suitable for ensuring fairness.

## Generic Range Test (e.g., 1-25, single number)

- **Date:** 2025-06-11
- **Objective:** Test if the vetted tools can generate a single random number within a generic range (e.g., 1-25).

### `shuf` (Linux - based on documentation)

- **Syntax:** `shuf -i MIN-MAX -n 1`
- **Example (1-25):** `shuf -i 1-25 -n 1`
- **Expected Output:** A single number between 1 and 25.
- **Notes:** Appears suitable.

### `jot` (macOS - tested)

- **Syntax:** `jot -r 1 MIN MAX`
- **Example (1-25):** `jot -r 1 1 25`
- **Test Command:** `jot -r 1 1 25`
- **Actual Output:** `10` (example)
- **Notes:** Successfully generated a single number in the specified range.

### `bash $RANDOM` (Universal \*nix - tested)

- **Syntax:** `echo $((RANDOM % MAX_VAL + MIN_VAL))` (Note: for range MIN to MAX, use `MAX_VAL = MAX - MIN + 1`, then add `MIN_VAL -1` if `MIN_VAL` is not 1. Simpler: `echo $((RANDOM % (MAX - MIN + 1) + MIN))` )
- **Example (1-25):** `echo $((RANDOM % 25 + 1))`
- **Test Command:** `echo $((RANDOM % 25 + 1))`
- **Actual Output:** `4` (example)
- **Notes:** Successfully generated a single number in the specified range. Formula for range `MIN` to `MAX` is `$((RANDOM % (MAX - MIN + 1) + MIN))`.

### `/dev/urandom` pipeline (Advanced Universal \*nix)

- **Notes:** While the existing pipeline is excellent for sequences of single digits (e.g., 1-6 for dice), adapting it to reliably and simply generate a single number within a generic multi-digit range (e.g., 1-25) using `sed` for filtering is complex. Other methods (`jot`, `$RANDOM`, `shuf`) are more straightforward for this specific use case. The strength of this pipeline is in generating bias-free sequences of characters/digits from a defined set.
