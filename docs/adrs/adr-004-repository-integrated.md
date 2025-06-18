---
id: "adr-004"
title: "Repository-Integrated Framework"
status: "Accepted"
date: "2025-05-19"
tags: "architecture;version-control;documentation-storage;core-concept"
---

# ADR-004: Repository-Integrated Framework

## Context

A key aspect of Vibe Tasking is how and where its artifacts (stories, guides, context files, ADRs themselves) are stored and managed. For a framework designed to work closely with software development projects, which are almost universally managed in version control systems (VCS) like Git, the location of its documentation is critical for accessibility, versioning, and integration with developer workflows.

## Alternatives Considered

1.  **External Documentation System:** Use a separate, dedicated documentation platform or wiki (e.g., Confluence, SharePoint, a dedicated website).

    - _Pros:_ Mature features for content organization, search, and access control often available.
    - _Cons:_ Creates a disconnect between the project's code/tasks and its documentation. Documentation can easily become out of sync with the codebase. Requires users to manage and navigate a separate system. May not be easily accessible or parsable by AI assistants working within the IDE/repository.

2.  **Database-Driven System:** Store all Vibe Tasking artifacts in a database.

    - _Pros:_ Powerful querying and relational capabilities.
    - _Cons:_ Introduces significant complexity (database setup, maintenance, schema management). Moves away from simple, human-readable text files. Less transparent and harder for standard developer tools (and AI operating on file systems) to interact with directly.

3.  **Local File System (Outside VCS):** Store Vibe Tasking documents on the user's local file system but not necessarily within the project's version-controlled repository.
    - _Pros:_ Simple to set up initially.
    - _Cons:_ Lacks versioning, backup, and sharing capabilities inherent to VCS. Prone to data loss. Not easily shareable with team members or across different environments.

## Decision

Vibe Tasking will be a **repository-integrated framework**. All its core artifacts, including stories, journals, guides, context files, and ADRs, will be stored as plain text files (primarily Markdown) directly within the user's project repository.

This means these documents live alongside the source code and other project assets and are managed by the same version control system (e.g., Git).

## Consequences

### Positive

- **Single Source of Truth:** Code, tasks, and documentation reside together, reducing the chance of them becoming desynchronized.
- **Versioning:** All Vibe Tasking artifacts benefit from the versioning capabilities of the VCS (history, branching, merging). Changes to tasks or documentation can be tracked alongside code changes.
- **Accessibility:** Developers and AI assistants already working within the repository have immediate access to all Vibe Tasking documents.
- **Standard Tooling:** Common developer tools (text editors, IDEs, `grep`, etc.) can be used to interact with Vibe Tasking files.
- **Collaboration:** VCS platforms (like GitHub, GitLab) provide established mechanisms for collaboration, review (e.g., pull requests for documentation changes), and issue tracking that can be leveraged.
- **Backup and Distribution:** Handled by the existing VCS mechanisms.
- **Offline Access:** Documents are available locally as part of the repository clone.

### Negative

- **Repository Size:** For very large projects with extensive documentation, this could contribute to repository size, though text files are generally small.
- **Merge Conflicts:** Like any text-based artifact in VCS, concurrent edits to the same Vibe Tasking file can lead to merge conflicts, though this is a standard part of VCS workflows.
- **Not Ideal for Large Binary Artifacts:** While story `artifacts/` directories can store files, very large binary files are generally better handled by dedicated artifact storage solutions (e.g., Git LFS, or external storage linked from the story). Vibe Tasking itself doesn't prescribe a solution for large binaries beyond what the underlying VCS offers.

This decision aligns with the goal of making Vibe Tasking a natural extension of existing developer workflows and ensuring that task management and project context are tightly coupled with the project's evolution.
