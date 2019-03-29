MESSAGE = "It was a bright cold day in April, and the clocks were striking thirteen."
COUNT = {}

for character in MESSAGE:

    COUNT.setdefault(character, 0)
    COUNT[character] = COUNT[character] + 1

print(COUNT)
