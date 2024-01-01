a=int(input("Enter The Number You Wanna Check :"))
sum=0
for i in range (1,a):
    if a%i==0:
        sum=sum+i
if sum==a:
        print("It Is Perfect Number")
else:
        print("It is not a perfect Number ")        