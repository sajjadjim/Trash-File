import numpy as np

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1.max())
print(array1.min())
print(array1.sum())
print(array1.var())
print(array1.mean())

num1 = np.arange(1,5)
print(num1)

num2 = num1.copy()
print(num2)

num1[2] *= 5
print(num1)
