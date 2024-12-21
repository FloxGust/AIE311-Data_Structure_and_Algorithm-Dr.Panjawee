def binarySearch(arr, value, first, last):
    mid = 0

    while (first <= last):
        mid = (first + last) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
            
    return -1
    
numArray = [1, 2, 7, 10, 22, 31]
number = 22
result = binarySearch(numArray, number, 0, len(numArray) - 1)
print(result)