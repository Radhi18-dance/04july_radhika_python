fl=open('newapp.txt','a')

strength=int(input("how many tables you want to enter:?"))

for i in range(strength):
    t=int(input("which table you want?"))
    j=1
    while j<=10:
       
        fl.write(f"\n{t}* {j} = {t*j}")
        j+=1
 
  
   
