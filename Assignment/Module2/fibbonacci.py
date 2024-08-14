a=0
b=1
count=0
x=int(input("Up to how many terms you want to count:"))
while count<x:
    print(a)
    n=a+b
    a=b
    b=n
    count+=1
