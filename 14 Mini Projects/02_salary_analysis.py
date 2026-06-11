import numpy as np

salaries = np.array([30000, 45000, 50000, 70000, 90000, 120000])

print("Salaries:", salaries)

# Basic Statistics
print(f"Average Salary: {salaries.mean():.2f}")
print("Highest Salary:", salaries.max())
print("Lowest Salary:", salaries.min())

# High Earners
high_earners = salaries[salaries >= 70000]

print("High Earners:", high_earners)
print("Number of High Earners:", high_earners.size)

# Count High Earners
print("Count of High Earners:", np.sum(salaries >= 70000))

# Total Salary of High Earners
print("Total High Earner Salary:", np.sum(salaries[salaries >= 70000]))

# Categories
categories = np.where(
    salaries >= 100000,
    "Senior",
    "Junior"
)

print("Employee Categories:", categories)

# Percentage of High Earners
print(
    f"High Earner Percentage: "
    f"{np.mean(salaries >= 70000) * 100:.2f}%"
)

