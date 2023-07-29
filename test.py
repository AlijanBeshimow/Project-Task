import random
from classes import Task
from files import load_tasks
from functions import add_task, find_by_category, find_task, update_task, view_task, remove_task


def create_task(num: int = 0):
    for _ in range(num):
        name = random.choice(["go to work", "go to meeting",
                             "check a mail", "print a document", "do a thing"])
        user = random.choice(["avi", "tal", "gal", "raz", "alex", "roni"])
        task_info = 'wwww'
        category = 'job'
        add_task(Task(name=name, user=user,
                 task_info=task_info, category=category))
        view_task()


def found_task(name="name"):
    tasks = load_tasks()
    for task in tasks:
        if name == task.name:
            return task
    else:
        return print("Task not found")


def test():
    test_task = Task(name="test something")
    add_task(test_task)
    if found_task(test_task.name):
        print("Added success")
    else:
        print("Add failed")


find_task("go to work")

find_by_category("job")

remove_task("test something")

update_task()

test()

view_task()
