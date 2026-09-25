# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    @staticmethod
    def getPrice(price, size):
        if size == "small":
            return price

        elif size == "medium":
            return price + (price * 10 / 100)

        elif size == "large":
            return price + (price * 20 / 100)

        elif size == "xlarge":
            return price + (price * 30 / 100)

    def __init__(self, sid=1, sname="Shirt", type="Formal",
                 price=1000, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Object is destroyed")

    def showShirt(self):
        print("ID :", self.sid)
        print("Name :", self.sname)
        print("Type :", self.type)
        print("Price :", Shirt.getPrice(self.price, self.size))
        print("Size :", self.size)


obj1 = Shirt()
obj1.showShirt()

obj2 = Shirt(2, "T-Shirt", "Casual", 1000, "large")
obj2.showShirt()