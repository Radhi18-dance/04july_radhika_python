count=0
mystring=input("enter string:")
print(mystring)
char=input("enter character:")
if char in mystring:
 print(mystring.count(char))
elif char>=1:
 print(mystring.count(char))
else:
 print("no")
