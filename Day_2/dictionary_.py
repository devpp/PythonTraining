# Clear screen
import os

os.system('cls')

myD = {1: "Delhi", 2: "Chennai", 3: "Trichy", 4 : ["A","B","C"]}
print(type(myD))
print(myD)
print(len(myD))

# update
myD.update({5 : "London"})
print(myD)

mylist = myD.get(4)
for a in mylist:
    print(a)

mykeys = myD.keys()
print("Keys are ", mykeys)

myD.pop(5)
print(myD)

myD.popitem()
print(myD)

myD2 = myD.copy()
print(myD2)