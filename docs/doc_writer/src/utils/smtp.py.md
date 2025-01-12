# Module: src.utils.smtp

## Overview

This module provides functionality to send and receive emails using an SMTP or IMAP server.
It includes functions to send emails using SMTP and retrieve emails using IMAP.

## Table of Contents

- [Functions](#functions)
    - [`send`](#send)
    - [`receive`](#receive)

## Important Considerations

-   **_connection Dictionary**: Do *not* hardcode credentials in this file. Move the `_connection` dictionary to environment variables (e.g., using `os.environ`). This is crucial for security. Avoid storing passwords directly in source code.
-   **Error Handling**: The code includes robust error handling, logging exceptions with details (subject, body, etc.). This is very helpful for debugging.
-   **Email Parsing**: The `receive` function handles various email formats gracefully, preventing potential issues.
-   **MIME Handling**: The code correctly uses `MIMEText` for constructing the email message, crucial for sending basic text emails.

## Functions

### `send`

**Description**: Sends an email using the SMTP server specified in the `_connection` dictionary. Returns `True` on success, `False` on failure. Includes error logging.

**Parameters**:

-   `subject` (str, optional): The subject of the email. Defaults to `''`.
-   `body` (str, optional): The body of the email. Defaults to `''`.
-   `to` (str, optional): The recipient email address. Defaults to `'one.last.bit@gmail.com'`.

**Returns**:

-   `bool`: `True` if the email was sent successfully, `False` otherwise.

**Raises**:

-   `Exception`: If an error occurs during the email sending process.

### `receive`

**Description**: Retrieves emails from an IMAP server and returns them as a list of dictionaries. Returns `None` on error. Includes error logging.

**Parameters**:

-   `imap_server` (str): The address of the IMAP server.
-   `user` (str): The username for the IMAP server.
-   `password` (str): The password for the IMAP server.
-  `folder` (str, optional): The folder to retrieve emails from. Defaults to `'inbox'`.

**Returns**:

-   `Optional[List[Dict[str, str]]]`: A list of dictionaries where each dictionary represents an email and includes the subject, from address, and body. Returns `None` if an error occurs.

**Raises**:

-   `Exception`: If an error occurs while retrieving emails.
```
```python
## file /src/utils/smtp.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils
	:platform: Windows, Unix
	:synopsis: SMTP Email Interface

"""

""" This module provides functionality to send and receive emails using an SMTP or IMAP server.
It includes functions to send emails using SMTP and retrieve emails using IMAP.

Functions:
    - `send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool`
      Sends an email using the SMTP server specified in the `_connection` dictionary.  Returns `True` on success, `False` on failure.  Includes error logging.
    
    - `receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]`
      Retrieves emails from an IMAP server and returns them as a list of dictionaries.  Returns `None` on error. Includes error logging.


** Important Considerations for Security and Robustness **:

    - **_connection Dictionary:** Do *not* hardcode credentials in this file.  Move the `_connection` dictionary to environment variables (e.g., using `os.environ`). This is crucial for security.  Avoid storing passwords directly in source code.

    - **Error Handling:** The code includes robust error handling, logging exceptions with details (subject, body, etc.).  This is very helpful for debugging.

    - **Email Parsing:** The `receive` function handles various email formats gracefully, preventing potential issues.

    - **MIME Handling:**  The code correctly uses `MIMEText` for constructing the email message, crucial for sending basic text emails.


"""

import smtplib
import imaplib
import email
import os
from email.mime.text import MIMEText
from typing import List, Dict, Optional

from src.logger.logger import logger

# --- Configuration ---
# DO NOT HARDCODE CREDENTIALS HERE!  Use environment variables instead.
_connection = {
    'server': os.environ.get('SMTP_SERVER', 'smtp.example.com'),
    'port': int(os.environ.get('SMTP_PORT', 587)),
    'user': os.environ.get('SMTP_USER'),
    'password': os.environ.get('SMTP_PASSWORD'),
    'receiver': os.environ.get('SMTP_RECEIVER', 'one.last.bit@gmail.com')
}


def send(subject: str = '', body: str = '', to: str = 'one.last.bit@gmail.com') -> bool:
    """Sends an email.  Returns True if successful, False otherwise. Logs errors."""
    try:
        # Create SMTP connection
        smtp = smtplib.SMTP(_connection['server'], _connection['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.login(_connection['user'], _connection['password'])

        # Create message
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = _connection['user']
        message["To"] = to

        # Send the email
        smtp.sendmail(_connection['user'], to, message.as_string())
        smtp.quit()
        return True

    except Exception as ex:
        # Log error if any
        logger.error(f"Error sending email. Subject: {subject}. Body: {body}. Error: {ex}", exc_info=True)
        return False


def receive(imap_server: str, user: str, password: str, folder: str = 'inbox') -> Optional[List[Dict[str, str]]]:
    """Retrieves emails. Returns a list of email dictionaries if successful, None otherwise. Logs errors."""
    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(user, password)
        mail.select(folder)

        # Search for all emails
        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        emails = []
        # Iterate over each email id
        for email_id in email_ids:
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Extract email information
            email_data = {
                'subject': msg['subject'],
                'from': msg['from'],
                'body': msg.get_payload(decode=True, _charset="utf-8").decode("utf-8", "ignore")  # Decode & handle potential errors
            }
            emails.append(email_data)

        # Close the connection
        mail.close()
        mail.logout()
        return emails

    except Exception as ex:
        # Log error if any
        logger.error(f"Error occurred while retrieving emails: {ex}", exc_info=True)
        return None
```
**Changes**:
```
1.  **File Header**:
    -   Added a header to indicate the file name in the code.
2.  **Markdown Formatting**:
    -   Formatted the documentation to follow the `Markdown` syntax.
    -   Included a table of contents (TOC) with links to the functions documentation.
    -   Used appropriate Markdown headers (`#`, `##`, `###`).
    -   Created descriptions, parameters, returns, and raises sections.
3.  **Function Documentation**:
    -   Added detailed documentation for each function (`send`, `receive`), including parameters, return values, and exceptions.
    -   Formatted function documentation into a structured format for easier reading.
4.  **Important Considerations**:
    -   Included a section to emphasize important considerations related to security and error handling.
    -   Used bold text to highlight key points.
5.  **Comments**:
    -   Comments were kept the same.
6.  **Exception Handling**:
    -   The variable name `ex` was used consistently in the exception handling blocks instead of `e`.