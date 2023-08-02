import pandas as p
order={"CustomerID":{1:102,2:121,3:154,4:111,5:121},
       "OrderDate":{1:"20july",2:"23july",3:"23july",4:"26july",5:"23july"},
       "ProdName":{1:"Shampoo",2:"Perfumes",3:"Shampoo",4:"sugar",5:"Shampoo"},
        "Order Quantaity":{1:15,2:21,3:20,4:11,5:10}}
df=p.DataFrame(order)
print(df)
tot=df.groupby('CustomerID').size()
print(tot)
avg=df.groupby('ProdName')['Order Quantaity'].mean()
print(avg)
min=df['OrderDate'].min()
print("Earliest:",min)
max=df['OrderDate'].max()
print("Latest:",max)