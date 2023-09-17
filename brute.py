# imports 
import hashlib
import itertools
import string
import time

def sha1(text):
    s = hashlib.sha1()
    s.update(text.encode("utf-8"))
    return s.hexdigest()
# All modes 
def get_charset(mode):
    if mode == "Alphabetical":
        return string.ascii_letters
    elif mode == "Numbers":
        return string.digits
    elif mode == "Basic Symbols":
        return "!$@*()"
    elif mode == "All Symbols":
        return string.punctuation
    elif mode == "Only Lowercase":
        return string.ascii_lowercase
    elif mode == "Only Uppercase":
        return string.ascii_uppercase
    elif mode == "All":
        return string.printable[:-6]
    else:
        return string.printable[:-6]

def brute_force_sha1(target_hash, min_length, max_length, mode):
    charset = get_charset(mode)
    for length in range(min_length, max_length + 1):
        print(f"Trying length {length}")
        for guess in itertools.product(charset, repeat=length):
            guess_text = "".join(guess)
            print(f"Trying: {guess_text}")
            if sha1(guess_text) == target_hash:
                print("\033[92mSUCCESS: The original text is: {}\033[0m".format(guess_text))
                return guess_text
    return None

if __name__ == "__main__":
# starting screen 
    print("Made By Bytelabs")

    
    print("\033[94m")
    print("""
d8888b. db    db d888888b d88888b db       .d8b.  d8888b. .d8888.
88  `8D `8b  d8' `~~88~~' 88'     88      d8' `8b 88  `8D 88'  YP
88oooY'  `8bd8'     88    88ooooo 88      88ooo88 88oooY' `8bo.
88~~~b.    88       88    88~~~~~ 88      88~~~88 88~~~b.   `Y8b.
88   8D    88       88    88.     88booo. 88   88 88   8D db   8D
Y8888P'    YP       YP    Y88888P Y88888P YP   YP Y8888P' `8888Y
    """)
    print("\033[0m")

    
    print("Starting the script....")
    time.sleep(5)
    
    # Target hash to brute-force
    target_hash = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"  # Example SHA-1 hash for the password "password" This MUST be a SHA1 hash.

    # Choose the mode for the character set
    mode = "all"  # Options: "Alphabetical", "Numbers", "Basic Symbols", "All Symbols", "Only Lowercase", "Only Uppercase", "All"
    
    # I recommend lowercase as it is faster 

    # Warning: This can take a very long time depending on the min_length, max_length, and charset
    min_length = 1  # Minimum length of the string to be guessed
    max_length = 5 # Maximum length of the string to be guessed. 

    found_text = brute_force_sha1(target_hash, min_length, max_length, mode)

    if not found_text:
        print("Not found within the given length and charset.")
