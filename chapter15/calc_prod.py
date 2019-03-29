import time


def calc_prod():
    # Calculate the product of the first 100,000 numbers.

    product = 1

    for i in range(1, 100000):

        product = product * i

    return product


START_TIME = time.time()
PROD = calc_prod()
END_TIME = time.time()
print("The result is %s digits long." % len(str(PROD)))
print("Took %s seconds to calculate." % (END_TIME - START_TIME))
