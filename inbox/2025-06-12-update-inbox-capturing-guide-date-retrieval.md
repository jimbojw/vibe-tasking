# Update `inbox-capturing-guide.md` for Date Retrieval

Based on the retrospective following the AI cognition case study, this is a proposal to update the `inbox-capturing-guide.md`.

The guide should be updated to more prominently feature checking `environment_details` for the current date as the primary method for generating the filename's date stamp. This reinforces the core AI principle of using immediately available context before resorting to external commands (the "fallback method"). This change will help prevent future instances of the AI unnecessarily executing a `date` command when the information is already present.

**Context:** This suggestion originated from the retrospective following the creation of the [AI Cognition Case Study](../../docs/reference/ai-cognition-case-study/README.md). The AI's failure to use the available date from `environment_details` was a direct example of the cognitive inertia analyzed in the study.
