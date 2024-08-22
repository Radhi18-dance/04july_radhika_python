mylist=[]
no=int(input("enter number of strings:"))
count=0
for i in range(no):  
    str1=input("enter string:")
    mylist.append(str1)
print(mylist)
print(len(mylist))
for i in mylist:
    if len(mylist)>=2 and i[0]==i[-1]:
        count+=1
print(count)


