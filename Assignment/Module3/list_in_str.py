myli=[]
string=''
n=int(input("enter size:"))
for i in range(n):
    new=input("enter character:")
    myli.append(new)
print(myli)
for i in myli:
    string=string+i
print(f"string is:{string}")

