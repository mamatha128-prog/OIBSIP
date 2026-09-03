# OIBSIP - Python Programming
# Task 3: Random Password Generator
# Beginner Tier

import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generate a random password based on user-selected character types."""

    character_pool = ""

    if use_uppercase:
        character_pool += string.ascii_uppercase

    if use_lowercase:
        character_pool += string.ascii_lowercase

    if use_numbers:
        character_pool += string.digits

    if use_symbols:
        character_pool += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(character_pool)

    return password


def get_yes_no(prompt):
    """Get a yes/no answer from the user."""

    while True:
        answer = input(prompt).strip().lower()

        if answer in ["y", "yes"]:
            return True

        if answer in ["n", "no"]:
            return False

        print("Please enter Y for Yes or N for No.")


def main():
    print("=" * 45)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    while True:

        # Get password length
        while True:
            try:
                length = int(input("\nEnter password length (minimum 8): "))

                if length < 8:
                    print("Password length must be at least 8 characters.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        print("\nChoose the character types:")

        use_uppercase = get_yes_no("Include uppercase letters (A-Z)? (Y/N): ")
        use_lowercase = get_yes_no("Include lowercase letters (a-z)? (Y/N): ")
        use_numbers = get_yes_no("Include numbers (0-9)? (Y/N): ")
        use_symbols = get_yes_no("Include symbols (!@#$...)? (Y/N): ")

        # Count selected character types
        selected_types = sum([
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        ])

        if selected_types < 2:
            print("\nError: Please select at least 2 character types.")
            continue

        # Generate password
        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )

        print("\n" + "=" * 45)
        print("Generated Password:")
        print(password)
        print("=" * 45)

        # Generate another password
        again = get_yes_no("\nGenerate another password? (Y/N): ")

        if not again:
            print("\nThank you for using the Random Password Generator!")
            break


if __name__ == "__main__":
    main()
