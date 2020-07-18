import click
from .test import test
from .start import start


@click.group()
def cli():
    pass


cli.add_command(test)
cli.add_command(start)
