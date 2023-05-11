import os
import time
from typing import NoReturn, Union

from utils import cross_out

file_name = "tasks.case"


class Tasks:
    def __init__(self, data: list = None):
        self.tasks = data.copy() if data else []
        self.completed = []

    def add(self, data: str):
        self.tasks.append(data)

    def add_list(self, data: list):
        self.tasks = data.copy() if data else []

    def remove_to_completed(self, index: int):
        self.completed.append(self.tasks[index])
        self.tasks.pop(index)

    def remover_to_tasks(self, index: int):
        self.tasks.append(self.tasks[index])
        self.completed.pop(index)

    def print_tasks(self):
        print("---------------------------------------")

        if self.tasks:
            print("Current tasks:")
            for num, task in enumerate(self.tasks, 1):
                print(f"{num}. {task}")
            print("---------------------------------------\n")

        if self.completed:
            print("Completed tasks:")
            for num, task in enumerate(self.completed, 1):
                print(f"{num}. {cross_out(task)}")
            print("---------------------------------------\n\n")

    def save_tasks_to_file(self, path: Union[os.PathLike, str] = file_name) -> NoReturn:
        with open(path, "w") as file:
            file.write("\n".join(self.tasks))

    def read_tasks_from_file(self, path: Union[os.PathLike, str] = file_name) -> list:
        with open(path, "r") as file:
            data = file.readlines()
            # self.tasks = data
        return data

    @property
    def list(self):
        return self.tasks


if __name__ == "__main__":
    tasks = Tasks()
    data = tasks.read_tasks_from_file(file_name)
    data = map(lambda c: c.replace("\n", ""), data)

    tasks.add_list(list(data))
    # item = "Video downloader program."

    while True:
        command = input("Type 'add (task)' or 'complete (index of task)' or 'tasks': ")
        if command.startswith("add"):
            try:
                arg = command.replace("add ", "", 1)
                if arg:
                    tasks.add(arg)

                tasks.save_tasks_to_file(file_name)
            except IndexError:
                print("Wrong command")

        elif command.startswith("complete"):
            try:
                arg = command.replace("complete ", "", 1)
                tasks.remove_to_completed(int(arg) - 1)

                tasks.save_tasks_to_file(file_name)
            except (IndexError, ValueError):
                print("Wrong command")

        elif command == "tasks":
            tasks.print_tasks()

        else:
            print("Wrong command")
