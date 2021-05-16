import subprocess
import sys


def check_virtual_env_installed() -> bool:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    return "virtualenv" in installed_packages
