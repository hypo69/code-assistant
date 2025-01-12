# Module: src.utils.file

## Overview

This module provides a set of utility functions for performing various file operations such as saving, reading, listing, and processing files and directories. It supports reading and writing text files, searching files by patterns, and handling BOM (Byte Order Mark) in UTF-8 encoded files.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
  - [`save_text_file`](#save_text_file)
  - [`read_text_file`](#read_text_file)
  - [`get_filenames`](#get_filenames)
  - [`recursively_yield_file_path`](#recursively_yield_file_path)
  - [`recursively_get_file_path`](#recursively_get_file_path)
  - [`recursively_read_text_files`](#recursively_read_text_files)
  - [`get_directory_names`](#get_directory_names)
  - [`read_files_content`](#read_files_content)
  - [`remove_bom`](#remove_bom)
  - [`traverse_and_clean`](#traverse_and_clean)
  - [`main`](#main)

## Functions

### `save_text_file`

**Description**: Saves data to a text file. The data can be a string, list of strings, or a dictionary.

**Parameters**:
- `data` (str | list[str] | dict): Data to write to the file. Can be a string, list of strings, or a dictionary.
- `file_path` (str | Path): Path where the file will be saved.
- `mode` (str, optional): Write mode (`'w'` for write, `'a'` for append). Defaults to `'w'`.
- `exc_info` (bool, optional): If `True`, logs traceback on error. Defaults to `True`.

**Returns**:
- `bool`: `True` if the file was successfully saved, `False` otherwise.

**Raises**:
- `Exception`: If an error occurs while saving the file, it will be logged and `False` will be returned.

### `read_text_file`

**Description**: Reads the contents of a file or files from a directory.

**Parameters**:
- `file_path` (str | Path): Path to the file or directory.
- `as_list` (bool, optional): If `True`, returns the file content as a list of lines. Defaults to `False`.
- `extensions` (list[str], optional): List of file extensions to include when reading a directory. Defaults to `None`.
- `exc_info` (bool, optional): If `True`, logs traceback on error. Defaults to `True`.

**Returns**:
- `str | list[str] | None`: File content as a string or list of lines, or `None` if an error occurs.

**Raises**:
- `Exception`: If an error occurs while reading the file, it will be logged and `None` will be returned.

### `get_filenames`

**Description**: Gets filenames in a directory, optionally filtered by file extensions.

**Parameters**:
- `directory` (str | Path): Directory to search.
- `extensions` (str | list[str], optional): File extensions to filter. Defaults to `'*'`.
- `exc_info` (bool, optional): If `True`, logs traceback on error. Defaults to `True`.

**Returns**:
- `list[str]`: List of filenames found in the directory.

**Raises**:
- `Exception`: If an error occurs while listing the files, it will be logged, and an empty list will be returned.

### `recursively_yield_file_path`

**Description**: Recursively yields file paths matching given patterns.

**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str], optional): Patterns to filter files. Defaults to `'*'`.
- `exc_info` (bool, optional): If `True`, logs traceback on error. Defaults to `True`.

**Yields**:
- `Path`: File paths matching the patterns.

**Raises**:
- `Exception`: If an error occurs during file search, it will be logged.

### `recursively_get_file_path`

**Description**: Recursively gets file paths matching given patterns.

**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str], optional): Patterns to filter files. Defaults to `'*'`.
- `exc_info` (bool, optional): If `True`, logs traceback on error. Defaults to `True`.

**Returns**:
- `list[Path]`: List of file paths matching the patterns.

**Raises**:
- `Exception`: If an error occurs during file search, it will be logged and an empty list will be returned.

### `recursively_read_text_files`

**Description**: Recursively reads text files from a specified root directory that match given patterns.

**Parameters**:
- `root_dir` (str | Path): Path to the root directory for the search.
- `patterns` (str | list[str]): Filename pattern(s) to filter the files. Can be a single pattern (e.g., `'*.txt'`) or a list of patterns.
- `as_list` (bool, optional): If `True`, returns the file content as a list of lines. Defaults to `False`.
- `exc_info` (bool, optional): If `True`, includes exception information in warnings. Defaults to `True`.

**Returns**:
- `list[str]`: List of file contents (or lines if `as_list=True`) that match the specified patterns.

**Raises**:
- `Exception`: If an error occurs while reading a file, it will be logged.

### `get_directory_names`

**Description**: Retrieves all directory names from the specified directory.

**Parameters**:
- `directory` (str | Path): Path to the directory from which directory names should be retrieved.
- `exc_info` (bool, optional): If `True`, logs traceback information in case of an error. Defaults to `True`.

**Returns**:
- `list[str]`: List of directory names found in the specified directory.

**Raises**:
- `Exception`: If an error occurs while retrieving the directory names, it will be logged and `None` will be returned.

### `read_files_content`

**Description**: Reads the contents of files that match given patterns.

**Parameters**:
- `root_dir` (str | Path): Root directory to search.
- `patterns` (str | list[str]): File patterns to match.
- `as_list` (bool, optional): Return content as list of lines. Defaults to `False`.
- `exc_info` (bool, optional): If `True`, logs traceback on error. Defaults to `True`.

**Returns**:
- `list[str]`: List of file contents.

### `remove_bom`

**Description**: Removes the BOM (Byte Order Mark) from a text file.

**Parameters**:
- `file_path` (str | Path): Path to the file to be processed.

**Returns**:
- `None`

**Raises**:
- `Exception`: If an error occurs while removing the BOM, it will be logged.

### `traverse_and_clean`

**Description**: Traverses a directory and removes BOM from all Python files.

**Parameters**:
- `directory` (str | Path): Root directory to process.

**Returns**:
- `None`

**Raises**:
- `Exception`: If an error occurs while traversing or cleaning, it will be logged.

### `main`

**Description**: Entry point for BOM removal in Python files.

**Parameters**:
- `None`

**Returns**:
- `None`
```
```
{'Original code': '```## \\file /src/utils/file.py\n# -*- coding: utf-8 -*-\n\n#! venv/bin/python/python3.12\n\n"""\n.. module:: src.utils \n\t:platform: Windows, Unix\n\t:synopsis:  Module for file operations\n\n"""\n\n\n\nimport os\nimport json\nimport fnmatch\nfrom pathlib import Path\nfrom typing import List, Optional, Union, Generator\nfrom src.logger.logger import logger\n\n\ndef save_text_file(\n    data: str | list[str] | dict,\n    file_path: Union[str, Path],\n    mode: str = "w",\n    exc_info: bool = True,\n) -> bool:\n    """\n    Save data to a text file.\n\n    Args:\n        data (str | list[str] | dict): Data to write (can be string, list of strings, or dictionary).\n        file_path (str | Path): Path where the file will be saved.\n        mode (str, optional): Write mode (`w` for write, `a` for append). Defaults to \'w\'.\n        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.\n\n    Returns:\n        bool: True if the file was successfully saved, False otherwise.\n    """\n    try:\n        file_path = Path(file_path)\n        file_path.parent.mkdir(parents=True, exist_ok=True)\n\n        with file_path.open(mode, encoding="utf-8") as file:\n            if isinstance(data, list):\n                file.writelines(f"{line}\\n" for line in data)\n            elif isinstance(data, dict):\n                json.dump(data, file, ensure_ascii=False, indent=4)\n            else:\n                file.write(data)\n        return True\n    except Exception as ex:\n        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)\n        return False\n\ndef read_text_file(\n    file_path: Union[str, Path],\n    as_list: bool = False,\n    extensions: Optional[list[str]] = None,\n    exc_info: bool = True,\n) -> Union[str, list[str], None]:\n    """\n    Read the contents of a file.\n\n    Args:\n        file_path (str | Path): Path to the file or directory.\n        as_list (bool, optional): If True, returns content as list of lines. Defaults to False.\n        extensions (list[str], optional): List of file extensions to include if reading a directory. Defaults to None.\n        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.\n\n    Returns:\n        str | list[str] | None: File content as a string or list of lines, or None if an error occurs.\n    """\n    try:\n        path = Path(file_path)\n        if path.is_file():\n            with path.open("r", encoding="utf-8") as f:\n                return f.readlines() if as_list else f.read()\n        elif path.is_dir():\n            files = [\n                p for p in path.rglob("*") if p.is_file() and (not extensions or p.suffix in extensions)\n            ]\n            contents = [read_text_file(p, as_list) for p in files]\n            return [item for sublist in contents if sublist for item in sublist] if as_list else "\\n".join(filter(None, contents))\n        else:\n            logger.warning(f"Path \'{file_path}\' is invalid.")\n            return None\n    except Exception as ex:\n        logger.error(f"Failed to read file {file_path}.", ex, exc_info=exc_info)\n        return None\n\ndef get_filenames(\n    directory: Union[str, Path], extensions: Union[str, list[str]] = "*", exc_info: bool = True\n) -> list[str]:\n    """\n    Get filenames in a directory optionally filtered by extension.\n\n    Args:\n        directory (str | Path): Directory to search.\n        extensions (str | list[str], optional): Extensions to filter. Defaults to \'*\'.\n\n    Returns:\n        list[str]: Filenames found in the directory.\n    """\n    try:\n        path = Path(directory)\n        if isinstance(extensions, str):\n            extensions = [extensions] if extensions != "*" else []\n        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]\n\n        return [\n            file.name\n            for file in path.iterdir()\n            if file.is_file() and (not extensions or file.suffix in extensions)\n        ]\n    except Exception as ex:\n        logger.warning(f"Failed to list filenames in \'{directory}\'.", ex, exc_info=exc_info)\n        return []\n\ndef recursively_yield_file_path(\n    root_dir: Union[str, Path], patterns: Union[str, list[str]] = "*", exc_info: bool = True\n) -> Generator[Path, None, None]:\n    """\n    Recursively yield file paths matching given patterns.\n\n    Args:\n        root_dir (str | Path): Root directory to search.\n        patterns (str | list[str]): Patterns to filter files.\n\n    Yields:\n        Path: File paths matching the patterns.\n    """\n    try:\n        patterns = [patterns] if isinstance(patterns, str) else patterns\n        for pattern in patterns:\n            yield from Path(root_dir).rglob(pattern)\n    except Exception as ex:\n        logger.error(f"Failed to search files in \'{root_dir}\'.", ex, exc_info=exc_info)\n\ndef recursively_get_file_path(\n    root_dir: Union[str, Path], \n    patterns: Union[str, list[str]] = "*", \n    exc_info: bool = True\n) -> list[Path]:\n    """\n    Recursively get file paths matching given patterns.\n\n    Args:\n        root_dir (str | Path): Root directory to search.\n        patterns (str | list[str]): Patterns to filter files.\n\n    Returns:\n        list[Path]: List of file paths matching the patterns.\n    """\n    try:\n        file_paths = []\n        patterns = [patterns] if isinstance(patterns, str) else patterns\n        for pattern in patterns:\n            file_paths.extend(Path(root_dir).rglob(pattern))\n        return file_paths\n    except Exception as ex:\n        logger.error(f"Failed to search files in \'{root_dir}\'.", ex, exc_info=exc_info)\n        return []\n\ndef recursively_read_text_files(\n    root_dir: str | Path, \n    patterns: str | list[str], \n    as_list: bool = False, \n    exc_info: bool = True\n) -> list[str]:\n    """\n    Recursively reads text files from the specified root directory that match the given patterns.\n\n    Args:\n        root_dir (str | Path): Path to the root directory for the search.\n        patterns (str | list[str]): Filename pattern(s) to filter the files.\n                                    Can be a single pattern (e.g., \'*.txt\') or a list of patterns.\n        as_list (bool, optional): If True, returns the file content as a list of lines.\n                                  Defaults to False.\n        exc_info (bool, optional): If True, includes exception information in warnings. Defaults to True.\n\n    Returns:\n        list[str]: List of file contents (or lines if `as_list=True`) that match the specified patterns.\n\n    Example:\n        >>> contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)\n        >>> for line in contents:\n        ...     print(line)\n        This will print each line from all matched text files in the specified directory.\n    """\n    matches = []\n    root_path = Path(root_dir)\n\n    # Check if the root directory exists\n    if not root_path.is_dir():\n        logger.debug(f"The root directory \'{root_path}\' does not exist or is not a directory.")\n        return []\n\n    print(f"Searching in directory: {root_path}")\n\n    # Normalize patterns to a list if it\'s a single string\n    if isinstance(patterns, str):\n        patterns = [patterns]\n\n    for root, dirs, files in os.walk(root_path):\n        for filename in files:\n            # Check if the filename matches any of the specified patterns\n            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):\n                file_path = Path(root) / filename\n\n                try:\n                    with file_path.open("r", encoding="utf-8") as file:\n                        if as_list:\n                            # Read lines if `as_list=True`\n                            matches.extend(file.readlines())\n                        else:\n                            # Read entire content otherwise\n                            matches.append(file.read())\n                except Exception as ex:\n                    logger.warning(f"Failed to read file \'{file_path}\'.", exc_info=exc_info)\n\n    return matches\n\ndef get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:\n    """\n    Retrieves all directory names from the specified directory.\n\n    Args:\n        directory (str | Path): Path to the directory from which directory names should be retrieved.\n        exc_info (bool, optional): If True, logs traceback information in case of an error. Defaults to True.\n\n    Returns:\n        list[str]: List of directory names found in the specified directory.\n\n    Example:\n        >>> directories: list[str] = get_directory_names(directory=".") \n        >>> print(directories)\n        [\'dir1\', \'dir2\']\n    \n    More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names\n    """\n    try:\n        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]\n    except Exception as ex:\n        if exc_info:\n            logger.warning(\n                f"Failed to get directory names from \'{directory}\'.",\n                ex,\n                exc_info=exc_info,\n            )\n        return \n\ndef read_files_content(\n    root_dir: Union[str, Path],\n    patterns: Union[str, list[str]],\n    as_list: bool = False,\n    exc_info: bool = True,\n) -> list[str]:\n    """\n    Read contents of files matching patterns.\n\n    Args:\n        root_dir (str | Path): Root directory to search.\n        patterns (str | list[str]): File patterns to match.\n        as_list (bool, optional): Return content as list of lines. Defaults to False.\n\n    Returns:\n        list[str]: List of file contents.\n    """\n    content = []\n    for file_path in recursively_get_files(root_dir, patterns, exc_info):\n        file_content = read_text_file(file_path, as_list, exc_info=exc_info)\n        if file_content:\n            content.extend(file_content if as_list else [file_content])\n    return content\n\ndef remove_bom(file_path: Union[str, Path]) -> None:\n    """\n    Remove BOM from a text file.\n\n    Args:\n        file_path (str | Path): File to process.\n    """\n    path = Path(file_path)\n    try:\n        with path.open("r+", encoding="utf-8") as file:\n            content = file.read().replace("\\ufeff", "")\n            file.seek(0)\n            file.write(content)\n            file.truncate()\n    except Exception as ex:\n        logger.error(f"Failed to remove BOM from \'{file_path}\'.", ex)\n\ndef traverse_and_clean(directory: Union[str, Path]) -> None:\n    """\n    Traverse directory and remove BOM from Python files.\n\n    Args:\n        directory (str | Path): Root directory to process.\n    """\n    for file in recursively_get_files(directory, "*.py"):\n        remove_bom(file)\n\n\ndef main() -> None:\n    """Entry point for BOM removal in Python files."""\n    root_dir = Path("..", "src")\n    logger.info(f"Starting BOM removal in {root_dir}")\n    traverse_and_clean(root_dir)\n\n\nif __name__ == "__main__":\n    main()\n```', 'Improved code': '```python\n## \\file /src/utils/file.py\n# -*- coding: utf-8 -*-\n\n#! venv/bin/python/python3.12\n\n"""\n.. module:: src.utils \n\t:platform: Windows, Unix\n\t:synopsis:  Module for file operations\n\n"""\n\nimport os\nimport json\nimport fnmatch\nfrom pathlib import Path\nfrom typing import List, Optional, Generator\n\nfrom src.logger.logger import logger\n\n\ndef save_text_file(\n    data: str | list[str] | dict,\n    file_path: str | Path,\n    mode: str = \'w\',\n    exc_info: bool = True,\n) -> bool:\n    """\n    Saves data to a text file.\n\n    :param data: Data to write (can be string, list of strings, or dictionary).\n    :type data: str | list[str] | dict\n    :param file_path: Path where the file will be saved.\n    :type file_path: str | Path\n    :param mode: Write mode (\'w\' for write, \'a\' for append). Defaults to \'w\'.\n    :type mode: str, optional\n    :param exc_info: If True, logs traceback on error. Defaults to True.\n    :type exc_info: bool, optional\n\n    :returns: True if the file was successfully saved, False otherwise.\n    :rtype: bool\n    """\n    try:\n        file_path = Path(file_path)\n        # Ensure the parent directory exists.\n        file_path.parent.mkdir(parents = True, exist_ok = True)\n\n        with file_path.open(mode, encoding = \'utf-8\') as file:\n            if isinstance(data, list):\n                # Write each line from the list to the file.\n                file.writelines(f\'{line}\\n\' for line in data)\n            elif isinstance(data, dict):\n                # Write dictionary to the file as json.\n                json.dump(data, file, ensure_ascii = False, indent = 4)\n            else:\n                # Write the string data to the file.\n                file.write(data)\n        return True\n    except Exception as ex:\n        logger.error(f\'Failed to save file {file_path}.\', ex, exc_info = exc_info)\n        return False\n\n\ndef read_text_file(\n    file_path: str | Path,\n    as_list: bool = False,\n    extensions: Optional[list[str]] = None,\n    exc_info: bool = True,\n) -> str | list[str] | None:\n    """\n    Reads the contents of a file.\n\n    :param file_path: Path to the file or directory.\n    :type file_path: str | Path\n    :param as_list: If True, returns content as list of lines. Defaults to False.\n    :type as_list: bool, optional\n    :param extensions: List of file extensions to include if reading a directory. Defaults to None.\n    :type extensions: Optional[list[str]], optional\n    :param exc_info: If True, logs traceback on error. Defaults to True.\n    :type exc_info: bool, optional\n\n    :returns: File content as a string or list of lines, or None if an error occurs.\n    :rtype: str | list[str] | None\n    """\n    try:\n        path = Path(file_path)\n        if path.is_file():\n            # Read the file if it is a file path.\n            with path.open(\'r\', encoding = \'utf-8\') as f:\n                return f.readlines() if as_list else f.read()\n        elif path.is_dir():\n            # Collect all files from the directory with the given extensions.\n            files = [\n                p for p in path.rglob(\'*\') if p.is_file() and (not extensions or p.suffix in extensions)\n            ]\n            # Read the contents of the files\n            contents = [read_text_file(p, as_list) for p in files]\n            # Return as list or string.\n            return [item for sublist in contents if sublist for item in sublist] if as_list else \'\\n\'.join(filter(None, contents))\n        else:\n            logger.warning(f\'Path \'{file_path}\' is invalid.\')\n            return None\n    except Exception as ex:\n        logger.error(f\'Failed to read file {file_path}.\', ex, exc_info = exc_info)\n        return None\n\n\ndef get_filenames(\n    directory: str | Path,\n    extensions: str | list[str] = \'*\',\n    exc_info: bool = True,\n) -> list[str]:\n    """\n    Gets filenames in a directory optionally filtered by extension.\n\n    :param directory: Directory to search.\n    :type directory: str | Path\n    :param extensions: Extensions to filter. Defaults to \'*\'.\n    :type extensions: str | list[str], optional\n    :param exc_info: If True, logs traceback on error. Defaults to True.\n    :type exc_info: bool, optional\n\n    :returns: Filenames found in the directory.\n    :rtype: list[str]\n    """\n    try:\n        path = Path(directory)\n        if isinstance(extensions, str):\n            # Convert string extension to list of extension.\n            extensions = [extensions] if extensions != \'*\' else []\n        # Normalize extensions with a dot.\n        extensions = [ext if ext.startswith(\'.\') else f\'.{ext}\' for ext in extensions]\n        # Get list of files.\n        return [\n            file.name\n            for file in path.iterdir()\n            if file.is_file() and (not extensions or file.suffix in extensions)\n        ]\n    except Exception as ex:\n        logger.warning(f\'Failed to list filenames in \'{directory}\'.\', ex, exc_info = exc_info)\n        return []\n\n\ndef recursively_yield_file_path(\n    root_dir: str | Path,\n    patterns: str | list[str] = \'*\',\n    exc_info: bool = True,\n) -> Generator[Path, None, None]:\n    """\n    Recursively yields file paths matching given patterns.\n\n    :param root_dir: Root directory to search.\n    :type root_dir: str | Path\n    :param patterns: Patterns to filter files.\n    :type patterns: str | list[str], optional\n    :param exc_info: If True, logs traceback on error. Defaults to True.\n    :type exc_info: bool, optional\n\n    :yields: File paths matching the patterns.\n    :rtype: Generator[Path, None, None]\n    """\n    try:\n        patterns = [patterns] if isinstance(patterns, str) else patterns\n        for pattern in patterns:\n            # Yield files recursively that match the given pattern.\n            yield from Path(root_dir).rglob(pattern)\n    except Exception as ex:\n        logger.error(f\'Failed to search files in \'{root_dir}\'.\', ex, exc_info = exc_info)\n\n\ndef recursively_get_file_path(\n    root_dir: str | Path,\n    patterns: str | list[str] = \'*\',\n    exc_info: bool = True,\n) -> list[Path]:\n    """\n    Recursively gets file paths matching given patterns.\n\n    :param root_dir: Root directory to search.\n    :type root_dir: str | Path\n    :param patterns: Patterns to filter files.\n    :type patterns: str | list[str], optional\n    :param exc_info: If True, logs traceback on error. Defaults to True.\n    :type exc_info: bool, optional\n\n    :returns: List of file paths matching the patterns.\n    :rtype: list[Path]\n    """\n    try:\n        file_paths = []\n        patterns = [patterns] if isinstance(patterns, str) else patterns\n        for pattern in patterns:\n            # Extend list with files that match the given patterns.\n            file_paths.extend(Path(root_dir).rglob(pattern))\n        return file_paths\n    except Exception as ex:\n        logger.error(f\'Failed to search files in \'{root_dir}\'.\', ex, exc_info = exc_info)\n        return []\n\n\ndef recursively_read_text_files(\n    root_dir: str | Path,\n    patterns: str | list[str],\n    as_list: bool = False,\n    exc_info: bool = True,\n) -> list[str]:\n    """\n    Recursively reads text files from the specified root directory that match the given patterns.\n\n    :param root_dir: Path to the root directory for the search.\n    :type root_dir: str | Path\n    :param patterns: Filename pattern(s) to filter the files. Can be a single pattern (e.g., \'*.txt\') or a list of patterns.\n    :type patterns: str | list[str]\n    :param as_list: If True, returns the file content as a list of lines. Defaults to False.\n    :type as_list: bool, optional\n    :param exc_info: If True, includes exception information in warnings. Defaults to True.\n    :type exc_info: bool, optional\n\n    :returns: List of file contents (or lines if `as_list=True`) that match the specified patterns.\n    :rtype: list[str]\n\n    :Example:\n        >>> contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)\n        >>> for line in contents:\n        ...     print(line)\n        This will print each line from all matched text files in the specified directory.\n    """\n    matches = []\n    root_path = Path(root_dir)\n\n    # Check if the root directory exists\n    if not root_path.is_dir():\n        logger.debug(f\'The root directory \'{root_path}\' does not exist or is not a directory.\')\n        return []\n\n    print(f\'Searching in directory: {root_path}\')\n\n    # Normalize patterns to a list if it\'s a single string\n    if isinstance(patterns, str):\n        patterns = [patterns]\n\n    for root, dirs, files in os.walk(root_path):\n        for filename in files:\n            # Check if the filename matches any of the specified patterns\n            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):\n                file_path = Path(root) / filename\n\n                try:\n                    with file_path.open(\'r\', encoding = \'utf-8\') as file:\n                        if as_list:\n                            # Read lines if `as_list=True`\n                            matches.extend(file.readlines())\n                        else:\n                            # Read entire content otherwise\n                            matches.append(file.read())\n                except Exception as ex:\n                    logger.warning(f\'Failed to read file \'{file_path}\'.\', exc_info = exc_info)\n\n    return matches\n\n\ndef get_directory_names(\n    directory: str | Path,\n    exc_info: bool = True,\n) -> list[str]:\n    """\n    Retrieves all directory names from the specified directory.\n\n    :param directory: Path to the directory from which directory names should be retrieved.\n    :type directory: str | Path\n    :param exc_info: If True, logs traceback information in case of an error. Defaults to True.\n    :type exc_info: bool, optional\n\n    :returns: List of directory names found in the specified directory.\n    :rtype: list[str]\n\n    :Example:\n        >>> directories: list[str] = get_directory_names(directory=".") \n        >>> print(directories)\n        [\'dir1\', \'dir2\']\n    \n    More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names\n    """\n    try:\n        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]\n    except Exception as ex:\n        if exc_info:\n            logger.warning(\n                f\'Failed to get directory names from \'{directory}\'.\',\n                ex,\n                exc_info = exc_info,\n            )\n        return\n\n\ndef read_files_content(\n    root_dir: str | Path,\n    patterns: str | list[str],\n    as_list: bool = False,\n    exc_info: bool = True,\n) -> list[str]:\n    """\n    Reads contents of files matching patterns.\n\n    :param root_dir: Root directory to search.\n    :type root_dir: str | Path\n    :param patterns: File patterns to match.\n    :type patterns: str | list[str]\n    :param as_list: Return content as list of lines. Defaults to False.\n    :type as_list: bool, optional\n    :param exc_info: If True, logs traceback on error. Defaults to True.\n    :type exc_