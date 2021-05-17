import os

# INIT API
AUTHOR_NAME = os.environ.get("AUTHOR_NAME", "")
AUTHOR_EMAIL = os.environ.get("AUTHOR_EMAIL", "")
GITHUB_USER = os.environ.get("GITHUB_USER", "")

# venv API
COS_VENV_DIR = os.environ.get("COS_VENV_DIR", os.path.join(
    os.path.expanduser("~"), "cos_venvs"))
