def user_register():
    user_info = {}
    print("\n\033[35mRegister Here\033[0m\n")
    first_name = input("Enter your First name: ").title()
    user_info["First Name"] = first_name
    last_name = input("Enter your Last name: ").title()
    user_info["Last Name"] = last_name
    email = input("Enter your Email-Id: ")
    if "@" and "." in email:
        print("Valid email id")
    else:
        print("Invalid email id")
    user_info["Email-id"] = email
    username = input("Create your username: ")
    user_info["username"] = username
    password = True
    passcode = input("Create password: ")
    while password:
        if passcode == username:
            print("\033[1;91mUsername and password cannot be same.\033[0m]")
            passcode = input("Try creating again: ")
        elif passcode != username:
            re_enter = input("Enter password again: ")
            user_info["Password"] = re_enter
            break
    print("Registeration Successful")

register = input("Enter 'Yes' for registeration: ").lower()
if register == "yes":
    user_register()
