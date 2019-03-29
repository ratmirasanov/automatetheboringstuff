def spam():

    eggs = "spam local"
    print(eggs) # Prints "spam local".

def bacon():

    eggs = "bacon local"
    print(eggs) # Prints "bacon local".
    spam()
    print(eggs) # Prints "bacon local".


EGGS = "global"
bacon()
print(EGGS) # Prints "global".
