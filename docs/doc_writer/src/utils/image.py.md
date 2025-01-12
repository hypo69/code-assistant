# src.utils

## Overview

This module provides asynchronous functions for downloading, saving, and manipulating images.
It includes functionalities such as saving images from URLs, saving image data to files,
retrieving image data, finding random images within directories, adding watermarks, resizing,
and converting image formats.

## Table of Contents
- [Classes](#classes)
  - [`ImageError`](#imageerror)
- [Functions](#functions)
  - [`save_image_from_url`](#save_image_from_url)
  - [`save_image`](#save_image)
  - [`get_image_bytes`](#get_image_bytes)
  - [`get_raw_image_data`](#get_raw_image_data)
  - [`random_image`](#random_image)
  - [`add_text_watermark`](#add_text_watermark)
  - [`add_image_watermark`](#add_image_watermark)
  - [`resize_image`](#resize_image)
  - [`convert_image`](#convert_image)
  - [`process_images_with_watermark`](#process_images_with_watermark)

## Classes

### `ImageError`

**Description**: Custom exception for image-related errors.

## Functions

### `save_image_from_url`

**Description**: Downloads an image from a URL and saves it locally asynchronously.

**Parameters**:
- `image_url` (str): The URL to download the image from.
- `filename` (Union[str, Path]): The name of the file to save the image to.

**Returns**:
- `Optional[str]`: The path to the saved file, or None if the operation failed.

**Raises**:
- `ImageError`: If the image download or save operation fails.

### `save_image`

**Description**: Saves image data to a file in the specified format asynchronously.

**Parameters**:
- `image_data` (bytes): The binary image data.
- `file_name` (Union[str, Path]): The name of the file to save the image to.
- `format` (str): The format to save the image in, default is PNG.

**Returns**:
- `Optional[str]`: The path to the saved file, or None if the operation failed.

**Raises**:
- `ImageError`: If the file cannot be created, saved, or if the saved file is empty.

### `get_image_bytes`

**Description**: Reads an image using Pillow and returns its bytes in JPEG format.

**Parameters**:
- `image_path` (Path): The path to the image file.
- `raw` (bool): If True, returns a BytesIO object; otherwise, returns bytes. Defaults to True.

**Returns**:
- `Optional[Union[BytesIO, bytes]]`: The bytes of the image in JPEG format, or None if an error occurs.

### `get_raw_image_data`

**Description**: Retrieves the raw binary data of a file if it exists.

**Parameters**:
- `file_name` (Union[str, Path]): The name or path of the file to read.

**Returns**:
- `Optional[bytes]`: The binary data of the file, or None if the file does not exist or an error occurs.

### `random_image`

**Description**: Recursively searches for a random image in the specified directory.

**Parameters**:
- `root_path` (Union[str, Path]): The directory to search for images.

**Returns**:
- `Optional[str]`: The path to a random image, or None if no images are found.

### `add_text_watermark`

**Description**: Adds a text watermark to an image.

**Parameters**:
- `image_path` (Union[str, Path]): Path to the image file.
- `watermark_text` (str): Text to use as the watermark.
- `output_path` (Optional[Union[str, Path]]): Path to save the watermarked image.
    Defaults to overwriting the original image.

**Returns**:
- `Optional[str]`: Path to the watermarked image, or None on failure.

### `add_image_watermark`

**Description**: Adds a watermark to an image and saves the result to the specified output path.

**Parameters**:
- `input_image_path` (Path): Path to the input image.
- `watermark_image_path` (Path): Path to the watermark image.
- `output_image_path` (Optional[Path]): Path to save the watermarked image.
    If not provided, the image will be saved in an "output" directory.

**Returns**:
- `Optional[Path]`: Path to the saved watermarked image, or None if the operation failed.

### `resize_image`

**Description**: Resizes an image to the specified dimensions.

**Parameters**:
- `image_path` (Union[str, Path]): Path to the image file.
- `size` (Tuple[int, int]): A tuple containing the desired width and height of the image.
- `output_path` (Optional[Union[str, Path]]): Path to save the resized image.
    Defaults to overwriting the original image.

**Returns**:
- `Optional[str]`: Path to the resized image, or None on failure.

### `convert_image`

**Description**: Converts an image to the specified format.

**Parameters**:
- `image_path` (Union[str, Path]): Path to the image file.
- `format` (str): Format to convert image to (e.g., "JPEG", "PNG").
- `output_path` (Optional[Union[str, Path]]): Path to save the converted image.
    Defaults to overwriting the original image.

**Returns**:
- `Optional[str]`: Path to the converted image or None on failure.

### `process_images_with_watermark`

**Description**: Processes all images in the specified folder by adding a watermark and saving them in an "output" directory.

**Parameters**:
- `folder_path` (Path): Path to the folder containing images.
- `watermark_path` (Path): Path to the watermark image.