import random
li=[]
tup=[]
n=int(input("enter size:"))
for i in range(n):
    val=input("enter values:")
    li.append(val)

n2=int(input("enter size of tuple:"))
for i in range(n2):
    val2=input("enter values:")
    tup.append(val2)
print(tuple(tup))
ran_list=random.choice(li)

ran_tuple=random.choice(tup)

print(f'List= {li}')
print(f'The Random Number From list is: {ran_list}\n')

print(f'Tuple= {tuple(tup)}')
print(f'The Random Number From Tuple is: {ran_tuple}')
