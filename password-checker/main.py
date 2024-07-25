import hashlib
import json


def save_password(data):
    try:
        with open("password-checker/password.json", "w", buffering=1024) as f:
            json.dump({"password": data}, f, indent=2)
    except:
        return None


def generate_hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_password(password):
    hashed_password = generate_hash(password)
    save_password(hashed_password)

    return hashed_password 


def check_password(password):
    try:
        with open("password-checker/password.json", "rb") as f:
            previous_password = json.load(f)
            hashed_data = generate_hash(password)
            return previous_password["password"] == hashed_data
    except:
        return None


password = input("Create a password: ")

create_password(password)
loop = True

while loop:
    user_operation = input(
        "\nPress 's' to create a new password and press 'c' to check the passowrd: "
    )
    user_operation = user_operation.lower()

    if user_operation == "s":
        password = input("Enter a password: ")
        create_password(password)
    elif user_operation == "c":
        password = input("Enter you password: ")
        print(check_password(password))
    elif user_operation == "x":
        loop = False
    else:
        print("Enter a valid command")
        save_password(None)


print("Terminated")
