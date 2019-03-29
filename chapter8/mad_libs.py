"""
Create a Mad Libs program that reads in text files and lets the user add their own text
 anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
 For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
"""

import re


KEYWORDS = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
MAD_LIBS_FILE = open("mad_libs.txt")
CONTENT = MAD_LIBS_FILE.read()

if any(keyword in CONTENT for keyword in KEYWORDS):

    for word in CONTENT.split():

        if re.sub("[.,!?:;]", "", word) in KEYWORDS:

            if "ADJECTIVE" in word:

                print("Enter an adjective: ")
                adjective = input()
                CONTENT = CONTENT.replace(re.sub("[.,!?:;]", "", word), adjective, 1)

            elif "NOUN" in word:

                print("Enter a noun: ")
                noun = input()
                CONTENT = CONTENT.replace(re.sub("[.,!?:;]", "", word), noun, 1)

            elif "ADVERB" in word:

                print("Enter a adverb: ")
                adverb = input()
                CONTENT = CONTENT.replace(re.sub("[.,!?:;]", "", word), adverb, 1)

            elif "VERB" in word:

                print("Enter a verb: ")
                verb = input()
                CONTENT = CONTENT.replace(re.sub("[.,!?:;]", "", word), verb, 1)

    print(CONTENT)
    MAD_LIBS_NEW_FILE = open("mad_libs_new.txt", "w")
    MAD_LIBS_NEW_FILE.write(CONTENT)

else:

    print("No matching keywords in the string.")

MAD_LIBS_FILE.close()
MAD_LIBS_NEW_FILE.close()
