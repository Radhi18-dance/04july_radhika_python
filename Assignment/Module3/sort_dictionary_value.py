myli={}
n=int(input("enter size:"))
for i in range(n):
    key=input(f"enter key:")
    val=input(f"enter values:")
    myli[key]=val
ascending=sorted(myli.items())
print("value sorted:",dict(ascending))
descending=sorted(myli.items(),reverse=True)
print("value sorted:",dict(descending))

