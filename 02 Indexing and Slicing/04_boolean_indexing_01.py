import numpy as np

arr = np.array([10, 21, 30, 43, 50, 67])

print(arr[arr % 2 == 0])
#[10 30 50]

print(arr[arr % 2 != 0])
#[21 43 67]

print(arr[(arr >= 20) & (arr <= 50)])

print(arr[(arr < 20) | (arr > 50)])