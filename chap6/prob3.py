geek = {}
geek["404"] = "clueless."
geek["Uninstalled"] = "being fired. Especially popular during the dot-bomb era."

while True:
    print("\n\tGeek Translator\n")
    print("\t0 - Quit")
    print("\t1 - Look Up a Geek Term")
    print("\t2- Add a Geek Term")
    print("\t3 - Redefine a Geek Term")
    print("\t4 - Delete a Geek Term\n")

    choice = input("Choice: ")

    if choice == '0':
        break;
    
    elif choice == '1':
        term = input("\nWhat term do you want me to translate?: ")
        if term in geek:
            print("\n" + term + " means " + geek[term])
        else:
            print("\nI have no idea what " + term + " is.")

    elif choice == '2':
        term = input("\nWhat term do you want to add?: ")
        if term not in geek:
            define = input("\nWhat is the definition?: ")
            geek[term] = define
            print("\n" + term + " has been added.")
        else:
            print("\nThat term already exists.")

    elif choice == '3':
        term = input("\nWhat term do you want to redefine?: ")
        if term in geek:
            define = input("\nWhat is the new definition?: ")
            geek[term] = define
            print("\n" + term + " has been redefined.")
        else:
            print("\nThat term doesn't exist.")
        
    elif choice == '4':
        term = input("\nWhich term would you like to delete?: ")
        if term in geek:
            del(geek[term])
            print("\n" + term + " has been deleted.")
        else:
            print("\nThat term doesn't exist.")
