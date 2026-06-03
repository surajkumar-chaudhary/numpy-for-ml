import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

flat1 = arr.flatten()
flat2 = arr.ravel()

flat1[0] = 999
flat2[1] = 888

print(flat1)
print(flat2)

print("\nOriginal array:")
print(arr)

# flatten()
# ↓
# Copy
# ↓
# Changes do not affect original array

# ravel()
# ↓
# View
# ↓
# Changes affect original array