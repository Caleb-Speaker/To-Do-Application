def display_menu():
    """Displays the main menu options to the user."""
    print("\n---- To-Do List Application ----")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")
    print("--------------------------------")

def add_task(tasks):
    """Prompts the user to add a new task."""
    task = input("Enter the task description: ")
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """Displays all tasks. Alerts if no tasks exist."""
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to view.")

def delete_task(tasks):
    """Prompts the user to delete a task."""
    if tasks:
        try:
            task_id = int(input("Enter the task number to delete: "))
            if 1 <= task_id <= len(tasks):
                deleted_task = tasks.pop(task_id - 1)
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Error: Please enter a valid number.")
    else:
        print("No tasks to delete.")

def quit_application():
    """Exits the application."""
    print("Exiting the application. Goodbye!")
    exit()

def main():
    """Main function to run the To-Do List application."""
    tasks = [] 
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                quit_application()
            else:
                print("Error: Invalid choice, please select between 1 and 4.")
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
