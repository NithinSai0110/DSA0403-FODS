import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_values = [1000, 1200, 800, 1500, 1400, 1600, 1100, 1300, 1700, 1900, 2000, 1800]

plt.figure(figsize=(8, 6)) 
plt.bar(months, sales_values, color='g')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True) 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show()
