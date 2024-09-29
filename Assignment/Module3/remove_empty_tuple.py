empty_tuple = [] 
n1 = int(input("How many tuple do you want to enter? : "))

for i in range(n1):
    val = input("Enter value : ")
    empty_tuple.append(val)


print("Original List:", empty_tuple)

for i in empty_tuple:
     if len(i) == 0:
        empty_tuple.remove(i)
print(f'Removing Empty tuple from tuple_list: {empty_tuple}')