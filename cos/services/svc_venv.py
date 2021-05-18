import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict

import click
from rich.console import Console
from rich.table import Table

from cos.utils import create_folder
from cos.utils import create_json_file

# constants
VENV_META = os.path.join(
    Path(os.path.dirname(__file__)).parent, "meta", "venv")

# make the directory is it does not exists
create_folder(VENV_META)

# make the venvs.json file if ot does not exists
json_file = os.path.join(VENV_META, "venvs.json")
create_json_file(json_file)


def get_venv_data() -> Dict[str, str]:
    with open(os.path.join(VENV_META, "venvs.json"), "r") as f:
        return json.load(f)


def update_venv_data(data: Dict[str, str]) -> None:
    with open(os.path.join(VENV_META, "venvs.json"), "w") as f:
        json.dump(data, f)


def list_venvs() -> None:
    table = Table(title="Virtualenv")
    table.add_column("venv           ", justify="center",
                     style="cyan", no_wrap=True)

    for venv in get_venv_data().keys():
        table.add_row(venv)

    console = Console()
    console.print(table)


def check_venv_exists(env_name: str) -> bool:
    return True if env_name in get_venv_data().keys() else False


def _add_venv_to_list(env_name: str, path: str) -> None:
    data = get_venv_data()
    data[env_name] = path
    update_venv_data(data)


def _remove_venv_from_list(env_name: str) -> None:
    data = get_venv_data()
    del data[env_name]
    update_venv_data(data)


def create_new_venv(env_name: str, path: str, python: str) -> int:
    cmd = f"virtualenv {os.path.join(path, env_name)} -p {python} -qq"
    p = subprocess.run(cmd, shell=True, capture_output=True)
    rc = p.returncode

    if rc == 0:
        _add_venv_to_list(env_name, path)
        return rc

    return rc


def remove_venv(env_name: str) -> None:
    venv_dir = os.path.join(get_venv_data()[env_name], env_name)
    shutil.rmtree(venv_dir, ignore_errors=True)
    _remove_venv_from_list(env_name)


def venv_does_not_exist_msg(venv_name: str) -> None:
    click.echo(click.style(
        f"Virtualenv {venv_name!r} does not exists", fg="red"), file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    a = create_new_venv("test", "./test", "3.9")
    print(a)
