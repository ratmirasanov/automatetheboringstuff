"""This program says hello and asks for my name."""


print("Hello world!")

print("What is your name?") # Ask for their name.
MY_NAME = input()
print("It is good to meet you, " + MY_NAME)
print("The length of your name is: ")
print(len(MY_NAME))

print("What is your age?") # Ask for their age.
MY_AGE = input()
print("You will be " + str(int(MY_AGE) + 1) + " in a year.")
