f = open("text.txt", "w")
print("Creating a text file with the write() method.\n")
print("Reading the newly created file.")
f.write("Line 1\n")
f.write("This is line 2\n")
f.write("And that would make this the third line.\n")
f.close()

f = open("text.txt", "r")
whole = f.read()
print(whole)
f.close()

f = open("text.txt", "w")
print("Creating a text file with the writelines() method.\n")
print("Reading the newly created file.")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
f.writelines(lines)
f.close()

f = open("text.txt", "r")
whole = f.read()
print(whole)
f.close()
