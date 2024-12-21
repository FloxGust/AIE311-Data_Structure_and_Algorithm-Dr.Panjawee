import random  

def quickSortHoare(arr, l_idx, h_idx):  # ฟังก์ชันสำหรับการแบ่ง array โดยใช้ Hoare Partition Scheme 
                                        # เป็นฟังก์ชันสำหรับแบ่งข้อมูล (Partition) โดยใช้ Pivot เพื่อแยกค่าที่น้อยกว่าไปทางซ้ายและค่าที่มากกว่าไปทางขวา
    pivot = arr[l_idx]                  # กำหนดค่า Pivot เป็นค่าของตำแหน่งซ้ายสุดของ array ย่อย
    i = l_idx - 1                       # กำหนดตัวชี้สำหรับตำแหน่งเริ่มต้นที่ซ้ายสุดก่อนตำแหน่งแรก
    j = h_idx + 1                       # กำหนดตัวชี้สำหรับตำแหน่งเริ่มต้นที่ขวาสุดหลังตำแหน่งสุดท้าย
    
    while i < j:               # Loop จนกว่าตัวชี้ซ้ายและขวาจะตัดกัน
        i += 1                 # ขยับตัวชี้ i ไปทางขวา
        while arr[i] < pivot:  # ตรวจสอบค่าใน array ตำแหน่ง i ว่าน้อยกว่า Pivot หรือไม่
            i += 1             # ถ้าน้อยกว่า ขยับตัวชี้ i ต่อไป
        
        j -= 1                 # ขยับตัวชี้ j ไปทางซ้าย
        while arr[j] > pivot:  # ตรวจสอบค่าใน array ตำแหน่ง j ว่ามากกว่า Pivot หรือไม่
            j -= 1             # ถ้ามากกว่า ขยับตัวชี้ j ต่อไป
        
        if i >= j:      # ถ้าตัวชี้ทั้งสองทับกันหรือข้ามกัน
            return j    # ส่งคืนตำแหน่งตัวชี้ j เพื่อแบ่ง array ในขั้นถัดไป
        
        # สลับค่าระหว่างตำแหน่ง i และ j
        tmp0 = arr[i]
        tmp1 = arr[j]
        arr[i] = tmp1
        arr[j] = tmp0

def quickSort(arr, l_idx, h_idx):              # ฟังก์ชัน Quick Sort หลัก
    if l_idx < h_idx:                          # ตรวจสอบว่ามีข้อมูลอย่างน้อย 2 ตำแหน่งในช่วงที่พิจารณา
        j = quickSortHoare(arr, l_idx, h_idx)  # เรียกฟังก์ชันแบ่ง array เพื่อหา Pivot ใหม่
        quickSort(arr, l_idx, j)               # เรียก Quick Sort ซ้ำสำหรับฝั่งซ้ายของ Pivot
        quickSort(arr, j+1, h_idx)             # เรียก Quick Sort ซ้ำสำหรับฝั่งขวาของ Pivot
    return arr                                 # คืนค่า array ที่จัดเรียงเสร็จ

arr = [random.randint(0, 100) for i in range(6)]
print("Unsorted data: " , arr)
sorted_arr = quickSort(arr, 0, len(arr) - 1)
print("Sorted data:", sorted_arr)