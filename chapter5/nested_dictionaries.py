def total_brought(guests, item):

    num_brought = 0

    for key, value in guests.items():

        num_brought = num_brought + value.get(item, 0)

    return num_brought


ALL_GUESTS = {"Alice": {"apples": 5, "pretzels": 12},
              "Bob": {"ham sandwiches": 3, "apples": 2},
              "Carol": {"cups": 3, "apple pies": 1}}

print("Number of things being brought:")
print(" - Apples         " + str(total_brought(ALL_GUESTS, "apples")))
print(" - Cups           " + str(total_brought(ALL_GUESTS, "cups")))
print(" - Cakes          " + str(total_brought(ALL_GUESTS, "cakes")))
print(" - Ham Sandwiches " + str(total_brought(ALL_GUESTS, "ham sandwiches")))
print(" - Apple Pies     " + str(total_brought(ALL_GUESTS, "apple pies")))
