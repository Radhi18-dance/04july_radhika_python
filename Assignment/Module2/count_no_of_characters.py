count=0
mystring=input("enter string:")
print(mystring.split())
char=input("enter character:")
if char in mystring:
    print(mystring.count(char))
else :
    print("error")