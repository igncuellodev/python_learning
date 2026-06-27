

def register():
    created_username = input("Create your username:\n")
    created_password = input("Create your password " + created_username + ":\n")
    repeat_created_password = input("Repeat your password " + created_username + ":\n")

    while repeat_created_password != created_password:
        print("Your passwords doesnt match, Try again.")
        created_username = input("Create your password " + created_username + ":\n")
        repeat_created_password = input("Repeat your password " + created_username + ":\n")

    else:
        print("Your registration was successfull")
        return created_username, created_password

def login(created_username, created_password):
    username = input("Username:\n")
    password = input("Password:\n")

    while username != created_username or password != created_password:
        print("Either the username or password are incorrect:\n")
        username = input("Username:\n")
        password = input("Password:\n")

    else:
        print("Welcome back!")



created_username, created_password = register()
login(created_username, created_password)