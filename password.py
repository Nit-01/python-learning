import re
password=input()

try:
    if len(password)<8:
        print(f"{password} is less than 8 letter")

    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain a special character")
        print("Password not created")
    else:
        print("Strong password")
        print("Password created")
finally:
    print()