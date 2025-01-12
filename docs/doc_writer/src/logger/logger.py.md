# Module `src.logger.logger`

## Overview

This module provides a comprehensive logging solution using the Singleton pattern. It supports logging to console, multiple files (info, debug, errors), and JSON format. It includes colored output for better readability and detailed exception information.

## Table of Contents

- [Classes](#classes)
    - [`SingletonMeta`](#singletonmeta)
    - [`JsonFormatter`](#jsonformatter)
    - [`Logger`](#logger)
- [Functions](#functions)
    - [`_format_message`](#_format_message)
    - [`_ex_full_info`](#_ex_full_info)
    - [`log`](#log)
    - [`info`](#info)
    - [`success`](#success)
    - [`warning`](#warning)
    - [`debug`](#debug)
    - [`error`](#error)
    - [`critical`](#critical)

## Classes

### `SingletonMeta`

**Description**: Metaclass for implementing the Singleton pattern.

**Methods**:

- `__call__(cls, *args, **kwargs)`: Creates or returns a single instance of the class.

### `JsonFormatter`

**Description**: Custom formatter for logging in JSON format.

**Methods**:

- `format(self, record)`: Formats the log record as JSON.

### `Logger`

**Description**: Logger class implementing the Singleton pattern with console, file, and JSON logging.

**Attributes**:

- `log_files_path` (Path): The path to the directory where log files are stored.
- `info_log_path` (Path): The path to the info log file.
- `debug_log_path` (Path): The path to the debug log file.
- `errors_log_path` (Path): The path to the errors log file.
- `json_log_path` (Path): The path to the JSON log file.

**Methods**:

- `__init__(self, info_log_path: Optional[str] = None, debug_log_path: Optional[str] = None, errors_log_path: Optional[str] = None, json_log_path: Optional[str] = None)`:
  - **Description**: Initializes the logger with the specified log file paths.
  - **Parameters**:
    - `info_log_path` (Optional[str], optional): Path to the info log file. Defaults to `None`.
    - `debug_log_path` (Optional[str], optional): Path to the debug log file. Defaults to `None`.
    - `errors_log_path` (Optional[str], optional): Path to the errors log file. Defaults to `None`.
    - `json_log_path` (Optional[str], optional): Path to the JSON log file. Defaults to `None`.

## Functions

### `_format_message`

**Description**: Returns formatted message with optional color and exception information.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `color` (Optional[Tuple[str, str]], optional): Tuple with text and background color names. Defaults to `None`.

**Returns**:
- `str`: The formatted log message.

### `_ex_full_info`

**Description**: Returns full exception information along with the previous function, file, and line details.

**Parameters**:
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.

**Returns**:
- `str`: The formatted exception information.

### `log`

**Description**: General method to log messages at specified level with optional color.

**Parameters**:
- `level` (int): The logging level.
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `False`.
- `color` (Optional[Tuple[str, str]], optional): Tuple with text and background color names. Defaults to `None`.

**Returns**:
- `None`

### `info`

**Description**: Logs an info message with optional text and background colors.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `False`.
- `text_color` (str, optional): Text color name. Defaults to "green".
- `bg_color` (str, optional): Background color name. Defaults to "".

**Returns**:
- `None`

### `success`

**Description**: Logs a success message with optional text and background colors.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `False`.
- `text_color` (str, optional): Text color name. Defaults to "yellow".
- `bg_color` (str, optional): Background color name. Defaults to "".

**Returns**:
- `None`

### `warning`

**Description**: Logs a warning message with optional text and background colors.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `False`.
- `text_color` (str, optional): Text color name. Defaults to "black".
- `bg_color` (str, optional): Background color name. Defaults to "yellow".

**Returns**:
- `None`

### `debug`

**Description**: Logs a debug message with optional text and background colors.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `True`.
- `text_color` (str, optional): Text color name. Defaults to "cyan".
- `bg_color` (str, optional): Background color name. Defaults to "".

**Returns**:
- `None`

### `error`

**Description**: Logs an error message with optional text and background colors.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `True`.
- `text_color` (str, optional): Text color name. Defaults to "red".
- `bg_color` (str, optional): Background color name. Defaults to "".

**Returns**:
- `None`

### `critical`

**Description**: Logs a critical message with optional text and background colors.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[str], optional): The exception message. Defaults to `None`.
- `exc_info` (bool, optional): Flag to include exception info. Defaults to `True`.
- `text_color` (str, optional): Text color name. Defaults to "red".
- `bg_color` (str, optional): Background color name. Defaults to "white".

**Returns**:
- `None`