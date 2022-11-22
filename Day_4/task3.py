# clear screen
import os

os.system('cls')

# Accept  Strings
strn = input("Enter the string value :-")

vowels = ["a","e","i","o","u"]
noofvow = 0
vowres = []
cons = []
for a in strn:
    if a in vowels:
        noofvow += 1
        if a not in vowres:
            vowres.append(a) 
    else:
        if a not in cons:
            cons.append(a)

myd= {}.fromkeys(vowels,0)
# To count the vowels
for character in strn:
    if character in myd:
        myd[character] += 1   

print("No of Vowels :- ",noofvow)
print("Vowels : ",vowres)
print("Consonants : ",cons)
print(myd)