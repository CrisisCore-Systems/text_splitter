# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0-alpha] - 2025-10-20

### Added
- Comprehensive documentation in README.md with usage examples
- Full docstrings for all classes and methods
- Logging support throughout the application
- GitHub Actions CI/CD pipeline for automated testing
- CONTRIBUTING.md with contribution guidelines
- setup.py for pip installation support
- File existence validation in CrisisCoreSplitter.__init__()
- Updated .gitignore for test outputs and coverage files

### Changed
- Version number updated from v1.0 to v0.1.0-alpha
- Replaced all print statements with proper logging
- Fixed import errors in gui.py and main.py
- Improved test cleanup patterns

### Fixed
- Missing import for CrisisCoreSplitter in gui.py
- Incorrect import path in main.py
- UTF-8 BOM markers removed from all Python files
- pyproject.toml format issues (literal \n characters)

### Removed
- Orphaned TypeScript files (src/lib/utils.ts, src/components/ui/)
- Duplicate text_splitter_project/ directory
- UTF-8 BOM markers from Python source files

### Moved
- script.py relocated to examples/semantic_splitter.py

## [0.1.0] - 2025-01-26

### Added
- Initial release with basic text splitting functionality
- GUI interface using PySimpleGUI
- CLI interface with argparse
- Basic test suite with pytest
- MIT License
- requirements.txt with dependencies
- pyproject.toml for modern Python packaging
