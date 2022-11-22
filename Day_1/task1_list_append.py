# clear screen
import os
os.system('cls')

#Get inputs from user
x = int(input("Enter number 1 :- "))
y = int(input("Enter number 2 :- "))
z = int(input("Enter number 3 :- "))

#Declare and append list
mylist = []
mylist.append(x)
mylist.append(y)
mylist.append(z)

#output
print("The list is :- ",mylist)

summ = mylist[0] + mylist[1] + mylist[2]
print("The sum : ",summ)

#method 2
summm = 0
for xx in mylist:
    summm = summm + xx
print(summm)

#end of program