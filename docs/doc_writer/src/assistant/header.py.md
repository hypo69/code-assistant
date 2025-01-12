# Module: src.logger.header

## Overview

This module defines the root path to the project. All imports are built relative to this path. It also loads project settings from `settings.json` and the project's documentation from `README.MD`.

## Table of Contents
- [Functions](#functions)
    - [`set_project_root`](#set_project_root)
- [Global Variables](#global-variables)
    - [`__root__`](#__root__)
    - [`settings`](#settings)
    - [`doc_str`](#doc_str)
    - [`__project_name__`](#__project_name__)
    - [`__version__`](#__version__)
    - [`__doc__`](#__doc__)
    - [`__details__`](#__details__)
    - [`__author__`](#__author__)
    - [`__copyright__`](#__copyright__)
    - [`__cofee__`](#__cofee__)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory. It stops at the first directory containing any of the specified marker files.

**Parameters**:
- `marker_files` (tuple): Filenames or directory names used to identify the project root. Defaults to `('__root__', '.git')`.

**Returns**:
- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

## Global Variables

### `__root__`
**Description**: The root directory of the project. This variable is set by the `set_project_root` function.

### `settings`
**Description**: A dictionary containing project settings loaded from `settings.json`. This is `None` if the file cannot be loaded or decoded.

### `doc_str`
**Description**: A string containing project documentation loaded from `README.MD`. This is `None` if the file cannot be loaded or decoded.

### `__project_name__`
**Description**: The name of the project loaded from settings, default is 'hypotez'.

### `__version__`
**Description**: The project version loaded from settings, default is ''.

### `__doc__`
**Description**: The project documentation loaded from `README.MD` as string.

### `__details__`
**Description**: An empty string placeholder for project details.

### `__author__`
**Description**: The author of the project loaded from settings, default is ''.

### `__copyright__`
**Description**: The project copyright information loaded from settings, default is ''.

### `__cofee__`
**Description**:  A message with a link for supporting the developer loaded from settings, default is "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69".