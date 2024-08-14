import requests


url="https://api.covid19india.org/data.json"

req=requests.get(url)
data=req.json()
for i in data["statewise"]: 
   print(i["state"])
   print(f"confirmed is :{i["confirmed"]}")
   print(f"deaths is:{i["deaths"]}")
