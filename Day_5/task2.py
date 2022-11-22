import secrets
import checkprime

secretcodes = secrets.SystemRandom()

usrRangeSt = int(input("Enter a range - start :- "))
usrRangeEn = int(input("Enter a range - end :- "))

mylist = []

for i in range(1, 5):
    otp = secretcodes.randrange(usrRangeSt, usrRangeEn)
    mylist.append(otp)

print("The random number list between ", usrRangeSt, " and ", usrRangeEn, " is: -",mylist)
print("--------------Even Odd Check----------------")
for i in mylist:
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")
print("--------------Prime Number Check----------------")
for i in mylist:
    if checkprime.isPrimeNum(i):
        print(i, " is prime")
    else:
        print(i, " is not prime")
