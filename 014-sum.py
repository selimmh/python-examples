# This program calculates sum of integers up to given range using list

num = int(input("Enter number: "))
my_list = []

if num < 0:
    print("Enter positive number")

else:
    for i in range(0,num):
        my_list.append(i)

print(my_list)
print(sum(my_list))
    
    