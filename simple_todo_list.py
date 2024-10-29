from datetime import datetime

print("Simple To-Do List")

def checkuser():
    while True:
        try:
            check = int(input("Do you have an Account? ([1] Login [2] Sign Up): "))
            if check == 1:
                return 1
            elif check == 2:
                return 2
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_credentials(user_id, password):
    with open("userid.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:  # Ensure each line has 3 parts
                saved_user_id, saved_password, saved_name = parts
                if saved_user_id == user_id and saved_password == password:
                    return saved_name  # Return the name if credentials match
    return None  # Return None if no match

def add_task(user_id):
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(f"{user_id}_tasks.txt", "a") as file:
        file.write(f"{title},{description},{timestamp},Incomplete\n")
    print("Task added successfully!")

def view_tasks(user_id):
    try:
        with open(f"{user_id}_tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, 1):
                    title, description, timestamp, status = task.strip().split(",")
                    print(f"[{idx}] Title: {title}, Description: {description}, Date: {timestamp}, Status: {status}")
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found.")

def mark_task_done(user_id):
    view_tasks(user_id)
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        with open(f"{user_id}_tasks.txt", "r") as file:
            tasks = file.readlines()

        if 0 < task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1].replace("Incomplete", "Complete")
            with open(f"{user_id}_tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except (ValueError, FileNotFoundError):
        print("An error occurred. Make sure to enter a valid task number.")

# Main Program
login = checkuser()

if login == 1:
    check_user_id = input("Enter User ID: ")
    check_password = input("Enter Password: ")
    user_name = check_credentials(check_user_id, check_password)

    if user_name:
        print(f"\nWelcome, {user_name}!")
        while True:
            try:
                choice = int(input("\nWhat would you like to do? ([1] Add Task [2] View Tasks [3] Mark Task as Done [4] Exit): "))
                if choice == 1:
                    add_task(check_user_id)
                elif choice == 2:
                    view_tasks(check_user_id)
                elif choice == 3:
                    mark_task_done(check_user_id)
                elif choice == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Sorry, you're not in our database.")

elif login == 2:
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")
    name = input("Enter your Name: ")

    # Save new user credentials to file
    with open("userid.txt", "a") as file:
        file.write(f"{user_id},{password},{name}\n")
    print("Account created successfully! You can now log in.")
