str="\t\t\t\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM"
print(str.title())
data={}


def Role():
    role=0
    while(True):
   
        def bank_menu(data):

            print("========================================================")
            print("========================================================")
            
            while(True):

                print("==================================================")
                print("||                                              ||")
                print("||\t        WELCOME TO BANKER'S APP      \t||")
                print("||                                              ||")
                print("==================================================")
   
                print("=====Oprations menu======")
                print("\t")
                print("1)adding customer")
                print("2)view customer")
                print("3)search customer")
                print("4)view all customer")
                print("5)total amounts in bank")
                print("6)Exit")
                print("---------------------------------------")
                print("\t")
                p=input("enter operations number to perform:")

                if p == '1':
                    print("\t")
                    print("=====adding customer=====")
                    print("\t")
                    acc=int(input("Enter Account Number:"))
                    data[acc]={}
                    print("\t")
                    data[acc]["name"]=input(f"Enter  Name:")
                    print("\t")
                    data[acc]["balance"]=int(input(f"Enter Balance:")) 
                    print("\t")
                    print(f"customer added succesfully:")
                    print("\t")
                    print("-----------------------------------------")
                    print("\t")
                        
                elif p == '2':
                    print("\t")
                    print("============================")
                    print("\t")
                    print(data)
                    print("\t")  
                    print("============================")
                    print("\t")
                
                elif p == '3':
                    print("\t")
                    print("-------------------------------------")
                    print("\t")
                    search=int(input("Enter account number for searching:"))
                    print("\t")
                    print("-----RESULT------")
                    print("\t")
                    print(data[search])
                    print("\t")
                    print("-------------------------------------")
                    print("\t")
            
                elif p == '4':
                    print("\t")
                    print("=====All Costomers======")
                    print("===================================")
                    for i in data.keys():
                        print("\t")
                        print(f"costomer account number is:{i}")
                        print("\t")
                        print(f"customer Name is:{data[i]["name"]}")
                        print("\t")
                        print(f"customer Balance is:{data[i]["balance"]}")
                        print("\t")
                        print("------------------------------------------")
                        print("\t")
        
                elif p == '5':
                    print("\t")
                    print("======Amount in bank========")
                    sum1=0
                    totl=0
                    for i in data:
                        sum1=data[i]["balance"]
                        totl=totl+sum1
                            
                        # for i in data[acc]["balance"].values():
                            # totl=totl+i
                    print("\t")
                    print("Total amount in bank is=",totl)
                    print("\t")
                    print("------------------------------------")
                    print("\t")

                elif p == '6':
                    break
        
                else:
                    print("\t")
                    print("==================================================")
                    print("||                                              ||")
                    print("||\tplease enter valid input for opration\t||")
                    print("||                                              ||")
                    print("==================================================")
                    print("\t")

        def Customer_menu(data):
            depo=0
            withdraw=0
            cu=0
            d=0
            ac=0            
            print("======================================================")
            print("======================================================")
            print("==================================================")
            print("||                                              ||")
            print("||\t        WELCOME TO CUSTOMER'S APP    \t||")
            print("||                                              ||")
            print("==================================================")
            print("\t")
            ac=int(input("Enter your Account number:"))
            print("\t")
            while(True):

                print("=================================")
                print("=====Oprations menu======")
                print("\t")
                print("1)Withdraw Amount")
                print("2)Deposite Amount")
                print("3)View Balance")
                print("04)Exit")
                print("\t")
                op=input("enter operations number to perform:")
                print("\t")

                
                if op == '1':
                    print("\t")
                    print("=====Withdraw Section=====")
                    print("\t")
                    withdraw=int(input("Enter Amount  you want to Withdraw:"))
                    if withdraw<=data[ac]["balance"]:
                        cu=data[ac]["balance"]-withdraw
                        print("\t")
                        print("Withdraw sucessfully")
                        print("\t")
                        print("your current balance is:",cu)
                        data[ac]["balance"]=cu
                        print("\t")
                    else:
  
                        print("==========================================================")
                        print("\t")
                        print("sorry!you not have enough money please check your balance")
                        print("\t")
                    
                elif op == '2':
                    print("========Deposite Amount==========")
                    print("\t")
                    depo=int(input("Enter Amount you want to Deposite:"))
                    if depo>0:
                        d=data[ac]["balance"]+depo
                        print("\t")
                        print("Deposite sucessfuly")
                        print("\t")
                        print("your current balance is:",d)
                        data[ac]["balance"]=d
                    else:
                        print("Your Deposite Amount must be greaterthan zero")

                elif op == '3':
                    print("\t")
                    print("======YOUR TOTAL BALANCE=======")
                    print("\t")
                    print(f"Your Total Balance is:{data[ac]["balance"]}")
                    
                
                elif op == '4':
                    break
                
                else:
                    print("==================================================")
                    print("||                                              ||")
                    print("||\tplease enter valid input for opration\t||")
                    print("||                                              ||")
                    print("==================================================")


        print("============================")
        print("\t")
        print("Select your role")
        print("1)Banker")
        print("2)Customer")
        print("3)Exit")
        print("============================")
        print("\t")
        role=int(input("select your role(1/2/3):"))

        if role == 1:
            bank_menu(data)

        elif role == 2:
            Customer_menu(data)
        elif role == 3:
            break
        else :
            print("==================================================")
            print("||                                              ||")
            print("||\t\tplease enter valid Role     \t||")
            print("||                                              ||")
            print("==================================================")
            break


Role()