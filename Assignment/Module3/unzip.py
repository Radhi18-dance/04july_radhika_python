myli=[]
myli2=[]
def func(myli,myli2):
     n=int(input("enter size:"))
     for i in range(n):
        val=input(f"enter{i+1} values:")
        myli.append(val)
        print(tuple(myli))
     n2=int(input("enter size:"))
     for i in range(n2):
        val2=input(f"enter{i+1} values:")
        myli2.append(val2)
        print(tuple(myli2))
        res=list(zip(myli,myli2))
        print("modified list is:",res)
dt=map(func(myli,myli2))
print(list(dt))

