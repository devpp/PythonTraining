# clear screen
# import os
#
# os.system('cls')

# Get inputs from user
ii = int(input("Enter the number of even numbers to be calculated :- "))  # 20
yy = int(input("Enter the first number :- "))  # 1

i = 1

while i < ii:
    if yy % 2 == 0:
        print(yy, " - counter - ", i)
        i += 1
    yy += 1
