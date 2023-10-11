print("\tHigh Scores Keeper\n")
print("\t0 - Quit")
print("\t1 - List Scores")
print("\t2 - Add a Score\n")

l = []
a = int(input("Choice: "))
print()

while a == 1 or a == 2:

    if a == 2:
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        
        entry = ([name, score])
        l.append(entry)
        l.sort(key=lambda x: x[1], reverse=True)

    elif a == 1:
        print("High Scores\n")
        print("NAME", "\t", "SCORE")
        for i in l:
            x, y = i
            print(x, "\t", y)
        
    print()  
    print("\tHigh Scores Keeper\n")
    print("\t0 - Quit")
    print("\t1 - List scores")
    print("\t2 - Add a Score\n")
    a = int(input("Choice: "))
    print()
