# Contributing to RustChain Bounties

Thank you for your interest in contributing to the RustChain Bounties repository! This document provides guidelines for setting up the project, submitting pull requests, and maintaining code style. By following these guidelines, you help ensure a smooth and consistent contribution process.

## Table of Contents

- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
- [How to Contribute](#how-to-contribute)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Code Style](#code-style)
- [Issue Reporting](#issue-reporting)
- [Community and Communication](#community-and-communication)

## Getting Started

This repository is a bounty board for the RustChain ecosystem. It does not contain executable code but rather issues and documentation. Contributions typically involve:

- Creating or updating issues with bounty tags
- Improving documentation (like this file)
- Reviewing and validating bounty submissions

To get started, ensure you have:

- A GitHub account
- Basic familiarity with Markdown
- Understanding of the RustChain project (optional but helpful)

## Repository Structure

```
rustchain-bounties/
├── README.md          # Project overview and badges
├── CONTRIBUTING.md    # This file
├── .github/
│   ├── ISSUE_TEMPLATE/ # Templates for creating issues
│   └── workflows/      # GitHub Actions (if any)
└── (other files as needed)
```

## Setup Instructions

Since this is a documentation-only repository, no local development environment is required. However, to contribute via GitHub:

1. **Fork the repository**  
   Click the "Fork" button at the top-right of the repository page.

2. **Clone your fork**  
   ```bash
   git clone https://github.com/<your-username>/rustchain-bounties.git
   cd rustchain-bounties
   ```

3. **Create a new branch**  
   ```bash
   git checkout -b your-feature-branch
   ```

4. **Make your changes**  
   Edit files using any text editor (e.g., VS Code, Vim, or GitHub's web editor).

5. **Commit and push**  
   ```bash
   git add .
   git commit -m "Brief description of changes"
   git push origin your-feature-branch
   ```

6. **Open a pull request**  
   Go to the original repository and click "New Pull Request."

## How to Contribute

### Types of Contributions

- **Creating a bounty issue**: Add a new issue with the `bounty` label, following the issue template.
- **Updating documentation**: Improve existing files like `README.md` or `CONTRIBUTING.md`.
- **Validating submissions**: Review pull requests linked to bounty issues and provide feedback.

### Bounty Process

1. An issue is created with the `bounty` label and a description of the task.
2. Contributors claim the bounty by commenting on the issue (if applicable).
3. Work is submitted via a pull request referencing the issue.
4. Maintainers review and, if accepted, the bounty is awarded in RTC.

## Pull Request Guidelines

- **Reference the issue**: Include `Closes #<issue-number>` or `Related to #<issue-number>` in the PR description.
- **Keep PRs focused**: One PR per bounty or logical change.
- **Provide a clear description**: Explain what the PR does and why.
- **Be responsive**: Address reviewer comments promptly.
- **No merge conflicts**: Ensure your branch is up-to-date with the main branch before submitting.

### PR Template

```markdown
## Description
Briefly describe the changes made.

## Related Issue
Closes #<issue-number>

## Checklist
- [ ] I have read the CONTRIBUTING.md
- [ ] My changes follow the code style guidelines
- [ ] I have tested my changes (if applicable)
```

## Code Style

Since this repository contains only Markdown files, code style refers to formatting and structure:

- **Markdown**: Use standard GitHub-flavored Markdown. Avoid HTML unless necessary.
- **Headings**: Use `##` for top-level sections, `###` for subsections, etc.
- **Lists**: Use `-` for unordered lists, `1.` for ordered lists.
- **Code blocks**: Use triple backticks with language specifiers (e.g., ` ```bash `).
- **Links**: Use descriptive link text, not raw URLs.
- **Consistency**: Follow the existing style in the repository.

### Example

```markdown
### Setup Instructions

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/<your-username>/rustchain-bounties.git
   ```
```

## Issue Reporting

- **Use issue templates**: When creating a bounty, use the provided template.
- **Be specific**: Clearly describe the task, expected outcome, and bounty amount.
- **Tag appropriately**: Add labels like `bounty`, `easy`, `documentation`, etc.
- **No duplicates**: Search existing issues before creating a new one.

## Community and Communication

- **GitHub Issues**: Primary channel for bounty-related discussions.
- **RustChain Community**: For broader questions, refer to the [RustChain repository](https://github.com/Scottcjn/RustChain).
- **Code of Conduct**: Be respectful and constructive. Harassment or spam will not be tolerated.

## License

By contributing, you agree that your contributions will be licensed under the same license as this repository (if applicable). If no license is specified, contributions are considered public domain.

---

Thank you for helping grow the RustChain ecosystem! Happy contributing.