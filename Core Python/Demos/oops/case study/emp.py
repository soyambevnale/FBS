class Employee:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal
        
    def getId(self):
        return self.__id
    
    def setId(self,new_id):
        self.__id = new_id

    def getName(self):
        return self.__name
    
    def setName(self,new_name):
        self.__name=new_name
        
    def getSal(self):
        return self.__sal
    
    def setSal(self,new_sal):
        self.__sal=new_sal
        
        
    def __str__(self):
        return f"Id = {self.__id}  ,  Name = {self.__name}  ,  sal = {self.__sal} "