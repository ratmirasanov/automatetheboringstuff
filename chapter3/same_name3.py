def spam():

    global EGGS
    EGGS = "spam" # This is the global.

def bacon():

    eggs = "bacon" # This is a local.

def ham():

    print(EGGS) # This is the global.


EGGS = 42 # This is the global.
spam()
print(EGGS)
