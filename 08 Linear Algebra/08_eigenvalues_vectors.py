import numpy as np

A = np.array([
    [2,0],
    [0,3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

# Eigenvalues
# ↓
# How much scaling happens

# Eigenvectors
# ↓
# Directions that remain unchanged
# An eigenvector keeps the same direction after a matrix transformation.
# Stretch
# Shrink
# Flip direction (negative eigenvalue)