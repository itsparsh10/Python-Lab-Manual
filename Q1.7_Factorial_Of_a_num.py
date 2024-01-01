n=int(input(" Enter The value :"))
if n<0:
        print(" it is not a factorial :")
else:
    fact=1
    for i in range (1,n+1):
        fact =fact*i

print(f" The Factorial Of {n} is : {fact} ")