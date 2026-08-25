# def rec(val):
#     val += 1
#     print(val)
#     return rec(val)

# print(rec(1))

# def func(i,n):
#     if i > n:
#         return
#     print(i)
#     func(i+1, n)
#     # print(i)

# func(1,4)    

def SumofDigits(total,i,n):
    if i > n:
        print(total)
        return
    SumofDigits(total+i,i+1, n)
    # print(total)
SumofDigits(0,1,5)