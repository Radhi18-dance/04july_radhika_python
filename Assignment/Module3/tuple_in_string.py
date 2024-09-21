my_tuple=[]
string=''
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:") 
    my_tuple.append(val)

tupple=tuple(my_tuple)
print(tupple)
for i in tupple:
    string=string+i
print(f"string is:{string}")