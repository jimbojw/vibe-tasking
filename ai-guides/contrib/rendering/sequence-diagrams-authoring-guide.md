---
id: "sequence-diagrams-authoring-guide"
title: "Guide: Effective ASCII-Art Sequence Diagrams"
usage: "Use this guide for principles and best practices when creating clear, consistent, and maintainable ASCII-art sequence diagrams, particularly for version-control friendliness and Markdown integration."
tags: "ascii-art;diagrams;sequence-diagrams;documentation;style-guide;uml"
---

# Guide: Effective ASCII-Art Sequence Diagrams

**(Primary Audience: AI Assistant (for creating clear, consistent, and maintainable ASCII-art sequence diagrams). Project Contributors may also find this guide useful for understanding these standards.)**

## Introduction

This guide provides principles and best practices for creating effective ASCII-art sequence diagrams within this project. Sequence diagrams are a type of interaction diagram that shows how processes operate with one another and in what order. Clear, consistent, and maintainable diagrams are crucial for effective communication and documentation. Adhering to these guidelines will help ensure that our diagrams serve their purpose well.

The use of ASCII-art for diagrams is a deliberate choice, as outlined in [ADR-016: ASCII-Art Diagrams](../../../docs/adrs/adr-016-ascii-art-diagrams.md), primarily for its version-control friendliness, accessibility, and ease of integration into Markdown documentation.

This guide synthesizes lessons learned from general diagramming efforts and aims to establish a common standard for sequence diagrams.

## Key Diagram Components

Sequence diagrams in this guide utilize several common visual components. Understanding these upfront will help in interpreting and creating diagrams:

- **Participant Box:** Identifies an actor, object, or system component involved in the sequence.

  ```
     ┌─────────────┐
     │ Participant │
     └─────────────┘
  ```

- **Lifeline:** A vertical solid line (`│`) extending down from a participant box, representing the participant's existence through time.

  ```
         │
         │
         │
  ```

- **Message:** An arrow indicating communication from one lifeline to another. The arrow is typically labeled with the message name or content.

  ```
         ├─── Label() ───►│
         │◄── Reply() ────┤
  ```

  (See Principle 2 for different arrow styles like synchronous/asynchronous.)

- **Activation Bar (Execution Occurrence):** A rectangle or thickened portion on a lifeline, showing the period during which the participant is active or processing a message. Styles can vary:

  - _Simple Style (using T-junctions and corners):_
    ```
           ├─┐
           │ │ Active
           └─┘
    ```
  - _Boxed Style (for emphasis or longer processes, often with double lines):_
    ```
           ╔═════════╗
           ║ Process ║
           ╚═════════╝
    ```
    (See Principle 3 for more on activation bars.)

- **Interaction Fragment Frame:** A box that encloses a portion of the sequence to denote conditional logic (`alt`, `opt`), loops (`loop`), or parallel execution (`par`).
  ```
     ┌─ loop (condition) ──────────┐
     │  Message()                  │
     │  ...                        │
     └─────────────────────────────┘
  ```
  (See Principle 10 for more on fragments.)

---

## Core Principles

### 1. Represent Lifelines Clearly

**Rationale:** Lifelines represent participants (e.g., actors, objects, components) in the interaction. They must be clearly delineated and consistently named.

**DO (Clear Lifeline Representation):**

- Use a box at the top for the participant name (see "Participant Box" under Key Diagram Components).
- Extend a vertical solid line (`│`) downwards from the participant box (see "Lifeline" under Key Diagram Components).
- Align lifelines horizontally.

**Example:**

```
   ┌───────┐         ┌───────────┐         ┌───────────┐
   │ Actor │         │ Service A │         │ Service B │
   └───────┘         └───────────┘         └───────────┘
       │                 │                     │
       │                 │                     │
       ├─ Message 1 ────►│                     │
       │                 │                     │
       │                 ├─ Message 2 ────────►│
       │                 │                     │
       │                 │                     │
```

**Explanation of Diagram Elements:**

