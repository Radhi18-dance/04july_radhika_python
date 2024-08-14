
cdata={}
bal=0

def acopening():
    acno=input("Enter an A/c No.:")
    acnm=input("Enter A/c Holder Name:")
    actype=input("Enter A/c TYpe:")
    cdata["acno"]=acno
    cdata["acnm"]=acnm
    cdata['actype']=actype

    print(cdata)

def deposite():
    bal=int(input("Enter your amount for deposite:"))
    print("Current Balance:",bal)



acopening()
deposite()


