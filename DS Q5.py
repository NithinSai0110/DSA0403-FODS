import numpy as np
names=["Model name","Fuel Eff"]
cars=np.array([["Volvo",25],["Ferrari",15],["Bugati",16]])
m=(eval(cars[0,1])+eval(cars[1,1]))/2
per=100*((eval(cars[0,1])-eval(cars[1,1]))/m)
print("percentage change between volvo and ferrari",per)