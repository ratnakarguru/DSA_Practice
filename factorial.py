def func(n):
    if n == 0 or n == 1:
        return 1

    return n * func (n-1)

f = func(5)
print(f)

n = 5
fact = 1
for i in range(1,n+1):
    # print(i)
    fact = fact * i
    i += 1

print(fact)