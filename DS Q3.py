import numpy as np
a=np.array([[1,2,12000],[5,5,50000],[3,7,75000],[4,3,25000]])
s=0
c=0
for j in a:
    if(j[0]>=4):
        c+=1
        s = s + j[2]
print("The Avarage sales are:",s/c)

