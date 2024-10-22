class Rectangle:
    def getdata(self):

        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))
        
        # Calculate the area directly upon initialization
    def area(self):
        self.area = self.length * self.width

rect = Rectangle()
rect.getdata()
rect.area()
print("area is :",rect.area)