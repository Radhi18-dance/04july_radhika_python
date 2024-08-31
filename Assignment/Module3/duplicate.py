mylist=[]
new=[]
no=int(input("enter no:"))
for i in range(no):
        du=input("enter value:")
        mylist.append(du)
        for i in mylist:
                new=list(set(mylist))

print(new)