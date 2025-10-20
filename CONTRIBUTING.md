# Contributing to CrisisCore Text Splitter

Thank you for your interest in contributing to CrisisCore Text Splitter! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

This project adheres to a code of conduct that we expect all contributors to follow. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**: Explain the problem clearly
- **Steps to reproduce**: Detailed steps to reproduce the issue
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment details**: OS, Python version, package versions
- **Screenshots**: If applicable
- **Error messages**: Full error traceback if available

Use the GitHub issue tracker: https://github.com/CrisisCore-Systems/text_splitter/issues

### Suggesting Features

Feature suggestions are welcome! Please:

1. Check existing issues to see if it's already suggested
2. Provide a clear use case for the feature
3. Explain why this feature would be useful to most users
4. Consider if it fits the project's scope and goals

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- pip package manager

### Setting Up Your Development Environment

1. Fork the repository on GitHub

2. Clone your fork:
```bash
git clone https://github.com/YOUR-USERNAME/text_splitter.git
cd text_splitter
```

3. Add the upstream repository:
```bash
git remote add upstream https://github.com/CrisisCore-Systems/text_splitter.git
```

4. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Install the package in development mode:
```bash
pip install -e .
```

### Keeping Your Fork Updated

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Keep functions focused and small
- Maximum line length: 100 characters (with some flexibility for readability)

### Documentation

- Add docstrings to all public classes, methods, and functions
- Use Google-style docstrings format
- Include type hints where appropriate
- Update README.md if adding new features

### Code Structure

```python
"""Module docstring explaining the purpose."""
import standard_library
import third_party_library
from local_module import LocalClass

# Constants
CONSTANT_NAME = value


class MyClass:
    """Class docstring."""
    
    def __init__(self, param):
        """
        Initialize the class.
        
        Args:
            param (type): Description of parameter.
        """
        self.param = param
    
    def my_method(self):
        """
        Method description.
        
        Returns:
            type: Description of return value.
        """
        pass
```

## Testing Requirements

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names that explain what is being tested
- Follow the existing test structure in `tests/`

### Running Tests

Run all tests:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest tests/ --cov=src --cov-report=term-missing
```

Run specific test file:
```bash
pytest tests/test_splitter.py -v
```

### Test Requirements

- All tests must pass before submitting a pull request
- New features must include tests
- Bug fixes should include regression tests
- Aim for >80% code coverage

## Pull Request Process

### Before Submitting

1. **Update from upstream**: Ensure your branch is up to date
2. **Run tests**: All tests must pass
3. **Check code style**: Follow PEP 8 guidelines
4. **Update documentation**: Update README, docstrings, etc.
5. **Update CHANGELOG**: Add entry for your changes

### Submitting a Pull Request

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Add feature: brief description"
```

3. Push to your fork:
```bash
git push origin feature/your-feature-name
```

4. Open a Pull Request on GitHub

### Pull Request Guidelines

- **Title**: Clear, concise description of changes
- **Description**: Explain what, why, and how
  - What problem does it solve?
  - How does it solve it?
  - Any breaking changes?
  - Related issues?
- **Small PRs**: Keep changes focused and minimal
- **Tests**: Include tests for new functionality
- **Documentation**: Update relevant documentation
- **Clean history**: Squash commits if needed

### PR Review Process

1. Automated tests will run (must pass)
2. Maintainers will review your code
3. Address any feedback or requested changes
4. Once approved, a maintainer will merge your PR

## Reporting Bugs

### Bug Report Template

```markdown
**Bug Description**
A clear description of the bug.

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g., Ubuntu 20.04, Windows 10]
- Python Version: [e.g., 3.9.5]
- Package Version: [e.g., 0.1.0]

**Additional Context**
Any other relevant information, logs, or screenshots.
```

## Suggesting Features

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature.

**Use Case**
Why is this feature needed? What problem does it solve?

**Proposed Solution**
How would you implement this feature?

**Alternatives Considered**
Other approaches you've considered.

**Additional Context**
Any other relevant information.
```

## Questions?

If you have questions about contributing, feel free to:

- Open an issue with the "question" label
- Contact the maintainers at Crisiscore.systems@proton.me

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to CrisisCore Text Splitter! 🎉
