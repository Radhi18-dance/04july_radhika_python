Rlist=[]
n=int(input("enter size:"))
for i in range(n):
    str=input("enter values:")
    Rlist.append(str)
print("old :",Rlist)
unique_list=set(Rlist)
print("unique list:",list(unique_list))