myli=[]


n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    myli.append(val)
print(tuple(myli))



res=list(zip(*myli))
print("modified list is:",res)