- **Participant Boxes:** Each participant in the interaction (e.g., the "Actor", "Service A", and "Service B" boxes shown above) is represented by a box with its name.
- **Lifelines:** The vertical solid lines (`│`) extending downwards from each participant box are the lifelines. These represent each participant's presence over time and are the standard style for lifelines in this guide.
- **Messages:** Communication, such as `Message 1` from Actor to Service A, and `Message 2` from Service A to Service B, is shown with horizontal arrows.
  - The message itself is labeled _on_ or _within_ the arrow line.
  - When a message arrow originates from a lifeline, the lifeline character at that point becomes a T-junction character (e.g., `├` where `Message 1` originates). This clearly indicates the message branching from the lifeline.

### 2. Use Clear Connecting Characters and Arrowheads for Messages

**Rationale:** Messages represent communication between lifelines. Clear connectors and arrowheads are essential for showing the direction and type of message.

**DO (Clear Message Connectors and Arrowheads):**

- **Horizontal lines:** Use `─` (box drawings light horizontal) for messages.
- **Arrowheads:**
  - Synchronous call: `──►` or `────►`
  - Asynchronous signal: `─→` or `────→`
  - Reply/Return message: `◄──` or `◄────` (often dashed: `◄- - -`)
- Connect messages to the lifelines or activation bars.

**Example:**

```
   ┌───────┐         ┌───────────┐
   │Client │         │  Server   │
   └───────┘         └───────────┘
       │                 │
       │───Request()────►│
       │                 │
       │                 │░░░░░░░░░░░│
       │                 │░ Process ░│
       │                 │░░░░░░░░░░░│
       │                 │
       │◄───Response()───│
       │                 │
```

**Explanation of Diagram Elements:**

- The shaded bar (using `░` characters) on the Server's lifeline, labeled "Process", is an example of an **activation bar**. It visually represents the period during which the Server is active processing the `Request()`. This is one optional style for depicting activation.

### 3. Indicate Activation Bars (Execution Occurrences)

**Rationale:** Activation bars show the period during which a participant is performing an action (i.e., the focus of control).

**DO (Use Activation Bars):**

- Draw a tall, thin rectangle (or a thicker line segment) on the lifeline.
- Messages should originate from and arrive at these activation bars if they are shown.
- Simple alternative: Indent messages under a lifeline to imply activation.

**Example with Activation Bars:**

```
   ┌───────┐         ┌───────────┐         ┌───────────┐
   │ User  │         │  SystemA  │         │  SystemB  │
   └───────┘         └───────────┘         └───────────┘
       │                 │                     │
       │──Action1()─────►│                     │
       │                 ├─┐                   │
       │                 │ │                   │
       │                 │ │──Action2()───────►│
       │                 │ │                   ├─┐
       │                 │ │                   │ │
       │                 │ │                   │ │ Process
       │                 │ │                   │ │
       │                 │ │◄──Result2()───────│ │
       │                 │ │                   └─┘
       │                 │ │                   │
       │◄──Result1()─────│ │                   │
       │                 └─┘                   │
       │                 │                     │
```

**Explanation of Diagram Elements:**

- **Activation on SystemA:** After `Action1()` is sent to `SystemA`, an activation bar (shown with `├─┐` and `└─┘`) appears on `SystemA`'s lifeline. This signifies that `SystemA` is active.
- **Activation on SystemB:** Similarly, when `SystemA` sends `Action2()` to `SystemB`, an activation bar appears on `SystemB`'s lifeline. The label "Process" within this activation bar indicates what `SystemB` is doing.
- Messages like `Action1()` and `Action2()` originate from one lifeline (or an activation bar on it) and terminate on another, often initiating an activation. Reply messages like `Result1()` and `Result2()` show the flow of information back.

### 4. Maintain Consistent Time Progression

**Rationale:** In sequence diagrams, time progresses downwards. Messages should be ordered chronologically from top to bottom.

**DO (Order Messages Chronologically):**
This first diagram illustrates an error in chronological ordering.

