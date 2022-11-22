# clear screen
import os

os.system('cls')

# Accept 6 numbers
n = 6
mylist = []
i = 1

while i <= n:
    num = int(input("Enter number  " + str(i) + ":"))
    mylist.append(num)
    i += 1

# Create a list with duplicates
uniqueList = []
duplicateList = []

for j in mylist:
    if j not in uniqueList:
        uniqueList.append(j)
    elif j not in duplicateList:
        duplicateList.append(j)

print("Unique list is :- ", uniqueList)
print("Duplicate list is :-", duplicateList)
