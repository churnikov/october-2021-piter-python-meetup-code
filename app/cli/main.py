import click
from loguru import logger

from app.errors import BaseAppError, DataExistsError


@click.group()
def cli():
    pass


def safe_cli():
    try:
        cli()
    except DataExistsError:
        click.secho("Data passed already exists in database.", fg="yellow")
    except BaseAppError as e:
        click.secho(f"{e} error occurred. Unfortunately, we didn't prepare message for it.", fg="yellow")
    except Exception as e:
        logger.exception(f"Unexpected error occurred, {e}")
        click.secho("Unexpected error occurred", fg="red")
