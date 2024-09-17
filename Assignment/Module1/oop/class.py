class studinfo:
    id=12
    name="radhi"

    def myfunc(self):#if we define func in class we have to write default argument 'self'
        #(first arg is self only compulsory)
        print("this is demo class:")
    def getsum(self,a,b):
        print("sum:",a+b)
st=studinfo()#object of class 
print("id:",st.id)
print("name:",st.name)
st.myfunc()
st.getsum(12,42)

#class property if we want to use inside class use self and if outside use object