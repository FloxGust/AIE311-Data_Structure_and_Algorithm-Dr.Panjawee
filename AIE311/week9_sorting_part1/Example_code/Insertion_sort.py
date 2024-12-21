import random

def InsertionSort(list):
   
   for i in range(1,len(list)):
     tmp = list[i]
     idx = i
     while idx > 0 and list[idx - 1] > tmp : 
         list[idx] = list[idx - 1]
         idx = idx-1
     list[idx] = tmp

   return list

data = [random.randint(0, 100) for i in range(15)]

print("Unsorted data: ", data)
sorted_data = InsertionSort(data)
print("Sorted data:", sorted_data)