str="\t\t\t\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM"
print(str.title())
role=input("select your role(1/2/3):")
thisdict={
    '1':'banker','2':'customer', '3':'exit'
}

if role=='1':
    print(" welcome to bankers app:")
n=0
acc_no=0
bal=0
   
def bank_menu():
    users={'name':n,'balance':bal,'acc_no':acc_no}
    

    print("1:adding customer")
    print("2:view customer:")
    print("3:search customer:")
    print("4: viewall customer:")
    print("5:total amounts in bank:")
    p=int(input("enter operations to perform:"))

    if p == 1:
      
        print("adding customer:")
    
        users['name']=input("enter customer name:")
        users['balance']=int(input("enter balance:"))
        users['acc_no']=int(input("enter account no:"))
      
        if acc_no in data:
            print("exist:")
        print(f"added customer name is :{users.n},account number:{users.acc_no} and balance is:{users.bal}")      
        print(f"customer name added succesfully:")
        print(data)


    if p==2: 
         print("view customer:")
         acc_no=int(input("enter id to view:"))
         if acc_no in data:
            print(acc_no(data))
           
   

   
bank_menu()


           
        


    

