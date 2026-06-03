import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original:")
print(arr)
print("Shape:", arr.shape)

flat = arr.flatten()

print("\nFlattened:")
print(flat)
print("Shape:", flat.shape)

#Will this work?
# flat = arr.flatten()

# flat.reshape(3,2)

#Answer: ✅ Yes.

#Because:
# flatten()
# ↓
# didn't remove data

# reshape()
# ↓
# doesn't change data