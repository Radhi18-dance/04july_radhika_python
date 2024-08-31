mylist=[]
str=int(input("enter string size:"))
for i in range(str):
    n=input("values:")
    mylist.append(n)
length=len(mylist)
print(mylist)
if length<=0:
    print("empty")
else:
    print("not empty:")


