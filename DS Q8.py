import pandas as pd
data={"OrderID":{1:101,2:103,3:121,4:132,5:123,6:120,7:121,8:103},
      "OrderName":{1:'Shampoo',2:'biscut',3:'bottle',4:'soap',5:'sanitizer',5:'mask',6:'Pens',7:'bottle',8:'biscut'},
      "Quan":{1:10,2:23,3:21,4:32,5:23,6:20,7:12,8:10}}
df=pd.DataFrame(data)
print(df)
s=df.groupby('OrderName')['Quan'].sum()
df1=pd.DataFrame(s)
t=df1.sort_values('Quan')
print(t.tail(5))