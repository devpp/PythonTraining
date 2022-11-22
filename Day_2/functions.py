# Clear screen
import os

os.system('cls')


class test:

    def sum(self):
        print("value printed")

    def summ(self):
        print("value summed")


a = test()
a.sum()
a.summ()

# Returing parameter to mail program
def add(a, b):
    c = a + b
    print("the sum is - ", c)
    return c


add(5, 20)
val = add(5, 10)
print(val / 2)
