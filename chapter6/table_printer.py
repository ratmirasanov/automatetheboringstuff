TABLE_DATA = [["apples", "oranges", "cherries", "banana", "lemons"],
              ["Alice", "Bob", "Carol", "David"],
              ["dogs", "cats", "moose", "goose"]]


def print_table():

    col_widths = [0] * len(TABLE_DATA)

    for i in range(len(TABLE_DATA)):

        for j in range(len(TABLE_DATA[i])):

            if len(TABLE_DATA[i][j]) > col_widths[i]:

                col_widths[i] = len(TABLE_DATA[i][j])

    max_width = max(col_widths)

    longest_list_value = len(max(TABLE_DATA, key=len))

    for i in range(longest_list_value):

        formatted_row = []

        for row in TABLE_DATA:

            try:

                formatted_row.append(row[i].rjust(max_width))

            except IndexError:

                formatted_row.append(" ")

        print("".join(formatted_row))


print_table()
