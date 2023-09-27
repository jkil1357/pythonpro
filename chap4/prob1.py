import random

print("I sense your energy.  Your true emotions are coming across my screen.")
print("You are...\n")

mood = random.randrange(0, 3)

if mood == 0:
    print("---------------")
    print("|             |")
    print("| O       O   |")
    print("|    <        |")
    print("|             |")
    print("|  \"       \"  |")
    print("|   `_ _ _`   |")
    print("---------------")

elif mood == 1:
    print("---------------")
    print("|             |")
    print("| O       O   |")
    print("|    <        |")
    print("|             |")
    print("|  ------     |")
    print("|             |")
    print("---------------")

elif mood == 2:
    print("---------------")
    print("|             |")
    print("|  O      O   |")
    print("|    <        |")
    print("|     _       |")
    print("|   =   =     |")
    print("|  =     =    |")
    print("|             |")
    print("---------------")

print("\n...today.")

