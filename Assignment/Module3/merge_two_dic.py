dic1={}
dic2={}
n1= int(input("enter size : "))

for i in range(n1):
    key=input(f"enter{i+1}key:")
    val=input(f"enter{i+1}values:")
    dic1[key]=val
print("dictionary 1 is:",dic1)
n2= int(input("enter size : "))

for i in range(n2):
    key=input(f"enter{i+1}key:")
    val=input(f"enter{i+1}values:")
    dic2[key]=val
print("dictionary 2 is:",dict(dic2))
dic1.update(dic2)
print(dic1)