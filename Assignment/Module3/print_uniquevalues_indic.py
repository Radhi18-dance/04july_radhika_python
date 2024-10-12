d1={}
d2=[]
n1= int(input("Enter the number of key-value pairs: "))
for i in range(n1):
    key = input("Enter key : ")
    value = input("Enter value for key : ")
    d1[key] = value
print(d1)
for i,j in d1.items():
    if j not in d2:
        d2.append(j)

print(f'Dict: {d1}\n')

print('Unique Value in Dictionary: ',d2)