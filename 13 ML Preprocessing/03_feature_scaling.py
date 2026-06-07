import numpy as np 

salary = np.array([30000,50000,70000])

scaled = salary/1000

print(scaled)

# Why?

# Sometimes you don't need full normalization.

# Simple scaling is enough.

# Example:

# 30000
# 50000
# 70000

# ↓

# 30
# 50
# 70

# Easier to work with.