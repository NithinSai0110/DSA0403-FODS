import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_values = [1000, 1200, 800, 1500, 1400, 1600, 1100, 1300, 1700, 1900, 2000, 1800]

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Set the figure size
plt.scatter(months, sales_values, color='r', marker='o')
plt.title('Product Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)  # Show gridlines
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
