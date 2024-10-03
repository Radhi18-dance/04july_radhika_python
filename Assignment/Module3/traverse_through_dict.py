mydict={}
n = int(input("Enter the size of the dictionary: "))

for i in range(n):
    key = input(f"Enter {i+1} key: ")
    val = input(f"Enter {i+1} value: ")
    mydict[key] = val
for key,val in mydict.items():
     print(f"Key: {key}, Value: {val}")