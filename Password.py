import re
password_history = []
def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*' for c in password)
    length = len(password)
    if length < 6:
        return "Weak"
    elif has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif has_upper and has_lower and has_digit:
        return "Medium"
    else:
        return "Weak"
def get_password():
    while True:
        password = input("Enter your password: ")
        if password in password_history:
            print("Password used before. Try again.")
            continue
        password_history.append(password)
        strength = check_strength(password)
        if strength == "Weak":
            print("Weak password. It must be at least 6 characters.")
        elif strength == "Medium":
            print("Medium password. It should contain special characters as well.")
        else:
            print("Strong password. Well done!")
            break
get_password()