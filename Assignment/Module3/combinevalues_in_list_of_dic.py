d1={}
d2={}
d3={}
n1 = int(input("Enter the number of key-value pairs for the first dictionary: "))
for i in range(n1):
    key = input("Enter key {}: ".format(i+1))
    value = int(input("Enter value for key {}: ".format(key)))
    d1[key] = value
print("dictionary 1:",d1)

n2= int(input("Enter the number of key-value pairs for the second dictionary: "))
for i in range(n2):
    key = input("Enter key {}: ".format(i+1))
    value = int(input("Enter value for key {}: ".format(key)))
    d2[key] = value
print("dictionary 2:",d2)
'''counter = Counter(d1)'''
a=list(d1.values())
b=list(d2.values())
for i in range(len(a)):
    c= a[i] + b[i]
    for j in d1:
         d3[j] = c

print(f'Dict_1: {d1}\n')
print(f'Dict_2: {d2}\n')

print('New_dict:' ,list[dict[d3]])
    