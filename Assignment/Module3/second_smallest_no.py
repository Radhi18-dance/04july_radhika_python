numlist=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    numlist.append(val)
    length=len(numlist)
print(length)


print("Second Smallest element is:", numlist[1])