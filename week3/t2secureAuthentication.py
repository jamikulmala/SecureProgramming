# secure authentication following owasp authentication guidelines

import hashlib # library for secure hashes
import secrets
import zxcvbn # zxcvbn-ts library for python. A password strength meter to help users create a more complex password and block common and previously breached passwords.
import csv

# Generate random 16 byte string salt
def generate_salt():
    return secrets.token_hex(16)

# Hash password with salt using sha256
def hash_password(password, salt):
    combined = password + salt
    hashed_password = hashlib.sha256(combined.encode()).hexdigest()
    return hashed_password

# Function to check password strength using zxcvbn
def check_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    return result['score'] >= 0  # possible 0-4 higher the score higher the security.

# Function to write user credentials to a file
def write_user_credentials(filename, credentials):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Username", "Salt", "HashedPassword"])
        for username, (salt, hashed_password) in credentials.items():
            writer.writerow([username, salt, hashed_password])

# Function to read user credentials from a file
def read_user_credentials(filename):
    credentials = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row["Username"]
            salt = row["Salt"]
            hashed_password = row["HashedPassword"]
            credentials[username] = (salt, hashed_password)
    return credentials

# Function to authenticate a user
def authenticate_user(username, password, credentials_store):

    # Converting to lowercase since usernames should be compared case-insensitively
    username = username.lower()

    # Check if the user exists
    if username in credentials_store:
        stored_salt, stored_password_hash = credentials_store[username]

        # Hash the provided password with the stored salt
        hashed_password = hash_password(password, stored_salt)

        # Check if the hashed password matches the stored hash
        if hashed_password == stored_password_hash:
            # Check password strength
            if not check_password_strength(password):
                return "Weak password! Please choose a stronger password."

            return "Authentication successful!"
        else:
            return "Invalid Password!"
    else:
        return "Invalid Username!"
    

if __name__ == "__main__":

    # Example user data
    credentials_file = "user_credentials.csv"
    user_data = {
        'Jami': 'qwerty123'
    }

    # write hashed user information to file for demonstration
    actual_credentials = {}
    for username, password in user_data.items():
        username_lower = username.lower()  # Convert to lowercase
        salt = generate_salt()
        hashed_password = hash_password(password, salt)
        actual_credentials[username_lower] = (salt, hashed_password)
    write_user_credentials(credentials_file, actual_credentials)

    # Reading user credentials from file
    loaded_credentials = read_user_credentials(credentials_file)

    # Simple example authentication
    username = input("Enter username: ")
    password = input("Enter password: ")

    result = authenticate_user(username, password, loaded_credentials)
    print(result)