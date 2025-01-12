# Documentation for the `src.logger` Module

## Overview

The `src.logger` module provides a flexible logging system that supports console, file, and JSON logging. It utilizes the Singleton design pattern to ensure only a single instance of the logger is used across the application. The logger supports various log levels (e.g., `INFO`, `ERROR`, `DEBUG`) and includes colorized output for console logs. You can also customize the log output formats and control logging to different files.

## Table of Contents
- [Classes](#classes)
    - [SingletonMeta](#singletonmeta)
    - [JsonFormatter](#jsonformatter)
    - [Logger](#logger)
- [Functions](#functions)
    - [`__init__`](#__init__)
    - [`_configure_logger`](#_configure_logger)
    - [`initialize_loggers`](#initialize_loggers)
    - [`log`](#log)
    - [`info`](#info)
    - [`success`](#success)
    - [`warning`](#warning)
    - [`debug`](#debug)
    - [`error`](#error)
    - [`critical`](#critical)
- [Parameters for the Logger](#parameters-for-the-logger)
- [File Logging Configuration (`config`)](#file-logging-configuration-config)
- [Example Usage](#example-usage)
    - [Initializing the Logger](#1-initializing-the-logger)
    - [Logging Messages at Different Levels](#2-logging-messages-at-different-levels)
    - [Customizing Colors](#3-customizing-colors)

---

## Classes

### `SingletonMeta`

**Description**: Metaclass that implements the Singleton design pattern for the logger.

### `JsonFormatter`

**Description**: A custom formatter that outputs logs in JSON format.

### `Logger`

**Description**: The main logger class that supports console, file, and JSON logging.

**Methods**:
- `__init__`: Initializes the Logger instance.
- `_configure_logger`: Configures and returns a logger instance.
- `initialize_loggers`: Initializes the loggers for console and file logging.
- `log`: Logs a message at the specified level.
- `info`: Logs an info message.
- `success`: Logs a success message.
- `warning`: Logs a warning message.
- `debug`: Logs a debug message.
- `error`: Logs an error message.
- `critical`: Logs a critical message.


---

## Functions

### `__init__`

**Description**: Initializes the Logger instance with placeholders for different logger types (console, file, and JSON).

### `_configure_logger`

**Description**: Configures and returns a logger instance.

**Parameters**:
- `name` (str): Name of the logger.
- `log_path` (str): Path to the log file.
- `level` (Optional[int], optional): Logging level, e.g., `logging.DEBUG`. Default is `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Custom formatter (optional).
- `mode` (Optional[str], optional): File mode, e.g., `'a'` for append (default).

**Returns**:
- `logging.Logger`: Configured `logging.Logger` instance.

### `initialize_loggers`

**Description**: Initializes the loggers for console and file logging (info, debug, error, and JSON).

**Parameters**:
- `info_log_path` (Optional[str], optional): Path for info log file (optional).
- `debug_log_path` (Optional[str], optional): Path for debug log file (optional).
- `errors_log_path` (Optional[str], optional): Path for error log file (optional).
- `json_log_path` (Optional[str], optional): Path for JSON log file (optional).

### `log`

**Description**: Logs a message at the specified level (e.g., `INFO`, `DEBUG`, `ERROR`) with optional exception and color formatting.

**Parameters**:
- `level`: Logging level (e.g., `logging.INFO`, `logging.DEBUG`).
- `message` (str): The log message.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception information (default is `False`).
- `color` (Optional[tuple], optional): Tuple with text and background colors for console output (optional).

### `info`

**Description**: Logs an info message.

**Parameters**:
- `message` (str): The info message to log.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception info (default is `False`).
- `colors` (Optional[tuple], optional): Tuple of color values for the message (optional).

### `success`

**Description**: Logs a success message.

**Parameters**:
- `message` (str): The success message to log.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception info (default is `False`).
- `colors` (Optional[tuple], optional): Tuple of color values for the message (optional).

### `warning`

**Description**: Logs a warning message.

**Parameters**:
- `message` (str): The warning message to log.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception info (default is `False`).
- `colors` (Optional[tuple], optional): Tuple of color values for the message (optional).

### `debug`

**Description**: Logs a debug message.

**Parameters**:
- `message` (str): The debug message to log.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception info (default is `True`).
- `colors` (Optional[tuple], optional): Tuple of color values for the message (optional).

### `error`

**Description**: Logs an error message.

**Parameters**:
- `message` (str): The error message to log.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception info (default is `True`).
- `colors` (Optional[tuple], optional): Tuple of color values for the message (optional).

### `critical`

**Description**: Logs a critical message.

**Parameters**:
- `message` (str): The critical message to log.
- `ex` (Optional[Exception], optional): Optional exception to log.
- `exc_info` (bool, optional): Whether to include exception info (default is `True`).
- `colors` (Optional[tuple], optional): Tuple of color values for the message (optional).

---

## Parameters for the Logger

The `Logger` class accepts several optional parameters for customizing the logging behavior.

- **Level**: Controls the severity of logs that are captured. Common levels include:
  - `logging.DEBUG`: Detailed information, useful for diagnosing issues.
  - `logging.INFO`: General information, such as successful operations.
  - `logging.WARNING`: Warnings that do not necessarily require immediate action.
  - `logging.ERROR`: Error messages.
  - `logging.CRITICAL`: Critical errors that require immediate attention.

- **Formatter**: Defines how the log messages are formatted. By default, messages are formatted as `'%(asctime)s - %(levelname)s - %(message)s'`. You can provide a custom formatter for different formats, such as JSON.

- **Color**: Colors for the log messages in the console. The colors are specified as a tuple with two elements:
  - **Text color**: Specifies the text color (e.g., `colorama.Fore.RED`).
  - **Background color**: Specifies the background color (e.g., `colorama.Back.WHITE`).

The color can be customized for different log levels (e.g., green for info, red for errors, etc.).

---

## File Logging Configuration (`config`)

To log messages to a file, you can specify the file paths in the configuration.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

The file paths provided in `config` are used to write logs to the respective files for each log level.

---

## Example Usage

### 1. Initializing the Logger

```python
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

### 2. Logging Messages at Different Levels

```python
logger.info('This is an info message')
logger.success('This is a success message')
logger.warning('This is a warning message')
logger.debug('This is a debug message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

### 3. Customizing Colors

```python
logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

---

This module provides a comprehensive and flexible logging system for Python applications. You can configure console and file logging with different formats and colors, manage logging levels, and handle exceptions gracefully. The configuration for file logging is stored in a `config` dictionary, which allows for easy customization.