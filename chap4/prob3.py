import random

print("\tWelcome to 'Guess My Number'!\n")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

num = random.randrange(1, 101)
guess = int(input("Take a guess: "))
tries = 1

while num != guess:
    tries = tries + 1
    if guess > num:
        print("Lower...")
        guess = int(input("Take a guess: "))
    elif guess < num:
        print("Higher...")
        guess = int(input("Take a guess: "))

if guess == num:
    print("You guessed it! The number was", guess)
    print("And it only took you", tries, "tries!")
