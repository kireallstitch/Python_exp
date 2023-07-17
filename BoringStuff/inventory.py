PlayerInventory = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby", "gold coin"]


def displayInventory(inventory):  # Displays the Inventory
    print("Inventory:")
    cnt = 0
    for k, v in inventory.items():
        print(k + " : " + str(v))
        cnt += v
    print(f"Total number of items: {cnt}")


def addToInventory(inventory, addedItems):  # Add items to the provided inventory
    for item in addedItems:  # Loops through the provided list.
        inventory.setdefault(item, 0)  # Checks if the key exists. If not, adds it with a value of 0.
        inventory[item] += 1  # Adds 1 to the value.
    return inventory  # returns the complete Dictionary


PlayerInventory = addToInventory(PlayerInventory, dragonLoot)
displayInventory(PlayerInventory)