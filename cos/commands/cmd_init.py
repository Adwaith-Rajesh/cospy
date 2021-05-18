import sys
from pathlib import Path

import click

from cos.config import AUTHOR_EMAIL
from cos.config import AUTHOR_NAME
from cos.services.svc_init import get_langs_and_licenses
from cos.services.svc_init import Init


@click.command()
@click.option("-l", "--language", type=str, help="The language used in the project")
@click.option("-n", "--name", type=str, help="The name of the project")
@click.option("--license", type=str, help="The LICENSE to use", default="mit", show_default=True)
@click.option("-d", "--directory", type=str, help="The directory to create all the starter files and folders.", default=".", show_default=True)
@click.option("--env", help="Create a virtual env for Python projects", is_flag=True)
@click.option("--no-git", type=bool, is_flag=True, default=False, help="Do not initialize a git repo", show_default=False)
def cli(language: str, name: str, directory: str, license: str, env: bool, no_git: bool) -> None:
    """Start a new project in any language"""

    if not Path(directory).is_dir():
        click.echo(click.style(
            f"Directory {directory!r} does not exists.", fg="red", bold=True), file=sys.stderr)
        sys.exit(1)

    langs_and_lice = get_langs_and_licenses()

    if name and language:
        if language in langs_and_lice["langs"]:
            if license.lower() not in langs_and_lice["lice"]:
                click.echo(click.style(
                    "unrecognized license. Using MIT instead.", fg="yellow"))
                click.echo(click.style(
                    f"Available Licenses: {langs_and_lice['lice']}"))

                license = "mit"

            init = Init()
            init.name = name
            init.author = AUTHOR_NAME
            init.author_email = AUTHOR_EMAIL
            init.directory = directory
            init.license = license
            init.make_env = env
            init.language = language
            init.git = not no_git
            init.start_project()

        else:
            click.echo(click.style("unrecognized language.", fg="red"))
            click.echo(click.style(
                f"Available languages: {langs_and_lice['langs']}"))

    else:
        click.echo(click.style(
            "Name and language are required.", fg="red"))
