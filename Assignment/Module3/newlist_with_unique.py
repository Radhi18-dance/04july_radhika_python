Rlist=[]
my=[]
n=int(input("enter size:"))
for i in range(n):
    str=input("enter values:")
    Rlist.append(str)
print("old :",Rlist)
for i in Rlist:
    my.append(i)
    unique_list=set(my)
print("unique list:",list(unique_list))
