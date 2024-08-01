string=input("enter element:")
words=input("enter words:")
count=0
x=string.split(" ")
print(len(x))
for i in range(0,len(x)):
    if words==x[i]:
        count=count+1
print("occurence of word is:",count)
    