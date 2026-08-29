def merge_array(left,right):
    result = []
    i , j = 0, 0 
    n, m = len(left), len(right)
    while i < n  and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i  += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_array(left,right)

# left = [1,1,2,4,2]
# right = [1,2,5,4]
arr = [5,1,5,4,7,2]
print(merge_sort(arr))