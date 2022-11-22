# Clear screen
import os

os.system('cls')


#  Inheritance
class test:
    def printname(self):
        print("Hello Python")


class test2(test):
    def hello(self):
        print("child class")


o = test2()
o.printname()  # Parent class
o.hello()  # child class
