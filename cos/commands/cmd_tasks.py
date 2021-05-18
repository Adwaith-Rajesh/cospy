import sys

import click

from cos.services.svc_tasks import check_grp_exists
from cos.services.svc_tasks import create_new_group
from cos.services.svc_tasks import delete_group
from cos.services.svc_tasks import print_all_grp_names
from cos.services.svc_tasks import print_all_tasks
from cos.services.svc_tasks import Tasks


@click.group(invoke_without_command=True)
@click.option("-g", "--group", default="", type=str, help="The group to make changes to.")
@click.option("-a", "--add", type=str, help="add a new task.")
@click.option("-r", "--remove", type=str, help="remove a task.")
@click.option("-d", "--done", type=str, help="mark task as done.")
def cli(group: str, add: str, remove: int, done: int) -> None:
    """Manage programming tasks more easily"""
    if group:
        if check_grp_exists(group):
            tasks = Tasks(group)
            if add:
                tasks.add(add)
            if remove:
                tasks.remove(remove)
            if done != None:
                tasks.done(done)

        else:
            click.echo(click.style(
                f"Group {group!r} does not exists.", fg="red", bold=True), file=sys.stderr)
            sys.exit(1)

        # if an action is done on a group then don't move forward to other commands
        exit()


@cli.command()
@click.argument("group_name", type=str)
def new(group_name: str) -> None:
    """Create new task group"""
    create_new_group(group_name)


@cli.command()
@click.argument("group_name", type=str)
def delete(group_name: str) -> None:
    """Delete a task group"""
    delete_group(group_name)


@cli.command()
@click.argument("group_name", type=str, required=False)
def ls(group_name: str):
    """List all the groups or task in a group  cos tasks ls <group-name>[OPTIONAL]"""

    if group_name != None:
        print_all_tasks(group_name)
    else:
        print_all_grp_names()
