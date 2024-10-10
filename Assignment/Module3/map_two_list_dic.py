list1=[]
list2=[]
n1=int(input("enter size:"))
for i in range(n1):
    val=input("enter values:")
    list1.append(val)
print(list1)
n2=int(input("enter size:"))
for i in range(n2):
    val2=input("enter values:")
    list2.append(val2)
print(list2)
newdic=dict(zip(list1,list2))
print(newdic)

