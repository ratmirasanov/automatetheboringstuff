BIRTHDAYS = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while True:

    print("Enter a name: (blank to quit).")
    NAME = input()

    if NAME == "":

        break

    if NAME in BIRTHDAYS:

        print(BIRTHDAYS[NAME] + " is the birthday of " + NAME + ".")

    else:

        print("I do not have birthday information for " + NAME + ".")
        print("What is their birthday?")
        BDAY = input()
        BIRTHDAYS[NAME] = BDAY
        print("Birthday database updated.")
