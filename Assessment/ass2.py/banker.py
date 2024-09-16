customers={}
def bank(customers):
        while True:
         print("========")
         print("||||||||THIS IS BANK MENU|||||||")
         print("=====Operations menu======")
         print("\t")
         print("1.Register ")
         print("2.Login")
         print("3.update ")
         print("4.view all customers:")
         print("5.delete")
         print("6.exit")
         p=input("enter operations number to perform:")
        
         if p=='1':
            print("\t")
            print("=====register customer name =====")
            print("\t")
            usernm=input("enter username:")
            customers['usernm'] = usernm
            if usernm in customers:
                print("Customer already exists.")
            else:
               
                password=input(f"enter password:")
                customers['password']=password
                print("customer register done:")
                print(customers)
               
       
         elif p=='2':
            print("login:")
            usernm=input("enter username:")
            if usernm in customers:
                password=input("enter password:")
                if customers['password'] == password:
                    print("Customer logged in successfully.")
                else:
                    print("Invalid password.")
            else:
                print("Invalid username.")
            print(customers)
         elif p=='3':
            print("update:")
            username = input("Enter customer username to update: ")
            if username in customers:
                new_password = input("Enter new password: ")
                customers[username]["password"] = new_password
                print("Customer password updated successfully.")
            else:
                print("Customer not found.")
         elif p=='4':
            print("view all customer:")
            if not customers:
                print("No customers registered.")
            else:
                for i in customers.keys():
                    print(f"Customer: {i}")
         elif p=='5':
            print("delete:")
            username = input("Enter customer username to delete: ")
            if username in customers:
                del customers[username]
                print("Customer deleted successfully.")
            else:
                print("Customer not found.")
         elif p=='6':
            print("Exiting the system.")
            break
         else:
            print("Invalid choice. Please try again")
