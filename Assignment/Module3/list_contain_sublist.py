mylist=[]
sub=[]
n1=int(input("enter size for main list:"))
n2=int(input("enter size for sub list:"))
for i in range(n1):
    str=input("enter values:")
    mylist.append(str)
for j in range(n2):
    sub_list=input("enter value for sublist:")
    sub.append(sub_list)
set_mylist=set(mylist)
set_sublist=set(sub)
print(set_mylist.intersection(set_sublist))
if(set_mylist.intersection(set_sublist)):
    print("sublist is there::")
else:
    print("not there")
