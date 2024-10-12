import random
fr=open('list.txt','r')

read_lines=fr.readlines()
x=random.choice(read_lines)

print(x)