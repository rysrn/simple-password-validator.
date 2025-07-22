# in this project we will cross-check passowrds and review which aligns with the validation requirements put in place.
"""
1. Passwords should not be less than 8 characters.
2. Passwords should not contain atleast one number, one uppercase.
3. Passwords should have a special character. 
"""

password = input("Enter your password: ")

if len(password) < 8:
    print("Your password is invalid.")
elif not password.find (" ") == -1:
    print("Your password cannot contain spaces.")
else:
    print("Successful login")
    