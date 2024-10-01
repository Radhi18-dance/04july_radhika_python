tup1=[]
tup2=[]
dic={}
n1=int(input("enter size:"))
for i in range(n1):
    val=input("enter values:")
    tup1.append(val)
n2=int(input("enter size:"))
for i in range(n2):
    val=input("enter values:")
    tup2.append(val)
print(tuple(tup1))
print(tuple(tup2))
for i in range(len(tup1)):
    dic[tup1[i]]=tup2[i]
print(dic)