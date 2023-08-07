import matplotlib.pyplot as plt

# Sample dataset containing month and sales values
months = ['January', 'February', 'March', 'April', 'May', 'June']
sales_values = [15000, 18000, 22000, 25000, 28000, 30000]

# Create a line plot
plt.figure(figsize=(8, 5))  # Optional: Set the figure size
plt.plot(months, sales_values, marker='o', color='b', linestyle='-')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)  # Optional: Add gridlines to the plot
plt.xticks(rotation=45)  # Optional: Rotate the x-axis labels for better visibility
plt.tight_layout()  # Optional: Adjust the layout for better appearance

# Save the plot as an image (optional)
plt.savefig('monthly_sales_line_plot.png')

# Show the plot
plt.show()
