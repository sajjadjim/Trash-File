import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)

#Accessing Elements

# Accessing elements in a 2D array
print(array_2d[0, 1])  # Output: 2
print(array_2d[1, 2])  # Output: 6
#Slicing a 2D Array

# Slicing a 2D array
print(array_2d[:, 1])  # Output: [2 5] (second column)
print(array_2d[0, :])  # Output: [1 2 3] (first row)

#Operations on 2D Arrays

# Adding two 2D arrays
array_2d_2 = np.array([[7, 8, 9], [10, 11, 12]])
result_add = array_2d + array_2d_2
print(result_add)

# Element-wise multiplication
result_mul = array_2d * array_2d_2
print(result_mul)

#3D Arrays
#Creating a 3D Array

# Creating a 3D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                     [[7, 8, 9], [10, 11, 12]]])
print(array_3d)

#Accessing Elements

# Accessing elements in a 3D array
print(array_3d[0, 1, 2])  # Output: 6
print(array_3d[1, 0, 1])  # Output: 8

#Slicing a 3D Array

# Slicing a 3D array
print(array_3d[:, 0, :])  # Output: [[ 1  2  3]
                           #          [ 7  8  9]]

print(array_3d[0, :, 1])  # Output: [2 5]

#Operations on 3D Arrays

# Adding two 3D arrays
array_3d_2 = np.array([[[13, 14, 15], [16, 17, 18]],
                       [[19, 20, 21], [22, 23, 24]]])
result_add_3d = array_3d + array_3d_2
print(result_add_3d)

# Element-wise multiplication
result_mul_3d = array_3d * array_3d_2
print(result_mul_3d)

#Additional Operations

# Reshaping a 2D array into a 3D array
reshaped_array = array_2d.reshape((3, 2, 1))
print(reshaped_array)

#Broadcasting

# Broadcasting in 2D arrays
array_2d_b = np.array([[1], [2]])
result_broadcast = array_2d + array_2d_b
print(result_broadcast)

#Aggregation Functions

# Sum of all elements in 2D array
sum_2d = np.sum(array_2d)
print(sum_2d)

# Mean of elements along an axis in 3D array
mean_3d = np.mean(array_3d, axis=0)
print(mean_3d)