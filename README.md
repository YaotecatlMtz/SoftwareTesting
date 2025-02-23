# SoftwareTesting

### This repo is intended for store first software testing's homework

## Commit Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org) specification for commit messages in this repository. This ensures a consistent and readable commit history, making it easier to understand changes and automate versioning.

### Commit Message Format

Each commit message must follow this format:

&lt;type&gt;[optional scope]: &lt;description&gt;

[optional body]

[optional footer]

- **Type**: Describes the kind of change being made. Common types include:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation changes
  - `style`: Code style changes (e.g., formatting)
  - `refactor`: Code refactoring
  - `test`: Adding or updating tests
  - `chore`: Maintenance or tooling changes
- **Scope** (optional): Specifies the part of the codebase affected by the change (e.g., `api`, `ui`, `config`).
- **Description**: A concise summary of the change.
- **Body** (optional): A detailed explanation of the change, if necessary.
- **Footer** (optional): Used for referencing issues (e.g., `Closes #123`) or breaking changes.

### Examples

- `feat(api): add user authentication endpoint`
- `fix(ui): resolve button alignment issue`
- `docs: update installation guide`
- `chore: update dependencies`

### Why Use Conventional Commits?

- **Improved readability**: Commit messages are easier to understand.
- **Automated versioning**: Tools like [semantic-release](https://semantic-release.gitbook.io/) can automatically determine version bumps based on commit types.
- **Better changelogs**: Commit history can be used to generate detailed and structured changelogs.

Please ensure all commits adhere to this convention. Thank you for your cooperation!
