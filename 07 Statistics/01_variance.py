import numpy as np

a = np.array([10,20,30,40,50])
b = np.array([28,29,30,31,32])

print("Variance of A:", a.var())
print("Variance of B:", b.var())

# One thing to remember

# Variance is measured in squared units.

# For example:
# Height → cm

# Variance → cm²
# That's why people often prefer Standard Deviation, because:
# Standard Deviation = √Variance
# and it returns to the original units.
# Example:
# Variance = 25
# Standard Deviation = 5
# Much easier to interpret.