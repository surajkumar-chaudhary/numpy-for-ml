import numpy as np

arr = np.array([10,20,30,40,50])

arr[arr>30] = 999

print(arr)

# [ 10  20  30 999 999]
# What's happening?

# First create mask:

# 10 > 30 → False
# 20 > 30 → False
# 30 > 30 → False
# 40 > 30 → True
# 50 > 30 → True

# Then replace all True positions with:

# 999