```
   ┌─────┐       ┌─────┐
   │  A  │       │  B  │
   └─────┘       └─────┘
      │             │
      │──Msg1─────► │
      │             │
      │             │──Msg2─────►
      │             │
      │◄──Msg3──────│
      │             │
```

**Explanation of Diagram Elements (Illustrating an Error):**

- **The Error Illustrated:** In this diagram, `Msg2` (sent from B) is drawn higher on the page than `Msg3` (sent from B to A). In sequence diagrams, time flows downwards. Therefore, this visual representation implies that `Msg2` occurs _before_ `Msg3`. If the intended sequence was for `Msg3` to actually happen _before_ `Msg2`, then this diagram is incorrect because `Msg3` should be drawn above `Msg2`.

**DO INSTEAD (Correct Chronological Order):**
This second diagram shows the correct chronological order, assuming `Msg3` occurs before `Msg2`.

```
   ┌─────┐       ┌─────┐
   │  A  │       │  B  │
   └─────┘       └─────┘
      │             │
      │──Msg1─────► │
      │             │
      │◄──Msg3──────│
      │             │
      │             │──Msg2─────►
      │             │
```

**Explanation of Diagram Elements (Correct Order):**

- **Corrected Order:** Here, `Msg3` (from B to A) is drawn _above_ `Msg2` (from B). This correctly depicts that `Msg3` occurs before `Msg2` in the sequence, adhering to the downward flow of time.
  (Example context: `Msg3` could be a reply to `Msg1`. `Msg2` is then sent by B after events related to `Msg1` and/or `Msg3` have concluded.)

### 5. Strive for Optimal Width (Avoid Wrapping)

**Rationale:** ASCII-art diagrams are often viewed in environments with line length limits (e.g., code editors, Markdown viewers). Diagrams that are too wide (typically exceeding 80-100 columns) can wrap, breaking their visual integrity and making them hard to read. The goal is to create diagrams that are compact enough to avoid wrapping, while still being clear and not overly dense. This involves:

- Keeping lifelines reasonably spaced.
- Avoiding excessive horizontal sprawl or gratuitous empty space.
- Balancing diagram width with the clarity of labels (see Principle 6 and Principle 9).

**DO (Strategies for Optimal Width):**

- Keep lifeline names concise.
- Use shorter message arrows if space is tight, but always prioritize clarity. If a shorter arrow makes the message ambiguous, consider if the diagram needs more width or if the message label can be more concise.
- Be mindful of the overall width as you add participants and messages.

### 6. Keep Diagram Labels Concise ("Text-Light")

**Rationale:** Overly verbose labels on lifelines or messages create clutter. The diagram should provide clear visual structure; elaborate details in accompanying text.

**DO INSTEAD (Concise Labels with Numbering):**

```
   ┌───────┐       ┌─────────┐
   │ Actor │       │ System  │
   └───────┘       └─────────┘
       │               │
       │──1. Req()────►│
       │               │ ╔══════════╗
       │               │ ║ Process  ║
       │               │ ╚══════════╝
       │◄──2. Resp()───│
       │               │
```

1.  **Req():** User initiates a request.
2.  **Resp():** System returns a response.

### 7. Use Supplementary Explanations Below Diagrams

**Rationale:** Keeping diagrams clean is key. Use numbered lists or paragraphs below the diagram for details about messages or participant responsibilities.

**DO (Clean Diagram with Numbered Supplementary Text):**
(See example in Principle 6)

### 8. Consistent Styling and Casing

**Rationale:** Consistency in visual elements aids readability and professionalism.

**DO (Recommended Style):**

- **Lifelines:**
  ```
  ┌─────────┐
  │  Label  │
  └─────────┘
      │   (standard: solid line, e.g., `│`)
      .
      .
  ```
- **Activation Bars (choose one style and be consistent):**
  - `│ ▓▓▓ │` (shaded)
  - `│ ███ │` (solid block)
  - `├─┐` and `└─┘` to denote start/end on the lifeline.
  - `║` (double vertical line)
