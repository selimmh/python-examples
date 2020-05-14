# This program checks if number is prime or not

num = int(input("Enter number: "))

if num > 1:
   for i in range(2,num):
        if (num % i) == 0:
           print("Not prime")
           break
        else:
            print("Prime")
            break

else:
   print("Not prime, n < 1")