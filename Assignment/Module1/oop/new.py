class Employee:
    # define a property
    employee_id:int 
    def mydata(self):
        n=int(input("enter no of id:"))
        for i in range(n):
          self.employee_id=int(input("enter id:"))
        
    def printing(self):
        for i in range(self.employee_id):

            print("id:" ,self.employee_id)




# create two objects of the Employee class
e=Employee()
e.mydata()
e.printing()


