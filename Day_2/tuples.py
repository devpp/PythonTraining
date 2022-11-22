# Clear screen
import os

os.system('cls')

# Tuples
mytup = (10, 20, 30, 40, 50)
mytup2 = (10, "A", 30, "B", 40)
print(mytup)
print(type(mytup))

mytup3 = ("A",) # without comma it is a string
print(type(mytup3))

mylist = list(mytup)
mylist.append(90)
print(mylist)

mytup3 = mytup + mytup2
print(mytup3)