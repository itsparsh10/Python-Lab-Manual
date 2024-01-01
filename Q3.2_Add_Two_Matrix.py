x = [[11,22,33],[44,55,66],[77,88,99]]
y = [[10,11,12],[1,3,7],[8,5,4]]

for i in range(0,3):
    for j in range(0,3):
        x[i][j]+=y[i][j]
print("Addition of matires is:-\n",x)