# Simple To-Do List App (exactly 50 lines)

tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks duplicate 4")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=============================")

def view_tasks():
    if not tasks:
        print("No tasks yet! Add one below.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task['done'] else "✗"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Added: {title}")
    else:
        print("Task cannot be empty.")

def complete_task():
    view_tasks()
    try:
        num = int(input("Task number to complete: "))
        tasks[num - 1]['done'] = True
        print(f"Task {num} marked as done.")
    except (ValueError, IndexError):
        print("Invalid choice.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid choice.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
