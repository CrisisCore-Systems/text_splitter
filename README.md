# CrisisCore Text Splitter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

An intelligent text file splitting utility with both GUI and CLI interfaces. Split large text files into manageable chunks while preserving line boundaries.

## Features

- **Dual Interface**: Both graphical (GUI) and command-line (CLI) interfaces
- **Intelligent Splitting**: Splits files based on byte size while respecting line boundaries
- **Configurable**: Customizable chunk sizes to fit your needs
- **Safe Processing**: Validates input files and chunk sizes before processing
- **Progress Tracking**: Visual feedback during file processing (GUI mode)
- **Comprehensive Logging**: Detailed logging for debugging and monitoring

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/CrisisCore-Systems/text_splitter.git
cd text_splitter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install in development mode:
```bash
pip install -e .
```

## Quick Start

### Command Line Interface (CLI)

Split a file with default settings (1MB chunks):
```bash
python src/main.py input.txt
```

Split a file with custom chunk size (in bytes):
```bash
python src/main.py input.txt -s 512000
```

Or use the installed command:
```bash
text-splitter input.txt -s 1048576
```

### Graphical User Interface (GUI)

Launch the GUI:
```bash
python src/gui.py
```

Then:
1. Click "Browse" to select your input file
2. Enter the desired chunk size in KB
3. Click "Process" to split the file
4. Monitor progress in the output window

## Usage

### CLI Options

```
usage: main.py [-h] [-s SIZE] file

CrisisCore-Systems Text Splitting Tool

positional arguments:
  file                  Input file path

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Maximum chunk size in bytes (default: 1MB)
```

### Output Files

Split files are created in the same directory as the input file with the naming pattern:
```
<input_file>.cc000.txt
<input_file>.cc001.txt
<input_file>.cc002.txt
...
```

## Configuration

### Chunk Size Guidelines

- **Small files (< 1MB)**: Use 100KB - 500KB chunks
- **Medium files (1-10MB)**: Use 1MB - 2MB chunks (default)
- **Large files (> 10MB)**: Use 5MB - 10MB chunks

### Behavior Notes

- Lines that exceed the maximum chunk size are skipped with a warning
- Empty chunks are not created
- UTF-8 encoding is used for all file operations

## API Documentation

### CrisisCoreSplitter Class

```python
from src.text_splitter import CrisisCoreSplitter

# Initialize splitter
splitter = CrisisCoreSplitter(
    input_file='data.txt',
    max_chunk_size=1024*1024  # 1MB in bytes
)

# Split the file
num_chunks = splitter.split_file()
print(f"Created {num_chunks} chunks")
```

#### Methods

- `__init__(input_file, max_chunk_size=1024*1024)`: Initialize the splitter
- `split_file()`: Split the input file and return the number of chunks created

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setting Up Development Environment

1. Clone and enter the repository:
```bash
git clone https://github.com/CrisisCore-Systems/text_splitter.git
cd text_splitter
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

Run all tests:
```bash
pytest tests/
```

Run with coverage report:
```bash
pytest tests/ --cov=src --cov-report=term-missing
```

Run specific test file:
```bash
pytest tests/test_splitter.py -v
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure everything works
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## Support

For bugs, questions, and discussions please use the [GitHub Issues](https://github.com/CrisisCore-Systems/text_splitter/issues).

## Authors

- **CrisisCore-Systems** - *Initial work* - [CrisisCore-Systems](https://github.com/CrisisCore-Systems)

## Acknowledgments

- Built with [PySimpleGUI](https://pysimplegui.readthedocs.io/) for the graphical interface
- Tested with [pytest](https://pytest.org/)

---

## Recommended VS Code Extensions

To enhance your development experience, consider installing the following Visual Studio Code extensions:

### Python
- **Python**: Provides rich support for the Python language, including features such as IntelliSense, linting, debugging, and more.
- **Pylance**: Offers performant, feature-rich language support for Python, including type checking and auto-completions.
- **Pytest**: Integrates pytest with Visual Studio Code, allowing you to run and debug tests easily.

### TypeScript
- **TypeScript**: Adds support for TypeScript, including IntelliSense, debugging, and more.
- **ESLint**: Integrates ESLint into Visual Studio Code, providing linting and code quality checks for TypeScript and JavaScript files.
- **Prettier - Code formatter**: Automatically formats your code to ensure consistent style across your project.

### Markdown
- **Markdown All in One**: Provides comprehensive support for Markdown, including preview, shortcuts, and more.
- **Markdownlint**: Offers linting for Markdown files to ensure consistent style and formatting.

### Version Control
- **GitLens**: Enhances the built-in Git capabilities of Visual Studio Code, providing features such as blame annotations, repository insights, and more.

### File Management
- **Path Intellisense**: Autocompletes filenames in your code, making it easier to reference files in your project.

### Utilities
- **Bracket Pair Colorizer**: Adds color to matching brackets, making it easier to navigate complex code.
- **Live Server**: If you are developing web applications, this extension allows you to launch a local development server with live reload.
