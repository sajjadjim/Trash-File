import numpy as np

# Create a 4x3 matrix
matrix = np.zeros((4, 3))

# Fill the first and third row with values from 10 to 30 with the same distance
matrix[0, :] = np.arange(10, 31, 2).reshape(1, -1)
matrix[2, :] = np.arange(10, 31, 2).reshape(1, -1)

print("Original Matrix:")
print(matrix)
print()


# i. Identify the shape of diagonal, above and below diagonal values
diagonal = np.diag(matrix)
above_diagonal = np.diag(matrix, k=1)
below_diagonal = np.diag(matrix, k=-1)

print("Diagonal values:", diagonal)
print("Above diagonal values:", above_diagonal)
print("Below diagonal values:", below_diagonal)
print()

# ii. Construct a 3x4 matrix from the previous one
matrix_3x4 = matrix[:, :4]
print("3x4 Matrix:")
print(matrix_3x4)
print()

# Calculate mean, max, variance values of 2nd to 4th column
column_2_to_4 = matrix_3x4[:, 1:]
column_mean = np.mean(column_2_to_4, axis=0)
column_max = np.max(column_2_to_4, axis=0)
column_variance = np.var(column_2_to_4, axis=0)

print("Mean of columns 2 to 4:", column_mean)
print("Max of columns 2 to 4:", column_max)
print("Variance of columns 2 to 4:", column_variance)
print()

# iii. Describe the difference between a numpy array can access previous memory or can not access.
# Numpy array with contiguous memory layout can access previous memory efficiently due to better caching.
# On the other hand, non-contiguous arrays may not be able to access previous memory efficiently.
