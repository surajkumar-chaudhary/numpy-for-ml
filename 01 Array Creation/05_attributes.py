import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("===== 1D Array =====")
print(arr1)
print("Type:", type(arr1))
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Datatype:", arr1.dtype)

print()

print("===== 2D Array =====")
print(arr2)
print("Type:", type(arr2))
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Datatype:", arr2.dtype)