import numpy as np

arr = np.array([10, 20, np.nan, 40, 50])

print(arr)

arr2 = np.array([10,20,np.nan,40])

arr2[np.isnan(arr2)] = 0
# What does np.isnan() do?
# np.isnan(arr)

# returns:

# [False False True False]

# Then:

# arr[np.isnan(arr)] = 0

# replaces every True position with 0.

print(arr2)

# What is np.nan?
# nan = Not A Number

# Used to represent:

# Missing data
# Unknown value
# Empty value

# Example:

# Age
# 20
# 25
# ?
# 30

# becomes:

# [20, 25, np.nan, 30]