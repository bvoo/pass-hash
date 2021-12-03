import json
from argon2 import PasswordHasher, Type


def hash_pass(password):
    """
    1. Use the PasswordHasher object, which is the main object used to hash and check passwords.
    2. Memory cost is 512MB, time cost to 4 seconds, and parallelism to 2.
    3. The hash length is 32 characters, and the hash type is Argon2ID.
    4. Hash the password.
    5. Return the hashed password.
    """
    hashed = hasher.hash(password)
    return hashed


def verify_pass(pwhash, password):
    """
    1. It calls the function verify_pass with the hash and password to verify.
    2. If it matches, return True. Otherwise, return False.
    """
    if hasher.verify(pwhash, password):
        return True
    else:
        return False


def sign_up():
    """ 
    1. The user enters their username and password.
    2. The username is checked to see if it already exists.
    3. If the username does not exist, the user is stored with the Argon2 hash of their password.
    """
    username = input('Username: ')
    password = input('Password: ')

    with open('db.json', 'r') as f:
        db = json.load(f)

    if username in db:
        print('User already exists')
    else:
        hashed = hash_pass(password)

        with open('db.json', 'r') as f:
            db = json.load(f)

        db[username] = {'password': hashed}

        with open('db.json', 'w') as f:
            json.dump(db, f)

        print('User created successfully')


def log_in():
    """ 
    1. Opens the json file containing the user database.
    2. Asks the user for their username and password, and stores them in variables.
    3. Checks if the username exists in the database.
    4. If it does, check if the password is correct.
    5. If it is, print a message saying that the login was successful.
    """
    username = input('Username: ')
    password = input('Password: ')

    with open('db.json', 'r') as f:
        db = json.load(f)

    if username in db:
        if verify_pass(db[username]['password'], password):
            print('Login successful')
        else:
            print('Wrong password')
    else:
        print('User not found')


def remove():
    """ 
    The code above does the following, explained in English:
    1. Opens the file db.json in read mode.
    2. Saves the data into a variable.
    3. Checks if the username is in the database.
    4. If it is, checks if the password is correct.
    5. If it is, deletes the user from the database.
    6. Prints a message saying the user has been removed.
    """
    username = input('Username: ')
    password = input('Password: ')

    with open('db.json', 'r') as f:
        db = json.load(f)

    if username in db:
        if verify_pass(db[username]['password'], password):
            del db[username]
            with open('db.json', 'w') as f:
                json.dump(db, f)
            print('User removed successfully')
        else:
            print('Wrong password')
    else:
        print('User not found')


def list_users():
    """
    1. Loads the database into a variable called 'db'.
    2. Opens the database file 'db.json' in read mode.
    3. Prints the list of users.
    """
    with open('db.json', 'r') as f:
        db = json.load(f)
    i = 0
    for name in db:
        i += 1
        print(f'{i}: {name}')

"""
Creates a PasswordHasher object.
Main object used to hash and check passwords.
"""
hasher = PasswordHasher(
    memory_cost=65536,
    time_cost=4,
    parallelism=2,
    hash_len=32,
    salt_len=16,
    type=Type.ID
)

while True:
    """
    1. Asks the user to input the login or signup.
    2. Checks if the input is login or signup, if it is not login or signup it repeats the loop.
    3. If the input is login, it runs the login function.
    4. If the input is signup, it runs the signup function.
    5. It repeats the loop.
    """
    r = input('Login, Signup, Remove or List?\n')
    r = r.lower()
    if r == 'login':
        log_in()
        break
    elif r == 'signup':
        sign_up()
        break
    elif r == 'remove':
        remove()
        break
    elif r == 'list':
        list_users()
        break
    else:
        print('Invalid input')
