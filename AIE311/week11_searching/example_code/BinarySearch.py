def BinarySearch(arr, l_idx, h_idx, target_val):
    

    if h_idx >= l_idx:
 
        mid_idx = (h_idx + l_idx) // 2

        if arr[mid_idx] == target_val:
            return mid_idx
 
        elif arr[mid_idx] > target_val:

            return BinarySearch(arr, l_idx, h_idx - 1, target_val)
 
        else:
            return BinarySearch(arr, mid_idx + 1, h_idx, target_val)
 
    else:
       
        return -1
 

arr = [7, 10, 13, 19, 25, 30, 34, 42, 45, 50, 58, 63, 63, 73, 93, 95]
value = 58

idx = BinarySearch(arr, 0, len(arr), value)
 
if(idx == -1):
    print("The element is not found in this array")
else:
    print("Result index: ", idx)