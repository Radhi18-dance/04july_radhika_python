import random
mylist=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    mylist.append(val)
random_item=random.choice(mylist)
print("randomly selected item:",random_item)