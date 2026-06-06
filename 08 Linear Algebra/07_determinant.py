import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

print(np.linalg.det(A))

# Determinant tells us:

# Can this matrix be inverted?

# If:

# det(A) = 0

# ❌ No inverse exists.

# If:

# det(A) ≠ 0

# ✅ Inverse exists.

# A = np.array([
#     [1,2],
#     [2,4]
# ])

# You said:

# det(A) = 0

# ✅ Correct.

# Why?

# Because:

# Row2 = 2 × Row1

# The rows are dependent.

# This means the matrix doesn't contain enough independent information.

# Therefore:

# det(A) = 0

# and:

# No inverse exists.