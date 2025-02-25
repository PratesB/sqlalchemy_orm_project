from view import display_menu, register_user, login_user


def main():
    while True:
        option = display_menu()
        if option == 1:
            register_user()
        elif option == 2:
            login_user()
        elif option == 3:
            break


if __name__ == "__main__":
    main()