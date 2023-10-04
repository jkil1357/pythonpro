import random

words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n")
ch = random.choice(words)

print("Length of the selected word:", len(ch))
guess = None
att = len(ch)
a = 1
print(ch)

while guess != ch:
    print("Remaining attempts:", att)
    print("Current guessed word: ", end='')
    while a <= len(ch):
        print("_ ", end='')
        a += 1
    guess = input("\nGuess a letter: ")
    if guess in ch:
        print("")
