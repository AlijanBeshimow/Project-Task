from classes import Task
from files import load_tasks, save_tasks


def add_task(task: Task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)


def view_task():
    tasks = load_tasks()
    for task in tasks:
        print(task)


def find_task(name="name"):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if name == task.name:
            print(task)
            found = True
    if not found:
        print("Task not found")


def remove_task(name="name"):
    tasks = load_tasks()
    removed = False
    for task in tasks.copy():
        if name == task.name:
            tasks.remove(task)
            save_tasks(tasks)
            removed = True
    if removed:
        print("Task removed")
    else:
        print("Task not found")


def find_by_category(name="name"):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if name == task.category:
            print(task)
            found = True
    if not found:
        print("Category not found")


def update_task():
    tasks = load_tasks()
    user_input = input("Enter USER name to update details: ")
    print()
    for task in tasks:
        if user_input == task.user:
            option = input(f"""
What you want to update for User: {task.user.capitalize()}

1. Task Name  
2. User name
3. Task Category 
4. Task info
5. Change All
6. Exit

             Choice: """)
            print()
            if option == '1':
                task.name = input("New task name: ")
                print("Task name updated")
            elif option == '2':
                task.user = input("New User name: ")
                print("User name updated")
            elif option == '3':
                task.category = input("New task category: ")
                print("Task category updated")
            elif option == '4':
                task.task_info = input("New Task information: ")
            elif option == '5':
                task.name = input("New Task name: ")
                task.user = input("New Task user: ")
                task.category = input("New Task category: ")
                task.task_info = input("New Task info: ")
                print("All details changed")
            save_tasks(tasks)
            break
    else:
        print("User not found.Please try again.")
