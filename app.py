from tasks import todo_list, create_task,delete_all_tasks,delete_task,mark_as_finished,run_tasks
from accounts import accounts, add_account,login
if __name__ == "__main__":
    name = input(str("Enter your name: "))
    if not name:
        name = 'tests'
    password = input(str("Enter your password: "))
    if login(name,password) == True:
        while login(name,password)== True:
            print("Select Option:")
            print()
            print("     1: Creating a Task")
            print("     2: Deleting a Task")
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
    else:
        add_account(name,password)
        print("welcome "+ name)
        print("Account successuly created!!")
        run_tasks()
        



