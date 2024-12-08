import click
from .apps import *
from .sites import *
from .main import *

@click.group()
def cli():
    pass

cli.add_command(newapp)
cli.add_command(dropapp)
cli.add_command(getapp)
cli.add_command(newmodule)
cli.add_command(dropmodule)
cli.add_command(newdoc)
cli.add_command(dropdoc)
cli.add_command(movedoc)

cli.add_command(newsite)
cli.add_command(installapp)
cli.add_command(uninstallapp)
cli.add_command(dropsite)
cli.add_command(installmodule)
cli.add_command(installdoc)

cli.add_command(pip)
cli.add_command(npm)

cli.add_command(install)
cli.add_command(i)

cli.add_command(migrate)
cli.add_command(update)
cli.add_command(registermodels)


cli.add_command(django)

cli.add_command(start)
cli.add_command(build)

cli.add_command(usesite)


# Add other commands as needed

if __name__ == "__main__":
    cli()
