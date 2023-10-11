item = ["sword", "armor", "shield", "healing potion", "gold", "gems"]

print("Press the enter key to continue.")
print("You trade your sword for a crossbow.")
item[0] = "crossbow"
print("Your inventory is now:")
print(item)
print()

print("Press the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
del item[4:6]
item.append("orb of future telling")
print("Your inventory is now:")
print(item)
print()

print("Press the enter key to continue.")
print("In a great battle, your shiled is destroyed.")
del item[2]
print("Your inventory is now:")
print(item)
print()

print("Press the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
del item[0:2]
print("Your inventory is now:")
print(item)

