# Module `Code Assistant`

## Overview

The `Code Assistant` module is a set of tools designed to interact with **Gemini** and **OpenAI** models to process project source code. It performs tasks such as documentation creation, code checking, and test generation based on specified files. It also includes scripts to create a `SUMMARY.md` file for compiling documentation and a Telegram bot for handling code-related tasks.

## Table of Contents

1.  [Overview](#overview)
2.  [Main Features](#main-features)
    -   [`code_assistant.py`](#code_assistantpy)
    -   [`make_summary.py`](#make_summarypy)
    -   [`onela_bot.py` and `bot_handlers.py`](#onela_botpy-and-bot_handlerspy)
3.  [Project Structure](#project-structure)
4.  [Usage Examples](#usage-examples)
5.  [Command Line Parameters](#command-line-parameters)
6.  [Work Logic](#work-logic)
7.  [Exceptions](#exceptions)
8.  [Logging](#logging)
9.  [Dependencies](#dependencies)
10. [Creating a New Role for AI Models](#creating-a-new-role-for-ai-models)

## Main Features

### `code_assistant.py`

-   **File Reading**: Reads code from files with `.py` and `README.MD` extensions in specified directories.
-   **Model Interaction**: Sends code to models to perform tasks, such as creating documentation or checking for errors.
-   **Result Generation**: Saves model responses to specified directories for each role.

### `make_summary.py`

-   **`SUMMARY.md` Generation**: Recursively traverses a directory to create a `SUMMARY.md` file for compiling documentation.
-   **Language Filtering**: Supports filtering files by language (`ru` or `en`).

### `onela_bot.py` and `bot_handlers.py`

-   **Telegram Bot**: A bot for handling code-related tasks, such as sending code snippets for review or generating documentation.
-   **Bot Handlers**: Contains handlers for bot commands and messages.

## Project Structure

-   **Models**: Uses **Gemini** and **OpenAI** models to process requests.
-   **Prompts**: Reads prompts from files in the `src/ai/prompts/developer/` directory (e.g., `doc_writer_en.md`).
-   **Files**: Processes files with `.py` and `README.MD` extensions in specified directories.

## Usage Examples

### Running with Settings from JSON:

```bash
python code_assistant.py --settings settings.json
```

### Running with Explicit Parameters:

```bash
python code_assistant.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
```

### Example for the `code_checker` Role:

```bash
python code_assistant.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
```

### Example for the `openai` Model:

```bash
python code_assistant.py --role doc_writer --lang en --models openai
```

## Command Line Parameters

-   `--settings`: Path to the JSON file with settings. Loads parameters from the file.
-   `--role`: Model role for task execution (e.g., `doc_writer`, `code_checker`).
-   `--lang`: Language for task execution (e.g., `ru` or `en`).
-   `--models`: List of models to initialize (e.g., `gemini`, `openai`).
-   `--start_dirs`: List of directories to process (e.g., `/path/to/dir1`).

## Work Logic

1.  **File Reading**: Searches for files with `.py` and `README.MD` extensions in the specified directories.
2.  **Prompt Loading**: Loads prompts for each role from the `src/ai/prompts/developer/` directory.
3.  **Request Processing**: Forms requests based on the loaded files and sends them to the models.
4.  **Response Saving**: Saves model responses to directories corresponding to the role and model (e.g., `docs/raw_rst_from_<model>/<lang>/`).

## Exceptions

Configuration of exceptions for files and directories using parameters:

-   `exclude_file_patterns`: List of regular expressions for excluding files.
-   `exclude_dirs`: List of directories to exclude.
-   `exclude_files`: List of files to exclude.

## Logging

Logs are saved using the `logger` library and contain information about the file processing and received responses.

## Dependencies

-   **Gemini API**: An API key is required to work with the Gemini model.
-   **OpenAI API**: An API key is required to work with the OpenAI model.

## Creating a New Role for AI Models

1.  **Update `code_assistant.json`**:
    -   Add a new role to the list of roles:

        ```json
        "roles": [
          "code_checker",
          ...
        ]
        ```
    - Or exclude it in `"exclude-roles"`.
2.  **Adding a Role to Translations**:
    - Update the `translations/translations.json` file with the new role.
3.  **Creating a System Prompt**:
    - Add a new system prompt to the `ai/prompts/developer/` directory.
4.  **Creating a Command Instruction**:
    - Add a new command to the `instructions/` directory.