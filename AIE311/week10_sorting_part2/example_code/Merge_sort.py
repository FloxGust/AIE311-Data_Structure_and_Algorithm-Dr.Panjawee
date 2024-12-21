import random

def merge_sort(arr):
    
    size_arr = len(arr)
    
    if size_arr > 1:
        
        mid_idx = size_arr//2
        
        l_arr = arr[: mid_idx]
        r_arr = arr[mid_idx :]
    
        merge_sort(l_arr)
        merge_sort(r_arr)
        
        l_arr_idx, r_arr_idx, m_arr_idx = 0, 0, 0  

        while l_arr_idx < len(l_arr) and r_arr_idx < len(r_arr):
            if l_arr[l_arr_idx] < r_arr[r_arr_idx]:
                
                arr[m_arr_idx] = l_arr[l_arr_idx]
                l_arr_idx += 1
            else:
                
                arr[m_arr_idx] = r_arr[r_arr_idx]
                r_arr_idx += 1
            m_arr_idx += 1
            
        while l_arr_idx < len(l_arr):
            
            arr[m_arr_idx] = l_arr[l_arr_idx]
            l_arr_idx += 1
            m_arr_idx += 1
        
        while r_arr_idx < len(r_arr):
            
            arr[m_arr_idx] = r_arr[r_arr_idx]
            r_arr_idx += 1
            m_arr_idx += 1
    return arr
            

arr = [random.randint(0, 100) for i in range(15)]

print("Unsorted data: " , arr)
sorted_arr = merge_sort(arr)
print("Sorted data:", sorted_arr)