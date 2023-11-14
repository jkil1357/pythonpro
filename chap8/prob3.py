f = open("text.txt", "w")

print("Input your string...")
while True:
    t = input(">> ")
    
    if t == 'Q':
        print("Write process has been finished\n")
        break;
    else:
        f.write(t + "\n")
f.close()

f = open("text.txt", "r")
print("\nYour inputs are below..")
whole = f.read()
print(whole)

f.close()
