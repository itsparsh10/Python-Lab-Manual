# 3.5 Write a Python function that accepts a string and counts the number of upper-
# and lower-case letters.

# string_test= 'Today is My Best Day'
x=input("Enter a string: ")
uppercount=0
lowercount=0

for i in x:
    if i.isupper():
        lowercount+=1
    elif i.islower():
        uppercount+=1
print(x)
print('Upper case letters =',uppercount,'\nLower case letters =',lowercount)

        
    
    