import numpy as np

# Sample grayscale image
image = np.array([
    [100, 150, 200],
    [50,  75,  125],
    [25,  225, 255]
])

print("Original Image:")
print(image)

# Basic Statistics
print("\nHighest Pixel Value:", image.max())
print("Lowest Pixel Value:", image.min())

# Brightness Adjustment
bright = image + 50

print("\nBrightened Image:")
print(bright)

# Darkening
dark = image - 25

print("\nDarkened Image:")
print(dark)

# Binary Thresholding
binary = np.where(image > 100, 255, 0)

print("\nBinary Image:")
print(binary)