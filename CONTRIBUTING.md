# Contributing to kr-translator

Thank you for considering contributing to kr-translator! We welcome contributions from everyone. Please take a moment to review this document to help you make your contribution.

## Code of Conduct

Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms. You can head on to read the full code of conduct, but simply keep this in mind: "Treat others how you would like to be treated".

## How to Contribute

### Reporting Bugs

If you find a bug in the source code, you can help us by submitting an issue to our [GitHub Repository](https://github.com/novel-zlood/kr-translator/issues). If you can submit a Pull Request with a fix, that's even better. Keep reading to see how we can help you with that.

### Suggesting Features

If you have an idea for a new feature, please open an issue with a detailed description of the feature and why it would be useful. 

### Submitting Changes

If you want to submit changes, please start with commenting the issue page where your changes applies. Simply saying "I'll work on this" is enough to let other people know that someone is working on it and therefore avoid conflict. If the changes that you plan to submit has no relevant issue yet, please start with creating one. Again, it will let maintainers aware that someone is working on it.

## Development Setup

### Prerequisites

- Python 3.10+
- Poetry

### Installation and Development

1. Fork the repository and clone your fork.
   ```bash
   git clone https://github.com/novel-zlood/kr-translator
   cd your-repo
   ```

2. Create a new branch

   ```bash
   git checkout -b my-new-feature
   ```

3. Prepare a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
4. Install dependencies.

   ```bash
   poetry install
   ```
   
5. Run the test

   ```bash
   poetry run pytest
   ```
   
## Style Guidelines

### Coding Standard

- Follow PEP 8 guidelines for Python code.
- Use meaningful variable and function names.
- Write docstrings for all public methods and functions.

### Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally.

## Creating PR

1. On your local repository, push your changes

   ```bash
   git push origin my-new-feature
   ```

2. Create a PR on github

   - Go to your forked repository on GitHub (e.g., https://github.com/yourusername/kr-translator).
   - Click the "Compare & pull request" button. 
   - Ensure the base repository points to the original repository and the base branch points to the branch you want to merge into (e.g., main). 
   - Provide a descriptive title and a detailed description of your changes in the PR form. Please quote the URL of Issue that is relevant to this changes within the description. 
   - Click the "Create pull request" button.

3. Wait for reviews

4. Merge your PR

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE.md).
