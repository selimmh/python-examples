# This programs tells if number is perfect or not
# Perfect number is a positive integer that is equal to the sum of its proper divisors 

def perfect():
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i 

    if sum == num:
        print(num, "is perfect number")
    else:
        print(num, "is not perfect")

num = int(input("Number: "))
perfect()