import numpy as np

arr = np.array([10,20,30,40,50])

result = np.array_split(arr, 2)

print(result)

# split()
# ↓
# Equal parts only

# array_split()
# ↓
# Unequal parts allowed