myli=[]
myli2=[]
n=int(input("enter size:"))
for i in range(n):
   val=input(f"enter{i+1} values:")
   myli.append(tuple(val.split()))
   print(myli)
n2=int(input("enter size:"))
for i in range(n2):
   val2=input(f"enter{i+1} values:")
   myli2.append(tuple(val2.split()))    
   print(myli2)
res=list(zip(*myli,*myli2))
print("modified list is:",res)

