import inventory


def add_to_inventory(inventory, added_items):

    temp = inventory

    for item in added_items:

        if item in inventory.keys():

            temp[item] = temp[item] + 1

        else:

            temp[item] = 1

    return temp


INV = {"gold coin": 42, "rope": 1}
DRAGON_LOOT = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
INV = add_to_inventory(INV, DRAGON_LOOT)
inventory.display_inventory(INV)
