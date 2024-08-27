import random
import string

def generate_password(length=12):
    #define character to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("enter the desired password length: "))


    if password_length < 6:
        print("password length must be atleast a 6 character. ")
    else:
        generate_password = generate_password(password_length)

        print("generate password:",generate_password)