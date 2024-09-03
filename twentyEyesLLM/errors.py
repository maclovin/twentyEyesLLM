"""This module provides errors messages."""

OLLAMA_ERROR = (
    "Ollama setup fails. please, check the server or the configuration settings."
)
FILE_ERROR = "Error on load the image"
DIR_ERROR = "Error on load file"
JSON_ERROR = "Error on parse the json local file"
CLI_MODEL_PARAM_ERROR = (
    'You must choose one LLM to run. Type "run --help" to see the running options.\n'
)
CLI_REPORT_DATE_ERROR = 'You must choose at least one date. Type "history --list" to see the list of dates available in your local cache.\n'
CLI_HISTORY_PARAM_ERROR = 'Type "history --help" to see the history command options.\n'
HISTORY_FILE_NOT_FOUND_ERROR = "No history found for this date.\n"
HISTORY_FILE_DELETE_PERMS_ERROR = "Permission denied to delete history file.\n"
OPENAI_ERROR = "OpenAI API connection failed. Please check your connectivity and the provided credentials."
