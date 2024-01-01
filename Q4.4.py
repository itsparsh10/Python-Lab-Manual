class Store:
    __itemCode = 0
    __price = 0

    def setdata(self):
        self.a = int(input("Product:\n1. Soap\n2. Shampoo\n3. Bread\n4. Milk\n"))

        if self.a == 1:
            self.__itemCode = 1
            self.__price = 10
            self.price = self.__price
            self.n = int(input("How many do you want: "))
        elif self.a == 2:
            self.__itemCode = 2
            self.__price = 100
            self.price = self.__price
            self.n = int(input("How many do you want: "))
        elif self.a == 3:
            self.__itemCode = 3
            self.__price = 40
            self.price = self.__price
            self.n = int(input("How many do you want: "))
        elif self.a == 4:
            self.__itemCode = 4
            self.__price = 30
            self.price = self.__price
            self.n = int(input("How many do you want: "))
        else:
            print("INVALID INPUT")

    def getdata(self):
        if self.a == 1:
            print(f"FOR {self.n}  Packs of Soap, You Have To Pay: Rs.{self.n * self.price}")
        elif self.a == 2:
            print(f"FOR {self.n} Packs of Shampoo, You Have To Pay: Rs.{self.n * self.price}")
        elif self.a == 3:
            print(f"FOR {self.n} Packs of Bread, You Have To Pay: Rs.{self.n * self.price}")
        elif self.a == 4:
            print(f"FOR {self.n}  Packs of Milk, You Have To Pay: Rs.{self.n * self.price}")

obj = Store()
obj.setdata()
obj.getdata()
