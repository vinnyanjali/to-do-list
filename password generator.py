import random
import string

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the length is at least 8 characters
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None
    # Generate the password using random.choices()
    password = ''.join(random.choices(characters, k=length))

    return password

# Main program
while True:
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)

        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

    another = input("Generate another password? (yes/no): ").lower()
    if another != "yes":
        break
