#overloading not support in python
class index:
    def mydata(self,a,b):
        print("class result:")
        print("sum:",a+b)
class home(index):
    print("this is home page:")
    def mydata(self, a, b):
        return super().mydata(a, b)
class result(index):
    print("this is result:")
    def mydata(self, a, b):
        return super().mydata(a, b)
o=index()
o.mydata(12,25)


