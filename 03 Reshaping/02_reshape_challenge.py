import numpy as np 
arr = np.array([1,2,3,4,5,6])

print(arr.reshape(3,2))

#arr.reshape(2,4)
#ValueError: cannot reshape array of size 6 into shape (2,4)
#Required elements = 8
#Available elements = 6