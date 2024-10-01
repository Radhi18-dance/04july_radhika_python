myli=[]
empty_tuple = [] 
n= int(input("How many tuple do you want to enter? : "))

for i in range(n):
    val=input(f"enter{i+1}values for tupple:")
    myli.append(tuple(val.split()))


print("Original List:",myli)


for j in myli:
     if j:
        empty_tuple.append(j)
print(f'Removing Empty tuple from tuple_list: {empty_tuple}')