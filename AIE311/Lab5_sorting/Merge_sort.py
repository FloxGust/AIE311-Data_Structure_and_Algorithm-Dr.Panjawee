import random

def merge_sort(arr): 
    
    size_arr = len(arr)  # กำหนดตัวแปร size_arr เพื่อเก็บขนาดของ array
    
    if size_arr > 1:  # ตรวจสอบว่า array มีมากกว่า 1 หรือไม่ 
        
        mid_idx = size_arr // 2  # ใช้หาตำแหน่งตรงกลางของ array
        
        l_arr = arr[:mid_idx]  # แบ่งส่วน array ซ้ายจากเริ่มต้นถึงตำแหน่งกลาง
        r_arr = arr[mid_idx:]  # แบ่งส่วน array ขวาจากตำแหน่งกลางถึงจบ
        
        merge_sort(l_arr)  # เรียก merge_sort สำหรับ array ด้านซ้าย
        merge_sort(r_arr)  # เรียก merge_sort สำหรับ array ด้านขวา
        
        l_arr_idx, r_arr_idx, m_arr_idx = 0, 0, 0  # กำหนดค่า array ซ้าย, ขวา และหลัก เป็น 0
        
        
        while l_arr_idx < len(l_arr) and r_arr_idx < len(r_arr):  
            if l_arr[l_arr_idx] < r_arr[r_arr_idx]:  # เปรียบเทียบค่าระหว่าง array ซ้ายและขวา
                arr[m_arr_idx] = l_arr[l_arr_idx]    # ถ้าค่าของ array ซ้ายมีขนาดเล็กกว่า ให้นำค่าใส่ใน array หลัก
                l_arr_idx += 1                       # เลื่อนตำแหน่งของ array ซ้าย
            else:
                arr[m_arr_idx] = r_arr[r_arr_idx]   # ถ้าค่าของ array ขวามีขนาดเล็กกว่า ให้นำค่าใส่ใน array หลัก
                r_arr_idx += 1                      # เลื่อนตำแหน่งของ array ขวา
            m_arr_idx += 1                          # เลื่อนตำแหน่งของ array หลัก
        
        while l_arr_idx < len(l_arr):                # เพิ่มค่าที่เหลือใน array ซ้ายเข้าสู่ array หลัก
            arr[m_arr_idx] = l_arr[l_arr_idx]        # ถ้าค่าของ array ซ้ายมีขนาดเล็กกว่า ให้นำค่าใส่ใน array หลัก
            l_arr_idx += 1                           # เลื่อนตำแหน่งของ array ซ้าย
            m_arr_idx += 1                           # เลื่อนตำแหน่งของ array หลัก
          
        while r_arr_idx < len(r_arr):               # เพิ่มค่าที่เหลือใน array ขวาเข้าสู่ array หลัก
            arr[m_arr_idx] = r_arr[r_arr_idx]       # ถ้าค่าของ array ขวามีขนาดเล็กกว่า ให้นำค่าใส่ใน array หลัก
            r_arr_idx += 1                          # เลื่อนตำแหน่งของ array ขวา
            m_arr_idx += 1                          # เลื่อนตำแหน่งของ array หลัก
    
    return arr  # คืนค่า array ที่จัดเรียงเสร็จ
            

arr = [random.randint(0, 100) for i in range(15)]

print("Unsorted data: " , arr)
sorted_arr = merge_sort(arr)
print("Sorted data:", sorted_arr)