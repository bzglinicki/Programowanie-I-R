# Programowanie I R
# Pakiet NumPy

import numpy as np

arr_list = np.array([1, 2, 3, 4, 5])

print(arr_list)
print(type(arr_list))
print()

arr_tuple = np.array((1, 2, 3, 4, 5))

print(arr_tuple)
print(type(arr_tuple))
print()

arr = np.array(42)
print(arr)
print(arr.ndim)
print()

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)
print()

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)
print()

arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print(arr.ndim)
print()

#***********************************************************************************

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3])
print()

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, 3])
print(arr[1, 2])
print(arr[1, -1]) 
print()

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print()

#***********************************************************************************

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[1:5:2])
print()

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 1:4])

#***********************************************************************************

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
print()

newarr = np.subtract(arr1, arr2)
print(newarr)
print()

newarr = np.multiply(arr1, arr2)
print(newarr)
print()

newarr = np.divide(arr1, arr2)
print(newarr)
print()