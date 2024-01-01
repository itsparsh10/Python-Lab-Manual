class Addition:
    @staticmethod
    def add(a, b):
        print("Sum:", a + b)

class Numbers(Addition):
    def getNumbers(self):
        c = float(input("Enter a number: "))
        d = float(input("Enter another number: "))
        self.add(c, d)

e = Numbers()
e.getNumbers()
