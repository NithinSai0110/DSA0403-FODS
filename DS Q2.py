import numpy as np
p=["year","soap","shampoo","perfume"]
a=np.array([[2012,50,46,250],[2013,55,51,258],[2014,49,52,240]])
for i in p:
    print(i,end=" ")
print()
for i in a:
    for j in i:
        print(j,end="   ")
    print()
print("\n")
av=[]
for i in range(1,len(a[0])):
               s=0
               for j in a:
                   s+=j[i]
               av.append(s/3)
for i in range(len(p)-1):
    print("Average price of ",p[i+1],"= ",av[i])