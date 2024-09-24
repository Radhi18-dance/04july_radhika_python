my_tuple=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    my_tuple.append(val)
print("tupple is:",tuple(my_tuple))
element_search=input("enter element to search:")
if element_search in my_tuple:
    print("element exists :")
else :
    print("element doesnt exist:")