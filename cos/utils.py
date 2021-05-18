import json
import subprocess
import sys
from pathlib import Path


def check_virtual_env_installed() -> bool:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    return "virtualenv" in installed_packages


def create_folder(folder_name: str) -> None:
    Path(folder_name).mkdir(exist_ok=True, parents=True)


def create_json_file(filename: str) -> None:
    if not Path(filename).is_file():
        with open(filename, "w") as f:
            json.dump({}, f, indent=4)
