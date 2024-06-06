import numpy as np
# Define the arrays
num = np.array([1, 2, 3, 4, 5, 6])
print(f"Matrix ->\n {num}")

num2 = np.arange(1, 5) * 5
print(f"Number ->> {num2}")

# Add num and num2 (note: they need to be the same shape for element-wise addition)
# For this example, let's only use the first four elements of num to match num2's shape
print("Addition result ->", np.add(num[:4], num2))

# Multiply num by 5
print("Multiplication result ->", np.multiply(num, 5))

# Calculate the square root of num2
print("Square root of num2 ->", np.sqrt(num2))


######################### Print
array1 =np.array([1,2,3,4,5])
print(array1)

print(array1[ :: ])
print(array1[1:3])

#   use :: for recerse print
print(array1[ :: -1])


print(f"Array ->> \n{np.array([[x for x in range(1,10,2)],[x for x in range(11,20,2)]])}")