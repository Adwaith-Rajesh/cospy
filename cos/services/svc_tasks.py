from pathlib import Path
from contextlib import suppress
import os
import json

from typing import Dict
from typing import List
from typing import Union

import click

# types
TASK_DATA_TYPE = Dict[str, Dict[str, Union[List[str], Dict[str, str]]]]

# constants
TASKS_META = os.path.join(
    Path(os.path.dirname(__file__)).parent, "meta", "tasks")

# make the directory is it does not exists
Path(TASKS_META).mkdir(exist_ok=True, parents=True)

# make the tasks.json file if ot does not exists
json_file = os.path.join(TASKS_META, "tasks.json")
if not Path(json_file).is_file:
    with open(json_file, "w") as f:
        json.dump({}, f, indent=4)


def get_tasks_data() -> TASK_DATA_TYPE:
    with open(os.path.join(TASKS_META, "tasks.json"), "r") as f:
        return json.load(f)


def check_grp_exists(group_name: str) -> bool:
    data = get_tasks_data()
    return True if group_name in data else False


def update_tasks_data(data: TASK_DATA_TYPE) -> None:
    with open(os.path.join(TASKS_META, "tasks.json"), "w") as f:
        json.dump(data, f, indent=4)


def create_new_group(group_name: str) -> None:

    if not check_grp_exists(group_name):
        data = get_tasks_data()
        try:
            data[group_name] = {"data": {}, "done": []}
            update_tasks_data(data)
            click.echo(click.style(
                f"Group {group_name!r} created successfully.", fg="green"))
        except Exception:
            pass
    else:
        click.echo(click.style(
            f"Group {group_name!r} already exists.", fg="yellow"))


def delete_group(group_name: str) -> None:
    if check_grp_exists(group_name):
        data = get_tasks_data()
        with suppress(KeyError):
            del data[group_name]
            update_tasks_data(data)
            click.echo(click.style(
                f"Group {group_name!r} deleted successfully.", fg="green"))

    else:
        click.echo(click.style(
            f"Group {group_name!r} does not exists.", fg="yellow"))


class Tasks:

    """Edit tasks group"""

    def __init__(self, group_name: str) -> None:
        self.group = group_name
        self.data = get_tasks_data()
        self.group_data = self.data.get(self.group).get("data")
        self.done_data = self.data.get(self.group).get("done")

    def add(self, task: str) -> None:
        _id = self.gen_id()
        self.data[self.group]["data"][_id] = task
        self.update()
        click.echo(click.style(f"Task added successfully! ", fg="green"))
        self.print_task_update_message(str(_id), task)

    def remove(self, _id: str):
        try:
            task = self.data[self.group]["data"][_id]
            del self.data[self.group]["data"][_id]
            with suppress(ValueError):
                self.data[self.group]["done"].remove(_id)
            self.update()
            click.echo(click.style(f"Task removed successfully! ", fg="green"))
            self.print_task_update_message(_id, task)
        except KeyError:
            click.echo(click.style(
                f"Task with ID {_id!r} does not exist", fg="yellow"))

    def done(self, _id: str):
        if _id in self.group_data and _id not in self.done_data:
            self.data[self.group]["done"].append(str(_id))
            self.update()

            task = self.data[self.group]["data"][_id]
            self.print_task_update_message(_id, task)
            click.echo(click.style("Marked as Done", fg="green"))

    def update(self) -> None:
        update_tasks_data(self.data)

    def gen_id(self) -> int:
        # gen a key for the task in a grp
        try:
            max_n = int(max(self.group_data.keys()))
        except ValueError:  # occurs when grp data is empty
            max_n = -1

        return max_n + 1

    @staticmethod
    def print_task_update_message(_id: str, task: str) -> None:
        click.echo(click.style(f"ID: {_id} - TASKS: {task!r}", fg="blue"))
