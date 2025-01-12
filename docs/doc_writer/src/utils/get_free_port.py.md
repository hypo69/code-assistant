# Module `src.utils.get_free_port`

## Overview

This module provides functionality to find a free port on a specified host. It supports searching within a given port range or finding the first available port if no range is specified.

## Table of Contents

- [Functions](#functions)
    - [`get_free_port`](#get_free_port)
    - [`_is_port_in_use`](#_is_port_in_use)
    - [`_parse_port_range`](#_parse_port_range)

## Functions

### `get_free_port`

**Description**: Finds and returns a free port within the specified range, or the first available port if no range is given.

**Parameters**:
- `host` (str): The host address to check for available ports.
- `port_range` (Optional[str | List[str]], optional): A port range specified as a string "min-max" or a list of strings. E.g.: "3000-3999", ["3000-3999", "8000-8010"], None. Defaults to None.

**Returns**:
- `int`: An available port number.

**Raises**:
- `ValueError`: If no free port can be found within the specified range, or if the port range is invalid.

### `_is_port_in_use`

**Description**: Checks if a given port is in use on the specified host.

**Parameters**:
- `host` (str): The host address.
- `port` (int): The port number to check.

**Returns**:
- `bool`: True if the port is in use, False otherwise.

### `_parse_port_range`

**Description**: Parses a port range string "min-max" into a tuple (min_port, max_port).

**Parameters**:
- `port_range_str` (str): A string specifying the port range in "min-max" format.

**Returns**:
- `Tuple[int, int]`: A tuple containing the minimum and maximum port numbers.

**Raises**:
- `ValueError`: If the port range string is invalid or if the minimum port is greater than or equal to the maximum port.
```
## Improved Optimized Full Code:

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
.. module:: src.utils.get_free_port
    :platform: Windows, Unix
    :synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
"""

import socket
from typing import Optional, Tuple, List


from src.logger import logger


def get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int:
    """
    Finds and returns a free port within the specified range, or the first available port if no range is given.

    :param host: The host address to check for available ports.
    :type host: str
    :param port_range: (Optional) A port range specified as a string "min-max" or a list of strings.
           E.g.: "3000-3999", ["3000-3999", "8000-8010"], None
    :type port_range: Optional[str | List[str]]
    :return: An available port number.
    :rtype: int
    :raises ValueError: If no free port can be found within the specified range, or if the port range is invalid.
    """

    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Checks if a given port is in use on the specified host.
        """
        # Create a socket object for checking the port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                # Attempt to bind the socket to the given host and port
                sock.bind((host, port))
                # If successful, the port is available
                return False
            except OSError:
                # If an OSError occurs, the port is in use
                return True

    def _parse_port_range(port_range_str: str) -> Tuple[int, int]:
        """Parses port range string "min-max" into a tuple (min_port, max_port)."""
        try:
            # Split the port range string into two parts
            parts = port_range_str.split('-')
            # Check that the range is in the correct format
            if len(parts) != 2:
                logger.error(f'Error: Invalid port range string format: {port_range_str}')
                raise ValueError(f'Invalid port range string format: {port_range_str}')
            # Parse the minimum port from string to integer
            min_port = int(parts[0])
            # Parse the maximum port from string to integer
            max_port = int(parts[1])
            # Check that the minimum port is less than the maximum port
            if min_port >= max_port:
                logger.error(f'Error: Invalid port range {port_range_str}')
                raise ValueError(f'Invalid port range {port_range_str}')
            # Return the parsed minimum and maximum ports
            return min_port, max_port

        except ValueError as ex:
            # If a ValueError occurs during parsing, log the error and re-raise it
            logger.error(f'Error: Invalid port range {port_range_str}, {ex}')
            raise ValueError(f'Invalid port range {port_range_str}') from ex

    # Check if a port range has been provided
    if port_range:
        # If port range is a string
        if isinstance(port_range, str):
            try:
                # Parse the provided string port range
                min_port, max_port = _parse_port_range(port_range)
            except ValueError as ex:
                # If a ValueError occurs, log the error and re-raise it
                logger.error(f'Error: {ex}')
                raise ValueError(f'Invalid port range {port_range}') from ex
            # Loop through the port range
            for port in range(min_port, max_port + 1):
                # Check if the port is not in use
                if not _is_port_in_use(host, port):
                    # If the port is free return it
                    return port
            # If no free port is found in the provided range
            logger.error(f'Error: No free port found in range {port_range}')
            raise ValueError(f'No free port found in range {port_range}')
        # If port range is a list
        elif isinstance(port_range, list):
            # Loop through each range in the list
            for item in port_range:
                try:
                    # If the range is a string then parse
                    if isinstance(item, str):
                        min_port, max_port = _parse_port_range(item)
                    else:
                        # If the range item is not a string log the error and raise value error
                        logger.error(f'Error: Invalid port range item {item}')
                        raise ValueError(f'Invalid port range item {item}')

                    # Loop through the range
                    for port in range(min_port, max_port + 1):
                        # Check if the port is not in use
                        if not _is_port_in_use(host, port):
                            # If the port is free return it
                            return port
                except ValueError as ex:
                    # If a ValueError occurs, log the error and continue with the next range
                    logger.error(f'Error: {ex}')
                    continue  # Skip to the next range in the list if any range fails parsing or no port
            # If no free port is found in the provided ranges
            logger.error(f'Error: No free port found in specified ranges {port_range}')
            raise ValueError(f'No free port found in specified ranges {port_range}')
        else:
            # If the port_range is not a list or a string
            logger.error(f'Error: Invalid port range type {type(port_range)}')
            raise ValueError(f'Invalid port range type {type(port_range)}')
    else:
        # If no range given, find the first available port
        port = 1024  # start from 1024, since lower ports are system ports
        # loop until the port is free
        while True:
            # check if the current port is in use
            if not _is_port_in_use(host, port):
                # If port is not in use return it
                return port
            # If port is in use try the next one
            port += 1
            # If there is no free port in range
            if port > 65535:
                logger.error(f'Error: No free port found')
                raise ValueError('No free port found')


if __name__ == '__main__':
    host = 'localhost'

    # Пример с одним диапазоном:
    try:
        port = get_free_port(host, '3000-3005')
        print(f'Свободный порт: {port}')
    except ValueError as ex:
        print(f'Ошибка: {ex}')

    # Пример со списком диапазонов:
    try:
        port = get_free_port(host, ['3000-3005', '8000-8005'])
        print(f'Свободный порт: {port}')
    except ValueError as ex:
        print(f'Ошибка: {ex}')

    # Пример без диапазона (первый свободный):
    try:
        port = get_free_port(host)
        print(f'Свободный порт: {port}')
    except ValueError as ex:
        print(f'Ошибка: {ex}')

    # Пример с некорректным форматом
    try:
        port = get_free_port(host, '3000-')
        print(f'Свободный порт: {port}')
    except ValueError as ex:
        print(f'Ошибка: {ex}')

    # Пример с некорректными портами
    try:
        port = get_free_port(host, '5000-4000')
        print(f'Свободный порт: {port}')
    except ValueError as ex:
        print(f'Ошибка: {ex}')
    try:
        port = get_free_port(host, [5000, 4000])
        print(f'Свободный порт: {port}')
    except ValueError as ex:
        print(f'Ошибка: {ex}')
```

## Changes:

1.  **Modified Exception Handling**: Replaced the generic exception variable `e` with `ex` in all `except` blocks. This change improves readability and avoids confusion.

2.  **Added Comments**: Added detailed comments to the code to explain the purpose of each block, function, and variable.

3.  **Improved Documentation**: Added documentation for all functions using reStructuredText (reST) format following Sphinx guidelines.

4.  **Added more descriptive error logging**: Added more details to the error logging to help with debugging.

5.  **Added `from ex` to the re-raised exceptions**: Add `from ex` to the re-raised exception to preserver the traceback.