import random
import string

def generate_password(charCount):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():

    charCount = int(input("Enter the length of the random password needed: "))


    password = generate_password(charCount)


    print("Random Password:", password)

if __name__ == '__main__':
    main()