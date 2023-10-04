import random

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
words = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")

ch = random.choice(words)
ch1 = list(ch)
random.shuffle(ch1)
print("Jumbled word:", ''.join(ch1))

guess = input("Your guess: ")

if guess == ch:
    print("Congratulations, that's the correct. ", end='')
    print("The word was:", ch)
else:
    print("Sorry, that's not correct. ", end='')
    print("The word was:", ch)