- **Labels:** Use Title Case for lifeline labels (e.g., `│ My System │`). For messages, use method call syntax (e.g., `doSomething()`) or concise descriptions (e.g., `User Data`).

### 9. Balance Vertical Space with Label Clarity

**Rationale:** While Principle 5 ("Minimize Horizontal Width") is important, for sequence diagrams with a manageable number of participants (e.g., 2-4), it's often preferable to use adequate horizontal space to allow for clear, descriptive message labels rather than overly abbreviating them to force a narrow diagram. Adding vertical space between messages can improve readability if the sequence is long.

A "taller" style (more vertical space between messages) might be specifically beneficial when:

- You have many participants (e.g., 5+), and horizontal screen real estate is severely limited.
- A very long sequence of messages occurs between just two or three participants, and you want to show the flow clearly without making the diagram excessively wide due to long message labels.

In most other cases, prioritize clear, reasonably complete message labels, even if it makes the diagram a bit wider, over extreme vertical compression that sacrifices clarity.

**DO (Example of Using Vertical Space for a Long Sequence):**
This example shows how adding vertical space can help readability for a sequence of messages, especially if message labels were longer.

```
   ┌─────┐       ┌─────┐
   │  A  │       │  B  │
   └─────┘       └─────┘
      │             │
      │──Msg1─────► │
      │             │
      │             │
      │             │
      │◄──Reply1────│
      │             │
      │             │
      │──Msg2─────► │
      │             │
      │             │
      │◄──Reply2────│
      │             │
```

### 10. (Optional) Use Fragments for Complex Interactions

**Rationale:** For more complex scenarios, standard UML sequence diagram fragments like `loop`, `alt` (alternatives), `opt` (optional), and `par` (parallel) can be represented.

**DO (Representing a Loop Fragment):**

```
   ┌─────┐       ┌─────┐
   │  A  │       │  B  │
   └─────┘       └─────┘
      │             │
      │             │
   ┌─ loop (for each item) ─┐
   │  │             │       │
   │  │──Process()─►│       │
   │  │             │       │
   │  │◄──Ack()─────│       │
   │  │             │       │
   └────────────────────────┘
      │             │
```

## Comprehensive Example

Here is an example of a simple "User Login" sequence:

```
   ┌──────────┐        ┌──────────────┐        ┌────────────────┐
   │  User    │        │ LoginService │        │ AuthService    │
   └──────────┘        └──────────────┘        └────────────────┘
        │                    │                         │
        │──1. EnterCreds()──►│                         │
        │                    │                         │
        │                    │  ╔══════════════════╗   │
        │                    │  ║ Validate Inputs  ║   │
        │                    │  ╚══════════════════╝   │
        │                    │                         │
        │                    │──2. AuthRequest()──────►│
        │                    │                         │ ╔═════════════╗
        │                    │                         │ ║ Check Creds ║
        │                    │                         │ ╚═════════════╝
        │                    │                         │
        │                    │◄──3. AuthResult()───────│
        │                    │                         │
        │                    │  ╔══════════════════╗   │
        │                    │  ║ Process Result   ║   │
        │                    │  ╚══════════════════╝   │
        │                    │                         │
        │◄──4.LoginStatus()──│                         │
        │                    │                         │
```

**Explanation of Diagram Elements:**

1.  **EnterCreds():** The User provides credentials to the LoginService.
2.  **AuthRequest():** The LoginService forwards an authentication request to the AuthService.
3.  **AuthResult():** The AuthService returns the result of the authentication attempt.
4.  **LoginStatus():** The LoginService informs the User of the login status.

This diagram uses:

- Clear lifelines with labels.
- Numbered messages with arrowheads indicating synchronous calls.
- Simple activation bar style (using `╔═╗` and `╚═╝`).
- Concise labels.
- Supplementary numbered explanations.

---

_This guide is a living document and may be updated as new best practices emerge._
