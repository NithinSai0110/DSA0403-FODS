import numpy as np
sold=np.array([[2,40],[4,35],[1,100],[2,90]])
total=0
for j in sold:
    total+=j[0] * j[1]
cost=total+(total*0.18)-(total*0.15)
print("Total cost(tax:18%, Discount: 15%)is:",cost)