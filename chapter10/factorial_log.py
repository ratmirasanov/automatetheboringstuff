import logging


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of program.")


def factorial(number):

    logging.debug("Start of factorial(%s)" % number)
    total = 1

    for i in range(1, number + 1):

        total *= i
        logging.debug("i is " + str(i) + ", total is " + str(total))

    logging.debug("End of factorial(%s)" % number)

    return total


print(factorial(5))
logging.debug("End of program.")
