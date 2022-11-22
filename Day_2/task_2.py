# clear screen
import os

os.system('cls')

# Enter the values
val1 = input("Enter the value 1 :-")
val2 = input("Enter the value 2 :-")
val3 = input("Enter the value 3 :-")
val4 = input("Enter the value 4 :-")
val5 = input("Enter the value 5 :-")

lord = input("Do you want to create a list or dictionary? (L or D) :- ")

if lord == "L" or lord == "l":
    mylist = []
    mylist.append(val1)
    mylist.append(val2)
    mylist.append(val3)
    mylist.append(val4)
    mylist.append(val5)
    print("The list is :-",mylist)
elif lord =="D" or lord =="d":
    myD = {0 : val1 , 1 : val2 , 2 : val3, 3 : val4, 4: val5}
    print("The dict is :-",myD)
else:
    print("Wrong input!!!")
    

