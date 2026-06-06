""" Assignment of 7th Feb """
print(" Create a password")
password = input("Enter password: ")

if len(password) < 8:
    print(" Password too short. Must be at least 8 characters.")
elif password.islower():
    print(" Password must contain at least one uppercase letter.")
elif password.isupper():
    print(" Password must contain at least one lowercase letter.")
elif password.isalpha():
    print(" Password must contain at least one number and one special character.")
elif password.isdigit():
    print(" Password must contain at least one letter and one special character.")
elif password.isalnum():
    print(" Password must contain at least one special character.")
else:
    print(" Password created successfully!")

    print("\n Login")
    login = input("Enter password again: ")

    if password == login:
        print(" Login successful!")
    else:
        print(" Incorrect password.")