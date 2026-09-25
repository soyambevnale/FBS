# 2. Create a class Product with members as pid,pname,price and quantity .Addfollowing methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class product:
    def __init__(self,pid=1,pname="Mobile",price=100000,quantity=1):
        self.id=pid
        self.name=pname
        self.price=price
        self.quantity=quantity
        
    def __del__(self):
        print("Object is destroyed")
        
    def showProductDetails(self):
        print("ID : ", self.id)
        print("Name : ", self.name)
        print("Price : ", self.price)
        print("Quantity : ", self.quantity)
        
obj1=product()
obj1.showProductDetails()

obj2=product(2,"Laptop",200000,2)
obj2.showProductDetails()