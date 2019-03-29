#! python3
# bullet_point_adder.py -- Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip


TEXT = pyperclip.paste()
# Separate lines and add stars.
LINES = TEXT.split("\n")

for i in range(len(LINES)):  # Loop through all indexes in the "LINES" list.

    LINES[i] = "* " + LINES[i]  # Add star to each string in "LINES" list.

TEXT = "\n".join(LINES)
pyperclip.copy(TEXT)
