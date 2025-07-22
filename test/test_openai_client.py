import pytest
from src.openai_client import OpenAIClient, create_image_message
import json


@pytest.mark.asyncio
async def test_chat_integration():
    """
    Integration test for the chat method.
    This test makes a real API call using credentials from the .env file.
    """
    # Initialize the client, which will load config from .env
    client = OpenAIClient()

    # Define a simple message to send
    messages = [{"role": "user", "content": "Hello, world!"}]
    kwargs = {"max_tokens": 5}
    # Call the chat method
    response = await client.chat(messages=messages, **kwargs)
    print(json.dumps(response, indent=2, ensure_ascii=False))

    # Assert that we got a response and it has the expected structure
    assert response is not None
    assert "id" in response
    assert "choices" in response
    assert len(response["choices"]) > 0
    assert "message" in response["choices"][0]
    assert "content" in response["choices"][0]["message"]
    assert response["choices"][0]["message"]["content"] is not None


@pytest.mark.asyncio
async def test_chat_with_image_integration():
    """
    Integration test for the chat method.
    This test makes a real API call using credentials from the .env file.
    """
    # Initialize the client, which will load config from .env
    client = OpenAIClient()

    # Define a simple message to send\
    query = "图片主要讲了什么?"
    image_url = "https://ark-project.tos-cn-beijing.ivolces.com/images/view.jpeg"
    messages = [create_image_message("user", query, [image_url])]

    # Call the chat method
    response = await client.chat(messages=messages)
    print(json.dumps(response, indent=2, ensure_ascii=False))

    # Assert that we got a response and it has the expected structure
    assert response is not None
    assert "id" in response
    assert "choices" in response
    assert len(response["choices"]) > 0
    assert "message" in response["choices"][0]
    assert "content" in response["choices"][0]["message"]
    assert response["choices"][0]["message"]["content"] is not None
