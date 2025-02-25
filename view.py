from controller import *

def translate_error_code(code):
    errors = {
        2: "Invalid name length.",
        3: "Email exceeds 200 characters.",
        4: "Invalid password length.",
        5: "Email already registered.",
        6: "Internal system error."
    }
    return errors.get(code, "Unknown error.")


def display_menu():
    print("\n===========[MENU]===========\n")
    print("Enter 1 to REGISTER")
    print("Enter 2 to LOGIN")
    print("Enter 3 to EXIT")
    return int(input("Enter your choice: "))


def register_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    result = ControllerRegister.register(name, email, password)
    if result == 1:
        print("\nRegistration successful!")
    else:
        print(translate_error_code(result))


def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    result = ControllerLogin.login(email, password)
    if result:
        print("\nLogin successful:", result)
    else:
        print("Invalid email or password.")


