n = int(input("Enter value:"))
num = n
rev = 0
# while n > 0:
#     temp = n % 10
#     rev = (rev * 10) + temp //Reverese a number
#     n = n // 10

#Count digits
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1

#Armstrong Number

power = len(str(n))
total = 0
while n > 0:
    temp  = n % 10
    total = (temp ** power) + total
    n = n // 10

if total == num:
    print(True)
else:
    print(False)
print(total) 