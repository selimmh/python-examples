# This program calculates 1st degree equation

print ("Equation is - A+ B*X = C\n")
a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

if b == 0:
  print("Equation is not 1st degree")

else: 
    x=(c-a)/b
    print ("Value of X: " + str(x))