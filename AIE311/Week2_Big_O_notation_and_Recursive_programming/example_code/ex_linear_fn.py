def searchNumber(arr, value):
    for i in range(len(arr)):
        if(arr[i] == value):
            return i
        
numArray = [7, 16, 2, 0, 5, 1, 30]
number = 30

result = searchNumber(numArray, number)
print(result)