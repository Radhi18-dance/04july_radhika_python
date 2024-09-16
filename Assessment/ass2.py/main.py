from banker import bank
from customer import user
str="\t\t\t\t\tBANK MANAGEMENT SYSTEM"
print(str.title())
customers={}

def Role():

    role=0
    while True:
      print("============================")
      print("\t")
      print("Select your role")
      print("1)Banker")
      print("2)Customer")
      print("3)Exit")
      print("============================")
      print("\t")
      role=input("select your role(1/2/3):")
      if role =='1':
         bank(customers)
      elif role =='2':
         user(customers)
      elif role == 3:
         break
      else:
         print("enter valid role:")
         break


Role()
    
