import click
from pyfiglet import Figlet


@click.command(name='start', help="Generate Video")
def start():
    f = Figlet(font='cricket')
    print(f.renderText("Igmov Create"))
    print()
