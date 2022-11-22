""" # clear screen
import os
os.system('cls')

#if else-if
x = 10
if x == 10 and x == 100:
    print("It is 10 or 100")
elif x == 30:
    print("It is 30")
elif x == 50:
    print("It is 50")
else:
    print("No match") 
# print(os.getlogin())

# For loop
mylist = [10,20,30,40,50,60]

for a in mylist:
    print(a)

str = "Hello"
for a in str:
    print(a)
 """
# While Loop
z = 1

while z <=10:
    print("Value is :- ", z)
    z += 1