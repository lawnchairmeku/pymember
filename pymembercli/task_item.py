from dataclasses import dataclass
from pympmyansi import pymp


@dataclass
class TaskItem:
    """Represents a todo item."""
    id: int
    name: str
    desc: str
    status: str
    start_date: str

    def __repr__(self):
        newname = self.name
        newstatus = self.status
        newdesc = pymp(self.desc, 'dark_gray')
        newdate = pymp(self.start_date, 'purple')
        if self.status == 'todo':
            newname = pymp(newname, 'red')
            newstatus = pymp(newstatus, 'red')
        elif self.status == 'doing':
            newname = pymp(newname, 'yellow')
            newstatus = pymp(newstatus, 'yellow')
        elif self.status == 'done':
            newname = pymp(newname, 'green')
            newstatus = pymp(newstatus, 'green')
        reprstr = str(self.id) + ". " + newname + " |  " + newdesc + \
            "\n" + newstatus + "  added: " + newdate
        return reprstr
