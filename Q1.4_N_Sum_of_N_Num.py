n = int(input("Enter the number you want to print up to: "))
sum_of_numbers = 0

for i in range(1, n + 1):
    sum_of_numbers += i
    print(i)

print("\nThe Sum of the numbers is:", sum_of_numbers)
