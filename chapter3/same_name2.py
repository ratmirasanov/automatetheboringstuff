def spam():

    global EGGS
    EGGS = "spam"


EGGS = "global"
spam()
print(EGGS)
