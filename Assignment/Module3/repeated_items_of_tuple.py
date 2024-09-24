mylist=[]
tem=[]
repeated=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    mylist.append(val)
for i in mylist:
    if i not in tem:
        tem.append(i)
    else:
        repeated.append(i)
print("original list:",tuple(mylist))
print("temp",tuple(tem))
print("repeated item:",tuple(repeated))
