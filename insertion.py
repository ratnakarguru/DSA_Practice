def func(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        # while j >= 0 and key > arr[j]:#if arr[j] > key then it short in asscending order and if it in reverse then it descending order
        while j >= 0 and arr[j] > key:#if arr[j] > key then it short in asscending order and if it in reverse then it descending order
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [4,8,7,6,0,1,10]
print(func(arr))
print(arr)