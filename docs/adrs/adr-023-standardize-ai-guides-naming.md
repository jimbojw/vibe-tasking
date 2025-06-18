---
id: "adr-023-standardize-ai-guides-naming"
title: "Standardize Naming Convention for AI-Guide Documents"
status: "Accepted"
date: "2025-05-29"
tags: "documentation;convention;ai-guide;naming"
deciders: "User, Roo (AI Assistant)"
---

# ADR-023: Standardize Naming Convention for AI-Guide Documents

## Context

Currently, files within the `docs/ai-guides/` directory and its subdirectories do not follow a strictly consistent naming convention. This can lead to:

- Difficulty in quickly locating specific guides, especially as the number of guides grows.
- Inconsistent alphabetical sorting, making it harder to browse related guides.
- Potential ambiguity regarding a guide's primary subject or purpose based on its filename alone.
- Increased cognitive load for developers and AI assistants trying to navigate and understand the guide structure.

A standardized naming convention is needed to improve discoverability, consistency, and maintainability of these important documents.

## Alternatives Considered

### Alternative 1: Verb-Object Convention (e.g., `writing-adrs-guide.md`)

- **Description:** Filenames start with the action (verb/gerund) followed by the object.
- **Pros:**
  - Can be intuitive for some users.
  - Clearly indicates the action related to the guide.
- **Cons:**
  - Does not group files by their primary subject matter as effectively when sorted alphabetically, making it harder to find all guides related to a specific topic (e.g., all "story" guides).

### Alternative 2: No Standardized Convention (Status Quo)

- **Description:** Continue with ad-hoc or loosely defined naming.
- **Pros:**
  - No immediate effort required to change existing files or define a new standard.
- **Cons:**
  - Perpetuates the existing issues of poor discoverability, inconsistency, and increased cognitive load.
  - Becomes increasingly problematic as the project scales and more guides are added.

### Alternative 3: Object-BaseVerb Convention (e.g., `stories-plan-guide.md`)

- **Description:** The object/subject of the guide appears first, followed by the base form of the verb (e.g., "plan", "write").
- **Pros:**
  - Achieves grouping by object for better alphabetical sorting.
  - More concise due to the use of the base verb.
- **Cons:**
  - Can sometimes sound less natural or descriptive for a guide's title compared to using a gerund (e.g., "planning," "writing").
  - The base verb might not always clearly convey the "guidance" aspect.

## Decision

We will adopt the following naming convention for AI-Guide documents located in `docs/ai-guides/` and its subdirectories:

**`[object-noun]-[gerund-action]-guide.md`**

- **`[object-noun]`**: The primary subject or entity the guide is about.
  - This noun should generally be in **plural form** (e.g., `stories`, `adrs`, `articles`, `tutorials`, `ai-guides`, `template-files`, `context-documents`).
  - For singular, abstract concepts, the singular form should be used (e.g., `onboarding` in `onboarding-updating-guide.md`).
- **`[gerund-action]`**: The primary activity, process, or aspect the guide addresses, using the gerund form (`-ing`) of a verb (e.g., `planning`, `writing`, `updating`, `designing`, `handling`, `working`).
- The filename always ends with `-guide.md`.

**Examples:**

- `stories-planning-guide.md`
- `adrs-writing-guide.md`
- `onboarding-updating-guide.md`
- `ai-guides-collaborative-designing-guide.md`

**Exception for Template Files:**
Template files within `docs/ai-guides/` (or its subdirectories) will continue to use the simpler `[object].template.md` convention (e.g., `adr.template.md`, `article.template.md`, `ai-guide.template.md`), as this clearly identifies them as templates for a specific object.

**Rationale:**
This convention was chosen because:

- It prioritizes grouping by subject matter (the "object") when files are sorted alphabetically, significantly improving discoverability.
- The use of a gerund for the "action" clearly and naturally describes the guide's purpose or the process it details.
- It strikes a balance between a systematic approach and clear, human-readable filenames.

## Consequences

### Positive

- **Improved Discoverability:** Guides related to the same topic (e.g., all guides about "stories") will be grouped together alphabetically.
- **Enhanced Consistency:** All AI-Guide filenames will follow a predictable and uniform structure.
- **Increased Clarity:** The purpose and subject of a guide will be more readily apparent from its filename.
- **Simplified Maintenance:** Easier to manage and organize AI-Guides as the project grows.
- **Better AI Interaction:** A consistent naming scheme can aid AI assistants in identifying and suggesting relevant guides more accurately.

### Negative

- **One-time Effort:** Requires an initial effort to rename all existing non-conforming AI-Guide files.
- **Link Maintenance:** Any existing internal links within the project (e.g., in other guides, stories, `CONTEXT.md`) that point to the old filenames will need to be identified and updated.
- **Awareness:** Team members and contributors will need to be made aware of and adhere to the new convention for future guides.
