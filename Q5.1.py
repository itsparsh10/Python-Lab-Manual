class Addition:
def add(self, x, y):
print("Sum:", x + y)
import my_module
a = my_module.Addition()
b = float(input("Enter First number: "))
c = float(input("Enter Second Number: "))
a.add(b, c)