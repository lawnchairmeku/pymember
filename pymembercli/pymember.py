from platformdirs import user_data_dir
from .task_item import TaskItem
from pathlib import Path
from . import cmds
import argparse
import json


def main():
    path = user_data_dir("pymembercli", "mekumotoki")
    args = make_parser()
    tasks = load_file(path)
    tasks = handle_args(tasks, args)
    # save before exit
    with open(path+'/tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4, default=vars)


def load_file(path) -> list:
    """Loads the tasks.json file and returns it as an object."""
    tasks = []
    Path(path).mkdir(parents=True, exist_ok=True)
    # check if file already exists
    try:
        open(path+'/tasks.json', 'x')
    except FileExistsError:
        with open(path+'/tasks.json') as file:
            data = json.load(file)
            for i, d in enumerate(data):
                t = TaskItem(id=i, name=d['name'], desc=d['desc'],
                             status=d['status'], start_date=d['start_date'])
                tasks.append(t)
    return tasks


def make_parser() -> argparse.Namespace:
    """Setup the CLI"""
    parser = argparse.ArgumentParser(
        description="A tool for todo-list keeping and helpful reminders.",
        prog="pymember")

    subparsers = parser.add_subparsers(dest='command')

    ls = subparsers.add_parser('ls', help='list tasks')
    ls.add_argument(
        'lstype', type=str, choices=['all', 'todo', 'doing', 'done'],
        default='all', nargs='?')

    add = subparsers.add_parser('new', help='add a new task to the list')
    add.add_argument('taskname', type=str, help='name of task')
    add.add_argument('-d', '--desc', type=str, help='set a description')

    set_state = subparsers.add_parser('set', help='set the status of task(s)')
    set_state.add_argument('taskids', type=int,
                           nargs="+", help='taskid(s) to set')
    set_state.add_argument('status', type=str, choices=[
                           'todo', 'doing', 'done'])

    del_task = subparsers.add_parser('del', help='delete task(s)')
    del_task.add_argument('-id', dest='taskids', type=int, nargs="+",
                          help='taskid(s) to delete')
    del_task.add_argument('-grp', dest='taskgrp', type=str,
                          choices=['all', 'todo', 'doing', 'done'],
                          help='taskgrp to delete')

    return parser.parse_args()


def handle_args(tasks, args) -> list:

    match args.command:
        case 'ls':
            cmds.list_tasks(args.lstype, tasks)
        case 'new':
            if args.desc is not None:
                cmds.add_task(name=args.taskname, desc=args.desc, tasks=tasks)
            else:
                cmds.add_task(name=args.taskname, tasks=tasks)
        case 'set':
            cmds.set_task(taskids=args.taskids, group=args.status, tasks=tasks)
        case 'del':
            if args.taskids is not None:
                tasks = cmds.del_task_by_id(args.taskids, tasks=tasks)
            if args.taskgrp is not None:
                tasks = cmds.del_task_by_grp(args.taskgrp, tasks=tasks)

    return tasks
