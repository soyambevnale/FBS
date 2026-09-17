class car:
    def __init__(self,price,brand,color):
        self.price=price
        self.brand=brand
        self.color=color
        
    def getPrice(self):
        return self.price
    def setPrice(self,newPrice):
        self.price=newPrice
        
    def getBrand(self):
            return self.brand  
    def setBrand(self,newBrand):
        self.brand=newBrand
        
    def getColor(self):
        return self.color   
    def setColor(self,newColor):
        self.color=newColor
        
    def show(self):
        print(f"Price : {self.price}  ,  brand : {self.brand} : color : {self.color}")
        
m=car(10000000,"Scorpio","black")
m.show()
m.setColor(30000)
print(m.getPrice())