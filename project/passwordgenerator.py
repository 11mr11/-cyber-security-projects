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
    print("Error:", ve)import random