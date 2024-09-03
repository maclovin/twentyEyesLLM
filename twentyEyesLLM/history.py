import os
import json
from typing import Any, List, NamedTuple
from enum import Enum
from twentyEyesLLM import __app_name__
from datetime import datetime

from .llm import Inference
from .config import HISTORY_FILE_PATH
from .report import Report
from .errors import HISTORY_FILE_NOT_FOUND_ERROR, HISTORY_FILE_DELETE_PERMS_ERROR

class ReportFormats(str, Enum):
    """
    Enum representing the supported report formats.
    """
    MARKDOWN = "markdown"
    PLAINTEXT = "plaintext"
    JSON = "json"

class History(NamedTuple):
    """
    NamedTuple representing the history of inferences.
    """
    inferences: List[Inference]

def _generate_file_name(date: Any = None) -> str:
    """
    Generate a file name based on the given date or the current date.

    Args:
        date (Any): The date to generate the file name from. Defaults to None.

    Returns:
        str: The generated file name.
    """
    if date is None:
        date = datetime.now()
    return date.strftime('%y_%m_%d')

def _get_history_file(file_name: str) -> Any:
    """
    Retrieve or create a history file.

    Args:
        file_name (str): The name of the file to retrieve or create.

    Returns:
        Any: The loaded history file content.
    """
    target_file = f"{HISTORY_FILE_PATH}{file_name}.json" if file_name else f"{HISTORY_FILE_PATH}{_generate_file_name()}.json"
    
    if not os.path.exists(target_file):
        directory_path = os.path.dirname(target_file)
        
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"[INFO] Creating '{directory_path}' directory.")
        
        with open(target_file, "w") as file:
            new_history = History(inferences=[])
            json.dump(new_history._asdict(), file)
        
        print(f"[INFO] File '{target_file}' created.")
    else:
        print(f"[INFO] File '{target_file}' already exists. Using it.")
        
    with open(target_file, "r") as history_file:
        return json.load(history_file)

def update_history(new_inference: Inference) -> None:
    """
    Update the history file with a new inference.

    Args:
        new_inference (Inference): The new inference to add to the history.
    """
    target_file_name = _generate_file_name()
    parsed_history = _get_history_file(file_name=target_file_name)
    parsed_history["inferences"].append(new_inference._asdict())
    
    with open(f"{HISTORY_FILE_PATH}{target_file_name}.json", "w") as file:
        json.dump(parsed_history, file)

def clear_history() -> None:
    """
    Clear the history by deleting the history file.
    """
    try:
        os.remove(HISTORY_FILE_PATH)
        print(f"File '{HISTORY_FILE_PATH}' deleted successfully.")
    except FileNotFoundError:
        print(HISTORY_FILE_NOT_FOUND_ERROR)
    except PermissionError:
        print(HISTORY_FILE_DELETE_PERMS_ERROR)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_all_history_file_names() -> List[str]:
    """
    Get all history file names.

    Returns:
        List[str]: A list of all history file names (without extensions).
    """
    files = []
    
    for _, __, filenames in os.walk(HISTORY_FILE_PATH):
        for filename in filenames:
            files.append(filename.split(".")[0])

    return files

def generate_history_report(date: str) -> None:
    """
    Generate a history report for the specified date.

    Args:
        date (str): The date for which to generate the history report.
    """
    history_files = get_all_history_file_names()
    
    if date in history_files:
        parsed_history = _get_history_file(date)
        
        report = Report(history=parsed_history)
        print(report.to_markdown())
    else:
        print(HISTORY_FILE_NOT_FOUND_ERROR)
