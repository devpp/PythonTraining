class test:
    def __init__(self, name, city):
        # print("def cons")
        self.name = name
        self.city = city

    def printName(self):
        print("values are ", self.name, self.city)


o = test("Praveen", "Trichy")
o.printName()
