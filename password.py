"""Password Strength Program"""

import string
import os

# Get the current directory and prepare file paths
current_dir = os.path.dirname(__file__)
wordlist_path = os.path.join(current_dir, "wordlist.txt")
toppasswords_path = os.path.join(current_dir, "toppasswords.txt")

# Function definitions
def word_has_character(word, char_type):
    """Check if a word has a specific character type."""
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
    """Check if a word exists in a file (one word per line)."""
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

def word_complexity(word):
    """Return a numeric complexity based on the types of characters in the word."""
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

def password_strength(password, min_length=10, strong_length=16):
    """
    Determine the password strength based on:
    - Dictionary word presence
    - Common password list
    - Length
    - Character complexity
    """
    if word_in_file(password, wordlist_path, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, toppasswords_path, case_sensitive=False):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long; length trumps complexity. This is a good password.")
        return 5

    complexity = word_complexity(password)
    return 1 + complexity

def strength_label(score):
    """Return a human-readable strength label for a given score."""
    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    return labels.get(score, "Unknown")

def main():
    while True:
        user_input = input("Enter a password to test (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        strength = password_strength(user_input)
        label = strength_label(strength)
        print(f"Password strength: {strength} - {label}")

if __name__ == "__main__":
    main()
