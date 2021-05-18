import click
from click.types import Choice

from cos.services.svc_clean import Clean


@click.command()
@click.option("-d", "--directory", type=str, default=".", help="The directory to clean", show_default=True)
@click.option("-ct", "--clean-type", type=Choice(["ext", "type"], case_sensitive=False), default="ext", show_default=True,
              help="ext: Group files by extension \t\t\t type: Group files by type")
def cli(directory: str, clean_type: str) -> None:
    """Clean / Sort directory"""

    clean = Clean(directory, clean_type)
    clean.clean()
