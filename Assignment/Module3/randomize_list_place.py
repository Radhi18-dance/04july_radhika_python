import random
mylist=[]
n2=int(input("enter size :"))
for i in range(n2):
    val2=input("enter values:")
    mylist.append(val2)
random.shuffle(mylist)

print(mylist)
