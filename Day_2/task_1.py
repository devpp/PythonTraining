# clear screen
import os

os.system('cls')

# 
usrinp = input("Enter the string: ")
st = int(input("Start of string : "))
en = int(input("End of string : "))

print(usrinp[st:en])

yn = input("Do you want to reverse the string? (yes/no) : ")

if yn == "yes":
    print("The reverse of string is : ", usrinp[::-1])
else:
    print("Bye!!!")
