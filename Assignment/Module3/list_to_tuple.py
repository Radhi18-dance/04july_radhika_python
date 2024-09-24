my_list=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:") 
    my_list.append(val)

tupple=tuple(my_list)
print("list into tupple is:",tupple)