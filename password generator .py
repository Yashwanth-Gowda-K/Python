import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("---------->This is the password generator!<----------")

    while True:
        try:
            length =int(input("Enter the password length: "))
            if length <4:
                print("Password must be grater than 4")
            else:
                break
        except ValueError:
            print("Enter the correct number.")

    password =password_generator(length)
    print(f"Your passowrd is---------->:  <----------{password}")
if __name__ == "__main__":
    main()

