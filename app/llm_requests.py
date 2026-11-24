import os

import requests

from config import LLM_API_URL, LLM_API_HEADERS, LLM_API_PAYLOAD, STATIC_DIR


def take_context_prompt() -> str:
    """
    Retrieve the context prompt for an LLM.

    :return: The prompt text.
    """
    FILE_PATH = os.path.join(STATIC_DIR, "prompts", "initial_prompt.md")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        context = f.read()

    return context


def make_request(message: str) -> dict:
    """
    Send a request containing prompts to an LLM.

    :param message: The user's message.
    :return: The LLM response.
    """
    LLM_API_PAYLOAD["messages"][0]["content"] = take_context_prompt()
    LLM_API_PAYLOAD["messages"][1]["content"] = message

    try:
        response = requests.post(
            url=LLM_API_URL,
            headers=LLM_API_HEADERS,
            json=LLM_API_PAYLOAD,
        )

        data = response.json()

    except Exception as e:
        raise ValueError(f"Error: '{e.__class__.__name__}' during the LLM API request.")

    return data
