todo_list = []
task_status = {}

def create_task(task):
    todo_list.append(task)
    task_status[task] = "Ongoing"
    return todo_list
    pass


def delete_task(task):
    for item in todo_list:
        if item == task and item in todo_list:
            todo_list.remove(task)
            print("Task deleted")
            return todo_list
        else:
            return "Item does not exist"
    pass


def mark_as_finished(task):
    for item in todo_list:
        for key,value in task_status.items():
            if key == task:
                task_status[key] = "Finished"
    print(task_status)
    pass

def delete_all_tasks():
    todo_list.clear()
    return todo_list
    pass
def run_tasks():
    print()
    print("     1: Creating a Task".rjust(10))
    print("     2: Deleting a Task".rjust(10))
    print("     3: Deleting all tasks")
    print("     4: Marking a Task Finished")
    print()

    selection = int(input("selection: "))
    if selection == 1:
        task = input("Enter Task: ")
        create_task(task)
        print(task + " added to list")

    elif selection == 2:
        task =  (input("Enter task to delete: "))
        delete_task(task)
        print(todo_list)

            
    elif  selection == 3:
        delete_all_tasks()
        print(todo_list)
        print("List is empty")

    elif selection == 4:
        mark_as_finished(input("Enter Task: "))
    
            







