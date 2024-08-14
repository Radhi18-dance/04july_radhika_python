import requests
import pandas as xd

url="https://fakestoreapi.com/products"
req=requests.get(url)
data=req.json()
for i in data:
    
    d={'id':i["id"],'title':i["title"],'price':i["price"],'rating':i["rating"]["rate"]}
    df=xd.DataFrame(d,index=[i["id"]])
    print(df.to_string())

