a=int(input("Enter a number: "))
b=len(str(a))
c=a
sum=0
while c!=0:
    d=c%10
    sum+=d**b
    c//=10
if sum==a:
    print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")