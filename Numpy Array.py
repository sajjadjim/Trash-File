import numpy as np
a = np.array([1,2,3,4,5,6,])
print(a)

# Create 2D Array
array2D =np.array([[1,2,3,4],[4,5,6,7]])
print(f"Array 2D Print->>\n{array2D}")

lst=[x for x in range(1,20,2)], [x for x in range(1,20,1)]        #createing array using List Comprehension
print(f"List comprehension ->> {lst}")

#### Print Array From slected Line to Line
array2D_create = np.array([[x for x in range(1,20,2)],[x for x in range(21,40,2)]])
print(array2D_create)

print(f"Dimention Print Array ->>> {array2D_create.ndim}")
print(f"Print the shape and Value---{array2D_create.shape}")
print(f"Element number of totall ---{array2D_create.size}")
print("\n\n")

# Reshape a Array
Array2D =np.array([[1,2,3,4],[5,6,7,8]] , dtype='int')
print(Array2D)
reshape =np.reshape(Array2D,(4,2))
print(f"New shape Array is Print-------\n{reshape}")
np.transpose(reshape)
print(reshape)


