# This program takes sides of a triangle from user and calculates its perimeter and area
# Perimeter: a+b+c | Area: √(s(s-a)*(s-b)*(s-c)), s = (a+b+c)/2

a = int(input("1st side: "))
b = int(input("2nd side: "))
c = int(input("3rd side: "))

per = a+b+c
print("Perimeter is:",per)

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area is:",area)