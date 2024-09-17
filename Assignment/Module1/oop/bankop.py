import random 

print("Bank Management system:")
class acop:
    acno=random.randint(1111,9999)
    ac_nm=" "
    ac_type=" "
    def acopdata(self):
        self.acno=int(input("enter account no:"))
        self.ac_nm=input("eneter holder's name:")
        self.ac_type=input("enter account type:")
class deposit(acop):
    bal=0
    def amount(self):
        while True:
         self.bal=int(input("enter balance:"))
         if self.bal<=2000:
                break
         else:
                print("low balance ")
class withdrawal(deposit):
    amt=0
    def amut(self):
        while True:
         self.amt=int(input("enter amount you want to withdraw:?"))
         if self.bal>=self.amt:
            print("withdraw successful")
            self.mb=self.bal-self.amt
            break 
        else:
            print("insufficient balance:")
class statement(withdrawal):
    def printdata(self):
     print("account number :",self.acno)
     print("holder name is:",self.ac_nm)
     print("account type is:",self.ac_type)
     print("current bal:",self.mb)
s=statement()
s.acopdata()
s.amount()
s.amut()
s.printdata()