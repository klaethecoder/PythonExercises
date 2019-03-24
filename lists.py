shoppingList = ["milk", "pasta", "spam", "bread","rice"]

for item in shoppingList:
    if item == "spam":
        # continue keyword allows us to make sure that we can check to see if something is there and move forward if it is something we don't want
        continue
    print("Buy %s" % item)