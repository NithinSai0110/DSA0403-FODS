import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_values = [10, 12, 15, 20, 25, 28, 30, 29, 26, 22, 18, 12]
rainfall_values = [50, 40, 30, 20, 10, 5, 3, 5, 10, 20, 30, 40]

# 1. Python program to create a line plot of the monthly temperature data
plt.figure(figsize=(8, 6))  # Set the figure size
plt.plot(months, temperature_values, marker='o', color='b', linestyle='-', linewidth=2)
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)  # Show gridlines
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()


# 2. Python program to create a scatter plot of the monthly rainfall data
plt.figure(figsize=(8, 6))  # Set the figure size
plt.scatter(months, rainfall_values, color='r', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)  # Show gridlines
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
