import platform
import sys

import click

from cos.config import COS_VENV_DIR
from cos.services.svc_venv import check_venv_exists
from cos.services.svc_venv import create_new_venv
from cos.services.svc_venv import list_venvs
from cos.services.svc_venv import remove_venv
from cos.services.svc_venv import venv_does_not_exist_msg


@click.group(invoke_without_command=True)
def cli() -> None:
    """Manage all your Python venv in a single place.
    """
    pass


@cli.command()
@click.argument("venv_name", type=str)
@click.option("-p", "--python", type=str, default=".", help="Specify a python version.")
def new(venv_name: str, python: str) -> None:
    """Create a new virtualenv"""
    rc = create_new_venv(venv_name, COS_VENV_DIR, python)
    if rc == 0:
        click.echo(click.style("Virtualenv created successfully",
                               fg="green"), file=sys.stdout)
        sys.exit(0)

    else:
        click.echo(click.style("Some error occurred",
                               fg="red"), file=sys.stderr)
        sys.exit(1)


@cli.command()
@click.argument("venv_name", type=str, )
def rm(venv_name: str) -> None:
    """Remove a virtual env"""
    if check_venv_exists(venv_name):
        remove_venv(venv_name)
        click.echo(click.style(f"Virtualenv {venv_name!r} removed successfully",
                               fg="green"), file=sys.stdout)
        sys.exit(0)

    else:
        venv_does_not_exist_msg(venv_name)


@cli.command()
def ls():
    """List all the venv created by 'cos venv'"""
    list_venvs()
