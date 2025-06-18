---
id: "adr-025-restructure-ai-guides-directory"
title: "Restructure docs/ai-guides Directory for Clarity"
status: "Accepted"
date: "2025-05-30"
tags: "documentation;structure;ai-guides;refactoring"
---

# ADR-025: Restructure docs/ai-guides Directory for Clarity

## Context

The `docs/ai-guides/` directory historically grew to include guides essential for the Vibe Tasking framework (primarily within a `vibe-tasking/` subdirectory) alongside other topic-specific guides, templates, and tutorials at its top level or in other subdirectories (e.g., `tutorials/`).

This mixed structure made it less clear to distinguish between:

- Core framework documentation (guides critical for understanding and using Vibe Tasking itself).
- Supplementary or contributed materials (guides on related topics, templates for various document types, tutorial series).

As the number of guides increased, discoverability and understanding the intended scope and audience of different guides became more challenging for both human users and AI assistants. A clearer organizational paradigm was needed to improve navigation and maintainability.

## Alternatives Considered

### 1. Keep Existing Structure

- **Description:** Maintain the current flat structure within `docs/ai-guides/` with `vibe-tasking/` for core guides and others at the top level or in specific subdirectories like `tutorials/`.
- **Pros:**
  - No immediate effort required for restructuring.
- **Cons:**
  - Does not address the existing clarity and discoverability issues.
  - Scalability becomes more difficult as more guides are added.
  - The distinction between "core" and "other" guides remains implicit.

### 2. Introduce More Granular Subdirectories by Topic/Type

- **Description:** Create multiple specific subdirectories under `docs/ai-guides/` based on guide type (e.g., `/templates`, `/framework-guides`, `/tooling-guides`, `/process-guides`) or specific topics.
- **Pros:**
  - Could provide very fine-grained organization.
- **Cons:**
  - Might lead to an overly complex directory tree that is difficult to navigate.
  - Defining and maintaining clear boundaries for numerous categories could be challenging.
  - May result in very few files per directory, leading to sprawl.

## Decision

Restructure the `docs/ai-guides/` directory to have two primary top-level subdirectories:

1.  **`core/`**:

    - **Purpose:** This directory will house AI guides that are essential to understanding and using the Vibe Tasking framework itself. These are considered fundamental to the project's methodology.
    - **Formation:** It is formed by renaming the existing `docs/ai-guides/core/` directory to `docs/ai-guides/core/`.

2.  **`contrib/`**:
    - **Purpose:** This directory will house all other AI guides. This includes topic-specific guides (e.g., how to write ADRs, how to author articles), templates for various document types (e.g., `adr.template.md`, `article.template.md`), and collections of tutorials (e.g., the `tutorials/` subdirectory). These materials supplement or extend the core framework documentation but are not strictly part of its fundamental definition.

The main `docs/ai-guides/README.md` will be updated to describe this new organization and the purpose of each subdirectory.

## Consequences

### Positive

- **Improved Clarity:** Provides a clear and explicit distinction between core Vibe Tasking framework documentation and other supplementary/contributed materials.
- **Enhanced Discoverability:** Makes it easier for users and AI assistants to locate specific types of guides based on whether they are looking for core framework information or other related topics.
- **Better Scalability:** Offers a more organized structure for adding new AI guides in the future, with clear placement guidelines (either in `core/` or `contrib/`).
- **Simplified Navigation:** Reduces clutter at the top level of `docs/ai-guides/`.

### Negative

- **Link Updates Required:** Necessitates a one-time effort to update all existing cross-references throughout the project that point to files previously within `docs/ai-guides/` or `docs/ai-guides/core/`. (This is addressed by story `s063-refactor-ai-guides-structure`).
- **Adaptation Period:** Users and AI assistants familiar with the old structure will need to adapt to the new paths and organization.

### Follow-up Work

- The `docs/ai-guides/README.md` file needs to be updated to reflect this new structure.
- All internal project cross-references to guides within `docs/ai-guides/` must be updated.
