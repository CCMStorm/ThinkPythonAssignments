# NAME: task_manager.py
# PROJECT: Personal Task Manager (Feature: History)

HISTORY_FILE = "completed_tasks.txt"


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


def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.\n")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter the number of the task to complete: "))

        if 1 <= choice <= len(tasks):
            completed_task = tasks.pop(choice - 1)

            # Save to history file
            with open(HISTORY_FILE, "a") as file:
                file.write(completed_task["name"] + "\n")

            print("Task completed and saved to history.\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def view_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No completed tasks yet.\n")
        else:
            print("\nCompleted Tasks:")
            for line in lines:
                print("- " + line.strip())
            print()

    except FileNotFoundError:
        print("No history file found yet.\n")


def main():
    tasks = []

    while True:
        print("Personal Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. View Completed History")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            view_history()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
