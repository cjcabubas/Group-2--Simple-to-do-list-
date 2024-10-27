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

# Main Program
login = checkuser()

if login == 1:
    check_user_id = input("Enter User ID: ")
    check_password = input("Enter Password: ")
    user_name = check_credentials(check_user_id, check_password)
    
    if user_name:
        print(f"Credentials are valid. Welcome, {user_name}!")
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
