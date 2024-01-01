# Write a program that creates dictionary of cube of odd numbers in the range.
a={x: (x**3) for x in range(1,11) if x%3==0}
print(a)
