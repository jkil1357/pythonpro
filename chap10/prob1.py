class Player:
    def blast(self, enemy):
        print("The player blasts an enemy.")
        enemy.die()

class Alien:
    def die(self):
        print("\nThe alien gasps and says, 'Oh, this is it. This is the big one.")
        print("Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")
        print("Good-bye, cruel universe.")

print("\t\tDeath of an Alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit.")
