"""
Base class for OpenAI API interactions.
"""

from retry import retry
from typing import List, Dict, Any
from openai import AsyncOpenAI
from abc import ABC, abstractmethod
from src.config import config


class OpenAIBase(ABC):
    """Base class for OpenAI API interactions."""

    def __init__(self):
        """
        Initialize the OpenAI client.
        """
        self.client = AsyncOpenAI(
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_BASE_URL,
        )

    @retry(tries=3, delay=2, backoff=2)
    async def chat(self, messages: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        Send a chat completion request to OpenAI API.

        Args:
            messages: List of message objects with role and content.
            **kwargs: Additional parameters to pass to the API.

        Returns:
            The API response as a dictionary.
        """
        response = await self.client.chat.completions.create(
            messages=messages,
            **kwargs,
        )
        return response.model_dump()

    @retry(tries=3, delay=2, backoff=2)
    async def chat_with_image(self, messages: List[Dict[str, Any]], **kwargs) -> Dict[str, Any]:
        """
        Send a chat completion request with image(s) to OpenAI API.

        Args:
            messages: List of message objects with role and content.
                For images, the content should be a list where some items contain image URLs or base64 data.
            **kwargs: Additional parameters to pass to the API.

        Returns:
            The API response as a dictionary.
        """
        try:
            # Ensure model is set to one that supports vision
            if "model" not in kwargs:
                kwargs["model"] = config.BASE_VLM_MODEL or "gpt-4-vision-preview"

            response = await self.client.chat.completions.create(
                messages=messages,
                **kwargs,
            )
            return response.model_dump()
        except Exception as e:
            print(e)
            return None
