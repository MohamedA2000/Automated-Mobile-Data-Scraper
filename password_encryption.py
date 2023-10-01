import bcrypt
import os


# Get the password from the environment variable
password = os.environ.get('KPass')


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def check_password(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)


# Set the username
username = os.environ.get('KUser')


def hash_username(username):
    salt = bcrypt.gensalt()
    hashed_username = bcrypt.hashpw(username, salt)
    return hashed_username


def check_username(username, hashed_username):
    return bcrypt.checkpw(username, hashed_username)

# Hash the password
hashed_password = hash_password(password.encode('utf-8'))

# Hash the username
hashed_username= hash_username(username.encode('utf-8'))


# Check password
if check_password(password.encode('utf-8'), hashed_password):
    print("Password is cddorrect!")
else:
    print("Password is incdorrect!")

# Check username
if check_username(username.encode('utf-8'), hashed_username):
    print("username is coddrrect!")
else:
    print("username is incddorrect!")


