import hashlib
import argparse

# The goal here is to make a simple password hasher that would allow me to break simple passwords through brute-force attacks.    

def main(): # Provides the basics for command line usage
    parser = argparse.ArgumentParser(description="Password Cracker") # Initializes Parser object
    parser.add_argument("--target", help="Target hash to crack", required=True) # Input 1: target hash you would like to crach
    parser.add_argument("--algorithm", help="Hash algorithm (e.g. sha256)", required=True) # Input 2: Type of hash algorithm you're using
    parser.add_argument("--wordlist", help="Path to wordlist file", required=True) # Input 3: Type of 
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

if __name__ == "__main__":
    main()

print("What type of passcode would you like to crack?")
print("[1] - 4 to 6 digit PIN")
print("[2] - Password")
choice = input().strip()
if  choice == "1":
    print("You have selected PIN mode. Please input the length of the PIN")
    print("[1] - 4 digits")
    print("[2] - 5 digits")
    print("[3] - 6 digits")
    pinCount = input().strip()
    if pinCount == "1":
        print("You have selected 4 digits")
        #4_digits()
    elif pinCount == "2":
        print("You have selected 5 digits")
        #5_digits()
    elif pinCount == "3":
        print("You have selected 6 digits")
        #6_digits()
    else:
        print("Invalid input. Please select 1, 2, or 3.")
    break
elif choice == "2":
    print("You have selected Password mode")
    password()
    break
else:
    print("Invalid input. Please select 1 or 2.")

