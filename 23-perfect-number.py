# This programs tells if number is perfect or not
# Perfect number is a positive integer that is equal to the sum of its proper divisors
# Some perfect numbers: 6, 28, 496, 8128, 33550336, 8589869056, 137438691328

def perfect_num():
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i 

    if sum == num:
        print(num, "is perfect number")
    else:
        print(num, "is not perfect number")

num = int(input("Enter number: "))
perfect_num()