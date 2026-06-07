import numpy as np 
arr = np.array([5,10,15,20,25])

mask = arr >= 15

print(mask)
print(arr[mask])