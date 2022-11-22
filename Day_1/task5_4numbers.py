#Clear screen
import os
os.system('cls')

#Get inputs from user
x = int(input("Enter number 1 :- "))
y = int(input("Enter number 2 :- "))
z = int(input("Enter number 3 :- "))
a = int(input("Enter number 4 :- "))

small = 0
large = 0

if x < y and x < z and x < a :
    small = x
elif y < z and y < a :
    small = y
elif z < a :
    small = z
else :
    small = a
print(small, "is the smallest")

if x > y and x > z and x > a :
    large = x
elif y > z and y > a :
    large = y
elif z > a :
    large = z
else :
    large = a
print(large, "is the largest")
