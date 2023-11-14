import pickle
import shelve

print("Pickling lists.\n")
print("Unpickling lists.")
v = ["sweet", "hot", "dill"]
with open("picklesl.dat", "wb") as p_f:
    pickle.dump(v, p_f)
with open("picklesl.dat", "rb") as p_f:
    read = pickle.load(p_f)
print(read)
v = ["whole", "spear", "chip"]
with open("picklesl.dat", "wb") as p_f:
    pickle.dump(v, p_f)
with open("picklesl.dat", "rb") as p_f:
    read = pickle.load(p_f)
print(read)
v = ["Claussen", "Heinz", "Vlassic"]
with open("picklesl.dat", "wb") as p_f:
    pickle.dump(v, p_f)
with open("picklesl.dat", "rb") as p_f:
    read = pickle.load(p_f)
print(read)
p_f.close()

print("\nShelving lists.\n")
print("Retrieving the lists from a shelved file:")
with shelve.open("pickles2.dat") as pickles:
    pickles["variety"] = ["sweet", "hot", "dill"]
    pickles["shape"] = ["whole", "spear", "chip"]
    pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]
    for key in pickles.keys():
        print(key, "-", pickles[key])
pickles.close()
