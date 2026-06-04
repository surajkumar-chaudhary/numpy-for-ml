import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print("Original:")
print(arr)
print(arr.shape)

transposed = arr.T

print("\nTransposed:")
print(transposed)
print(transposed.shape)