class test:

    def printName(self):
        print("Hello Python!")


class test3:
    name = "Anil"

    def printEmpName(self):
        print("name is ", self.name)


class test2(test, test3):
    def empPrint(self):
        print("Child own func. ", self.name)
        self.printEmpName()


o = test2()
o.empPrint()
o.printName()


class globaltest:
    x = 10
    def printname(self):
        global y
        self.y = 100
        print("Hello Python", self.x)
    def func2(self):
        print("y is ",self.y)

o = globaltest()
o.printname()
o.func2()
