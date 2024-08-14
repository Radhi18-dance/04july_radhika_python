list=[]
a=int(input("how many words:"))
for i  in range(a):
    word=input("enter word:")
    list.append(word)
maximum_length=len(list[0])
x=list[0]
for j in list:
    if len(j)>maximum_length:
        maximum_length=len(j)
        x=j
print(f"longest word is:{x} and length is :{maximum_length}")