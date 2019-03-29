while True:

    print("Enter your age:")
    AGE = input()

    if AGE.isdecimal():

        break

    print("Please enter a number for your age.")

while True:

    print("Select a new password (letters and numbers only):")
    PASSWORD = input()

    if PASSWORD.isalnum():

        break

    print("Passwords can only have letters and numbers.")
