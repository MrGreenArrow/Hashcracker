import hashlib
import argparse

# The goal here is to make a simple password hasher that would allow me to break simple passwords through brute-force attacks.

def password():
    parser = argparse.ArgumentParser(description="Password Cracker")
    parser.add_argument("--target", help="Target hash to crack", required=True)
    parser.add_argument("--algorithm", help="Hash algorithm (e.g. sha256)", required=True)
    parser.add_argument("--wordlist", help="Path to wordlist file", required=True)
    args = parser.parse_args()
    
    try:
        with open(args.wordlist, "r", encoding="utf-8") as file:
            for line in file:
                password = line.strip()
                hashed = hashlib.new(args.algorithm, password.encode()).hexdigest()
                if hashed == args.target:
                    print(f"Password found: {password}")
                    return
        print("Password not found in the wordlist")
    except FileNotFoundError:
        print("Wordlist file not found.")
        
if __name__ == "__password__":
    password()

while True:
    print("What type of passcode would you like to crack?")
    print("[1] - 4 to 6 digit PIN")
    print("[2] - Password")
    choice = input().strip()

    if  choice == "1":
        print("You have selected PIN mode")
        break
    elif choice == "2":
        print("You have selected Password mode")
        break
    else:
        print("Invalid input. Please select 1 or 2.")

