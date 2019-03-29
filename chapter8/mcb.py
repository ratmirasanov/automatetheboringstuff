#! python3
"""mcb.pyw -- Saves and loads pieces of text to the clipboard.
Usage: python mcb.py save <keyword> -- Saves clipboard to keyword.
       python mcb.py <keyword> -- Loads keyword to clipboard.
       python mcb.py list -- Loads all keywords to clipboard.
       python mcb.py delete <keyword> -- Delete keyword.
       python mcb.py delete -- Delete all keywords.
"""

import shelve
import sys
import pyperclip


MCB_SHELF = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":

    MCB_SHELF[sys.argv[2]] = pyperclip.paste()

# Delete keyword.
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":

    del MCB_SHELF[sys.argv[2]]

elif len(sys.argv) == 2:

    # List keywords and load content.
    if sys.argv[1].lower() == "list":

        pyperclip.copy(str(list(MCB_SHELF.keys())))

    # Delete all keywords.
    elif sys.argv[1].lower() == "delete":

        for keyword in MCB_SHELF.keys():

            del MCB_SHELF[keyword]

    elif sys.argv[1] in MCB_SHELF:

        pyperclip.copy(MCB_SHELF[sys.argv[1]])

MCB_SHELF.close()
