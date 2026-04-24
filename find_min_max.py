#Find Minimum and Maximum number in a array
def Find(arr):
    minn , maxx = arr[0], arr[0]
    for num in arr[1:]:
        if num < minn:
            minn = num
        elif num > maxx:
            maxx = num
    return minn , maxx 

arr = [12,1,4,5,6,8,1]
minn, maxx = Find(arr)
print(minn, maxx)
             
