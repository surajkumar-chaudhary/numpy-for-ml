import numpy as np

arr = np.array([1,2,3,4])

arr.resize((2,2))

print(arr)

# reshape()

# Returns a new view/array.
# arr2 = arr.reshape(2,2)
# Original array remains unchanged.

# resize()

# Changes the original array itself.
# arr.resize((2,2))
# print(arr)
# [
#  [1 2]
#  [3 4]
# ]

# reshape() returns a reshaped array and usually leaves the original unchanged.

# resize() modifies the original array in-place.