item = ("sword", "armor", "shield", "healing potion")
print("Your items:")

for a in item:
    print(a)

print("\nPress the enter key to continue.")
print("You have", len(item), "items in your possession.")

print("\nPress the enter key to continue.")
print("You Will live to fight another day.")

num = int(input("\nEnter the index number for an item in inventory: "))
print("At index", num , "is", item[num])

a = int(input("\nEnter the index number to begin a slice: "))
b = int(input("Enter the index number to end the slice: "))
print("inventory[", a, ":", b, "]\t\t", end = "")
print(item[a:b])

print("\nPress the enter key to continue.")
print("You find a chest.  It contains:")
additem = ("gold", "gems")
print(additem[0:])
item += additem
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
print(item[0:])
