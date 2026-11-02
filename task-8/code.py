import re


MIN_LENGTH = 8

PROHIBITED_SUBSTRINGS = [
    "password",
    "admin",
    "123456"
]

def validate_password(password):

    errors = []

    if len(password) < MIN_LENGTH:
        errors.append(
            "Password must contain at least 8 characters."
        )

    
    if not any(ch.isupper() for ch in password):
        errors.append(
            "Password must contain at least one uppercase letter."
        )

    
    if not any(ch.islower() for ch in password):
        errors.append(
            "Password must contain at least one lowercase letter."
        )

    
    if not any(ch.isdigit() for ch in password):
        errors.append(
            "Password must contain at least one digit."
        )

    
    if not any(not ch.isalnum() for ch in password):
        errors.append(
            "Password must contain at least one special character."
        )

    
    if re.search(r"(.)\1", password):
        errors.append(
            "Password must not contain consecutive repeated characters."
        )

    
    lower_password = password.lower()

    for word in PROHIBITED_SUBSTRINGS:
        if word in lower_password:
            errors.append(
                "Password contains prohibited substring: " + word
            )

    return errors



print("======= PASSWORD POLICY VALIDATION ENGINE =======")

n = int(input("Enter number of passwords to validate: "))

for i in range(n):

    print("\nEnter Password", i + 1, ":")
    password = input()

    
    errors = validate_password(password)

    print("\nPassword Validation Result:")

    if len(errors) == 0:
        print("VALID PASSWORD")
        print("All security rules are satisfied.")

    else:
        print("INVALID PASSWORD")
        print("Failed Conditions:")

        for error in errors:
            print("-", error)

    print("---------------------------------------------")

print("\nPassword validation completed.")
