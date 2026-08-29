def func(arr,left,right):
    # left = 0
    # right = len(arr) - 1
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]

    return func(arr,left+1,right-1)

arr = [2,5,8,7,9,1,0,5]
res = func(arr,3,len(arr)-1)
print(arr)


