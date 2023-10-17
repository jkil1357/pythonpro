word = "PYTHON"
word_l = ["-"] * len(word)
letter = []
att = len(word)

def mprint():
    print("\nYou've used the following letters:")
    print(letter)
    print("\nSo far, the word is:")
    print(''.join(word_l))

def hangman():
    print("\n---------")
    print("|       |")
    print("|       0")
    print("|      -+-")
    print("|")
    print("|")
    print("|")
    print("--------------")
    

while att > 0:
    cha = input("\nEnter your guess: ")

    if cha in word:        
        if cha in letter:
            print("\n" + cha + " has already been tried")
            hangman()
            mprint()
            continue
        else:
            letter.append(cha)
        
        for i in range(len(word)):
            if word[i] == cha:
                word_l[i] = cha
                
        print("\nYes! " + cha + " is in the word!")
        hangman()
        mprint()
        
    if cha not in word:
        if cha in letter:
            print("\n" + cha +  " has already been tried")
            hangman()
            mprint()
            continue
        else:
            letter.append(cha)
            
        print("\nNO! " + cha + " isn't included.")
        hangman()
        mprint()

    att -= 1

    if att == 0:
        print("\nGame Over!")
        print("Word is " + word)
