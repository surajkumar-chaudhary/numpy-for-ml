import numpy as np

arr = np.array([10,20,30,40])

print("Original:")
print(arr)
print("arr shape:",arr.shape)

print("\nColumn Vector:")
print(arr.reshape(-1,1))
print(arr.reshape(-1,1).shape)

print("\nRow Vector:")
print(arr.reshape(1,-1))
print(arr.reshape(1,-1).shape)