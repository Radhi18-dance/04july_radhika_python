myli=[]
empty_tuple = [] 
n1 = int(input("How many tuple do you want to enter? : "))

for i in range(n1):
    val=input("enter values for tupple:")
    myli.append(val)


print("Original List:",myli)
n2=int(input("enter size:"))
for i in range(n2):
    val=input("enter values for tupple:")
    empty_tuple.append(val)
print(empty_tuple)

for i in empty_tuple:
     if len(i) == 0:
        empty_tuple.remove(i)
print(f'Removing Empty tuple from tuple_list: {empty_tuple}')