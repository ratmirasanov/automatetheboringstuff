MY_PETS = ["Zophie", "Pooka", "Fat-tail"]
print("Enter a pet name:")
NAME = input()

if NAME not in MY_PETS:

    print("I do not have a pet named " + NAME + ".")

else:

    print(NAME + " is my pet.")
