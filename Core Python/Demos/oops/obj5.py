class bag:
    def __init__(self,color,company,weight):
        self.color=color
        self.company=company
        self.weight=weight
        
    def getColor(self):
        return self.color
    def setColor(self,newColor):
        self.color=newColor
        
    def getCompany(self):
            return self.company  
    def setCompany(self,newCompany):
        self.company=newCompany
        
    def getWeight(self):
        return self.weight   
    def setWeight(self,newWeight):
        self.weight=newWeight
        
    def show(self):
        print(f"Color : {self.color}  ,  company : {self.company} : weight : {self.weight}")
        
m=bag("Pink","Forever",23)
m.show()
m.setColor("black")
print(m.getColor())