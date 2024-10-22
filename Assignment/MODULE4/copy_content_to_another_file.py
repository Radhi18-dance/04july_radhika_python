f=open('stdata.txt','r')
copy=open('test.txt','a')
for i in f:
    copy.write(i)