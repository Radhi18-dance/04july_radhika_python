n=int(input("enter size:"))
l=int(input("enter length:"))
myli=[]
for i in range(n):
   mylist2=[]
   for j in range(l):
      val=input("enter values:")
      mylist2.append(val)
   myli.append(tuple(mylist2))
  
res=list(zip(*myli))
print(res)
for i in res:
   print(list(i))

