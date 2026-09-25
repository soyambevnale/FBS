# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class shirt:
    def __init__(self,sid=1,sname="Levis",type="Formal",price=5000,size="Large"):
        self.id=sid
        self.name=sname
        self.type=type
        self.price=price
        self.size=size
        
    def __del__(self):
        print("Object is destroyed ")
        
    def showShirtDetails(self):
        print("Id : ",self.id)
        print("Name : ",self.name)
        print("Type : ",self.type)
        print("Price : ",self.price)
        print("Size : ",self.size)
        
obj1=shirt()
obj1.showShirtDetails()

obj2=shirt(2,"Levisss","Non formal",6000,"XXL")
obj2.showShirtDetails()
        