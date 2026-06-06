import numpy as np

A = np.array([
    [1,0],
    [0,1]
])

B = np.array([
    [5,6],
    [7,8]
])


print(A @ B)

# Important

# This is NOT:

# A * B

# which is element-wise multiplication.