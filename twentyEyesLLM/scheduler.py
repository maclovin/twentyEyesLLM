"""
Scheduler module has methods to handle the screenshot and LLM invoke.
"""

from .llm import (
    invoke_ollama_image_inference,
    invoke_openai_image_inference,
    SupportedModels,
)
from .screenshot import take_screenshot, load_screenshot
from schedule import every
from .history import update_history


def _ollama_job() -> None:
    """
    Define the Ollama job. Take a screenshot and submit it to the server for inference.

    Args:
        None

    Returns:
        None
    """
    take_screenshot()
    screenshot = load_screenshot()
    inference = invoke_ollama_image_inference(image=screenshot)
    update_history(new_inference=inference)


def _openai_job() -> None:
    """
    Define the OpenAI job. Take a screenshot and submit it to the server for inference.

    Args:
        None

    Returns:
        None
    """

    take_screenshot()
    screenshot = load_screenshot()
    inference = invoke_openai_image_inference(image=screenshot)
    update_history(new_inference=inference)


def job(model: SupportedModels, interval: int) -> None:
    """
    Start the inference job.

    Args:
        model (SupportedModels): The LLM to be used for the job.
        interval (int): The interval in minutes at which the job should be executed.

    Returns:
        None
    """
    if model == SupportedModels.OLLAMA:
        _ollama_job()  # Initial execution
        every(interval).minutes.do(_ollama_job)  # Scheduled executions
    elif model == SupportedModels.OPENAI:
        _openai_job()  # Initial execution
        every(interval).minutes.do(_openai_job)  # Scheduled executions
