import hashlib
import random
import string
import json


def gen_salt():
    salt = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
    return salt


def hash_pass(password, salt):
    hashed = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    full_hash = hashed + salt
    return full_hash


def sign_up():
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