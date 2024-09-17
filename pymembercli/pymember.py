from dataclasses import dataclass
from datetime import datetime
from .util import colorize
import argparse
import json


@dataclass
class TaskItem:
    name: str
    desc: str
    status: str
    start_date: datetime
    end_date: datetime


def main():
    print(colorize("hiiiiii", "yellow"))


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="A tool for todo-list keeping and helpful reminders")
