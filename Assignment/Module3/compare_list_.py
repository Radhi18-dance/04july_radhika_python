mylist1=[]

n1=int(input("enter size:"))
for i in range(n1):
    str=input("enter values:")
    mylist1.append(str)
print(mylist1)
mylist2=[]
n2=int(input("enter size:"))
for i in range(n2):
    str2=input("enter values:")
    mylist2.append(str2)
print(mylist2)
set1=set(mylist1)
set2=set(mylist2)
if set1.intersection(set2):
    print("Compare success:")