# Clear screen
import os

os.system('cls')

# Get inputs from user
mylist = [int(input("Enter number 1 :- ")), int(input("Enter number 2 :- ")), int(input("Enter number 3 :- ")),
          int(input("Enter number 4 :- ")), int(input("Enter number 5 :- "))]

# Check even or odd
for xx in mylist:
    if xx % 2 == 0:
        print(xx, " - the number is even")
    else:
        print(xx, " - the number is odd")
#    print("square of - ",xx, " is ", xx ** 2)

# Square of numbers
for yy in mylist:
    print("square of - ", yy, " is ", yy ** 2)
"""

# Break
mylist = [10,20,30,40,50]

for a in mylist:
   print(a)
   if a == 40:
       print("Value matched :- ",a)
       break # terminates the loop

# Continue
mylist2 = [10,20,30,40,50]

for a in mylist2:
   if a == 40:
       continue # skips this line and continues to next line
   print(a) """
