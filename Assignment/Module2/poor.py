string=input("enter string:")
n=string.find('not')
p=string.find('poor')
if n>0 and p>0 and  n>p:
    print(string.replace(string[p:],'good'))
