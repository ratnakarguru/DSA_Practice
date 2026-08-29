def selection(num):
    n = len(num)
    for i in range(0,n):
        min_val = i
        for j in range(i+1,n):
           if num[min_val] < num[j]:# Decending order and if j < min_val then it asscending order
               min_val = j

        num[i], num[min_val] = num[min_val], num[i]
    return num      
        



arr = [8,2,5,1,9]
print(selection(arr))
print(arr)