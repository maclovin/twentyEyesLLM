"""config entry"""

import os

WORK_DIR_PATH = os.path.dirname(__file__)
HOME_DIR_PATH = os.path.expanduser("~")

LOCAL_PATH = os.path.join(HOME_DIR_PATH, ".twentyEyesLLM/")
IMAGE_FILE_PATH = os.path.join(HOME_DIR_PATH, ".twentyEyesLLM/temp.png")
HISTORY_FILE_PATH = os.path.join(HOME_DIR_PATH, ".twentyEyesLLM/history/")

OLLAMA_MODEL_FILE_PATH = os.path.join(WORK_DIR_PATH, "ollama/Modelfile")
OLLAMA_HOST = "http://127.0.0.1:11434"
OLLAMA_LOCAL_MODEL = "twentyEyesLLM"

DEFAULT_JOB_INTERVAL = 5
MAX_TOKENS_INFERENCE = 300

OPENAI_MODEL = "gpt-4o-mini"

VERBOSITY = False
