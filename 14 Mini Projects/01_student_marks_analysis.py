import numpy as np

marks = np.array([78, 85, 92, 67, 88, 95, 73])

print("Marks:", marks)
print("Average:", marks.mean())
pass_percentage = np.mean(marks>=75)
print("Highest mark:", marks.max())
print("Lowest mark:", marks.min())

print("Top Score Index:", marks.argmax())
print("Lowest Score Index:", marks.argmin())

print("Number of Students:", marks.size)

print("Students passed:", np.sum(marks>=75))
print("Students Failed:", np.sum(marks<75))

print(f"Pass percentage: {pass_percentage*100:.2f}%")