my_list=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:") 
    my_list.append(val)
my_list.reverse()
rev_tuple=tuple(my_list)
print("reverse tupple is:",rev_tuple)