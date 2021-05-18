import os
from typing import Iterable
from typing import Optional

import click
from click import Command
from click import Context


class Commands(click.MultiCommand):

    def list_commands(self, ctx: Context) -> Iterable[str]:
        commands = []
        commands_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace(
                    "cmd_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx: Context, cmd_name: str) -> Optional[Command]:
        try:
            mod = __import__(
                f"cos.commands.cmd_{cmd_name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=Commands)
def cli():
    """Welcome to cos"""
    pass
