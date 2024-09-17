mylist=[]
n=int(input("enter size:"))
for i in range(n):
    str=input("enter values:")
    mylist.append(str)
print("old :",mylist)
unique_list=set(mylist)
print(list(unique_list))