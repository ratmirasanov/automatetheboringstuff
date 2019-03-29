import random


HEADS = 0

for i in range(1, 1001):

    if random.randint(0, 1) == 1:

        HEADS = HEADS + 1

    if i == 500:

        print("Halfway done!")

print("Heads came up " + str(HEADS) + " times.")
