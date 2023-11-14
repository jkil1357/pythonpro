def one_block(file):
    category = file.readline()
    question = file.readline()
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correct = file.readline()
    if correct:
        correct = correct[0]
    explain = file.readline()

    return category, question, answers, correct, explain

def prob():
    file = open("trivia.txt", "w")
    c = "On the Run With a Mammal\n"
    q = "Let's say you turn state's evidence and need to \"get on the lamb.\" If you wait too long, what will happen?\n"
    a1 = "You'll end up on the sheep\n"
    a2 = "You'll end up on the cow\n"
    a3 = "You'll end up on the goat\n"
    a4 = "You'll end up on the emu\n"
    co = "1\n"
    e = "A lamb is just a young sheep.\n"
    file.write(c)
    file.write(q)
    file.write(a1)
    file.write(a2)
    file.write(a3)
    file.write(a4)
    file.write(co)
    file.write(e)
    c = "The Godfather Will Get Down With You Now\n"
    q = "Let's say you have an audience with the Godfather of Soul. How would it be smart to address him?\n"
    a1 = "Mr. Richard\n"
    a2 = "Mr. Domino\n"
    a3 = "Mr. Brown\n"
    a4 = "Mr. Checker\n"
    co = "3\n"
    e = "James Brown is the Godfather of soul.\n"
    file.write(c)
    file.write(q)
    file.write(a1)
    file.write(a2)
    file.write(a3)
    file.write(a4)
    file.write(co)
    file.write(e)
    c = "Animal Quiz\n"
    q = "Which of the following statements about koalas is NOT true?\n"
    a1 = "Koalas are native to Australia\n"
    a2 = "Koalas are a type of bear\n"
    a3 = "Koalas primarily eat eucalyptus leaves\n"
    a4 = "Koalas sleep for up to 20 hours a day\n"
    co = "2\n"
    e = "Koalas are marsupials, not bears.\n"
    file.write(c)
    file.write(q)
    file.write(a1)
    file.write(a2)
    file.write(a3)
    file.write(a4)
    file.write(co)
    file.write(e)

print("\t\tWelcome to Trivia Challenge!\n")
print("\t\tAn Episode You Can't Refuse\n\n")
prob()
file = open("trivia.txt", "r")
category, question, answers, correct, explain = one_block(file)
while category:
    print(category)
    print(question)
    for i in range(4):
        print("\t", i + 1, "-", answers[i])
    answer = input("What's your answer?: ")

    if answer == correct:
        print("\nRight!", end=" ")
    else:
        print("\nWrong!", end=" ")
    print(explain)
    category, question, answers, correct, explain = one_block(file)
    
file.close()
print("\nFinish Question!")
