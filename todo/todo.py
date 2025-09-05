tasks = []

#Functions
def show_tasks(tasks):
    if not tasks:
        print("\033[94mTask list is empty.\033[0m")
    else:
        print(f"\n\033[1;94mMy Tasks:\033[0m")
        for i, task in enumerate(tasks, 1):
            print(f"\t\033[35m{i}. {task}\033[0m")

def remove_tasks(functions):
        if functions.lower() in ["1","remove"]:
            task_remove = input("Enter Task's name to remove it: ").title()
            try:
                tasks.remove(task_remove)
                print(f"\n{task_remove.title()} removed from the tasks\n")
                # show_tasks(tasks)

            except ValueError:
                print(f"\n\033[1;91mTask doesn't exist in the Tasks.\033[0m")
                # show_tasks(tasks)
        print("\n\033[1;92mTasks Updated\033[0m\n")

def  reverse_tasks(functions):
    if functions.lower() in ["4","reverse"]:
        tasks.reverse()
        print("\n\033[1;34mTask in reverse:\033[0m")
        show_tasks(tasks)
        print("\nTasks are reversed.")

def sort_tasks(functions):
    if functions.lower() in ["3", "sort"]:
        tasks.sort()
        print(f"\nTask have been sorted:")
        show_tasks(tasks)

def clear_tasks(functions):
    tasks.clear()
    print("\n\033[1;91mAll tasks are cleared.\033[0m")

print("\n\033[1;92m------TO-DO List app------\033[0m\n")
print("\n\033[1;92m------Add Task------\033[0m\n")

#add
def main():
    while True:
        user = input("Enter Tasks or \033[1;91m'stop'\033[0m to exit: ").strip()
    
        if not user:
            print("\033[1;93mEmpty task not allowed!\033[0m")
            continue

        if user.lower() == "stop":
            print(f"\n\033[1;91mTasks cannot be added further.\033[0m\n")
            break

        add = user.title()
        tasks.append(add)

main()


while True:
    print("\n\033[1;92mMenu:\033[0m")
    print('''\033[1;93m1. Remove task.           2. Show task.\n3. Sort 'A to Z'.         4. Reverse task.\n5. Clear task.            6. Add tasks.\033[0m''')
    functions = input("\nEnter function's number or name (or \033[1;94m'q'\033[0m to exit): ")
    if functions.lower() in ["1","remove"]:
        remove_tasks(functions)
    elif functions.lower() in ["2", "show"]:
        show_tasks(tasks)
        print("\n")
    elif functions.lower() in ["3", "sort"]:
        sort_tasks(functions)
    elif functions.lower() in ["4", "reverse"]:
        reverse_tasks(functions)
    elif functions.lower() in ["5", "clear"]:
        clear_tasks(functions)
    elif functions.lower() in ["6", "add tasks"]:
        print("\nAdd tasks:")
        main()
    elif functions.lower() == "q":
        break
print("\n\033[91mFunction Closed.\033[0m\n")


