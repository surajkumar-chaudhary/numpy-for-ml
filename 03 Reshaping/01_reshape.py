import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(arr)
print("Shape:",arr.shape)

arr2 = arr.reshape(2,3)

print("\nReshaped Array:")
print(arr2)
print("Shape:", arr2.shape)
