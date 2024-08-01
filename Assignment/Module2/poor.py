string=input("enter string:")
n=string.find('not')
p=string.find('poor')
if n>0 and p>0 and  p>n:
    print(string.replace(string[n:],'good'))
