# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:

    discount = 10
    @staticmethod
    def applyDiscount(price):
        final_price = price - (price * Product.discount / 100)
        return final_price

    def __init__(self, pid=1, pname="Mobile", price=100000, quantity=1):
        self.id = pid
        self.name = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Object is destroyed")

    def showProductDetails(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Price :", self.price)
        print("Quantity :", self.quantity)
        print("Price after discount :", Product.applyDiscount(self.price))
        


obj1 = Product(1,"Mobile",10000,3)
obj1.showProductDetails()
# print("Price after discount :", Product.applyDiscount(obj1.price))


obj2 = Product(2, "Laptop", 200000, 2)
obj2.showProductDetails()
# print("Price after discount :", Product.applyDiscount(obj2.price))
