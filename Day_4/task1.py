# clear screen
import os

os.system('cls')

# Accept  Strings
n = int(input("Enter no of strings you want to enter :-"))
mylist = []
i = 1

while i <= n:
    num = input("Enter string  " + str(i) + ":")
    mylist.append(num)
    i += 1

mylist.sort()
maxlength = -1
minlength = 9999

for a in mylist:
    if len(a) > maxlength:
        maxlength = len(a)
        longest = a
    elif len(a) < minlength:
        minlength = len(a)
        shortest = a

print("Sorted list is :-", mylist)
print("Shortest is :-", shortest)
print("Longest is :- ", longest)

ii = 0
while ii == 0:
    stopr = input("Enter the string opr -\n (1) capitalize \n (2) to lower \n (3) to upper \n (4) to end \n:-")

    if stopr == "1":
        print(longest.capitalize())
    elif stopr == "2":
        print(longest.lower())
    elif stopr == "3":
        print(longest.upper())
    elif stopr == "4":
        print("Exiting!!!")
        ii = 1
