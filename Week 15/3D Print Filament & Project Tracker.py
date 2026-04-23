# NAME: dream_tool.py
# PROJECT: 3D Print Filament & Project Tracker

import csv
import os

FILE_NAME = "print_projects.csv"


def setup_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Project Name", "Filament Used (g)", "Spool Cost", "Spool Weight (g)", "Estimated Cost"])


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_project():
    project_name = input("Enter project name: ").strip()

    if project_name == "":
        print("Project name cannot be empty.")
        return

    filament_used = get_float("Enter filament used in grams: ")
    spool_cost = get_float("Enter spool cost in dollars: ")
    spool_weight = get_float("Enter spool weight in grams: ")

    if spool_weight == 0:
        print("Spool weight cannot be zero.")
        return

    cost_per_gram = spool_cost / spool_weight
    estimated_cost = filament_used * cost_per_gram

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            project_name,
            filament_used,
            spool_cost,
            spool_weight,
            round(estimated_cost, 2)
        ])

    print(f"Project saved. Estimated filament cost: ${estimated_cost:.2f}")


def view_projects():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) <= 1:
            print("No projects saved yet.")
            return

        print("\nSaved 3D Print Projects:")
        for row in rows[1:]:
            print(f"- {row[0]} | Filament: {row[1]}g | Estimated Cost: ${row[4]}")
        print()

    except FileNotFoundError:
        print("No saved project file found yet.")


def total_cost():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            total = 0

            for row in reader:
                total += float(row["Estimated Cost"])

        print(f"Total estimated filament cost for all projects: ${total:.2f}")

    except FileNotFoundError:
        print("No saved project file found yet.")


def main():
    setup_file()

    while True:
        print("\n3D Print Filament & Project Tracker")
        print("1. Add Print Project")
        print("2. View Saved Projects")
        print("3. View Total Filament Cost")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            total_cost()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()