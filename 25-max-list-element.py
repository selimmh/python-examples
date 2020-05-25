# This program takes list elements from user and prints max element

n = int(input("Length of list: "))
list = [0]*n

for i in range(n):
    a = int(input("Element ["+str(i+1)+"]: "))
    list[i] = a

print("\nMax element: ", max(list))