def duplicateCheck(arr):
    for i in range(len(arr)):
        a = arr[i]
        for j in range(i+1, len(arr)):
            b = arr[j]
            print(a,b)
            if (a == b):
                return 'duplicated'
    return 'not duplicated'

numArray = [1, 3, 5, 9]

result = duplicateCheck(numArray)
print(result)