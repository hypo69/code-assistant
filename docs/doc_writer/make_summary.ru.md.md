# Module `make_summary.py`

## Overview

This module is designed for automatically creating a `SUMMARY.md` file, which is used for compiling documentation with tools like `mdbook`. The module recursively traverses the specified directory with source `.md` files and generates a table of contents, including or excluding files depending on the specified language.

## Table of Contents

- [Overview](#overview)
- [Main Features](#main-features)
- [Installation and Usage](#installation-and-usage)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
- [Example Output](#example-output)
- [Author](#author)
- [License](#license)

## Main Features

- **`SUMMARY.md` Generation**:
    - Recursively traverses the directory with source `.md` files.
    - Creates a `SUMMARY.md` file with a table of contents for each `.md` file.

- **Language Filtering**:
    - Supports filtering files by language:
        - `ru`: Includes only files with the `.ru.md` suffix.
        - `en`: Excludes files with the `.ru.md` suffix.

- **Universality**:
    - All paths are built relative to the project root, making the module resistant to changes in directory structure.

## Installation and Usage

### Requirements

- Python 3.8 or higher.
- Installed dependencies from the `requirements.txt` file.

### Installation

1. Make sure you have Python and all the dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the `make_summary.py` script, specifying the `src` directory and the filtering language:
   ```bash
   python src/endpoints/hypo69/code_assistant/make_summary.py -lang ru src
   ```
    - The `-lang` parameter can take `ru` or `en` values.
    - The `src` argument specifies the directory containing the source `.md` files.

2. After the script execution, the `SUMMARY.md` file will be created in the `docs` directory.

## Example Output

### Example `SUMMARY.md` for language `ru`:
```
# Summary

- [file1](file1.md)
- [file2](file2.ru.md)
```

### Example `SUMMARY.md` for language `en`:
```
# Summary

- [file1](file1.md)
- [file3](file3.en.md)
```

## Author

- **Author Name**: [Your Name]
- **Email**: [Your Email]
- **Boosty Link**: [https://boosty.to/hypo69](https://boosty.to/hypo69)

## License

This module is licensed under the [MIT License](../../../LICENSE).