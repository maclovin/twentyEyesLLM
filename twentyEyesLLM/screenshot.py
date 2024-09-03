"""
This module provides screenshot capabilities.
"""

import base64
from PIL import ImageGrab
from .config import IMAGE_FILE_PATH


def take_screenshot() -> None:
    """
    Take a screenshot and save it as a PNG file.
    The saving is enabling any kind of analysis before submission to the inference server.

    Args:
        None

    Returns:
        None
    """
    screenshot = ImageGrab.grab()
    screenshot.save(IMAGE_FILE_PATH, "PNG")


def load_screenshot() -> str:
    """
    Load the saved screenshot, convert it to a base64 string, and return it.

    Args:
        None

    Returns:
        str: The base64 encoded string of the screenshot.
    """
    with open(IMAGE_FILE_PATH, "rb") as img_file:
        img_bytes = img_file.read()
        base64_str = base64.b64encode(img_bytes).decode("utf-8")

        return base64_str
