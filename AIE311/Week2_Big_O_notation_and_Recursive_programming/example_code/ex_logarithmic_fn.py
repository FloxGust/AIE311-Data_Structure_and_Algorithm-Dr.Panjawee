def binarySearch(arr, value, first, last):
    if last >= first:
        mid = (first + last) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binarySearch(arr, value, first, mid - 1)
        else:
            return binarySearch(arr, value, mid + 1, last)
    else:
        return -1
    
numArray = [1, 2, 7, 10, 22, 31]
number = 31
result = binarySearch(numArray, number, 0, len(numArray) - 1)
print(result)