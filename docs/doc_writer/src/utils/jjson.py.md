# Module Name

## Overview

This module provides utility functions for reading, writing, and manipulating JSON and CSV data. It includes functionalities for handling different input types (files, strings, objects), merging data, and converting data structures. The module also includes functions for loading and dumping JSON data, parsing JSON strings, and converting JSON data to SimpleNamespace objects. It incorporates logging for error handling and uses `json_repair` to correct malformed JSON data.

## Table of Contents
1. [Functions](#functions)
    - [`_convert_to_dict`](#_convert_to_dict)
    - [`_read_existing_data`](#_read_existing_data)
    - [`_merge_data`](#_merge_data)
    - [`j_dumps`](#j_dumps)
    - [`_decode_strings`](#_decode_strings)
    - [`_string_to_dict`](#_string_to_dict)
    - [`j_loads`](#j_loads)
    - [`j_loads_ns`](#j_loads_ns)
2. [Constants](#constants)
   - [`MODE_WRITE`](#MODE_WRITE)
   - [`MODE_APPEND_START`](#MODE_APPEND_START)
   - [`MODE_APPEND_END`](#MODE_APPEND_END)

## Constants
### `MODE_WRITE`
**Description**: Constant for write mode in file operations.

### `MODE_APPEND_START`
**Description**: Constant for append mode (start) in file operations.

### `MODE_APPEND_END`
**Description**: Constant for append mode (end) in file operations.

## Functions

### `_convert_to_dict`

**Description**: Converts SimpleNamespace and lists to dictionaries. This is a recursive function that ensures all nested structures of SimpleNamespace and list are properly converted to dictionaries.

**Parameters**:
- `value` (Any): The value to be converted, which can be a SimpleNamespace, a dictionary, a list, or any other type.

**Returns**:
- `Any`: The converted value, which is a dictionary if the input `value` is a SimpleNamespace, a list if it's a list, a dict if it's a dict, otherwise the original value.

### `_read_existing_data`

**Description**: Reads existing JSON data from a file.

**Parameters**:
- `path` (Path): The path to the file.
- `exc_info` (bool, optional): If True, includes exception info in log. Defaults to True.

**Returns**:
- `dict`: The JSON data as a dictionary, or an empty dictionary if there's an error during file reading or JSON parsing.

**Raises**:
- `json.JSONDecodeError`: If the specified JSON data is not valid.
- `Exception`: If any exception occurs while reading the data.

### `_merge_data`

**Description**: Merges new data with existing data based on the specified mode.

**Parameters**:
- `data` (Dict): The new data to be merged.
- `existing_data` (Dict): The existing data to merge with.
- `mode` (str): The merge mode, which can be `MODE_APPEND_START`, `MODE_APPEND_END`.

**Returns**:
- `Dict`: The merged data as a dictionary. If an error occurs during merging, an empty dict is returned.

**Raises**:
- `Exception`: If an error occurs during merging.

### `j_dumps`

**Description**: Dumps JSON data to a file or returns the JSON data as a dictionary. Handles SimpleNamespace objects and lists of dicts/SimpleNamespaces. It provides options for encoding, file open modes, and exception logging.

**Parameters**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.
- `file_path` (Optional[Path], optional): Path to the output file. If None, returns JSON as a dictionary. Defaults to None.
- `ensure_ascii` (bool, optional): If True, escapes non-ASCII characters in output. Defaults to True.
- `mode` (str, optional): File open mode ('w', 'a+', '+a'). Defaults to 'w'.
- `exc_info` (bool, optional): If True, logs exceptions with traceback. Defaults to True.

**Returns**:
- `Optional[Dict]`: JSON data as a dictionary if successful or None if an error occurs.

**Raises**:
- `ValueError`: If the file mode is unsupported.

### `_decode_strings`

**Description**: Recursively decodes strings in a data structure. It uses `codecs.decode` with `'unicode_escape'` to convert escaped unicode characters.

**Parameters**:
- `data` (Any): The data structure to decode. It can be a string, a list, a dictionary, or any other type.

**Returns**:
- `Any`: The decoded data structure, with all strings decoded.

### `_string_to_dict`

**Description**: Removes markdown quotes from the input string and parses it as JSON. This function handles both basic JSON strings and those wrapped in markdown code blocks, stripping the backticks before parsing.

**Parameters**:
- `json_string` (str): The JSON string, possibly wrapped in markdown code blocks.

**Returns**:
- `dict`: The parsed JSON data as a dictionary. Returns an empty dictionary if the JSON string cannot be parsed.

**Raises**:
- `json.JSONDecodeError`: If the JSON data cannot be parsed.

### `j_loads`

**Description**: Loads JSON or CSV data from a file, directory, string, or object. This function supports loading data from different sources, including file paths, directories, JSON strings, and JSON objects. It handles CSV files by converting them to a list of dictionaries.

**Parameters**:
- `jjson` (dict | SimpleNamespace | str | Path | list): Path to file/directory, JSON string, or JSON object.
- `ordered` (bool, optional): Use OrderedDict to preserve element order. Defaults to True.

**Returns**:
- `dict | list`: Processed data (dictionary or list of dictionaries).

**Raises**:
- `FileNotFoundError`: If the specified file is not found.
- `json.JSONDecodeError`: If the JSON data cannot be parsed.

### `j_loads_ns`

**Description**: Loads JSON/CSV data using `j_loads` and converts the data to SimpleNamespace objects. This function acts as a wrapper around the `j_loads` function, providing an easy way to convert the loaded data into a namespace object or a list of such objects.

**Parameters**:
- `jjson` (Path | SimpleNamespace | Dict | str): Path to file/directory, JSON string or JSON object.
- `ordered` (bool, optional): Use OrderedDict to preserve element order. Defaults to True.

**Returns**:
- `SimpleNamespace | List[SimpleNamespace] | Dict`: Processed data as SimpleNamespace object or list of SimpleNamespace objects or dictionary in case of error.