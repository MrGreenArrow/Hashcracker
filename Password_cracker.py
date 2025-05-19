import hashlib
import argparse

#--------------------------
# Terminal command line
#--------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Password/PIN Cracker") # Initializes Parser object
    
    # Required inputs
    parser.add_argument("--target", help="Target hash to crack", required=True) # Input 1: target hash you would like to crach
    parser.add_argument("--algorithm", help="Hash algorithm (e.g. sha256)", required=True) # Input 2: Type of hash algorithm you're using

    # Mutually exclusive: wordlist OR PIN generation
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pin-length", type=int, choices=[4,5,6], 
                    help="Generate PIN combinations (4, 5, or 6 digits)")
    
    #-----------------------------------------------------------
    # Dev Note: I recommend using the rockyou.txt list. This list can be obtained using the following terminal command:
    # $ wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
    # Note that this file has 14 million entries, so it's hefty.
    #-----------------------------------------------------------
    group.add_argument("--wordlist", help="Path to wordlist file") 
    
    return parser.parse_args()


#--------------------------
# PIN Functions
#--------------------------
def generate_pin_wordlist(length: int):
    # Generates all numeric combinations for a given digit length
    return (''.join(p) for p in itertools.product('0123456789', repeat=length))

def four_digits():
    return generate_pin_wordlist(4)

def five_digits():
    return generate_pin_wordlist(5)

def six_digits():
    return generate_pin_wordlist(6)

def crack_PIN(target_hash: str, algorithm: str, PIN_iter):
    for PIN in PIN_iter:
        hashed = hashlib.new(algorithm, password.encode()).hexdigest()
        if hashed == target_hash:
            return password
    return None

#--------------------------
# Password Functions
#--------------------------
def crack_password(target_hash: str, algorithm: str, password_iter):
    """Core cracking logic (works with any password generator)"""
    for password in password_iter:
        hashed = hashlib.new(algorithm, password.encode()).hexdigest()
        if hashed == target_hash:
            return password
    return None

#--------------------------
# Main Execution
#--------------------------
def main():
    args = parse_arguments()
    
    # Get password iterator (file or generated PINs)
    if args.wordlist:
        try:
            with open(args.wordlist, "r", encoding="utf-8") as f:
                password_iter = (line.strip() for line in f)
        except FileNotFoundError:
            print(f"Error: Wordlist '{args.wordlist}' not found")
            return
    else:
        password_iter = generate_pin_wordlist(args.pin_length)
    
    # Attempt crack
    result = crack_password(args.target, args.algorithm, password_iter)
    
    # Output results
    if result:
        print(f"Success! Password: {result}")
    else:
        print("Password not found")

if __name__ == "__main__":
    main()

#--------------------------
# User Input Tree
#--------------------------

print("What would you like to crack?")
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
        # four_digits()
    elif pinCount == "2":
        print("You have selected 5 digits")
        # five_digits()
    elif pinCount == "3":
        print("You have selected 6 digits")
        # six_digits()
    else:
        print("Invalid input. Please select 1, 2, or 3.")
    break
elif choice == "2":
    print("You have selected Password mode")
    password()
    break
else:
    print("Invalid input. Please select 1 or 2.")

