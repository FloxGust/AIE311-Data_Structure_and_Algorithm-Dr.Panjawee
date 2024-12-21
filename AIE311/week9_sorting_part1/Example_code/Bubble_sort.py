import random

def BubbleSort(list):

    start_idx, stop_idx = len(list) - 1,  0
    step = -1
    
    for n in range(start_idx, stop_idx, step):
        for idx in range(0, n):
            if list[idx + 1] < list[idx]:
                tmp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = tmp
               
    return list

data = [random.randint(0, 10000) for i in range(1500)]

print("Unsorted data: ", data)
sorted_data = BubbleSort(data) 
print("\nSorted data:", sorted_data)
