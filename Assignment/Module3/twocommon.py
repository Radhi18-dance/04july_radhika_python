list=[]
li=[]
s1=int(input("enter size:"))
for i in range(s1):
    n=input("enter values:")
    list.append(n)
s2=int(input("entern size:"))
for i in range(s2):
    M=input("enter values:")
    li.append(M)
p=set(list)
o=set(li)
print(p)
print(o)
i=p.intersection(o)
if i:
    print("True:")
else:
    print("false:")
