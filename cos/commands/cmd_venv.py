import click


@click.command()
@click.option("-n", "--new", is_flag=True, default=False, help="Create a new venv with the given name")
@click.option("-d", "--delete", is_flag=True, default=False, help="Delete the venv with the given name")
@click.option("-")
def cli(new: bool, delete: bool):
    """Manage all your Python venv in a single place"""
    print(f"{new=} {delete=}")
