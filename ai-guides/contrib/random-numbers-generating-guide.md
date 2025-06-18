---
id: "random-numbers-generating-guide"
title: "Guide: Generating Random Numbers via CLI"
usage: "Use this guide to select and execute appropriate command-line interface (CLI) tools for generating random numbers, ensuring verifiability and avoiding AI 'making up' numbers. Covers methods for Linux, macOS, and universal *nix systems."
tags: "random-numbers;cli;rng;prng;shuf;jot;bash-random;dev-urandom;dice-roll;generation;contrib-guide"
---

# Guide: Generating Random Numbers via CLI

**(Primary Audience: AI Assistant (to select and use reliable CLI tools for random number generation).)**

## Introduction

This guide details reliable command-line interface (CLI) methods for generating random numbers. When a user requests random numbers (e.g., for simulating dice rolls, picking random items), you **MUST** use the programmatic methods described here instead of "making up" numbers. This ensures transparency, verifiability, and often better statistical properties for the generated randomness.

The methods below cover common tools available on Linux, macOS, Windows (via PowerShell), and other \*nix-like systems.

## Why Use Programmatic/CLI Methods for Randomness?

AI language models are designed to generate plausible text, not to be true random number generators. When asked for a random number, an AI might:

- Produce numbers that appear random but are influenced by patterns in its training data.
- Exhibit biases or poor distribution if attempting to simulate randomness internally.
- Provide numbers that are not verifiable or reproducible in a controlled manner.

By using established CLI tools, we leverage system-level random number generators or well-vetted algorithms, providing a more trustworthy source of randomness.

## CLI Methods for Random Number Generation

### 1. `shuf` (Linux)

- **Target OS/Environment:** Linux (standard part of GNU Coreutils).
- **Description:** `shuf` can generate random permutations or select random lines/numbers from a range.
- **Command Syntax:**
  - **Generate X numbers in range MIN-MAX:** `shuf -i MIN-MAX -n X`
  - **Example (3 dice rolls, range 1-6):**
    ```bash
    shuf -i 1-6 -n 3
    ```
  - **Example (1 number, range 1-25):**
    ```bash
    shuf -i 1-25 -n 1
    ```
- **Explanation:**
  - `-i MIN-MAX` or `--input-range=MIN-MAX`: Specifies the inclusive integer range.
  - `-n X` or `--head-count=X`: Specifies the number of random items to select.
- **Expected Output Format:** One number per line.
- **Pros:** Direct, designed for this purpose, good randomness.
- **Cons:** Primarily Linux-specific (GNU Coreutils).
- **Notes:** Recommended method for Linux if available.

### 2. `jot` (macOS)

- **Target OS/Environment:** macOS (standard utility).
- **Description:** `jot` is a versatile utility for printing sequential or random data.
- **Command Syntax:**
  - **Generate X random numbers in range MIN-MAX:** `jot -r X MIN MAX`
  - **Example (3 dice rolls, range 1-6):**
    ```bash
    jot -r 3 1 6
    ```
  - **Example (1 number, range 1-25):**
    ```bash
    jot -r 1 1 25
    ```
- **Explanation:**
  - `-r`: Produces random numbers.
  - `X`: The count of numbers to generate.
  - `MIN`: The lower bound of the inclusive range.
  - `MAX`: The upper bound of the inclusive range.
- **Expected Output Format:** One number per line.
- **Pros:** Simple, idiomatic for macOS.
- **Cons:** macOS-specific.
- **Notes:** Recommended method for macOS.

### 3. `bash $RANDOM` (Universal for \*nix-like Shells)

- **Target OS/Environment:** Any system with `bash` or a compatible shell (Linux, macOS, etc.).
- **Description:** Leverages the shell's built-in `$RANDOM` variable.
- **Command Syntax:**
  - **Generate X numbers in range MIN-MAX (loop):**
    ```bash
    for i in $(seq 1 X); do echo $((RANDOM % (MAX - MIN + 1) + MIN)); done
    ```
  - **Example (3 dice rolls, range 1-6):**
    ```bash
    for i in $(seq 1 3); do echo $((RANDOM % 6 + 1)); done
    ```
  - **Example (1 number, range 1-25):**
    ```bash
    echo $((RANDOM % 25 + 1))
    ```
- **Explanation:**
  - `$RANDOM`: A shell variable that returns a pseudo-random integer between 0 and 32767.
  - `% (MAX - MIN + 1)`: Modulo operation to scale the number to the size of the desired range.
  - `+ MIN`: Adds the minimum value to shift the range to MIN-MAX.
- **Expected Output Format:** One number per line (when used in a loop with `echo`).
- **Pros:** Highly portable, no external commands needed if `bash` is present.
- **Cons:**
  - `$RANDOM` has a slight modulo bias when the size of the range (MAX - MIN + 1) does not evenly divide 32768. This bias is usually negligible for non-cryptographic uses like games.
- **Notes:** A good general-purpose option for \*nix-like shells if `shuf` or `jot` are unavailable. Not applicable to native Windows PowerShell.

### 4. `/dev/urandom` Pipeline (Advanced Universal for \*nix-like Systems)

- **Target OS/Environment:** Any \*nix system with `/dev/urandom`, `xxd`, `sed`, `head`, and `grep`.
- **Description:** A robust method using the system's cryptographically secure pseudo-random number generator (`/dev/urandom`) and filtering to achieve bias-free results for specific character sets (like single digits 1-6).
- **Command Syntax (for single digits, e.g., dice rolls 1-6):**
  - **Generate X digits, each on a new line:**
    ```bash
    xxd -p -l 256 /dev/urandom | sed 's/[^MIN-MAX_DIGITS]//g' | head -c X | grep -o .
    ```
    (Replace `MIN-MAX_DIGITS` with the actual digits, e.g., `1-6` for dice)
  - **Example (3 dice rolls, range 1-6, new lines):**
    ```bash
    xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c 3 | grep -o .
    ```
  - **Example (3 dice rolls, range 1-6, single string):**
    ```bash
    xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c 3
    ```
