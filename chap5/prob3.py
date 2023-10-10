import random

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")
ch = random.choice(words)
print(ch)

word = ["_"] * len(ch)
att = len(ch)
print("Length of the selected word:", len(ch))

while '_' in word and att > 0:
    print("Remaining attempts:", att)
    print("Current guessed word:",' '.join(word))
    guess = input("Guess a letter: ")

    if guess in ch:
        for i in range(len(ch)):
            if ch[i] == guess:
                word[i] = guess
    else:
        print("Incorrect guess.")
        att -= 1
    
    if '_' not in word:
        print("Congratulations! You guessed the word:", ch)
    elif att == 0:
        print("You've used up all your attempts. The correct word was", ch)
