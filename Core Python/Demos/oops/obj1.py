class mobile:
    def __init__(self,price,company,memory):
        self.price=price
        self.company=company
        self.memory=memory
        
    def getPrice(self):
        return self.price
    def setPrice(self,newPrice):
        self.price=newPrice
        
    def getCompany(self):
            return self.company  
    def setCompany(self,newCompany):
        self.company=newCompany
        
    def getMemory(self):
        return self.memory   
    def setMemory(self,newMemory):
        self.memory=newMemory
        
    def show(self):
        print(f"Price : {self.price}  ,  Company : {self.company} : Memory : {self.memory}")
        
m=mobile(20000,"vivo",8)
m.show()
m.setPrice(30000)
print(m.getPrice())


        
    
    