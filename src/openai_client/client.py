"""
Concrete implementation of OpenAI client.
"""

from typing import List, Dict, Any, Optional
from .base import OpenAIBase
from src.config import config


class OpenAIClient(OpenAIBase):
    """Concrete implementation of OpenAI client."""

    async def chat(self, messages: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        Send a chat completion request to OpenAI API.

        Args:
            messages: List of message objects with role and content.
            **kwargs: Additional parameters to pass to the API.
                model: The model to use (default: "gpt-3.5-turbo")
                temperature: Controls randomness (default: 0.7)
                max_tokens: Maximum number of tokens to generate (default: None)

        Returns:
            The API response as a dictionary.
        """
        # Set default model if not provided
        if "model" not in kwargs:
            kwargs["model"] = config.BASE_MODEL or "gpt-3.5-turbo"

        return await super().chat(messages, **kwargs)

    async def chat_with_image(self, messages: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        Send a chat completion request with image(s) to OpenAI API.

        Args:
            messages: List of message objects with role and content.
                For images, the content should include image data in the format:
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"}
                }
                or base64 encoded:
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/jpeg;base64,/9j/4AAQ..."}
                }
            **kwargs: Additional parameters to pass to the API.
                model: The model to use (default: "gpt-4-vision-preview")
                max_tokens: Maximum number of tokens to generate (default: 300)

        Returns:
            The API response as a dictionary.
        """
        # Set default max_tokens if not provided
        system_prompt = """
你是一个生活助手，擅长分析图片，并给出合理的建议。
你会收到一张桌面截图，请根据指令分析图片，并给出结果
使用中文回复
        """
        messages.insert(0, {"role": "system", "content": system_prompt})
        if "model" not in kwargs:
            kwargs["model"] = config.BASE_VLM_MODEL or "gpt-4-vision-preview"

        return await super().chat_with_image(messages, **kwargs)
