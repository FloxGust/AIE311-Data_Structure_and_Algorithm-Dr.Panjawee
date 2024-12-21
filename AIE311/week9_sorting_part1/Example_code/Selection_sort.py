import random

def SelectionSort(list):

    size_list = len(list)
    
    for i in range(0, size_list):
        min_idx = i
        for idx in range(i + 1, size_list):
            if list[min_idx] > list[idx]:
                min_idx = idx
                
        tmp = list[i]
        list[i] = list[min_idx]
        list[min_idx] = tmp

    return list

data = [random.randint(0, 100) for i in range(15)]

print("Unsorted data: ", data)
sorted_data = SelectionSort(data)
print("Sorted data:", sorted_data)
