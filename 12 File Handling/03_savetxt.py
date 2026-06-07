import numpy as np 

arr = np.array([10,20,30,40,50])

np.savetxt("data3.txt", arr , fmt="%d")

print("Text file saved!")