- **Explanation:**
  - `xxd -p -l 256 /dev/urandom`: Reads 256 bytes from `/dev/urandom` and outputs them as a continuous plain hex dump.
  - `sed 's/[^1-6]//g'`: Filters the hex stream, keeping only characters '1' through '6'.
  - `head -c X`: Takes the first X characters from the filtered stream.
  - `grep -o .` (optional): Prints each character on a new line.
- **Expected Output Format:** Single string of digits, or one digit per line if `grep -o .` is used.
- **Pros:** Statistically pure, bias-free for the filtered character set. Excellent for ensuring fairness.
- **Cons:**
  - More complex command pipeline.
  - Primarily suited for generating sequences of single digits from a specific set (e.g., 1-6). Adapting it for generic numeric ranges (e.g., 1-25) is significantly more complex than other methods and not recommended for that specific use case.
- **Notes:** Best for scenarios requiring high-quality, bias-free sequences of specific digits on \*nix-like systems. Not applicable to native Windows PowerShell.

### 5. `Get-Random` (Windows PowerShell)

- **Target OS/Environment:** Windows (with PowerShell).
- **Description:** `Get-Random` is the standard cmdlet in PowerShell for generating random numbers or selecting random items from a collection.
- **Command Syntax:**
  - **Generate X numbers in range MIN-MAX (upper bound is exclusive for integers):** `Get-Random -Minimum MIN -Maximum (MAX + 1) -Count X`
  - **Example (3 dice rolls, range 1-6):**
    ```powershell
    Get-Random -Minimum 1 -Maximum 7 -Count 3
    ```
  - **Example (1 number, range 1-25):**
    ```powershell
    Get-Random -Minimum 1 -Maximum 26
    ```
- **Explanation:**
  - `-Minimum MIN`: Specifies the inclusive lower bound.
  - `-Maximum (MAX + 1)`: Specifies the exclusive upper bound. So, for an inclusive range up to `MAX`, use `MAX + 1`.
  - `-Count X`: Specifies how many numbers to generate. If omitted, one number is generated.
- **Expected Output Format:** Numbers, typically one per line if multiple are generated by `-Count`.
- **Pros:** Standard, idiomatic for PowerShell. Good randomness.
- **Cons:** Windows/PowerShell specific. Note the exclusive upper bound for integer ranges.
- **Notes:** Recommended method for Windows PowerShell environments. Untested in this guide's creation.

## Choosing the Right Method

When tasked with generating random numbers:

1.  **Identify OS (if possible):**
    - If **Linux** and `shuf` is available, it's often the best choice.
    - If **macOS** and `jot` is available, it's often the best choice.
    - If **Windows (PowerShell)**, `Get-Random` is the standard choice.
2.  **Consider Portability:**
    - If a script for \*nix-like systems is needed and OS-specific tools (`shuf`, `jot`) are uncertain, `bash $RANDOM` is a good default, accepting its minor modulo bias.
    - The `/dev/urandom` pipeline is also for \*nix-like systems; it's more complex and best for sequences of specific digits where bias is a major concern.
3.  **Nature of Randomness Required:**
    - For simple dice rolls in a game: `shuf` (Linux), `jot` (macOS), `Get-Random` (Windows PowerShell), or `bash $RANDOM` (\*nix-like shells) are usually sufficient.
    - For tasks needing provably fair sequences of specific digits (e.g., 1-6) on \*nix-like systems: The `/dev/urandom` pipeline is superior.
4.  **Specific Range/Count:**
    - All listed methods can be adapted for different counts (`X`).
    - For a single number in a generic range (e.g., 1-25): `shuf -i 1-25 -n 1` (Linux), `jot -r 1 1 25` (macOS), `Get-Random -Minimum 1 -Maximum 26` (Windows PowerShell), or `echo $((RANDOM % 25 + 1))` (*nix-like shells) are straightforward. The `/dev/urandom` pipeline is overly complex for this specific sub-task on *nix systems.

**Always inform the user which method you are using and why, if relevant.**

## Summary of Methods

- **`shuf`**
  - **Best For:** Linux
  - **Example (3 dice, 1-6):** `shuf -i 1-6 -n 3`
  - **Notes:** Straightforward, recommended for Linux.
- **`jot`**
  - **Best For:** macOS
  - **Example (3 dice, 1-6):** `jot -r 3 1 6`
  - **Notes:** Idiomatic, simplest for macOS.
- **`bash $RANDOM`**
  - **Best For:** Universal for \*nix-like Shells
  - **Example (3 dice, 1-6):** `for i in $(seq 1 3); do echo $((RANDOM % 6 + 1)); done`
  - **Notes:** Highly portable. Negligible modulo bias.
- **`/dev/urandom` filter**
  - **Best For:** Advanced Universal for \*nix-like Systems
  - **Example (3 dice, 1-6, new lines):** `xxd -p -l 256 /dev/urandom | sed 's/[^1-6]//g' | head -c 3 | grep -o .`
  - **Notes:** Bias-free for specific digit sets. Best for fairness-critical digit sequences.
- **`Get-Random` (PowerShell)**
  - **Best For:** Windows
  - **Example (3 dice, 1-6):** `Get-Random -Minimum 1 -Maximum 7 -Count 3`
  - **Notes:** Standard for PowerShell. Upper bound is exclusive. Untested.

By following this guide, you can provide users with reliable and verifiable random numbers sourced from appropriate CLI tools.
