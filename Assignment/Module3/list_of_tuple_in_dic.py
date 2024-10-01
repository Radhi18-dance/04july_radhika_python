myli=[]

n= int(input("How many tuple do you want to enter? : "))

for i in range(n):
    val=input(f"enter{i+1}comma separated values:")
    myli.append(val.split(","))


print("Original List:",tuple(myli))
if n>=2:
    print(dict(myli))



