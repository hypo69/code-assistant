# Module: src.utils.pdf

## Overview

This module provides utilities for converting HTML content or files to PDF using various libraries such as `pdfkit`, `fpdf`, `weasyprint`, `xhtml2pdf`, and `pdfminer`. It also includes functionalities to convert PDF files to HTML and save dictionary data to PDF.

## Table of Contents
- [Functions](#functions)
  - [`set_project_root`](#set_project_root)
- [Classes](#classes)
  - [`PDFUtils`](#pdfutils)
    - [`save_pdf_pdfkit`](#save_pdf_pdfkit)
    - [`save_pdf_fpdf`](#save_pdf_fpdf)
    - [`save_pdf_weasyprint`](#save_pdf_weasyprint)
    - [`save_pdf_xhtml2pdf`](#save_pdf_xhtml2pdf)
    - [`html2pdf`](#html2pdf)
    - [`pdf_to_html`](#pdf_to_html)
    - [`dict2pdf`](#dict2pdf)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project.

**Parameters**:
- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('__root__','.git')`.

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.

    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    ...
```
## Classes

### `PDFUtils`

**Description**: This class provides methods for working with PDF files, offering functionalities to save HTML content to PDF using various libraries.

**Methods**:
- [`save_pdf_pdfkit`](#save_pdf_pdfkit): Save HTML content or file to PDF using `pdfkit`.
- [`save_pdf_fpdf`](#save_pdf_fpdf): Save text to PDF using `FPDF`.
- [`save_pdf_weasyprint`](#save_pdf_weasyprint): Save HTML content or file to PDF using `WeasyPrint`.
- [`save_pdf_xhtml2pdf`](#save_pdf_xhtml2pdf): Save HTML content or file to PDF using `xhtml2pdf`.
- [`html2pdf`](#html2pdf): Converts HTML content to a PDF file using `WeasyPrint`.
- [`pdf_to_html`](#pdf_to_html): Converts a PDF file to an HTML file.
- [`dict2pdf`](#dict2pdf): Save dictionary data to a PDF file.

### `save_pdf_pdfkit`

**Description**: Save HTML content or file to PDF using `pdfkit`.

**Parameters**:
- `data` (str | Path): HTML content or path to the HTML file.
- `pdf_file` (str | Path): Path to the saved PDF file.

**Returns**:
- `bool`: `True` if the PDF was successfully saved, otherwise `False`.

**Raises**:
- `pdfkit.PDFKitError`: If an error occurs during PDF generation with `pdfkit`.
- `OSError`: If a file access error occurs.

```python
    @staticmethod
    def save_pdf_pdfkit(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `pdfkit`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.

        Raises:
            pdfkit.PDFKitError: Ошибка генерации PDF через `pdfkit`.
            OSError: Ошибка доступа к файлу.
        """
        ...
```

### `save_pdf_fpdf`

**Description**: Save text to PDF using `FPDF`.

**Parameters**:
- `data` (str): Text to save in the PDF.
- `pdf_file` (str | Path): Path to the saved PDF file.

**Returns**:
- `bool`: `True` if the PDF was successfully saved, otherwise `False`.

```python
    @staticmethod
    def save_pdf_fpdf(data: str, pdf_file: str | Path) -> bool:
        """
        Сохранить текст в PDF с использованием библиотеки FPDF.

        Args:
            data (str): Текст, который необходимо сохранить в PDF.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True`, если PDF успешно сохранен, иначе `False`.
        """
        ...
```

### `save_pdf_weasyprint`

**Description**: Save HTML content or file to PDF using `WeasyPrint`.

**Parameters**:
- `data` (str | Path): HTML content or path to the HTML file.
- `pdf_file` (str | Path): Path to the saved PDF file.

**Returns**:
- `bool`: `True` if the PDF was successfully saved, otherwise `False`.

```python
    @staticmethod
    def save_pdf_weasyprint(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `WeasyPrint`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.
        """
        ...
```

### `save_pdf_xhtml2pdf`

**Description**: Save HTML content or file to PDF using `xhtml2pdf`.

**Parameters**:
- `data` (str | Path): HTML content or path to the HTML file.
- `pdf_file` (str | Path): Path to the saved PDF file.

**Returns**:
- `bool`: `True` if the PDF was successfully saved, otherwise `False`.

```python
    @staticmethod
    def save_pdf_xhtml2pdf(data: str | Path, pdf_file: str | Path) -> bool:
        """
        Сохранить HTML-контент или файл в PDF с использованием библиотеки `xhtml2pdf`.

        Args:
            data (str | Path): HTML-контент или путь к HTML-файлу.
            pdf_file (str | Path): Путь к сохраняемому PDF-файлу.

        Returns:
            bool: `True` если PDF успешно сохранен, иначе `False`.
        """
        ...
```

### `html2pdf`

**Description**: Converts HTML content to a PDF file using WeasyPrint.

**Parameters**:
- `html_str` (str): HTML content to convert.
- `pdf_file` (str | Path): Path to the output PDF file.

**Returns**:
- `bool | None`: `True` if the PDF was successfully generated, otherwise `None`.

```python
    @staticmethod
    def html2pdf(html_str: str, pdf_file: str | Path) -> bool | None:
        """Converts HTML content to a PDF file using WeasyPrint."""
        ...
```

### `pdf_to_html`

**Description**: Converts a PDF file to an HTML file.

**Parameters**:
- `pdf_file` (str | Path): Path to the source PDF file.
- `html_file` (str | Path): Path to the saved HTML file.

**Returns**:
- `bool`: `True` if the conversion was successful, otherwise `False`.

```python
    @staticmethod
    def pdf_to_html(pdf_file: str | Path, html_file: str | Path) -> bool:
        """
        Конвертирует PDF-файл в HTML-файл.

        Args:
            pdf_file (str | Path): Путь к исходному PDF-файлу.
            html_file (str | Path): Путь к сохраняемому HTML-файлу.

        Returns:
            bool: `True`, если конвертация прошла успешно, иначе `False`.
        """
        ...
```

### `dict2pdf`

**Description**: Save dictionary data to a PDF file.

**Parameters**:
- `data` (dict | SimpleNamespace): The dictionary to convert to PDF.
- `file_path` (str | Path): Path to the output PDF file.

```python
    @staticmethod
    def dict2pdf(data: dict | 'SimpleNamespace', file_path: str | Path) -> None:
        """
        Save dictionary data to a PDF file.

        Args:
            data (dict | SimpleNamespace): The dictionary to convert to PDF.
            file_path (str | Path): Path to the output PDF file.
        """
        ...