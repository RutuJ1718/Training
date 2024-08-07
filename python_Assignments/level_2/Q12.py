#Create a login page backend to ask users to enter the username and password:

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    attempts = 3
    while attempts > 0:
        retype_password = input("Re-Type Password: ")
        if retype_password == password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempts left.")
    print("Login failed.")
    return False

login()
