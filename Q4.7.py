class Grandfather:
    def __init__(self):
        self.name = "ABC"
        self.inherit = 10100
        self.purchase = 2100

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.name = " XYZ " + self.name
        self.inherit = self.inherit
        self.purchase = 10000 + self.purchase

class Child(Father):
    def __init__(self, name):
        super().__init__()
        self.name = name + self.name
        self.inherit = self.inherit
        self.purchase = self.purchase
        print("Hello", self.name)
        print("Inherited property: Rs", self.inherit)
        print("Purchased property: Rs", self.purchase)
        print("Total property:", self.inherit + self.purchase)

a = input("Enter your name: ")
obj = Child(a)
