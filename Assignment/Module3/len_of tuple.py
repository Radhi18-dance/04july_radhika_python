my_tuple=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    my_tuple.append(val)
print("my tuple is:",tuple(my_tuple))
print("length :",len(my_tuple))