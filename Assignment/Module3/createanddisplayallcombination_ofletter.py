d1={}
n1= int(input("Enter the number of key-value pairs: "))
for i in range(n1):
    key = input("Enter key : ")
    value = input("Enter value for key : ")
    d1[key] = value
print(d1)
mylist=list(d1.values())
for i in mylist[0]:
    for j in mylist[1]:
        print(i+j)