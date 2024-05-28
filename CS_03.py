def analyze_strength(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    digit_count = sum(1 for char in string if char.isdigit())
    special_count = len(string) - (uppercase_count + lowercase_count + digit_count)

    if lowercase_count == len(string):
        return "Very Weak"
    elif uppercase_count == 1 and lowercase_count == len(string) - 1:
        return "Weak"
    elif uppercase_count <= 3 and lowercase_count <= 3 and digit_count <= 3 and special_count <= 3:
        return "Weak"
    elif uppercase_count >= 4 and lowercase_count >= 4 and digit_count >= 4 and special_count >= 4:
        return "Very Strong"
    elif uppercase_count == 1 and lowercase_count == 1 and digit_count == 1 and special_count == 1:
        return "Slightly Weak"
    elif uppercase_count == 2 and lowercase_count == 2 and digit_count == 2 and special_count == 2:
        return "Medium"
    else:
        return "Strong"

def main():
    user_input = input("Enter a string: ")
    strength = analyze_strength(user_input)
    print("Strength of the string:", strength)

if __name__ == "__main__":
    main()
