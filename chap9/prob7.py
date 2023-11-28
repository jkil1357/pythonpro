class Critter(object):

    def __init__(self, name, mood = 2):
        self.name = name
        self.mood = mood

    def setMood(self, level):
        self.mood = level

    def getMood(self):
        return self.mood
    
    def talk(self):
        if self.mood >= 4:
            print("I'm", self.name, "and I feel happy now.")
        elif self.mood == 3:
            print("I'm", self.name, "and I feel pleased now.")
        elif self.mood == 2:
            print("I'm", self.name, "and I feel frustradted now.")
        elif self.mood <= 1:
            print("I'm", self.name, "and I feel mad now.") 
        self.mood -= 1

    def feed(self):
        print("Brruppp.")
        self.mood += 1

    def play(self):
        print("Wheee!")
        self.mood += 1
        

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choice = input("Choice: ")
        print()

        if choice == "0":
            break;

        elif choice == "1":
            crit.talk()

        elif choice == "2":
            crit.feed()

        elif choice == "3":
            crit.play()

        else:
            print("Sorry,", choice, "isn't a valid choice.")

main()

input("Press the enter key to exit.")
