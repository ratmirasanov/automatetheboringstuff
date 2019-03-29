while True:

    print("Who are you?")
    NAME = input()

    if NAME != "Joe":

        continue

    print("Hello, Joe. What is the password? (It is a fish.)")
    PASSWORD = input()

    if PASSWORD == "swordfish":

        break

print("Access granted.")
