import random


MESSAGES = ["It is certain",
            "It is decidedly so",
            "Yes definitely",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful"]

print(MESSAGES[random.randint(0, len(MESSAGES) - 1)])
