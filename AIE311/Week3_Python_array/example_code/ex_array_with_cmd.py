#Add value of array from behind 
A = [2,3,5,2,4]
A.append(5)

#clear value from array
B = [2, 3, 5]
B.clear()

#copy array
C = A.copy()

#count value from array
value = C.count(2)
print(value)

#find location of selected value 
idx_5 = A.index(5)
print(idx_5)

#find length of array
Array = [["Num","Name"], [1,"A"], [2,"B"]]
Array_Length = len(Array)
print(Array_Length)

#Merge 2 arrays together
Array_A = [2,3,5,2,4]
Array_B = [1,7,6,3,3]
Array_A.extend(Array_B)
print(Array_A)

#Remove value by address
Array_A = [2,3,5,2,4]
print(Array_A)
Array_A.pop(3)
print(Array_A)

#Remove value by first location of located value
Array_A = [2,3,5,2,4]
print(Array_A)
Array_A.remove(2)
print(Array_A)

#Reverse value inside array
Array_A = [2,3,5,2,4]
Array_A.reverse()
print(Array_A)
Array_B = [[1,2],[3,4]]
Array_B.reverse()
print(Array_B)
Array_B[1].reverse()
print(Array_B)

#Sorting value
Array_A = [2,3,5,2,4]
Array_A.sort()
Array_B = ["F","A","B","E","C"]
Array_B.sort()
Array_C = ["AC","AA","AB"]
Array_C.sort()
print(Array_A)
print(Array_B)
print(Array_C)