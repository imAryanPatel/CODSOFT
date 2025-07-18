import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. [{status}] {task['task']}")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        show_tasks(tasks)
        print("\nOptions: [1] Add  [2] Mark Done  [3] Delete  [4] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_text = input("Enter new task: ")
            tasks.append({"task": task_text, "done": False})
            save_tasks(tasks)

        elif choice == "2":
            num = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]['done'] = True
                save_tasks(tasks)

        elif choice == "3":
            num = int(input("Enter task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_tasks(tasks)

        elif choice == "4":
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
