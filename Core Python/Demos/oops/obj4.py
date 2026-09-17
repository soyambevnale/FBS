class notebook:
    def __init__(self,name,pages,type):
        self.name=name
        self.pages=pages
        self.type=type
        
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
        
    def getPages(self):
            return self.pages  
    def setPages(self,newPages):
        self.pages=newPages
        
    def getType(self):
        return self.type   
    def setType(self,newType):
        self.type=newType
        
    def show(self):
        print(f"Name : {self.name}  ,  Pages : {self.pages} : Type : {self.type}")
        
m=notebook("Classmate",120,"Plain")
m.show()
m.setPages(300)
print(m.getPages())