import nltk
from nltk.metrics import edit_distance
from nltk.tokenize import word_tokenize

# Load the dataset of leaked passwords
with open('leaked_passwords.txt', 'r') as f:
    passwords = f.read().splitlines()

# Define a function to search for a password in the dataset using fuzzy matching
def search_leaked_passwords(password):
    for leaked_password in passwords:
        # Use fuzzy matching to compare the two passwords
        distance = edit_distance(password, leaked_password)
        if distance <= 2:  # Set a threshold for fuzzy matching
            return True
    return False

# Define a function to check if the password is weak based on similarity with leaked passwords
def check_password_strength(password):
    password_tokens = word_tokenize(password)
    for token in password_tokens:
        if search_leaked_passwords(token):
            return "weak"
    return "strong"

# Prompt the user to enter their password
user_password = input("Enter your password: ")

# Check if the password is weak based on similarity with leaked passwords
password_strength = check_password_strength(user_password)

# Inform the user whether their password is strong or weak
if password_strength == "weak":
    print("Your password is weak and has been leaked. Please change it immediately!")
else:
    print("Your password is strong and has not been leaked.")
