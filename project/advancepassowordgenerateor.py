import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_punctuation=True, exclude_ambiguous=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    punctuation = string.punctuation if use_punctuation else ''
    
    # Exclude ambiguous characters
    if exclude_ambiguous:
        ambiguous_chars = 'Il1O0'
        lowercase = ''.join([char for char in lowercase if char not in ambiguous_chars])
        uppercase = ''.join([char for char in uppercase if char not in ambiguous_chars])
        digits = ''.join([char for char in digits if char not in ambiguous_chars])
        punctuation = ''.join([char for char in punctuation if char not in ambiguous_chars])

    # Combine all selected character sets
    characters = lowercase + uppercase + digits + punctuation
    
    # Ensure at least one character from each selected set is included
    if length < len([use_uppercase, use_digits, use_punctuation]) + 1:
        raise ValueError("Password length must be greater than the number of selected character sets")

    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_punctuation:
        password.append(random.choice(punctuation))
    
    password.extend(random.choice(characters) for _ in range(length - len(password)))
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        
        if password_length < 6:
            print("Password length must be at least 6 characters.")
        else:
            print("Include uppercase letters? (y/n): ", end="")
            include_uppercase = input().strip().lower() == 'y'
            print("Include digits? (y/n): ", end="")
            include_digits = input().strip().lower() == 'y'
            print("Include punctuation? (y/n): ", end="")
            include_punctuation = input().strip().lower() == 'y'
            print("Exclude ambiguous characters (e.g., 'Il1O0')? (y/n): ", end="")
            exclude_ambiguous_chars = input().strip().lower() == 'y'
            
            generated_password = generate_password(password_length, include_uppercase, include_digits, include_punctuation, exclude_ambiguous_chars)
            print("Generated password:", generated_password)
    except ValueError as ve:
        print("Error:", ve)