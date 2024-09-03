"""
This module provides inference methods and datatypes on top of supported LLMs.
"""

import json
from openai import OpenAI
from ollama import Client as OllamaClient
from typing import NamedTuple
from datetime import datetime
from enum import Enum

from .prompts import PROMPT_IMAGE_INFERENCE
from .config import (
    MAX_TOKENS_INFERENCE,
    OLLAMA_HOST,
    OLLAMA_LOCAL_MODEL,
    OLLAMA_MODEL_FILE_PATH,
    OPENAI_MODEL,
)

_ollama_client = OllamaClient(host=OLLAMA_HOST)
_openai_client = OpenAI()


class SupportedModels(Enum):
    """
    Enum representing the supported models.
    """

    OLLAMA = 1
    OPENAI = 2


class Inference(NamedTuple):
    """
    NamedTuple representing an inference result.
    """

    datetime: str
    content: str
    category: str


def _sanitize_json_response(response: str, replace_list: list) -> str:
    """
    Sanitize the JSON response by removing unwanted substrings.

    Args:
        response (str): The JSON response to sanitize.
        replace_list (list): List of substrings to remove from the response.

    Returns:
        str: The sanitized JSON response.
    """
    for item in replace_list:
        response = response.replace(item, "")

    return response


def _load_modelfile() -> str:
    """
    Load the model file from the specified location.

    Returns:
        str: The content of the model file.
    """

    with open(OLLAMA_MODEL_FILE_PATH, "r", encoding="utf-8") as file:
        modelfile = file.read()

    return modelfile


def init_ollama() -> None:
    """
    Initialize the Ollama client with the specified host.
    """
    _ollama_client.create(model=OLLAMA_LOCAL_MODEL, modelfile=_load_modelfile())


def invoke_ollama_image_inference(image: str) -> Inference:
    """
    Invoke an image inference using the Ollama model.

    Args:
        image (str): The base64 encoded image string.

    Returns:
        Inference: The inference result.
    """
    response = _ollama_client.generate(
        model=OLLAMA_LOCAL_MODEL,
        images=[image],
        prompt=PROMPT_IMAGE_INFERENCE,
        options={"num_predict": MAX_TOKENS_INFERENCE},
    )

    sanitized_result = _sanitize_json_response(
        response=response["response"], replace_list=["```json", "\n", "```"]
    )

    parsed_result = json.loads(sanitized_result)

    return Inference(
        datetime=datetime.now().isoformat(),
        content=parsed_result["description"],
        category=parsed_result["category"],
    )


def invoke_openai_image_inference(image: str) -> Inference:
    """
    Invoke an image inference using the OpenAI model.

    Args:
        image (str): The base64 encoded image string.

    Returns:
        Inference: The inference result.
    """
    response = _openai_client.chat.completions.create(
        model=OPENAI_MODEL,
        max_tokens=MAX_TOKENS_INFERENCE,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT_IMAGE_INFERENCE},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image}"},
                    },
                ],
            }
        ],
    )

    sanitized_result = _sanitize_json_response(
        response=response.choices[0].message.content,
        replace_list=["```json", "\n", "```"],
    )

    parsed_result = json.loads(sanitized_result)

    return Inference(
        datetime=datetime.now().isoformat(),
        content=parsed_result["description"],
        category=parsed_result["category"],
    )
