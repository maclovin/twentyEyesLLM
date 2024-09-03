"""This module provides the CLI itself."""

import time
from typing import Optional

import typer
from schedule import run_pending

from . import __app_name__, __version__
from .config import DEFAULT_JOB_INTERVAL
from .history import generate_history_report, get_all_history_file_names, clear_history
from .llm import init_ollama, SupportedModels
from .scheduler import job
from .errors import (
    OPENAI_ERROR,
    OLLAMA_ERROR,
    CLI_HISTORY_PARAM_ERROR,
    CLI_MODEL_PARAM_ERROR,
    CLI_REPORT_DATE_ERROR,
)

app = typer.Typer()


def _version_callback(value: bool) -> None:
    """
    Display the version of the application and exit.

    Args:
        value (bool): If True, display the version and exit.
    """

    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    """
    Main entry point for the CLI. This function handles the --version option.

    Args:
        version (Optional[bool]): If True, show the version and exit.
    """


@app.command()
def run(
    ollama: Optional[bool] = typer.Option(None, "--ollama"),
    openai: Optional[bool] = typer.Option(None, "--openai"),
    interval: int = typer.Option(DEFAULT_JOB_INTERVAL, "--interval"),
) -> None:
    """
    Run the job scheduler for the specified LLM.

    Args:
        ollama (Optional[bool]): If True, use the Ollama model.
        openai (Optional[bool]): If True, use the OpenAI model.
        host (Optional[str]): The host address for the Ollama model.
        interval (int): The interval at which to run the job.
    """

    if ollama:
        try:
            init_ollama()
            job(model=SupportedModels.OLLAMA, interval=interval)
        except Exception as e:
            print(f"{OLLAMA_ERROR} - {e}")

            return

    if openai:
        try:
            job(model=SupportedModels.OPENAI, interval=interval)
        except Exception as e:
            print(f"{OPENAI_ERROR} - {e}")

            return

    if not ollama and not openai:
        print(CLI_MODEL_PARAM_ERROR)

        return

    while True:
        run_pending()
        time.sleep(1)


@app.command()
def report(date: Optional[str] = typer.Option(None, "--date")) -> None:
    """
    Generate a history report for the specified date.

    Args:
        date (Optional[str]): The date for which to generate the report.
    """

    if date:
        generate_history_report(date)
    else:
        print(CLI_REPORT_DATE_ERROR)


@app.command()
def history(
    clear: Optional[bool] = typer.Option(None, "--clear"),
    list: Optional[bool] = typer.Option(None, "--list"),
) -> None:
    """
    Manage history files by clearing or listing them.

    Args:
        clear (Optional[bool]): If True, clear the history.
        list (Optional[bool]): If True, list all history file names.
    """

    if clear:
        clear_history()

        return

    if list:
        files = get_all_history_file_names()
        for file in files:
            print(f"{file}\t")

        return

    if not clear and not list:
        print(CLI_HISTORY_PARAM_ERROR)


if __name__ == "__main__":
    app()
