# I
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()
    
    
    
# II   
for i in range(1,6): 
    for j in range(i):
        print(i,end='')
    print("\n")
    
    

# III

num = int(input("Enter Number:"))

for i in range(0, num):
    for j in range(0, i+1):
        print("*", end=" ")

    print()