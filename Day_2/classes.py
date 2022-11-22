class Calc:
    def sum(self):
        print("Normal function")

    def sub(self, a, b):
        c = b - a
        print("sub is ", c)


obj = Calc()
obj.sum()
obj.sub(10, 30)
