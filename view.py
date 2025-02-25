from controller import *

print('\n')
while True:
    print("===========[MENU]===========\n")
    enter = int(input(
                        'Enter 1 to REGISTER \n'
                        'Enter 2 to LOGIN \n'
                        'Enter 3 to EXIT \n'))
    

    if enter == 1:
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        result = ControllerRegister.register(name, email, password)

        if result == 2:
            print('Invalid name length.')
        elif result == 3:
            print('Email exceeds 200 characters.')
        elif result == 4:
            print('Invalid password length')
        elif result == 5:
            print('Email already registered.')
        elif result == 6:
            print('Internal system error.')
        elif result == 1:
            print('\n')
            print('Registration successful!')


    elif enter == 2:
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        result2 = ControllerLogin.login(email, password)

        if not result2:
            print('Invalid email or password.')
        else:
            print('\n')
            print(result2)
    
    else:
        break