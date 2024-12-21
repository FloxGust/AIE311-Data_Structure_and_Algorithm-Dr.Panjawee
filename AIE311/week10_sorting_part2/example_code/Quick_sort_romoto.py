import random

def quickSort_lomuto(arr, l_idx, h_idx):
    
    if(l_idx >= h_idx):
        return
    
    pivot = arr[h_idx]
    j = l_idx
    
    for i in range(l_idx, h_idx):
        if (arr[i] <= pivot):
            tmp0 = arr[j]
            tmp1 = arr[i]
            arr[i] = tmp0
            arr[j] = tmp1
            j = j+1
            
    tmp0 = arr[j]
    tmp1 = arr[h_idx]
    arr[h_idx] = tmp0
    arr[j] = tmp1
    
    quickSort_lomuto(arr, l_idx, j-1)
    quickSort_lomuto(arr, j+1, h_idx)
    
    return arr
    
arr = [random.randint(0, 100) for i in range(6)]
print("Unsorted data: " , arr)
sorted_arr = quickSort_lomuto(arr, 0, len(arr)-1)
print("Sorted data:", sorted_arr)