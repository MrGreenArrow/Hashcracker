import hashlib
import argparse
import itertools

#--------------------------
# Terminal command line
#--------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Password/PIN Cracker") # Initializes Parser object
    
    # Required inputs
    parser.add_argument("--target", help="Target hash to crack", required=True) # Input 1: target hash you would like to crack
    parser.add_argument("--algorithm", help="Hash algorithm (e.g. sha256)", required=True) # Input 2: Type of hash algorithm being used
    
    # Mutually exclusive: wordlist OR PIN generation
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pin-length", type=int, choices=[4,5,6], 
                    help="Generate PIN combinations (4, 5, or 6 digits)")
    #-----------------------------------------------------------
    # Dev Note: I recommend using the rockyou.txt list. This list can be obtained using the following terminal command:
    # $ wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
    #-----------------------------------------------------------
    group.add_argument("--wordlist", help="Path to wordlist file") 
    
    return parser.parse_args()


#--------------------------
# PIN Functions
#--------------------------
def generate_pin_wordlist(length: int):
    # Generates all numeric combinations for a given digit length
    return (''.join(p) for p in itertools.product('0123456789', repeat=length))
    
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
    args = parse_args()
    
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
