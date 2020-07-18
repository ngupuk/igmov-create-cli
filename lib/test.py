import click


@click.command(name="test", help="Command Test")
def test():
    click.echo("Tested")
