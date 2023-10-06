# Define an empty to-do list
todo_list = []

# Function to display the to-do list
def display_todo_list():
    print("To-Do List:")
    if not todo_list:
        print("No tasks to display.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

# Function to update a task in the to-do list
def update_task(index, new_task):
    if index >= 1 and index <= len(todo_list):
        todo_list[index - 1] = new_task
        print(f"Updated task {index}: {new_task}")
    else:
        print("Invalid task index. Please provide a valid index.")

# Function to remove a task from the to-do list
def remove_task(index):
    if index >= 1 and index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Removed task {index}: {removed_task}")
    else:
        print("Invalid task index. Please provide a valid index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        display_todo_list()
    elif choice == "2":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "3":
        index = int(input("Enter the task index to update: "))
        new_task = input("Enter the new task description: ")
        update_task(index, new_task)
    elif choice == "4":
        index = int(input("Enter the task index to remove: "))
        remove_task(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")