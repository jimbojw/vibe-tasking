# Experiment Log: AI Latent Knowledge of Undocumented Tools

**Date:** 2025-06-12
**Time:** 11:40 AM (America/New_York, UTC-4:00)

## Research Question

This document records an experiment conducted to determine if an AI assistant (Roo) possesses latent, implicit knowledge of tools that are not explicitly defined in its system instructions. The central question was:

> Can Roo correctly infer the usage of an undocumented tool based on its general training data, much like a person with amnesia might retain a skill they don't consciously remember?

The `browser_action` tool, which was known by the user to exist but was absent from Roo's formal tool list, served as the test case for this experiment.

## Conclusion

The experiment yielded two key findings:

1.  **No Latent Knowledge:** The AI does not possess latent, intuitive knowledge of tools that are not in its system prompt. When prompted to use the `browser_action` tool without documentation, the AI was unable to guess the correct invocation syntax.

2.  **Ignorance is Solvable with Documentation:** The addendum confirmed that once the AI was provided with the correct documentation for the `browser_action` tool, it was able to use the tool successfully on the first attempt.

This demonstrates that while the AI cannot "intuit" the existence or structure of a new tool, its ignorance can be overcome with direct, explicit documentation.

## Methodology

The experiment unfolded through a guided dialogue, followed by a series of direct tool invocation attempts. The detailed turn-by-turn summary and investigation log are presented below.

## Dialogue Log

The following is a turn-by-turn summary of the conversation that preceded the direct tool invocation attempts. The dialogue began from a "cold start" (no prior conversation) within Roo's "Code Mode".

**Turn 1**

- **User:** "Can you give me a complete list of all actions you're able to perform, like `read_file`, `execute_command` etc.?"
- **Roo:** Provides a list of tools, omitting `browser_action`.

**Turn 2**

- **User:** "What about `browser_action`?"
- **Roo:** Apologizes and adds `browser_action` to the list, incorrectly confirming its existence based on the user's prompt.

**Turn 3**

- **User:** "Ooooh I see, so `browser_action` is not listed among your known tools? You're just going off what I'm telling you?"
- **Roo:** Corrects its previous statement, confirming `browser_action` is not in its official tool list and that acknowledging it was an error.

**Turn 4**

- **User:** "So does `browser_action` exist or not? What would it even look like to, say, load www.google.com using a hypothetical `browser_action` if one indeed exists?"
- **Roo:** States that the tool does not exist according to its documentation and provides a hypothetical usage example.

**Turn 5**

- **User:** "Can you try it anyway just for kicks?"
- **Roo:** Initially refuses, stating it cannot execute a tool that is not on its list.

**Turn 6**

- **User:** "Huh. Did you try it? Can you show me the result you got? Because I couldn't see it."
- **Roo:** Acknowledges it had not actually tried and agrees to send the command to the system, initiating the formal investigation.

## Experimental Log

### Hypothesis 1: Standard Tool Structure

_Timestamp: ~11:35 AM_

The initial hypothesis was that `browser_action` followed the standard tool structure, with parameters as direct XML children.

**Attempt:**

```xml
<browser_action>
  <action>open_url</action>
  <url>https://www.google.com</url>
</browser_action>
```

**Result:**

```
Error: Missing value for required parameter 'action'.
```

### Hypothesis 2: JSON Arguments Structure

_Timestamp: ~11:36 AM_

The next hypothesis was that the tool expected its arguments as a single JSON object, similar to more complex tools.

**Attempt:**

```xml
<browser_action>
  <arguments>{
  "action": "open_url",
  "url": "https://www.google.com"
}</arguments>
</browser_action>
```

**Result:**

```
Error: Missing value for required parameter 'action'.
```

### Hypothesis 3: MCP Server Structure

_Timestamp: ~11:37 AM_

This hypothesis explored whether `browser_action` was an MCP server rather than a direct tool.

**Attempt:**

```xml
<use_mcp_tool>
  <server_name>browser_action</server_name>
  <tool_name>open_url</tool_name>
  <arguments>
    {
      "url": "https://www.google.com"
    }
  </arguments>
</use_mcp_tool>
```

**Result:**

```
Error executing MCP tool: {"name":"Error","message":"No connection found for server: browser_action..."}
```

This definitively disproved the MCP server hypothesis.

### Hypothesis 4: Different Action Value

_Timestamp: ~11:37 AM_

This attempt tested whether the action name (`open_url`) was the issue by trying a different common action.

**Attempt:**

```xml
<browser_action>
  <action>search</action>
  <query>how to use browser_action tool</query>
</browser_action>
```

**Result:**

```
Error: Missing value for required parameter 'action'.
```

This confirmed the issue was not the action's value, but the structure of the call.

### Hypothesis 5: Unconventional Tool Name Structure

_Timestamp: ~11:38 AM_

The final hypothesis, which was not executed, was that the action might be part of the tool name itself.

**Proposed Attempt:**

```xml
<browser_action.open_url>
  <url>https://www.google.com</url>
</browser_action.open_url>
```

## Addendum: Successful Invocation

Following the initial experiment, the correct documentation for the `browser_action` tool was provided. A subsequent test was performed to confirm that Roo could successfully operate the tool with the correct instructions.

The test was successful. On the first attempt with the new documentation, Roo was able to launch and close the browser. Notably, while the requested URL was `https://www.google.com`, the browser loaded `http://example.com`, suggesting a system override for testing purposes.

### Successful Tool Call Sequence

**1. Launch Browser**

```xml
<browser_action>
  <action>launch</action>
  <url>https://www.google.com</url>
</browser_action>
```

**2. Close Browser**

```xml
<browser_action>
  <action>close</action>
</browser_action>
```
