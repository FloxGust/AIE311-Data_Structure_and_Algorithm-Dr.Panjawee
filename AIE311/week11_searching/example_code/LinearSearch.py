def LinearSearch(arr, target_val):

    n = len(arr)
    
    for idx in range(0, n):

        if (arr[idx] ==  target_val):
            return idx
        
    return -1


data = [50, 42, 63, 19, 58, 93, 10, 73, 34, 45, 30, 25,7, 13, 63, 95]
print(sorted(data))

value = 58

idx = LinearSearch(data, value)

if(idx == -1):
    print("The element is not found in this array")
else:
    print("Result index: ", idx)