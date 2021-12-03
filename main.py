import hashlib
import string
import json
import secrets

def gen_salt():
    """ 
    1. Generate a random string of 32 characters made up of letters, numbers and symbols.
    2. Return the salt.
    """
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    salt = ''.join(secrets.choice(chars) for _ in range(32))
    return salt


def hash_pass(password, salt):
    """ 
    1. Create a new object of the class hashlib.sha512().
    2. It encodes the password string as UTF-8.
    3. It encodes the salt string as UTF-8.
    6. It combines both strings and hashes them.
    7. It returns the full hash string.
    """
    hashed = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    full_hash = hashed + salt
    return full_hash


def sign_up():
    """ 
    1. Create a variable called 'username'.
    2. Get input from the user with 'input'.
    3. Save the input in the variable 'username'.
    4. Open the file 'db.json' in read mode.
    5. Load the contents of the file into a variable called 'db'.
    6. Check if the username already exists in the database.
    7. If the username doesn't exist in the database, create a new user with the username and password, with salt.
     """
    username = input('Username: ')
    password = input('Password: ')

    with open('db.json', 'r') as f:
        db = json.load(f)

    if username in db:
        print('User already exists')
    else:
        salt = gen_salt()
        hashed = hash_pass(password, salt)

        with open('db.json', 'r') as f:
            db = json.load(f)
        db[username] = {'password': hashed, 'salt': salt}
        with open('db.json', 'w') as f:
            json.dump(db, f)

        print('User created successfully')


def log_in():
    """ 
    1. Open db.json.
    2. Load the contents of the file into the variable db.
    3. Ask the user for the username and password.
    4. Use the hash_pass function to hash the password.
    5. Check if the username is in the db.
    6. If the username is in the db, then check if the password is correct
    7. Check if the password is correct.
    """
    username = input('Username: ')
    password = input('Password: ')

    with open('db.json', 'r') as f:
        db = json.load(f)

    if username in db:
        if db[username]['password'] == hash_pass(password, db[username]['salt']):
            print('Login successful')
        else:
            print('Wrong password')
    else:
        print('User not found')


while True:
    """
    1. Asks the user to input the login or signup.
    2. Checks if the input is login or signup, if it is not login or signup it repeats the loop.
    3. If the input is login, it runs the login function.
    4. If the input is signup, it runs the signup function.
    5. It repeats the loop.
    """
    r = input('Login or Signup?\n')
    r = r.lower()
    if r == 'login':
        log_in()
        break
    elif r == 'signup':
        sign_up()
        break
    else:
        print('Invalid input')
