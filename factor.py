from math import sqrt
#Find all factors given number
num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     if  num % i == 0:
#         print(i , end =" ")
# print()
result = []
for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
    if num // i != 0:
        result.append(num // i)
print(result)