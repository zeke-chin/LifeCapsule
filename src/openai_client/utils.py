"""
Utility functions for OpenAI API.
"""

import base64
from typing import Dict, List, Any, Optional
import os


def create_message(role: str, content: str) -> Dict[str, str]:
    """
    Create a message object for OpenAI chat API.

    Args:
        role: The role of the message sender (system, user, assistant).
        content: The content of the message.

    Returns:
        A message object.
    """
    return {"role": role, "content": content}


def encode_image_to_base64(image_path: str) -> str:
    """
    Encode an image to base64 for use with OpenAI API.

    Args:
        image_path: Path to the image file.

    Returns:
        Base64 encoded image string with data URI prefix.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded_string}"


def create_image_message(role: str, text: str, image_urls: List[str]) -> Dict[str, Any]:
    """
    Create a message with text and images for OpenAI vision API.

    Args:
        role: The role of the message sender (usually 'user').
        text: The text content of the message.
        image_urls: List of image URLs or base64 encoded images.

    Returns:
        A message object with text and images.
    """
    content = [{"type": "text", "text": text}]

    for url in image_urls:
        # Check if it's already a base64 data URI
        if url.startswith("data:") or url.startswith("http") or url.startswith("https"):
            image_url = url
        # Check if it's a local file path
        elif os.path.exists(url):
            image_url = encode_image_to_base64(url)
        # Assume it's a remote URL
        else:
            image_url = url

        content.append({"type": "image_url", "image_url": {"url": image_url}})

    return {"role": role, "content": content}
