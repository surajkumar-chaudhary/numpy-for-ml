import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60]
])


print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))