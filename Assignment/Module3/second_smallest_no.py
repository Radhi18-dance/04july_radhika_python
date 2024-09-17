numlist=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    numlist.append(val)
numlist.sort()
print(numlist)

print("Second Smallest element is:", numlist[1])