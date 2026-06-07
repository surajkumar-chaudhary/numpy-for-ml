import numpy as np 

arr = np.array([10,20,30,40,50])

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print(normalized)

# Question 1

# Which guarantees values between 0 and 1?

# You answered:

# B) Normalization

# ✅ Correct.

# Normalization:

# (arr - min) / (max - min)

# always gives:

# 0 ≤ value ≤ 1