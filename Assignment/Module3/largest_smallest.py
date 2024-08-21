mylist1=[]
sum=0
element=int(input("enter number :"))
for i in range(0,element):
    newele=int(input("enter elements:"))
    mylist1.append(newele)
    print(mylist1)
print(f"maximum  or largest number is:{max(mylist1)}")
print(f"smallest value is:{min(mylist1)}")
for i in range(len(mylist1)):
    sum=sum+mylist1[i]
print(f"sum of all digit is:{sum}")
   