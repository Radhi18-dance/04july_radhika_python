customers={}


def user(customers):
        accno=0
        depo=0
        withdraw=0
        cb=0
        n=0
        print("||                                              ||")
        print("||\t        WELCOME TO CUSTOMER'S MODULE   \t||")
        print("||                                              ||")
        print("==================================================")
        print("\t")
        accno=int(input("enter account number:"))
        customers['accno']=accno
        bal=int(input("enter balance:"))
        customers['bal']=bal
        
        print(customers)
        while(True):

            print("=================================")
            print("=====Operations menu======")
            print("\t")
            print("1)Register")
            print("2)Login")
            print("3)withdraw amount")
            print("04)deposit amount")
            print("5)view balance")
            print("\t")
            op=input("enter operations number to perform:")
            print("\t")
            if op =='1':
                print("\t")
                print("=====register yourself :=====")
                print("\t")
                usernm=input("enter username:")
                if usernm in customers:
                 print("Customer already exists.")
                else:
                 customers[usernm] = {}
                 customers[usernm]["password"]=input(f"enter password:")
                 print("customer register done:")
            elif op =='2':
               print("\t")
               print("===login====")
               print("\t")
               usernm=input("enter username:")
               if usernm in customers:
                  password=input("enter password:")
                  if customers[usernm]['password']==password:
                     print("customer logged in successfull:")
                  else:
                     print("invalid password:")
               else:
                  print("invalid username:")
            elif op =='3':          
               print("\t")
               print("========withdraw=====")        
               print("\t")
               withdraw=int(input("Enter Amount  you want to Withdraw:"))     
               if withdraw<=customers['bal']:
                  cb=customers['bal']-withdraw
                  print("\t")
                  print("Withdraw sucessfully")
                  print("\t")
                  print("your current balance is:",cb)
                  customers['bal']=cb
                  print("\t")
               else:
                  print("==========")
                  print("\t")
                  print("you don't have balance:")

            elif op =='4':
               print("\t")
               print("======deposit amount==========")
               print("\t")
               depo=int(input("Enter Amount you want to Deposit:"))
               if depo>0:
                  n=customers['bal']+depo
                  print("\t")
                  print("Deposite sucessfuly")
                  print("\t")
                  print("your current balance is:",n)
                  customers['bal']=n
               else:
                  print("your amount should be greater than zero:")
            elif op =='5':
               print("\t")
               print("=========view balance:==========")
               print("\t")
               print(f"Your Total Balance is:{customers['bal']}")
            elif op=='6':
               break
            else:
               print("==================================================")
               print("||                                              ||")
               print("||\tplease enter valid input for opration\t||")
               print("||                                              ||")
               print("==================================================")


