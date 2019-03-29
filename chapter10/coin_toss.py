import random


GUESS = ""

while GUESS not in ("1", "0"):

    print("Guess the coin toss! Enter heads or tails:")
    GUESS = input()

TOSS = random.randint(0, 1)  # 0 is tails, 1 is heads.

if TOSS == int(GUESS):

    print("You got it!")

else:

    print("Nope! Guess again!")
    GUESS = input()

    if TOSS == int(GUESS):

        print("You got it!")

    else:

        print("Nope. You are really bad at this game.")
