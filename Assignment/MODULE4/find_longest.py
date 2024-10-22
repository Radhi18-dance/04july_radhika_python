fl=open('stdata.txt','r')
max=0
long_word=''
for i in fl:
    word=i.strip().split()
    for j in word:
        if len(j)>max:
            max=len(j)
            long_word=j
        elif len(j)==max:
            long_word+=" "+j
print("longest word is :",long_word)