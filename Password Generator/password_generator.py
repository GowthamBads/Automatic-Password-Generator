import random
import string
import pyperclip 

def generate_password(min_length,use_numbers=True, use_special_chars=True):
    # Define character sets
    lower = string.ascii_lowercase
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special_chars else ''
    
    # Combine all selected character sets
    all_chars = lower + digits + special
    
    # Ensure there is a valid character set
    if not all_chars:
        raise ValueError("At least one character set must be selected.")
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(min_length))
    
    return password

def main():
    # User-defined password parameters
    min_length = int(input("Enter password length: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generate_password(min_length, use_numbers, use_special_chars)
    
    # Display and copy the password to the clipboard
    print("The Generated password is :", password )

if __name__ == "__main__":
    main()