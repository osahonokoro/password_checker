"""Password Strength Program"""

import string

# Add the Constants
LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?",
           "/", "`", "~"]

# Function definitions
def word_has_character(word, char_type):
    """function loops through each character in the string passed in the word parameter to see if that character is in the list of characters passed in the character_list parameter"""
    if char_type == "lower":
        return any(char.islower() for char in word)
    elif char_type == "upper":
        return any(char.isupper() for char in word)
    elif char_type == "digit":
        return any(char.isdigit() for char in word)
    elif char_type == "special":
        return any(char in string.punctuation for char in word)
    else:
        raise ValueError("Unknown character type: " + char_type)

def word_in_file(word, filename, case_sensitive=False):
    """This function reads a file in which each line of the file contains a single word"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not case_sensitive:
                word = word.lower()
                lines = [line.strip().lower() for line in lines]
            else:
                lines = [line.strip() for line in lines]
            return word in lines
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False 
    # pass

def word_complexity(word):
    """This function creates a numeric complexity value based on the types of characters the word parameter contains."""
    complexity = 0

    if word_has_character(word, "lower"):
        complexity += 1
    if word_has_character(word, "upper"):
        complexity += 1
    if word_has_character(word, "digit"):
        complexity += 1
    if word_has_character(word, "special"):
        complexity += 1

    return complexity
    # pass

def password_strength(password, min_length=10, strong_length=16):
   """This function checks length requirements, calls word_complexity function to calculate the words complexity, then determines the password's strength based on the user requirements."""
   # word = password
   # complexity=word_complexity(word)
    # 1. Check if password is a dictionary word
    # if word_in_file(password, "wordlist.txt", case_sensitive=False):
    if word_in_file(password, r"C:\Users\Otala\Desktop\Osahon\BYU\CSE111\password_checker\wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Check if password is in top passwords
    # if word_in_file(password, "toppasswords.txt", case_sensitive=True):
    if word_in_file(password, r"C:\Users\Otala\Desktop\Osahon\BYU\CSE111\password_checker\toppasswords.txt", case_sensitive=False):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Check for length restrictions
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity. This is a good password.")
        return 5

    # 4. Compute complexity
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

    # pass

def main():
    # Text Constants:
    #  
    # print("LOWER:", LOWER[:5])  
    # print("UPPER:", UPPER[:5])  
    # print("DIGITS:", DIGITS)    
    # print("SPECIAL:", SPECIAL[:5]) 

    # Text word_has_character() function:

    # print(word_has_character("Hello123", "digit"))   
    # print(word_has_character("Hello123", "special"))  

    while True:
        user_input = input("Enter a password to test (or 'q' to quit): ")
        if user_input == 'q' or user_input == 'Q':
            print("Goodbye!")
            break
        strength = password_strength(user_input)
        print(f"Password strength: {strength}")


if __name__ == "__main__":
    main()


