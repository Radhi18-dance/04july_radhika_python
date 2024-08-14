str=input("enter string:")
length=len(str)
if length>=3:
 if str.endswith('ing'):
    print(str+'ly')
 else :
    print(str+'ing')
print(str)