# print prime number

def isPrimeNum(num):
    if (num == 1 or num == 0):
        return False

    for i in range(2, int(num/2 + 1)):
        if (num % i) == 0:
            return False

    return True
#
#
# # Get input from user
# numbers = int(input("Numbers (till N) to check? :-"))
#
# for j in range(1, numbers + 1):
#     if isPrimeNum(j):
#         print(j)
#
# numrev = int(input("Enter the number to reverse :"))
# print(int(str(numrev)[::-1]))