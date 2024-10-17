
file=open('stdata.txt','a')

file=open('stdata.txt','r')

n=int(input('How many lines You want to read?: '))

for i in range(n):
    print(file.readline())

