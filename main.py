def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short"
    return "Password length is acceptable"

password = input("Enter a test password: ")
print(check_password_strength(password))
