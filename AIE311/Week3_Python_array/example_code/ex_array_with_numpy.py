import numpy as np

# 1D array
arr1 = np.array([6, 7, 8])
print(arr1)
#print shape of array
print(arr1.shape)
#print dimension of array
print(arr1.ndim)



#insert data to array
arr1[0] = 5
print(arr1)


#2D array
arr2 = np.array([[1,2,3], [3,4,5]])
print(arr2)
#print shape of array 
print(arr2.shape)
#print dimension of array
print(arr2.ndim)
print(arr2[0][1])

#3d array
arr3 = np.array([[[1,2,3],[4,5,6]],
                 [[7,8,9],[10,11,12]],
                 [[13,14,15],[16,17,19]]])
print(arr3)
#print shape of array 
print(arr3.shape)
#print dimension of array
print(arr3.ndim)
#access to the specific index of array
print(arr3[2][1][1])

