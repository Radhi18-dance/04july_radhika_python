my_list=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:") 
    my_list.append(val)

replace_value=input("enter element you want to replace:")
my_list[-1]=replace_value

tupple=tuple(my_list)
print("replaced value in list is:",list(my_list))