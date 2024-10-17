file=open('stdata.txt','a')

file=open('stdata.txt','r')

n=int(input('How many Last lines You want to read?: '))

list_data=file.readlines()[-n:]


for i in list_data:
    print(i)