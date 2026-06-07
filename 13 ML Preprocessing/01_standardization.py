import numpy as np 

arr = np.array([10,20,30,40,50])

print(arr - arr.mean())
print(arr.std())

standardized = (arr - arr.mean()) / arr.std()

print(standardized)

# Important ML Interview Fact

# After standardization:

# Mean ≈ 0
# Standard Deviation ≈ 1

# That's the whole goal.