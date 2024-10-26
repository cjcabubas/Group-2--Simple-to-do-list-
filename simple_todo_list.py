print("simple to do list")

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
            saved_user_id, saved_password = line.strip().split(",")  # Split ID and password
            if saved_user_id == user_id and saved_password == password:
                return True  # Match found
    return False  # No match found

        
login = checkuser()

if login == 1:
    check_user_id = input("Enter User ID to check: ")
    check_password = input("Enter Password to check: ")
 
elif login == 2:
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")

    with open("userid.txt", "a") as file:
        file.write(f"{user_id},{password}\n")


