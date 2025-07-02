import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) < 8:
        remarks.append("Too short (minimum 8 characters required).")
    else:
        strength += 1

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("No lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("No uppercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("No numbers.")

    if re.search(r"[\W_]", password):
        strength += 1
    else:
        remarks.append("No special characters.")

    if strength <= 2:
        level = "🔴 Weak"
    elif strength == 3 or strength == 4:
        level = "🟡 Moderate"
    else:
        level = "🟢 Strong"

    return level, remarks

# Main
if __name__ == "__main__":
    pwd = input("🔐 Enter your password: ")
    level, feedback = check_password_strength(pwd)

    print(f"\nPassword Strength: {level}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f" - {item}")
