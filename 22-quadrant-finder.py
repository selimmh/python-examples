# This program finds quadrant of given X and Y

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("\nX and Y are at 1st Quadrant")

elif x < 0 and y > 0:
    print("\nX and Y are at 2nd Quadrant")

elif x < 0 and y < 0:
    print("\nX and Y are at 3rd Quadrant")

elif x > 0 and y < 0:
    print("\nX and Y are at 4th Quadrant")

else:
    print("\nX and Y are at base")

print("X = {} | Y = {}".format(x,y))