import click

from app.crud import add_data_to_db
from app.validators import validate_add_data

from .main import cli


@cli.command()
@click.argument("data")
def add_data(data):
    validate_add_data({"data": data})
    add_data_to_db(data)
    click.echo("Added data to database!")
