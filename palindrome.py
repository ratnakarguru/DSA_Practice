# def func(n):
#     left = 0
#     right = len(n) - 1
#     while left < right:
#         if n[left] != n[right]:
#             return False
#         left += 1
#         right -=1
#     return True

# print(func("String"))
def func(n,left,right):
    # left = 0
    # right = len(n) - 1
    while left < right:
        if n[left] != n[right]:
            return False
        func(n,left+1,right-1)
    return True

str1 = "mom"
print(func(str1,0,len(str1)-1))