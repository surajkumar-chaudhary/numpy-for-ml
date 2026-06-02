import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)

#First row
print(arr[0])
#Second row
print(arr[1])
#First row first column
print(arr[0,0])
#First row second column
print(arr[0,1])
#First row 3rd column
print(arr[0,2])
#second row 1st column
print(arr[1,0])
#second row second column
print(arr[1,1])
#second row 3rd column
print(arr[1,2])

print(arr[:,0])
print(arr[:,1])
print(arr[:,2])

print(arr[1:,1:])
print(arr[0,:])