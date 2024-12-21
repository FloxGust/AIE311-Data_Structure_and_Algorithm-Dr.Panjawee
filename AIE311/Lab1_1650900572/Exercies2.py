first_array = [7, 5, 10, 14, 3, 9, 7]
second_array = [9, 10, 3, 4, 2, 5, 7, 1]

print("First Array:", first_array)
print("Second Array:", second_array)

print("Length of First Array:", len(first_array))
print("Length of Second Array:", len(second_array))

first_array.append(15)
print("Insert 15 in 1stArray:", first_array)

index_first = first_array.index(7)
index_second = second_array.index(7)
print(" Find index of 7 in First Array:", index_first)
print(" Find index of 7 in Second Array:", index_second)

first_array.append(1)
second_array.append(14)
print("First Array after appending 1:", first_array)
print("Second Array after appending 14:", second_array)

third_array = first_array.copy()
print("Third Array (copy of First Array):", third_array)

merged_array = third_array + second_array
print("\nMerged Array (Third Array + Second Array):\n", merged_array)

count_of_7_in_third = third_array.count(7)
print("\nCount of 7 in Third Array:", count_of_7_in_third)

third_array.sort()
print("\nThird Array after sorting:", third_array)

third_array = [value for value in third_array if value != 7]
print("\nThird Array after removing 7:", third_array)

fourth_array = third_array.copy()
print("\nFourth Array (copy of Third Array):", fourth_array)

fourth_array.reverse()
print("\nFourth Array after reversing:", fourth_array)

print("Final Third Array:", third_array)
print("Final Fourth Array:", fourth_array)