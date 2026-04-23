# NAME: dream_tool.py
# PROJECT: 3D Print Filament & Project Tracker

import csv
import os

FILE_NAME = "print_projects.csv"
SUMMARY_FILE = "project_summary.txt"


def setup_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Project Name",
                "Filament Used (g)",
                "Spool Cost",
                "Spool Weight (g)",
                "Estimated Cost"
            ])


def get_float(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt).strip())

            if value < 0:
                print("Please enter a positive number.")
            elif value == 0 and not allow_zero:
                print("This value cannot be zero.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_project_name():
    while True:
        project_name = input("Enter project name: ").strip()

        if project_name == "":
            print("Project name cannot be empty.")
        else:
            return project_name


def add_project():
    project_name = get_project_name()

    filament_used = get_float("Enter filament used in grams: ")
    spool_cost = get_float("Enter spool cost in dollars: ")
    spool_weight = get_float("Enter spool weight in grams: ", allow_zero=False)

    estimated_cost = filament_used * (spool_cost / spool_weight)

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
    setup_file()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No projects saved yet.")
        return

    print("\nSaved 3D Print Projects:")
    for row in rows[1:]:
        if len(row) == 5:
            print(f"- {row[0]} | Filament: {row[1]}g | Estimated Cost: ${row[4]}")
    print()


def total_cost():
    setup_file()

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                total += float(row["Estimated Cost"])
            except ValueError:
                print("Skipped a row with invalid cost data.")

    print(f"Total estimated filament cost for all projects: ${total:.2f}")


def export_summary():
    setup_file()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        projects = list(reader)

    if len(projects) == 0:
        print("No projects to export.")
        return

    with open(SUMMARY_FILE, "w") as file:
        file.write("3D Print Project Summary\n")
        file.write("------------------------\n")

        for project in projects:
            file.write(
                f"{project['Project Name']} - "
                f"{project['Filament Used (g)']}g used - "
                f"${project['Estimated Cost']} estimated cost\n"
            )

    print(f"Summary exported to {SUMMARY_FILE}")


def main():
    setup_file()

    while True:
        print("\n3D Print Filament & Project Tracker")
        print("1. Add Print Project")
        print("2. View Saved Projects")
        print("3. View Total Filament Cost")
        print("4. Export Project Summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            total_cost()
        elif choice == "4":
            export_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()