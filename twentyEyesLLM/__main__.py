"""entry-point script"""

from . import cli, __app_name__


def main():
    """
        main method, initiation CLI interface.
    """
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
