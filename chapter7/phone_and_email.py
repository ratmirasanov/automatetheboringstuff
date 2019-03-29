#! python3
# phone_and_email.py -- Finds phone numbers and email addresses on the clipboard.
import re
import pyperclip


PHONE_REGEX = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                # Area code.
    (\s|-|\.)?                        # Separator.
    (\d{3})                           # First 3 digits.
    (\s|-|\.)                         # Separator.
    (\d{4})                           # Last 4 digits.
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # Extension.
    )""", re.VERBOSE)

EMAIL_REGEX = re.compile(r"""(
    [a-zA-Z0-9._%+-]+      # Username.
    @                      # @ symbol.
    [a-zA-Z0-9.-]+         # Domain name.
    (\.[a-zA-Z]{2,4})      # Dot-something.
    )""", re.VERBOSE)

# Find matches in clipboard text.
TEXT = str(pyperclip.paste())
MATCHES = []

for groups in PHONE_REGEX.findall(TEXT):

    phone_num = "-".join([groups[1], groups[3], groups[5]])

    if groups[8] != "":

        phone_num += " x" + groups[8]

    MATCHES.append(phone_num)

for groups in EMAIL_REGEX.findall(TEXT):

    MATCHES.append(groups[0])

# Copy results to the clipboard.
if len(MATCHES) > 0:

    pyperclip.copy("\n".join(MATCHES))
    print("Copied to clipboard:")
    print("\n".join(MATCHES))

else:

    print("No phone numbers or email addresses found.")
