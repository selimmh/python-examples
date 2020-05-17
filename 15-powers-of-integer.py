# This program calculates the powers of given integer

num = int(input("Number: "))
terms = int(input("Terms: "))

answer = list(map(lambda x: num ** x, range(terms)))

for i in range(terms):
   print(num,"^",i,"=",answer[i])