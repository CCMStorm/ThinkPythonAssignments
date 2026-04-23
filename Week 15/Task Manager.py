# NAME: task_manager.py
# PROJECT: Personal Task Manager (Base Build)

def add_task(tasks):
    name = input("Enter task name: ").strip()

    while True:
        priority = input("Enter priority (1 = High, 2 = Medium, 3 = Low): ").strip()
        if priority in ["1", "2", "3"]:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

    task = {
        "name": name,
        "priority": int(priority)
    }

    tasks.append(task)
    print("Task added successfully.\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        priority_label = {1: "High", 2: "Medium", 3: "Low"}[task["priority"]]
        print(f"{i}. {task['name']} (Priority: {priority_label})")
    print()


def main():
    tasks = []

    while True:
        print("Personal Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()