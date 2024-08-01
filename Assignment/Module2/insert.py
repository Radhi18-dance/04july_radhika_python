str=input("enter any string:")
new=input("enter any new string:")

position=len(str)
if position%2:

 print(str[:position]+new+str[position:])


