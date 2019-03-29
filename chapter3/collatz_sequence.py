import sys


def collatz(number):

    if number % 2 == 0:

        print(number // 2)

        return number // 2

    elif number % 2 == 1:

        print(3 * number + 1)

        return 3 * number + 1

try:

    INPUT_VALUE = int(input())

except ValueError:

    print("Entered value should be an integer.")
    sys.exit()

RETURN_VALUE = collatz(INPUT_VALUE)

while not RETURN_VALUE == 1:

    RETURN_VALUE = collatz(RETURN_VALUE)
