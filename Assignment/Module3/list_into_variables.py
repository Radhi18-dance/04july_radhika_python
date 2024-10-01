colour=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    colour.append(val)
for i in range(len(colour)):
    print(f'var'+str(i),"=",colour[i])
 
 