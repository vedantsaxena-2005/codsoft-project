import random
import string

def generate_password(length, complexity_level):
    if complexity_level == '1':  # Easy
        characters = string.ascii_lowercase
    elif complexity_level == '2':  # Medium
        characters = string.ascii_letters + string.digits
    elif complexity_level == '3':  # Hard
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice. Using medium complexity by default.")
        characters = string.ascii_letters + string.digits

    return ''.join(random.choices(characters, k=length))

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return

        print("\nChoose password complexity:")
        print("1 - Easy (only lowercase letters)")
        print("2 - Medium (letters and digits)")
        print("3 - Hard (letters, digits, and special characters)")
        complexity = input("Enter your choice (1/2/3): ")

        password = generate_password(length, complexity)
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
# Run the generator
main()
