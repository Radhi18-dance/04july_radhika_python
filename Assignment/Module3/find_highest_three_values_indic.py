mydic={}
list=[]
n1= int(input("Enter the number of key-value pairs: "))
for i in range(n1):
    key = input("Enter key : ")
    value = input("Enter value for key : ")
    mydic[key] = value
print(mydic)
for i in mydic.values():
    list.append(i)

list.sort()

print(f'Dictionary: {mydic}\n')

print('3 Max_values:' ,list[-3:])