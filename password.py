import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Welcome to the Password Generator!")
    num_passwords = int(input("How many passwords would you like to generate? "))
    length = int(input("Enter the length of each password: "))
    
    print("\nHere are your passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

if __name__ == "__main__":
    main()
