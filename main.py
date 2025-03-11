import random
import string
import os
                                                                                  os.system("clear" if os.name == "posix" else "cls")


GREEN = "\033[92m"
RESET = "\033[0m"

logo = """
______               _____                           _
| ___ \             |  __ \                         | |
| |_/ /_ _ ___ ___  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __
|  __/ _` / __/ __| | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \ | |_\ \  __/ | | |  __/ | | (_| | || (_) | |
\_|  \__,_|___/___/  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|
"""

developer_info = """
-------------------------------------
 Developer : Tausif Zaman
 Github    : github.com/tausifzaman
-------------------------------------
"""

special_characters = "&@#*!%"

def generate_password(length):
    if length < 6:
        print("\n[!] Password length should be at least 6 characters for security.\n")
        return None

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(special_characters)
    ]


    all_characters = string.ascii_letters + string.digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    print(logo)
    print(developer_info)

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)

            if password:
                print(f"\n[+] Generated Secure Password: {GREEN}{password}{RESET}")
                break
        except ValueError:
            print("\n[!] Please enter a valid number.")

if __name__ == "__main__":
    main()
