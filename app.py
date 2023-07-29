from classes import Task
from functions import add_task, find_by_category, find_task, remove_task, update_task, view_task


while True:
    option = input("""              
1. Add New Task
2. View Tasks
3. Find Task
4. Find by Category 
5. Update Task
6. Remove Task
7. Exit
                   
                Choice: """)
    print()
    if option == '1':
        name = input("Task name: ")
        user = input("Task user: ")
        category = input("Category: ")
        task_info = input("Task info: ")
        add_task(Task(name=name, user=user,
                      category=category, task_info=task_info))
        print("New Task Added")

    elif option == '2':
        view_task()
    elif option == '3':
        name = input("Task name: ")
        find_task(name=name)
    elif option == '4':
        category_name = input("Category name: ")
        find_by_category(name=category_name)
    elif option == '5':
        update_task()
    elif option == '6':
        name = input("Task name: ")
        remove_task(name=name)
    elif option == 'q':
        print("Application closed\n")
        break
