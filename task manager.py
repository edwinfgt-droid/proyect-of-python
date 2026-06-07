tasks = []

def display_tasks(all_tasks):
    print("\nYour tasks:")
    if not all_tasks:
        print("  (no tasks yet)")
    for index, task in enumerate(all_tasks):
        print(f"{index + 1}. {task}")


def add_task(all_tasks):
    new_task = input("Add a task: ").strip()
    if new_task:
        all_tasks.append(new_task)
        print("Task added.")
    else:
        print("No task entered.")


def delete_task(all_tasks):
    display_tasks(all_tasks)
    if not all_tasks:
        return
    try:
        index = int(input("Enter task number to delete: "))
        removed = all_tasks.pop(index - 1)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def edit_task(all_tasks):
    display_tasks(all_tasks)
    if not all_tasks:
        return
    try:
        index = int(input("Enter task number to edit: "))
        new_text = input("New task text: ").strip()
        if new_text:
            all_tasks[index - 1] = new_text
            print("Task updated.")
        else:
            print("No changes made.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def new_operation(all_tasks):
    operation = input(
        "Press A to add a task, D to delete a task, V to view all tasks, H to edit a task, G to quit: "
    ).strip().upper()

    if operation == "A":
        add_task(all_tasks)
    elif operation == "D":
        delete_task(all_tasks)
    elif operation == "V":
        display_tasks(all_tasks)
    elif operation == "H":
        edit_task(all_tasks)
    elif operation == "G":
        print("Good bye!")
        exit()
    else:
        print("Unknown option. Please choose A, D, V, H, or G.")


def main():
    while True:
        new_operation(tasks)


if __name__ == "__main__":
    main()
