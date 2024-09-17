myli=[]
string=''
n=int(input("enter size:"))
for i in range(n):
    new=input("enter character:")
    myli.append(new)
for j in myli:
    join_string=string.join(myli)
print(join_string)

