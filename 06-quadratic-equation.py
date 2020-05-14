# This program calculates quadratic equation
# ax^2 + bx + c = 0 | a,b,c e R | a ≠ 0

import cmath

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# discriminant
d = (b**2) - (4*a*c)

# solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("Solution 1:", sol1)
print("Solution 2:", sol2)