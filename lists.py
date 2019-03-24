shoppingList = ["milk", "pasta", "spam", "bread","rice"]

for item in shoppingList:
    if item == "spam":
        # continue keyword allows us to make sure that we can check to see if something is there and move forward if it is something we don't want
        continue
    print("Buy %s" % item)
print("-"*20)
    
meal = ["eggs", "bacon", "spam", "sausages"]

for item in meal:
    grossFood = False
    if item == "spam":
            grossFood = True
            break

if grossFood:
        print("Can I have anything without Spam\n")