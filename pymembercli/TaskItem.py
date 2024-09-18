from dataclasses import dataclass


@dataclass
class TaskItem:
    id: int
    name: str
    desc: str
    status: str
    start_date: str

    def __repr__(self):
        return self.name
