import json

FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a task
def add_task(tasks):
    task = input("Enter task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Not Done"
        print(i, task["task"], "-", status)


# Mark task as completed
def mark_done(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark as done: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Task does not exist.")

    except ValueError:
        print("Please enter a valid number.")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Task does not exist.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        mark_done(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")