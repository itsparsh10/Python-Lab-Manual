#Write a program to perform arithmetic, Relational operators.
a = float(input("Enter first number :"))
b = float(input("Enter Second number :"))
print("Arithmetic operations are :-")

print("Addition of :",a,"+",b,"is",a+b)

print("Subtraction of :",a,"-",b,"is",a-b)

print("Multiplication of :",a,"*",b,"is",a*b)

print("Division of :",a,"/",b,"is",a/b)

print("Modules of :",a,"%",b,"is",a%b)

print(a,"//",b,"is",a//b)

print(a,"**",b,"is",a**b)



if a>b:
    print(a,"is greater")
elif b>a:
    print(b,"is greater")
elif a == b:
    print("Both are equal")
else :
    print("Invalid Input ")