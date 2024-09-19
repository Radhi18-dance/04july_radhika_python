mylist=[]
n=int(input("enter size:"))
for i in range(n):
    str=input("enter values:")
    mylist.append(str)
print(mylist)
new_value=set(mylist)
mylist.sort()
print("unique value is:",list(new_value))