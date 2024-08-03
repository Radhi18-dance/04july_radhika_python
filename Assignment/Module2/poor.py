string=input("enter string:")
n=string.find('not')
p=string.find('poor')
print("not pos",n)
print("poor pos",p)
#if n>0 and p>0 and  p>n:
    #print(string.replace(string[n:],'good'))
#for i in string:
if n!=-1:
    print(string.replace(string[n:],'good'))
if p!=-1:
    print(string.replace(string[p:],'good'))

else:
    print("string is not replacaeble:")