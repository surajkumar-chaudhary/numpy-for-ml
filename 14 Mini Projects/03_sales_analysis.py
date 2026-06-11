import numpy as np

sales = np.array([1200,1500,1800, 1000, 2500,3000,2200])

target_status = np.where(
    sales>= 2000,
    "Target Met",
    "Target Missed"
)

print(sales)

print(f"Average Sales: {sales.mean():.2f}")
print("Highest Sales:", sales.max())
print("Lowest Sales:", sales.min())

print("Best Sales Day Index:", sales.argmax())
print("Worst Sales Day Index:", sales.argmin())

print(target_status)

print(
    f"Target Achievement Rate:"
    f"{np.mean(sales >= 2000) * 100:.2f}%"
)

print("Total Sales:", sales.sum())