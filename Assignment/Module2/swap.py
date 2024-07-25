#without temp varaible
r=int(input("Enter no 1:"))
v=int(input("enter no 2:"))
r=r+v
v=r-v
r=r-v
print("swap :",r,v)


#with temp varaible 
r=int(input("Enter no 1:"))
v=int(input("enter no 2:"))
z=r
r=v
v=z
print("swap:",r,v)
