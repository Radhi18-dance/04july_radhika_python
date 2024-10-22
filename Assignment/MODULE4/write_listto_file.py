mylist=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter value:")
    mylist.append(val)
fl=open('stdata.txt','a')
for i in mylist:
    fl.write("\n"+i)
fl.close()