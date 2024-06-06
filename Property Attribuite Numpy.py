import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Shape of the array
print("Shape:", arr.shape)

# Size of the array
print("Size:", arr.size)

# Data type of the array elements
print("Data type:", arr.dtype)

# Number of dimensions of the array
print("Number of dimensions:", arr.ndim)

# Size (in bytes) of each element in the array
print("Item size:", arr.itemsize)

# Total number of bytes consumed by the elements of the array
print("Total bytes:", arr.nbytes)

# Transposed array
print("Transposed array:\n", arr.T)
