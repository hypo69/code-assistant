# Module `src.utils.ftp`

## Overview

This module provides an interface for interacting with FTP servers. It includes functions to send, receive, and delete files from an FTP server.

**Purpose**:
Allows for sending media files (images, videos), spreadsheets, and other files to and from an FTP server.

**Modules**:
- `src.logger.logger`: Local helper utilities for FTP operations.
- `typing`: Type hints for function parameters and return values.
- `ftplib`: Provides FTP protocol client capabilities.
- `pathlib`: For handling file system paths.

## Table of Contents

1.  [Functions](#functions)
    *   [`write`](#write)
    *   [`read`](#read)
    *   [`delete`](#delete)

## Functions

### `write`

**Description**: Sends a file to an FTP server.

**Parameters**:
- `source_file_path` (str): The path of the file to be sent.
- `dest_dir` (str): The destination directory on the FTP server.
- `dest_file_name` (str): The name of the file on the FTP server.

**Returns**:
- `bool`: `True` if the file is successfully sent, `False` otherwise.

**Example**:
```python
>>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
>>> print(success)
True
```

### `read`

**Description**: Retrieves a file from an FTP server.

**Parameters**:
- `source_file_path` (str): The path where the file will be saved locally.
- `dest_dir` (str): The directory on the FTP server where the file is located.
- `dest_file_name` (str): The name of the file on the FTP server.

**Returns**:
- `Union[str, bytes, None]`: The file content if successfully retrieved, `None` otherwise.

**Example**:
```python
>>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
>>> print(content)
b'Some file content'
```

### `delete`

**Description**: Deletes a file from an FTP server.

**Parameters**:
- `source_file_path` (str): The path where the file is located locally (not used).
- `dest_dir` (str): The directory on the FTP server where the file is located.
- `dest_file_name` (str): The name of the file on the FTP server.

**Returns**:
- `bool`: `True` if the file is successfully deleted, `False` otherwise.

**Example**:
```python
>>> success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
>>> print(success)
True
```