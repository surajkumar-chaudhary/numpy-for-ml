import numpy as np

arr = np.array([10,20,30,40,50,60])

filtered = arr[arr>30]
filtered2 = arr[(arr>20) & (arr<60)]

print(filtered)
print(filtered2)
