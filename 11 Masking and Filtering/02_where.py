import numpy as np 

arr = np.array([10,20,30,40,50])

result1 = np.where(arr > 25)


result = np.where(arr > 25 , 1 ,0)
# If condition is True → put 1
# Else → put 0

# np.where(age >= 18, "Adult", "Minor")
# If condition is True → put Adult
# Else → put Minor

# np.where(score >= 50, "Pass", "Fail")
# If condition is True → put Pass
# Else → put Fail

print(result1)

print(result)