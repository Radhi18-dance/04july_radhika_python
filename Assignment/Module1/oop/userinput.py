class stdinfo:
    stid:int
    stnm:str #stid =0(we can initialize also diff is declaration done through datatype nd intialization in value)

    def mydata(self):
        self.stid=input("enter id:")
        self.stnm=input("enter name:")

    def printing(self):
        print("id:",self.stid)
        print("name:",self.stnm)

st=stdinfo()
st.mydata() 
st.printing()

