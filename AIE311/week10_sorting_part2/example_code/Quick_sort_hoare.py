import random

def quickSortHoare(arr, l_idx, h_idx):
    pivot = arr[l_idx]
    i = l_idx - 1
    j = h_idx + 1
    while i<j:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        tmp0 = arr[i]
        tmp1 = arr[j]
        arr[i] = tmp1
        arr[j] = tmp0

def quickSort(arr, l_idx, h_idx):
    if l_idx < h_idx:
        j = quickSortHoare(arr, l_idx, h_idx)
        quickSort(arr, l_idx, j)
        quickSort(arr, j+1, h_idx)
    return arr

arr = [random.randint(0, 100) for i in range(6)]
print("Unsorted data: " , arr)
sorted_arr = quickSort(arr, 0, len(arr) - 1)
print("Sorted data:", sorted_arr)