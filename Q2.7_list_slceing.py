# Write a program for various list slicing operation.
# a= [10,20,30,40,50,60,70,80,90,100]
# i. Print Complete list
# ii. Print 4th element of list
# iii. Print list from0th to 4th index.
# iv. Print list -7th to 3rd element
# v. Appending an element to list.
# vi. Sorting the element of list.
# vii. Popping an element.
# viii. Removing Specified element.
# ix. Entering an element at specified index.
# x. Counting the occurrence of a specified element.
# xi. Extending list.
# xii. Reversing the list.
a= [10,20,30,40,50,60,70,80,90,100]
print(a)

# ii
z=a[4]
print(z)

# iii
b = a[0:4]
print(b)

# iv
c=a[-7:3]
print(c)

# v
d=a.append(110)
print(a)

# vi
e=sorted(a)
print(e)

# vii
f=a.pop(10)
print(a)


# viii
g=a.remove(50)
print(a)


# ix
h=a[5]
print(h)


# x. Extending list.
new_element = [110, 120, 130, 140]
a.extend(new_element)
print(a)


# xi Reversing
a.reverse()
print(a)



