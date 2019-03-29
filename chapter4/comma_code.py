def comma_code(some_list):

    temp_string = ""

    for item in some_list[:-1]:

        temp_string = item + ", " + temp_string

    temp_string = temp_string + " and " + some_list[-1] + "."

    return temp_string


SPAM = ["apples", "bananas", "tofu", "cats"]
print(comma_code(SPAM))
