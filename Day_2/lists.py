# Clear screen
import os

os.system('cls')

# Lists
mylist = [10, 20, 30, 40]
mylist2 = ["A", "B", "C", "D", "E"]
mylist3 = ["Chennai", 100, "Trichy", 0431.26]

print(type(mylist))
print(mylist3)

for a in mylist:
    print(a)

print(len(mylist3))
print(mylist3[2])

mylist3.append("Praveen")
print(mylist3)

mylist3.insert(3, "India")
print("List 3 is ", mylist3)

print(mylist3[0:2])
print(mylist3[1:])
print(mylist3[:3])
print(mylist3[::-1])

# Update values
mylist[0:2] = ["A", "B"]
print(mylist)

# CRUD - Delete -> pop()
mylist.remove("A")
mylist3.pop(3)
print(mylist3)
mylist3.reverse()
print(mylist3)
del (mylist3)
try:
    print(mylist3)
except:
    print("no list")

# Sort the list

mylist4 = ["Z", "G", "R", "D"]
mylist4.sort()
print(mylist4)
mylist4.sort(reverse=True)
print(mylist4)

#Copy list
#check notes