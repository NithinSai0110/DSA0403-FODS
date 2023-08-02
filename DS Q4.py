import numpy as n
sales=n.array([[3000,2800,3400,4050]])
print(sales[0])
print("Total sales of the year are:",n.sum(sales[0]))
for j in sales:
    m=(j[0]+j[3]/2)
    per=100*((j[3]-j[0])/m)
print("Percent change is: {:.2f}".format(per))